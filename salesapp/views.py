from django.shortcuts import render
from django.forms import modelformset_factory,inlineformset_factory
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from django.db.models import Q,Sum,DecimalField

from billingapp.models import (State,City,Unit,Category_GST,UOM,UOM_Conversion,Financial_Year,Company,Branch,
User,Product,Party,Payment_Mode,Payment_Details,Stock)

from billingapp.forms import (State_modelform,City_modelform,Unit_modelform,Category_GST_modelform,UOM_modelform,UOM_conversion_modelform,
Financial_year_modelform,Company_modelform,Branch_modelform,User_modelform,Product_modelform,Party_modelform,Payment_mode_modelform,
Payment_details_modelform,Stock_modelform)

from salesapp.models import (Sales,Sales_Items_Bridge,Sales_GST_Wise,Sales_Returns_GST_Wise,Sales_Returns,Sales_Items_Return_Bridge)

from salesapp.forms import (Sales_modelform,Sales_items_bridge_modelform,Sales_GST_Wise_modelform,Sales_Returns_modelform,Sales_Items_Return_Bridge_modelform,Sales_Returns_GST_Wise_modelform)


def salesform(request):
    assigned_state=settings.CUSTOM_VALUES[0]['state_code']
    #print(assigned_state[0]['state_code'])
    template_name="salesapp/sales.html"
    sales_formset=inlineformset_factory(Sales,Sales_Items_Bridge,fields=("sales_no","sales_item","sales_item_code","salesitem_quantity","salesitem_hsncode","sales_uom","salesitem_rate","salesitem_disc","salesitem_taxable","salesitem_tax","salesitem_CGST","salesitem_CGSTamnt","salesitem_SGSTamnt","salesitem_SGST","salesitem_IGST","salesitem_IGSTamnt","salesitem_amnt"),extra=1,can_delete=True)
    salesmodel=Sales_modelform()
    #gstwisemodellist=Sales_GST_Wise.objects.all()
    if request.method=="GET":
        sales_formsetmodel=sales_formset()
        context={"SalesForm":salesmodel,"ItemsBridgeForm":sales_formsetmodel,"StateCode":assigned_state}
        return render(request,template_name,context)
    elif request.method=="POST":
        sales_master=Sales_modelform(request.POST)
        if sales_master.is_valid():
            sales_master.save()
            latest_sales=Sales.objects.last()
            latest_salesobj=Sales.objects.get(sales_id=latest_sales.sales_id)
            sales_formsetmodel=sales_formset(request.POST)
            if sales_formsetmodel.is_valid():
                instances=sales_formsetmodel.save(commit=False)
                for instance in instances:
                    instance.sales_no=latest_salesobj
                    stock_update(instance.sales_item,instance.salesitem_quantity,instance.sales_uom,op="subtraction")
                    instance.save()

                sales_gst_wise_table(latest_sales,'create')
            salesmodel=Sales_modelform()
            sales_formsetmodel=sales_formset()
            context={"SalesForm":salesmodel,"ItemsBridgeForm":sales_formsetmodel,"StateCode":assigned_state}
            return render(request,template_name,context)
        else:
            print(sales_master.errors)
            sales_formsetmodel=sales_formset()
            context={"SalesForm":salesmodel,"ItemsBridgeForm":sales_formsetmodel,"StateCode":assigned_state}
            return render(request,template_name,context)


def sales_gst_wise_table(latest_sales,mode):
    sales_item_list=Sales_Items_Bridge.objects.filter(sales_no=latest_sales)
    #sales_item_details=Sales_Items_Bridge.objects.get(sales_no=latest_sales)
    #print(statecode)
    if mode=="edit":
        Sales_GST_Wise.filter(sales_no=latest_sales).delete()

    calculate_gstwise=sales_item_list.values('salesitem_tax').annotate(cgst_amnt=Sum('salesitem_CGSTamnt'),sgst_amnt=Sum('salesitem_SGSTamnt'),igst_amnt=Sum('salesitem_IGSTamnt'),taxable_amnt=Sum('salesitem_taxable'))
    #print (calculate_gstwise)
    gstwise_model=Sales_GST_Wise()
    for item in calculate_gstwise:
        gstwise_model.sales_no=latest_sales
        gstwise_model.sales_receiptno=latest_sales.sales_invoiceno
        gstwise_model.salesgst_rate=item['salesitem_tax']
        gstwise_model.sales_taxable_amount=item['taxable_amnt']
        gstwise_model.sales_CGST_amount=item['cgst_amnt']  
        gstwise_model.sales_SGST_amount=item['sgst_amnt']
        gstwise_model.sales_IGST_amount=item['igst_amnt']
        
        gstwise_model.sales_CGST=0
        gstwise_model.sales_SGST=0
        gstwise_model.sales_IGST=0
        gstwise_model.save()
def stock_update(item,quantity,unit,op):
    itemobj=Product.objects.get(product_id=item.product_id)
    stockobj=Stock.objects.filter(stock_item=itemobj).first()
    base_quantity=0
    if itemobj.base_unit!=unit:
        uom_conversionobj=UOM_Conversion.objects.get(fromunit=unit,tounit=itemobj.base_unit)
        operation=uom_conversionobj.operations
        conversion_factor=uom_conversionobj.conversion_value
        if operation=="Multiplication":
            base_quantity=quantity*conversion_factor
        if operation=="Division":
            base_quantity=quantity/conversion_factor
        else:
            base_quantity=quantity
        if stockobj==None:
            stock_obj=Stock()
            stock_obj.stock_item=itemobj
            stock_obj.stock_UOM=itemobj.base_unit
            stock_obj.stock_quantity=base_quantity
            stock_obj.save()
        elif stockobj!=None:
            stockobj.stock_item=itemobj
            stockobj.stock_UOM=itemobj.base_unit
            if op=="addition":
                stockobj.stock_quantity=stockobj.stock_quantity+base_quantity
            elif op=="subtraction":
                stockobj.stock_quantity=stockobj.stock_quantity-base_quantity
            stockobj.save()
        return base_quantity

def sales_register_reoprt(request):
    template_name="salesapp/sales_registerreport.html"
    salesitemslist=Sales_Items_Bridge.objects.all().order_by('sales_no__invoice_date','sales_no__customer__party_name')
    if request.method=="GET":
        context={"SalesItemsList":salesitemslist}
        return render(request,template_name,context)

def sales_summary_report(request):
    template_name="salesapp/sales_summary_report.html"
    salessummarylist=Sales.objects.all()
    if request.method=="GET":
        context={"SalesSummaryList":salessummarylist}
        return render(request,template_name,context)

# ** Sales ** set state code according to the selected state name 
def set_state_code(request):
    #print("hi")
    stateobj=request.GET.get('commonid')
    state=State.objects.get(state_id=stateobj)
    scode=state.state_code
    return JsonResponse(scode,safe=False)

# ** Sales ** set the contact number accoriding to the selected customer
def get_contactno(request):
    partyid=request.GET.get('commonid')
    partyobj=Party.objects.get(party_id=partyid)
    contact_no=partyobj.contact_no
    return JsonResponse(contact_no,safe=False)

# ** Sales ** set the  tax,hsn code and and item code according to the selected item
def sales_hsn_gst_select(request):
    itemid=request.GET.get('itemid')
    productobj=Product.objects.filter(product_id=itemid)[0]
    
    #print(productobj)
    dict_to_pass={"item_code":productobj.product_code,"hsn_code":productobj.category.hsn_code,"gst_percent":productobj.category.gst_percent}
    #print(dict_to_pass)
    return JsonResponse(dict_to_pass,safe=False)
def sales_formset_configuration(sales_formset):
    sales_formsetmodel=sales_formset()
    sales_formsetmodel[0].fields["sales_item_code"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_hsncode"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_taxable"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_tax"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_CGST"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_CGSTamnt"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_SGST"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_SGSTamnt"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_IGST"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_IGSTamnt"].widget.attrs.update({"readonly":"readonly"})
    sales_formsetmodel[0].fields["salesitem_amnt"].widget.attrs.update({"readonly":"readonly"})
    return sales_formsetmodel

def salesmodel_return_configuration():
    salesmodel=Sales_Returns_modelform()
    salesmodel.fields["sales_subtotal"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_SGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_CGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_IGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_taxableamnt"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_Discount"].widget.attrs.update({"readonly":"readonly","value":0})
    salesmodel.fields["sales_GTotal"].widget.attrs.update({"readonly":"readonly","value":0})
    return salesmodel

def sales_returnsform(request):
    template_name="salesapp/sales_returns.html"
    sales_return_formset=inlineformset_factory(Sales_Returns,Sales_Items_Return_Bridge,fields=("sales_returns_no","sales_item","sales_item_code","salesitem_quantity","salesitem_hsncode","sales_uom","salesitem_rate","salesitem_disc","salesitem_taxable","salesitem_tax","salesitem_CGST","salesitem_CGSTamnt","salesitem_SGSTamnt","salesitem_SGST","salesitem_IGST","salesitem_IGSTamnt","salesitem_amnt"),extra=1,can_delete=True)
    salesmodel=Sales_modelform()
    if request.method=="GET":
        #purchasemodel=purchasemodel_return_configuration()
        salesmodel=salesmodel_return_configuration()
        sales_returns_formsetmodel=sales_formset_configuration(sales_return_formset)
        context={"SalesReturnForm":salesmodel,"BridgeReturnForm":sales_returns_formsetmodel}
        return render(request,template_name,context)
    elif request.method=="POST":
        sales_returns_master=Sales_Returns_modelform(request.POST)
        if sales_returns_master.is_valid():
            sales_returns_master.save()
            latest_sales=Sales_Returns.objects.last()
            latest_salesobj=Sales_Returns.objects.get(salesreturns_id=latest_sales.salesreturns_id)
            sales_return_formsetmodel=sales_return_formset(request.POST)
            if sales_return_formsetmodel.is_valid():
                instances=sales_return_formsetmodel.save(commit=False)
                for instance in instances:
                    stockobj=Stock.objects.get(stock_item=instance.sales_item)
                    instance.base_uom=stockobj.stock_UOM
                    instance.sales_returns_no=latest_salesobj
                    base_quantity=stock_update(instance.sales_item,instance.salesitem_quantity,instance.sales_uom,op="subtraction")
                    print(base_quantity)
                    instance.base_salesitem_quantity=base_quantity
                    instance.save()
                return_gst_wise_table(latest_sales,mode='create')
            salesmodel=Sales_Returns_modelform()
            sales_return_formsetmodel=sales_formset_configuration(sales_return_formset)
        context={"SalesReturnForm": salesmodel,"BridgeReturnForm":sales_return_formsetmodel}
        return render(request,template_name,context)

def salesreturninfo(request):
    invoiceno=request.GET.get('invoice_no')
    #print(invoiceno)
    item_dict={}
    return_dict={}
    if request.method=="GET":
        salesinfoobj=Sales.objects.filter(sales_invoiceno=invoiceno).values('sales_state__state_name','invoice_date','sales_credit','customer__party_name','sales_type','sales_Discount','sales_Paymode__payment_method')
        sales=Sales.objects.get(sales_invoiceno=invoiceno)
        salesitemlist=Sales_Items_Bridge.objects.filter(sales_no=sales).values('sales_item__product_id','sales_item__product_name')
        for item in salesitemlist:
            item_dict[item.get('sales_item__product_id')]=item.get('sales_item__product_name')
        return_dict['sales_details']=salesinfoobj[0]
        return_dict['item_details']=item_dict
        return JsonResponse(return_dict,safe=False)

def salesitem_bridge_fields(request):
    #print('im here')
    all_dict={}
    item_dict={}
    invoice_no=request.GET.get('invoice_no')
    citem=request.GET.get('item')
    if request.method=="GET":
        #print('im here')
        sales_obj=Sales.objects.get(sales_invoiceno=invoice_no)
        itemobj=Product.objects.get(product_id=citem)
        itembridgelist=Sales_Items_Bridge.objects.filter(sales_item=itemobj).filter(sales_no=sales_obj).values('sales_item_code','salesitem_quantity','salesitem_hsncode','sales_uom__unit_shortname',
        'salesitem_rate','salesitem_disc','salesitem_taxable','salesitem_tax','salesitem_CGST','salesitem_CGSTamnt','salesitem_SGST','salesitem_SGSTamnt','salesitem_IGST','salesitem_IGSTamnt','salesitem_amnt')
        returned_quantitylist=Sales_Items_Return_Bridge.objects.filter(sales_item=itemobj).filter(sales_returns_no__return_salesinvoiceno=sales_obj).values('salesitem_quantity').aggregate(Sum('salesitem_quantity'))
        for item in itembridgelist:
            prev_quantity=item.get('salesitem_quantity')
            if returned_quantitylist ['salesitem_quantity__sum']!=None:
                current_quantity=prev_quantity-returned_quantitylist.get('salesitem_quantity__sum')
            else:
                current_quantity=prev_quantity
            item_dict['item_code']=item.get('sales_item_code')
            item_dict['quantity']=current_quantity
            item_dict['hsn_code']=item.get('salesitem_hsncode')
            item_dict['uom']=item.get('sales_uom__unit_shortname')
            item_dict['rate']=item.get('salesitem_rate')
            item_dict['disc']=item.get('salesitem_disc')
            item_dict['taxable']=item.get('salesitem_taxable')
            item_dict['tax']=item.get('salesitem_tax')
            item_dict['CGST']=item.get('salesitem_CGST')
            item_dict['CGSTamnt']=item.get('salesitem_CGSTamnt')
            item_dict['SGST']=item.get('salesitem_SGST')
            item_dict['SGSTamnt']=item.get('salesitem_SGSTamnt')
            item_dict['IGST']=item.get('salesitem_IGST')
            item_dict['IGSTamnt']=item.get('salesitem_IGSTamnt')
            item_dict['amount']=item.get('salesitem_amnt')
    return JsonResponse(item_dict,safe=False)
                






# Create your views here.
