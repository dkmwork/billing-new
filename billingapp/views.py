from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q,Sum,DecimalField
from django.forms import modelformset_factory,inlineformset_factory
from django.http import JsonResponse,HttpResponse
from billingapp.models import (State,City,Unit,Category_GST,UOM,UOM_Conversion,Financial_Year,Company,Branch,
User,Product,Party,Payment_Mode,Purchase,Payment_Details,Stock,Purchase_Items_Bridge,GST_wise,Purchase_Returns,Purchase_Items_Returns_Bridge,Purchase_Returns_GST_wise)
from billingapp.forms import (State_modelform,City_modelform,Unit_modelform,Category_GST_modelform,UOM_modelform,UOM_conversion_modelform,
Financial_year_modelform,Company_modelform,Branch_modelform,User_modelform,Product_modelform,Party_modelform,Payment_mode_modelform,
Purchase_modelform,Payment_details_modelform,Stock_modelform,Purchase_items_bridge_modelform,GST_wise_modelform,Purchase_returns_modelform,Purchase_items_returns_bridge_modelform,Purchase_returns_GST_wise_modelform)

def stateform(request):
    template_name="billingapp/stateform.html"
    stateform=State_modelform()
    if request.method=="GET":
        context={"MyState":stateform}
        return render(request,template_name,context)
    elif request.method=="POST":
       stateform=State_modelform(request.POST)
       context={"MyState":stateform}
       if stateform.is_valid():
           stateform.save()
           stateform=State_modelform()
           context={"MyState":stateform}
           return render(request,template_name,context) 
    return render(request,template_name,context)
def citymodelform(request):
    template_name="billingapp/cityform.html"
    if request.method=="GET":
        cityform=City_modelform()
        context={"MyCity":cityform}
        return render(request,template_name,context)
    elif request.method=="POST":
        cityform=City_modelform(request.POST)
        if cityform.is_valid():
            context={"MyCity":cityform}
            cityform.save()
            cityform=City_modelform()
            context={"MyCity":cityform}
            return render(request,template_name,context)
    return render(request,template_name,context)
'''def unitmodelform(request):
    template_name="billingapp/unitform.html"
    if request.method=="GET":
        unitform=Unit_modelform()
        context={"MyUnit":unitform}
        return render(request,template_name,context)
    elif request.method=="POST":
        unitform=Unit_modelform(request.POST)
        if unitform.is_valid():
            context={"MyUniut":unitform}
            unitform.save()
            unitform=Unit_modelform()
            context={"MyUniut":unitform}
            return render(request, template_name,context)
    return render(request, template_name,context)'''
def categorymodelform(request):
    template_name="billingapp/categoryform.html"
    if request.method=="GET":
        categoryform=Category_GST_modelform()
        context={"GST":categoryform}
        return render(request,template_name,context)
    elif request.method=="POST":
        categoryform=Category_GST_modelform(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            categoryform=Category_GST_modelform()
            context={"GST":categoryform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def uommodelform(request):
    template_name="billingapp/uomform.html"
    if request.method=="GET":
        uomform=UOM_modelform()
        context={"UOM":uomform}
        return render(request,template_name,context)
    elif request.method=="POST":
        uomform=UOM_modelform(request.POST)
        if uomform.is_valid():
            uomform.save()
            uomform=UOM_modelform()
            context={"UOM":uomform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def uomconversion_modelform(request):
    template_name='billingapp/uom_conversionform.html'
    if request.method=="GET":
        uomconversionform=UOM_conversion_modelform()
        context={"UOMConversion":uomconversionform}
        return render(request,template_name,context)
    elif request.method=="POST":
        uomconversionform=UOM_conversion_modelform(request.POST)
        if uomconversionform.is_valid():
            uomconversionform.save()
            uomconversionform=UOM_conversion_modelform()
            context={"UOMConversion":uomconversionform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def financialyear_modelformset(request):
    template_name="billingapp/financialyear_modelformset.html"
    financialyear_modelformset=modelformset_factory(Financial_Year,exclude=('year_id',),extra=1)
    financialyear_formset=financialyear_modelformset(queryset=Financial_Year.objects.filter(year_id=0))
    if request.method=="GET":
        context={"FinancialYear":financialyear_formset}
        return render(request,template_name,context)
    if request.method=="POST":
        financialyear_formset=financialyear_modelformset(request.POST)
        if financialyear_formset.is_valid():
            for year in financialyear_formset:
                year.save()       
        context={"FinancialYear":financialyear_formset}
        return render(request, template_name,context)
    return render(request, template_name,context)

def companymodelform(request):
    template_name='billingapp/companyform.html'
    if request.method=="GET":
        companyform=Company_modelform()
        context={"Company":companyform}
        return render(request,template_name,context)
    elif request.method=="POST":
        companyform=Company_modelform(request.POST)
        if companyform.is_valid():
            companyform.save()
            companyform=Company_modelform()
            context={"Company":companyform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def branchmodelform(request):
    template_name="billingapp/branchform.html"
    if request.method=="GET":
        branchform=Branch_modelform()
        context={"MyBranch":branchform}
        return render(request,template_name,context)
    elif request.method=="POST":
        branchform=Branch_modelform(request.POST)
        if branchform.is_valid():
            branchform.save()
            branchform=Branch_modelform()
            context={"MyBranch":branchform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def usermodelform(request):
    template_name="billingapp/userform.html"
    if request.method=="GET":
        userform=User_modelform()
        context={"MyUser":userform}
        return render(request,template_name,context)
    elif request.method=="POST":
        userform=User_modelform(request.POST)
        if userform.is_valid():
            userform.save()
            userform=User_modelform()
            context={"MyUser":userform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def productmodelform(request):
    template_name="billingapp/productform.html"
    if request.method=="GET":
        productform=Product_modelform()
        context={"MyProduct":productform}
        return render(request,template_name,context)
    elif request.method=="POST":
        productform=Product_modelform(request.POST)
        if productform.is_valid():
            productform.save()
            productform=Product_modelform()
            context={"MyProduct":productform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def change_to_dictionary_gst(current_list):
    change_dict=[item for item in current_list]
    new_dict={}
    for item in change_dict:
        itemid=item.category_id
        itemgst=item.gst_percent
        itemhsn=item.hsn_code
        current_dict={"item_id":itemid,"gst":itemgst,"hsn":itemhsn}
        new_dict[itemid]=current_dict
        #print(new_dict)
    return new_dict
def gst_and_hsn_select(request):
    if request.method=="GET":
        categoryname=request.GET.get('categoryname')
        #print(categoryname)
        current_list=Category_GST.objects.filter(category_id=categoryname)
        #print(current_list)
        new_list=change_to_dictionary_gst(current_list)
        #print(new_list)
        return JsonResponse(new_list,safe=False)

def partymodelform(request):
    template_name="billingapp/partyform.html"
    if request.method=="GET":
        partyform=Party_modelform()
        context={"MyParty":partyform}
        return render(request,template_name,context)
    elif request.method=="POST":
        partyform=Party_modelform(request.POST)
        if partyform.is_valid():
            partyform.save()
            partyform=Party_modelform()
            context={"MyParty":partyform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def Paymentmode_modelform(request):
    template_name="billingapp/paymentmodeform.html"
    if request.method=="GET":
        paymentform=Payment_mode_modelform()
        context={"MyPayment":paymentform}
        return render(request,template_name,context)
    elif request.method=="POST":
        paymentform=Payment_mode_modelform(request.POST)
        if paymentform.is_valid():
            paymentform.save()
            paymentform=Payment_mode_modelform()
            context={"MyPayment":paymentform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def is_present(value_obj):
    if len(value_obj)==0:
        x=0
        return x
    else:
        x=1
        return x
def check_duplicate(request):
    if request.method=="GET":
        check_no=request.GET.get('check_no')
        current_value=request.GET.get('value')
        if int(check_no)==0:
            state_obj=State.objects.filter(state_name__exact=current_value)
            x=is_present(state_obj)
            print (x)
            return JsonResponse(x,safe=False)
        elif int(check_no)==1:
            scode_obj=State.objects.filter(state_code__exact=current_value)
            x=is_present(scode_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==2:
            sshrtname_obj=State.objects.filter(state_shortname__exact=current_value)
            
            x=is_present(sshrtname_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==3:
            city_obj=City.objects.filter(city_name__exact=current_value)
            x=is_present(city_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==4:
            cshrtname_obj=City.objects.filter(city_shortname__exact=current_value)
            x=is_present(cshrtname_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==5:
            gst_obj=GST.objects.filter(gst_percent__exact=current_value)
            x=is_present(gst_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==6:
            unit_shrtname_obj=UOM.objects.filter(unit_shortname__exact=current_value)
            x=is_present(unit_shrtname_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==7:
            unit_longhname_obj=UOM.objects.filter(unit_longname__exact=current_value)
            x=is_present(unit_longhname_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==8:
            year_obj=Financial_Year.objects.filter(finacial_year__exact=current_value)
            x=is_present(year_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==9:
            company_obj=Company.objects.filter(company_name__exact=current_value)
            x=is_present(company_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==10:
            cemail_obj=Company.objects.filter(company_email__exact=current_value)
            x=is_present(cemail_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==11:
            curl_obj=Company.objects.filter(company_url__exact=current_value)
            x=is_present(curl_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==12:
            product_obj=Product.objects.filter(product_name__exact=current_value)
            x=is_present(product_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==13:
            pcode_obj=Product.objects.filter(product_code__exact=current_value)
            x=is_present(pcode_obj)
            return JsonResponse(x,safe=False)
        elif int(check_no)==14:
            party_obj=Party.objects.filter(party_name__exact=current_value)
            x=is_present(party_obj)
            return JsonResponse(x,safe=False)

def statelist(request):
    #print("I'm here")
    template_name="billingapp/statelistcard.html"
    statelist=State.objects.all()
    context={"StateList":statelist}
    if request.method=="GET":
        return render(request,template_name,context)
def state_edit(request,stateid=None):
    template_name="billingapp/stateinfo.html"
    if request.method=="GET" and stateid!=None:
        statemodel=State.objects.get(state_id=stateid)
        statemodelform=State_modelform(instance=statemodel)
        context={"stateinstance":statemodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and stateid!=None:
        statemodel=State.objects.get(state_id=stateid)
        statemodelform=State_modelform(request.POST,instance=statemodel)
        if statemodelform.is_valid():
            statemodelform.save()
            statemodelform=State_modelform()
            context={"stateinstance":statemodelform}
            return render(request,template_name,context)
        else:
            context={"stateinstance":statemodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def change_to_dictionary_state(statelist):
    state_dict=[state for state in statelist]
    #print(state_dict)
    dict_to_return={}
    for state_info in state_dict:
        statename=state_info.state_name
        statecode=state_info.state_code
        stateshortname=state_info.state_shortname
        new_dict={"statename":statename,"statecode":statecode,"stateshortname":stateshortname}
        #print(new_dict)
        dict_to_return[state_info.state_id]=new_dict
        #print(dict_to_return)
    return dict_to_return
def statesearch(request):
    #print("I'm here")
    template_name="billinghapp/stateinfo.html"
    query=Q()
    if request.method=="GET":
        page_num=request.GET.get('page',1)
        print(page_num)
        statename=request.GET.get('statename','')
        statecode=request.GET.get('statecode','')
        stateshortname=request.GET.get('stateshortname','')
        intpage_num=int(page_num)
        start_num=(intpage_num-1)*2
        end_num=start_num+2
        if statename !='':
            query &=Q(state_name__contains=statename)
        if statecode !='':
            query &=Q(state_code__contains=statecode)
        if stateshortname !='':
            query &=Q(state_shortname__contains=stateshortname)
        if query !='(AND: )':
            #print(query)
        
            statelist=State.objects.filter(query)
            #print(statelist)
            total_count=statelist.count()
            statelist=statelist[start_num:end_num]
            #print(statelist)
        else:
            statelist=State.objects.all()
            print("I'm in else")
        #print(statelist)
        new_statelist=change_to_dictionary_state(statelist)
        #print(new_statelist)
        new_statelist['total_count']={'queryset_count':total_count}
        print(new_statelist)
        return JsonResponse(new_statelist,safe=False)

def citylist(request):
    template_name="billingapp/citylistcard.html"
    citylist=City.objects.all()
    context={"CityList":citylist}
    if request.method=="GET":
        return render(request,template_name,context)
def city_edit(request,cityid=None):
    template_name="billingapp/cityinfo.html"
    if request.method=="GET" and cityid!=None:
        citymodel=City.objects.get(city_id=cityid)
        citymodelform=City_modelform(instance=citymodel)
        context={"cityinstance":citymodelform}
        return render(request,template_name,context)
    elif request.method=='POST' and cityid!=None:
        citymodel=City.objects.get(city_id=cityid)
        citymodelform=City_modelform(request.POST,instance=citymodel)
        if citymodelform.is_valid():
            citymodelform.save()
            citymodelform=City_modelform()
            context={"cityinstance":citymodelform}
            return render(request,template_name,context)
        else:
            context={"cityinstance":citymodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def financial_yearlist(request):
    template_name="billingapp/financial_yearlistcard.html"
    yearlist=Financial_Year.objects.all()
    context={"YearList":yearlist}
    return render(request,template_name,context)
def financial_year_edit(request,yearid=None):
    template_name="billingapp/financial_yearinfo.html"
    if request.method=="GET" and yearid!=None:
        yearlmodel=Financial_Year.objects.get(year_id=yearid)
        yearlmodelform=Financial_year_modelform(instance=yearlmodel)
        context={"yearinstance":yearlmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and yearid!=None:
        yearmodel=Financial_Year.objects.get(year_id=yearid)
        yearmodelform=Financial_year_modelform(request.POST,instance=yearmodel)
        if yearmodelform.is_valid():
            yearmodelform.save()
            yearmodelform=Financial_year_modelform()
            context={"yearinstance":yearmodelform}
            return render(request,template_name,context)
        else:
            context={"yearinstance":yearmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def categorylist(request):
    template_name="billingapp/categorylistcard.html"
    categorylist=Category_GST.objects.all()
    context={"CategoryList":categorylist}
    return render(request,template_name,context)
def category_edit(request,categoryid=None):
    template_name="billingapp/categoryinfo.html"
    if request.method=="GET" and categoryid!=None:
        categorymodel=Category_GST.objects.get(category_id=categoryid)
        categorymodelform=Category_GST_modelform(instance=categorymodel)
        context={"categoryinstance":categorymodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and categoryid!=None:
        categorymodel=Category_GST.objects.get(category_id=categoryid)
        categorymodelform=Category_GST_modelform(request.POST,instance=categorymodel)
        if categorymodelform.is_valid():
            categorymodelform.save()
            categorymodelform=Category_GST_modelform()
            context={"categoryinstance":categorymodelform}
            return render(request,template_name,context)
        else:
            context={"categoryinstance":categorymodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def change_to_dictionary_category(categorylist):
    category_dict=[item for item in categorylist]
    dict_to_return={}
    for category_info in category_dict:
        categoryname=category_info.category_name
        gstpercent=category_info.gst_percent
        hsncode=category_info.hsn_code
        financialyear=category_info.financial_year.finacial_year
        new_dict={"categoryname":categoryname,"gstpercent":gstpercent,"hsncode":hsncode,"financialyear":financialyear}
        dict_to_return[category_info.category_id]=new_dict
    return dict_to_return
def categorysearch(request):
    template_name="billingapp/categorylist.html"
    query=Q()
    if request.method=="GET":
        page_num=request.GET.get('page',1)
        categoryname=request.GET.get('categoryname','')
        gstpercent=request.GET.get('gstpercent','')
        hsncode=request.GET.get('hsncode','')
        financialyear=request.GET.get('financialyear','')
        intpage_num=int(page_num)
        start_num=(intpage_num-1)*2
        end_num=start_num+2
        if categoryname!='':
            query &=Q(category_name__contains=categoryname)
        if gstpercent!='':
            query &=Q(gst_percent__contains=gstpercent)
        if hsncode!='':
            query &=Q(hsn_code__contains=hsncode)
        if financialyear!='':
            query &=Q(financial_year__finacial_year__contains=financialyear)
        if query!='(AND: )':
            categorylist=Category_GST.objects.filter(query)
            #print(categorylist)
            total_count=categorylist.count()
            categorylist=categorylist[start_num:end_num]
            print(categorylist)
        else:
            categorylist=Category_GST.objects.all()
        new_categorylist=change_to_dictionary_category(categorylist)
        new_categorylist['total_count']={'queryset_count':total_count}
        return JsonResponse(new_categorylist,safe=False)

def uomlist(request):
    template_name="billingapp/uomlistcard.html"
    uomlist=UOM.objects.all()
    context={"UomList":uomlist}
    return render(request,template_name,context)
def uom_edit(request,uomid=None):
    template_name="billingapp/uominfo.html"
    if request.method=="GET" and uomid!=None:
        uommodel=UOM.objects.get(unit_id=uomid)
        uommodelform=UOM_modelform(instance=uommodel)
        context={"uominstance":uommodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and uomid!=None:
        uommodel=UOM.objects.get(unit_id=uomid)
        uommodelform=UOM_modelform(request.POST,instance=uommodel)
        if uommodelform.is_valid():
            uommodelform.save()
            uommodelform=UOM_modelform()
            context={"uominstance":uommodelform}
            return render(request,template_name,context)
        else:
            context={"uominstance":uommodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def uom_conversionlist(request):
    template_name="billingapp/uom_conversionlistcard.html"
    uom_conversionlist=UOM_Conversion.objects.all()
    context={"UomConversionList":uom_conversionlist}
    return render(request,template_name,context)
def uom_conversion_edit(request,conversionid=None):
    template_name="billingapp/uom_conversioninfo.html"
    if request.method=="GET" and conversionid!=None:
        uom_conversionmodel=UOM_Conversion.objects.get(conversion_id=conversionid)
        uom_conversionmodelform=UOM_conversion_modelform(instance=uom_conversionmodel)
        context={"uom_conversioninstance":uom_conversionmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and conversionid!=None:
        uommodel=UOM_Conversion.objects.get(conversion_id=conversionid)
        uom_conversionmodelform=UOM_conversion_modelform(request.POST,instance=uom_conversionmodel)
        if uom_conversionmodelform.is_valid():
            uom_conversionmodelform.save()
            uom_conversionmodelform=UOM_conversion_modelform()
            context={"uom_conversioninstance":uom_conversionmodelform}
            return render(request,template_name,context)
        else:
            context={"uom_conversioninstance":uom_conversionmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def companylist(request):
    template_name="billingapp/companylistcard.html"
    companylist=Company.objects.all()
    context={"CompanyList":companylist}
    return render(request,template_name,context)
def company_edit(request,companyid=None):
    template_name="billingapp/companyinfo.html"
    if request.method=="GET" and companyid!=None:
        companymodel=Company.objects.get(company_id=companyid)
        companymodelform=Company_modelform(instance=companymodel)
        context={"companyinstance":companymodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and companyid!=None:
        companymodel=Company.objects.get(company_id=companyid)
        companymodelform=Company_modelform(request.POST,instance=companymodel)
        print(companymodelform.errors)
        if companymodelform.is_valid():
            print("im here")
            companymodelform.save()
            companymodelform=Company_modelform()
            context={"companyinstance":companymodelform}
            return render(request,template_name,context)
        else:
            context={"companyinstance":companymodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def branchlist(request):
    template_name="billingapp/branchlistcard.html"
    branchlist=Branch.objects.all()
    context={"BranchList":branchlist}
    return render(request,template_name,context)
def branch_edit(request,branchid=None):
    template_name="billingapp/branchinfo.html"
    if request.method=="GET" and branchid!=None:
        branchmodel=Branch.objects.get(branch_id=branchid)
        branchmodelform=Branch_modelform(instance=branchmodel)
        context={"branchinstance":branchmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and branchid!=None:
        branchmodel=Branch.objects.get(branch_id=branchid)
        branchmodelform=Branch_modelform(request.POST,instance=branchmodel)
        if branchmodelform.is_valid():
            branchmodelform.save()
            branchmodelform=Branch_modelform()
            context={"branchinstance":branchmodelform}
            return render(request,template_name,context)
        else:
            context={"branchinstance":branchmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def userlist(request):
    template_name="billingapp/userlistcard.html"
    userlist=User.objects.all()
    context={"UserList":userlist}
    return render(request,template_name,context)
def user_edit(request,userid=None):
    template_name="billingapp/userinfo.html"
    if request.method=="GET" and userid!=None:
        usermodel=User.objects.get(user_id=userid)
        usermodelform=User_modelform(instance=usermodel)
        context={"userinstance":usermodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and userid!=None:
        usermodel=User.objects.get(user_id=userid)
        usermodelform=User_modelform(request.POST,instance=usermodel)
        if usermodelform.is_valid():
            usermodelform.save()
            usermodelform=User_modelform()
            context={"userinstance":usermodelform}
            return render(request,template_name,context)
        else:
            context={"userinstance":usermodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def productlist(request):
    template_name="billingapp/productlistcard.html"
    productlist=Product.objects.all()
    context={"ProductList":productlist}
    return render(request,template_name,context)
def product_edit(request,productid=None):
    template_name="billingapp/productinfo.html"
    if request.method=="GET" and productid!=None:
        productmodel=Product.objects.get(product_id=productid)
        productmodelform=Product_modelform(instance=productmodel)
        context={"productinstance":productmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and productid!=None:
        productmodel=Product.objects.get(product_id=productid)
        productmodelform=Product_modelform(request.POST,instance=productmodel)
        if productmodelform.is_valid():
            productmodelform.save()
            productmodelform=Product_modelform()
            context={"productinstance":productmodelform}
            return render(request,template_name,context)
        else:
            context={"productinstance":productmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def change_to_dictionary_product(productlist):
    product_dict=[item for item in productlist]
    dict_to_return={}
    for product_info in product_dict:
        pcategory=product_info.category.category_name
        productname=product_info.product_name
        productcode=product_info.product_code
        baseunit=product_info.base_unit.unit_shortname
        new_dict={"pcategory":pcategory,"productname":productname,"productcode":productcode,"baseunit":baseunit}
        dict_to_return[product_info.product_id]=new_dict
    return dict_to_return     
def productsearch(request):
    print("hi")
    template_name="billingapp/productlist.html"
    query=Q()
    if request.method=="GET":
        page_num=request.GET.get('page',1)
        pcategory=request.GET.get('pcategory','')
        print(pcategory)
        productname=request.GET.get('productname','')
        #print(productname)
        productcode=request.GET.get('productcode','')
        baseunit=request.GET.get('baseunit','')
        intpage_num=int(page_num)
        start_num=(intpage_num-1)*2
        end_num=start_num+2
        if pcategory!='':
            query &=Q(category__category_name__contains=pcategory)
        if productname!='':
            query &=Q(product_name__contains=productname)
        if productcode !='':
            query &=Q(product_code__contains=productcode)
        if baseunit!='':
            query &=Q(base_unit__unit_shortname__contains=baseunit) 
        if query!='(AND: )':
            print(query)
            productlist=Product.objects.filter(query)
            #print(productlist)
            total_count=productlist.count()
            print(total_count)
            productlist=productlist[start_num:end_num]
            #print(productlist)
        else:
            productlist=Product.objects.all()
        new_productlist=change_to_dictionary_product(productlist)
        new_productlist['total_count']={'queryset_count':total_count}
        return JsonResponse(new_productlist,safe=False)

def partylist(request):
    template_name="billingapp/partylistcard.html"
    partylist=Party.objects.all()
    context={"PartyList":partylist}
    return render(request,template_name,context)
def party_edit(request,partyid=None):
    template_name="billingapp/partyinfo.html"
    if request.method=="GET" and partyid!=None:
        partymodel=Party.objects.get(party_id=partyid)
        partymodelform=Party_modelform(instance=partymodel)
        context={"partyinstance":partymodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and partyid!=None:
        partymodel=Party.objects.get(party_id=partyid)
        partymodelform=Party_modelform(request.POST,instance=partymodel)
        if partymodelform.is_valid():
            partymodelform.save()
            partymodelform=Party_modelform()
            context={"partyinstance":partymodelform}
            return render(request,template_name,context)
        else:
            context={"partyinstance":partymodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def change_to_dictionary_party(partylist):
    party_dict=[item for item in partylist]
    dict_to_return={}
    for party_info in party_dict:
        partyname=party_info.party_name
        partystreet=party_info.party_street
        partycity=party_info.party_city.city_name
        partystate=party_info.party_state.state_name
        contactnumber=party_info.contact_no
        partyemail=party_info.party_email
        gst=party_info.party_GST
        partycategory=party_info.party_category
        partytype=party_info.party_type
        new_dict={"partyname":partyname,"partystreet":partystreet,"partycity":partycity,"partystate":partystate,"contactnumber":contactnumber,"partyemail":partyemail,"gst":gst,"partycategory":partycategory,"partytype":partytype}
        dict_to_return[party_info.party_id]=new_dict
    return dict_to_return     

def partysearch(request):
    template_name="billingapp/partylist.html"
    query=Q()
    if request.method=="GET":
        page_num=request.GET.get('page',1)
        partyname=request.GET.get('partyname','')
        contactno=request.GET.get('contactnumber','')
        intpage_num=int(page_num)
        start_num=(intpage_num-1)*2
        end_num=start_num+2
        if partyname!='':
            query &=Q(party_name__contains=partyname)
        if contactno !='':
            query &=Q(contact_no__contains=contactno)
        if query!='(AND: )':
            partylist=Party.objects.filter(query)
            #print(partylist)
            total_count=partylist.count()
            partylist=partylist[start_num:end_num]
        else:
            partylist=Party.objects.all()
        #print("here")
        new_partylist=change_to_dictionary_party(partylist)
        new_partylist['total_count']={'queryset_count':total_count}
        print(new_partylist)
        return JsonResponse(new_partylist,safe=False)

def payment_modelist(request):
    template_name="billingapp/payment_modelist.html"
    payment_modelist=Payment_Mode.objects.all()
    context={"Payment_ModeList":payment_modelist}
    return render(request,template_name,context)
def payment_mode_edit(request,payid=None):
    template_name="billingapp/payment_modeinfo.html"
    if request.method=="GET" and payid!=None:
        payment_modemodel=Payment_Mode.objects.get(pay_id=payid)
        payment_modemodelform=Payment_mode_modelform(instance=payment_modemodel)
        context={"payment_modeinstance":payment_modemodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and payid!=None:
        payment_modemodel=Payment_Mode.objects.get(pay_id=payid)
        payment_modemodelform=Payment_mode_modelform(request.POST,instance=payment_modemodel)
        if payment_modemodelform.is_valid():
            payment_modemodelform.save()
            payment_modemodelform=Payment_mode_modelform()
            context={"payment_modeinstance":payment_modemodelform}
            return render(request,template_name,context)
        else:
            context={"payment_modeinstance":payment_modemodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def purchasemodel_configuration():
    purchasemodel=Purchase_modelform()
    purchasemodel.fields["purchase_subtotal"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_SGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_CGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_IGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_GTotal"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_taxableamnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_Discount"].widget.attrs.update({"value":'0'})
    return purchasemodel
def purchaseformset_configuration(purchase_formset):
    purchase_formsetmodel=purchase_formset()
    purchase_formsetmodel[0].fields["item_hsncode"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_taxable"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_tax"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_CGST"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_SGST"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_IGST"].widget.attrs.update({"readonly":"readonly"})
    purchase_formsetmodel[0].fields["item_amnt"].widget.attrs.update({"readonly":"readonly"})
    return purchase_formsetmodel
def purchaseform(request):
    template_name="billingapp/purchase.html"
    purchase_formset=inlineformset_factory(Purchase,Purchase_Items_Bridge,fields=("purchase_no","item","item_hsncode","item_quantity","item_rate","uom","item_disc","item_taxable","item_tax","item_CGST","item_SGST","item_IGST","item_amnt"),extra=1,can_delete=True)
    #print(purchase_formset)
    #purchase_formset.fields["item_rate"].widget.attrs.update({"class":"to_be_calculated"})
    if request.method=="GET":
        purchasemodel=purchasemodel_configuration()
        purchase_formsetmodel=purchaseformset_configuration(purchase_formset)
        context={"PurchaseForm": purchasemodel,"BridgeForm":purchase_formsetmodel}
        return render(request,template_name,context)
    elif request.method=="POST":
        #stockmodel=Stock_modelform(request.POST)
        #print(stockmodel) 
        purchase_master=Purchase_modelform(request.POST)
        if purchase_master.is_valid():
            purchase_master.save()
            latest_purchase=Purchase.objects.last()
            latest_purchaseobj=Purchase.objects.get(purchase_id=latest_purchase.purchase_id)
            purchase_formsetmodel=purchase_formset(request.POST)
            #print(purchase_formsetmodel.errors)
            if  purchase_formsetmodel.is_valid():
                instances=purchase_formsetmodel.save(commit=False)
                for instance in instances:
                    print(instance,"purchase")
                    instance.purchase_no=latest_purchaseobj
                    #itemobj=Purchase_Items_Bridge.objects.get(item=instance.item.product_id)
                    #if itemobj!=None:
                        #stock_update(instance.item,instance.item_quantity,instance.uom,op="subtraction")
                        #stock_update(instance.item,instance.item_quantity,instance.uom,op="addition")
                    #else:
                        #stock_update(instance.item,instance.item_quantity,instance.uom,op="addition")
                    stock_update(instance.item,instance.item_quantity,instance.uom,op="addition")
                    instance.save()
                    '''if purchase_formsetmodel.deleted_forms:
                        for obj in purchase_formsetmodel.deleted_objects:
                            print(obj)
                            obj.delete()'''
                gst_wise_table(latest_purchase,mode='create')
            purchasemodel=Purchase_modelform()
            purchase_formsetmodel=purchaseformset_configuration(purchase_formset)
            context={"PurchaseForm": purchasemodel,"BridgeForm":purchase_formsetmodel}
            return render(request,template_name,context)
        else:
            print("i'm in error")
            print(purchase_master.errors)
            purchase_formsetmodel=purchaseformset_configuration(purchase_formset)
            context={"PurchaseForm": purchase_master,"BridgeForm":purchase_formsetmodel}
            return render(request,template_name,context)
def gst_wise_table(latest_purchase,mode):
    #print("here am in GST !!!")
    purchase_item_list=Purchase_Items_Bridge.objects.filter(purchase_no=latest_purchase)
    #***************************
    if mode=="edit":
        GST_wise.objects.filter(purchase_no=latest_purchase).delete()
    #**********************
    calculate_gstwise=purchase_item_list.values('item_tax').annotate(cgst=Sum('item_CGST'),sgst=Sum('item_SGST'),igst=Sum('item_IGST'),amount=Sum('item_amnt'))
    #delete all items that come under this particular purchase no
    '''gst_model=GST_wise.objects.filter(purchase=purchase_no)
    for item in gst_model:
        item.delete()'''
    gst_wisemodel=GST_wise()
    for item in calculate_gstwise:
        #print(item)
        #print(item['item_tax'])
        # purchase_no is a Foregnkey in GST_wise
        gst_wisemodel.purchase_no=latest_purchase
        gst_wisemodel.purchase_receiptno=latest_purchase.invoice_no
        gst_wisemodel.gst_rate=item['item_tax']
        gst_wisemodel.taxable_amnt=item['amount']
        gst_wisemodel.CGST=item['cgst']
        gst_wisemodel.SGST=item['sgst']
        gst_wisemodel.IGST=item['igst']
        gst_wisemodel.save()
    
def stock_update(item,quantity,unit,op):
    print('im in unit')
    print(unit)
    itemobj=Product.objects.get(product_id=item.product_id)
   #print(itemobj)
    '''try:
        stockobj=Stock.objects.get(stock_item=itemobj)
    except Stock.DoesNotExists:
        stockobj=None'''
    stockobj=Stock.objects.filter(stock_item=itemobj).first()
    #print(stockobj)
    base_quantity=0
    if itemobj.base_unit!=unit:
        #print('im in here')
        uom_conversionobj=UOM_Conversion.objects.get(fromunit=unit,tounit=itemobj.base_unit)
        operation=uom_conversionobj.operations
        #print(operation)
        conversion_factor=uom_conversionobj.conversion_value
        if operation=="Multiplication":
            base_quantity=quantity*conversion_factor
        elif operation=="Division":
           
            base_quantity=quantity/conversion_factor 
    else:
        base_quantity=quantity 
    print(base_quantity)  
    if stockobj==None:
        #print('im in here secnd if')
        #create model objects as the item doesnt exist in the model(create a new one)
        stock_obj=Stock()
        stock_obj.stock_item=itemobj
        stock_obj.stock_UOM=itemobj.base_unit
        stock_obj.stock_quantity=base_quantity
        stock_obj.save()
    elif stockobj!=None:
        #print('im in here secnd else')
        stockobj.stock_item=itemobj
        stockobj.stock_UOM=itemobj.base_unit
        if op=="addition":
            #print("Im in addition")
            #print(stockobj.stock_quantity)
            stockobj.stock_quantity=stockobj.stock_quantity+base_quantity
            #print(stockobj.stock_quantity)
        elif op=="subtraction":
            #print("Im in subtraction")
            stockobj.stock_quantity=stockobj.stock_quantity-base_quantity
        stockobj.save()
    return base_quantity

def change_to_dictionary_pgsthsn(current_list):
    change_dict=[item for item in current_list]
    new_dict={}
    for item in change_dict:
        itemid=item.category_id
        itemgst=item.gst_percent
        itemhsn=item.hsn_code
        current_dict={'item_id':itemid,"gst":itemgst,"hsn":itemhsn}
        new_dict[itemid]=current_dict
    return new_dict
def purchase_hsn_gst_select(request):
    #print("Im here")
    if request.method=="GET":
        itemid=request.GET.get('itemid')
        
        categoryobject=Product.objects.filter(product_id=itemid)[0].category
        print(categoryobject)
        #current_list=Category_GST.objects.filter(category_n=categoryname)
        #print (current_list)
        #new_list=change_to_dictionary_pgsthsn(categoryname)
        #print(new_list)
        categorydict={'hsn_code':categoryobject.hsn_code,"gst_percent":categoryobject.gst_percent}
        #print(categorydict)
        return JsonResponse(categorydict,safe=False)
def purchase_list(request):
    template_name="billingapp/purchaselist.html"
    purchaselist=Purchase.objects.all()
    context={"Purchaselist":purchaselist}
    return render(request,template_name,context)
def purchaselist_edit(request,purchaseid):
    template_name="billingapp/purchase.html"
    purchase_formset=inlineformset_factory(Purchase,Purchase_Items_Bridge,fields=("purchase_no","item","item_hsncode","item_quantity","item_rate","uom","item_disc","item_taxable","item_tax","item_CGST","item_SGST","item_IGST","item_amnt"),extra=0)
    purchaseobj=Purchase.objects.get(purchase_id=purchaseid)
    purchase_formsetmodel=purchase_formset(instance=purchaseobj)
    if request.method=="GET":
        purchasemodel=Purchase_modelform(instance=purchaseobj)
        #purchase_formsetmodel=purchase_formset()
        #purchasemodel.fields["purchase_state"].widget.attrs['disabled']=True
        purchasemodel.fields["purchase_state"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["invoice_no"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_subtotal"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_SGSTAmnt"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_CGSTAmnt"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_IGSTAmnt"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_GTotal"].widget.attrs.update({"readonly":"readonly"})
        purchasemodel.fields["purchase_taxableamnt"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_hsncode"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_taxable"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_tax"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_CGST"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_SGST"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_IGST"].widget.attrs.update({"readonly":"readonly"})
        purchase_formsetmodel[0].fields["item_amnt"].widget.attrs.update({"readonly":"readonly"})
        gst_wisemodellist=GST_wise.objects.filter(purchase_no=purchaseobj)
        context={"PurchaseForm": purchasemodel,"BridgeForm":purchase_formsetmodel,"GST_wiselist":gst_wisemodellist}
        return render(request,template_name,context)
    if request.method=="POST" and purchaseid!=None:
        purchasemodel=Purchase.objects.get(purchase_id=purchaseid)
        purchase_master=Purchase_modelform(request.POST,instance=purchasemodel)
        #print(purchase_master.errors)
        if purchase_master.is_valid():
            #print('im in master')
            purchase_master.save()
            #********************************************
            #purchase_existingmodel=Purchase_Items_Bridge.objects.filter(purchase_no=purchaseobj)
            #print(purchase_existingmodel)
            # add more rows to the bridge
            # edit any fields in the existing row
            # delete any of the existing rows
            #****************************************************

            purchase_formsetmodel=purchase_formset(request.POST,instance=purchasemodel)
            #print(purchase_formsetmodel.errors)
            if  purchase_formsetmodel.is_valid():
                #*************************
                for item in purchase_formsetmodel.deleted_forms:
                    if item.cleaned_data['DELETE']:
                        #print("i'm in delete")
                        id_to_delete=item.cleaned_data['purchasedetails_id'] 
                        #print(id_to_delete)
                        purchase_existingmodel=Purchase_Items_Bridge.objects.filter(purchasedetails_id=id_to_delete.purchasedetails_id)
                        item_to_delete=purchase_existingmodel[0].item
                        quantity_to_delete=purchase_existingmodel[0].item_quantity
                        uom=purchase_existingmodel[0].uom
                        print(uom,'1002')
                        stock_update(item_to_delete,quantity_to_delete,uom,op="subtraction")
                        Purchase_Items_Bridge.objects.get(purchasedetails_id=id_to_delete.purchasedetails_id).delete()    
                instances=purchase_formsetmodel.save(commit=False)
                
                for instance in instances:
                    #print("Im in instances")
                    
                    product=Product.objects.get(product_id=instance.item.product_id)
                    itemobj=Purchase_Items_Bridge.objects.filter(item=product,purchase_no=purchaseobj)
                    #print(itemobj)
                    if len(itemobj)!=0:
                        #print(itemobj[0].item_quantity) it is the item quantity befor the update
                        stock_update(instance.item,itemobj[0].item_quantity,instance.uom,op="subtraction")
                        stock_update(instance.item,instance.item_quantity,instance.uom,op="addition")
                    else:
                        stock_update(instance.item,instance.item_quantity,instance.uom,op="addition")
                    instance.save()
                gst_wise_table(purchaseobj,mode="edit")
                gst_wisemodellist=GST_wise.objects.filter(purchase_no=purchaseobj)
                purchasemodel=Purchase_modelform(instance=purchaseobj)
                purchasemodelobj=Purchase.objects.get(purchase_id=purchaseid)
                purchase_formsetmodel=purchase_formset(instance=purchasemodelobj)
        context={"PurchaseForm": purchasemodel,"BridgeForm":purchase_formsetmodel,"GST_wiselist":gst_wisemodellist}
        return render(request,template_name,context)
'''def change_to_dictionary(purchaseitemlist):
    purchase_dict=[item for item in purchaseitemlist]
    dict_to_return={}
    for purchase_info in purchase_dict:
        purchaseno=purchase_info.purchase_no
        item=purchase_info.item.product_name
        quantity=purchase_info.item_quantity
        uom=purchase_info.uom
        item_rate=purchase_info.item_rate
        disc=purchase_info.item_disc
        taxable=purchase_info.item_taxable
        cgst=purchase_info.item_CGST
        sgst=purchase_info.item_SGST
        igst=purchase_info.item_IGST
        amount=purchase_info.item_amnt
        new_dict={"purchase_no":purchaseno,"item":item,"item_quantity":quantity,"uom":uom,"item_rate":item_rate,"item_disc":disc,"item_taxable":taxable,"item_CGST":cgst,"item_SGST":sgst,"item_IGST":igst,"item_amnt":amount}
        dict_to_return[purchase_info.purchasedetails_id]=new_dict
    return dict_to_return
        

def purchase_register_report(request):
    template_name="billingapp/purchase_registerreport_practice.html"
    purchaseitemlist=Purchase_Items_Bridge.objects.all().order_by('purchase_no__invoice_date','purchase_no__supplier__party_name')
    print(purchaseitemlist)
    if request.method=="GET":
        newpurchase_itemlist=change_to_dictionary(purchaseitemlist)
        context={"PurchaseItemList":newpurchase_itemlist}
        return render(request,template_name,context)'''


def purchase_register_report(request):
    template_name="billingapp/purchase_registerreport_practice.html"
    purchaseitemlist=Purchase_Items_Bridge.objects.all().order_by('purchase_no__invoice_date','purchase_no__supplier__party_name')
    print(purchaseitemlist)
    if request.method=="GET":
        context={"PurchaseItemList":purchaseitemlist}
        return render(request,template_name,context)
        
def purchase_summary_report(request):
    template_name="billingapp/purchase_summaryreport.html"
    purchasesummarylist=Purchase.objects.all()
    if request.method=="GET":
        context={"PurchaseSummaryList":purchasesummarylist}
        return render(request,template_name,context)

def purchase_report(request):
    template_name="billingapp/purchase_report.html"
    #gstwiselist=GST_wise.objects.filter(purchase_no__invoice_no='45678').order_by('purchase_no__invoice_date','purchase_no__invoice_no','purchase_no__supplier__party_name')
    gstwiselist=GST_wise.objects.all().order_by('purchase_no__invoice_date','purchase_no__invoice_no','purchase_no__supplier__party_name')
    list_to_be_stuffed=['0.000','0.000','0.000','0.000']
    new_list=[]
    previous_invno=""
    gst_list=[]
    for item in gstwiselist:
        inner_list=[]
        check_rate=item.gst_rate
        #inner_list.append(item.purchase_no.invoice_no)
        inner_list.append(item.purchase_no)
        inner_list.append(item.gst_rate)
        gst_list.append(item.gst_rate)
        inner_list.append(item.taxable_amnt)
        inner_list.append(item.CGST)
        inner_list.append(item.SGST)
        inner_list.append(item.IGST)
        new_list.append(inner_list) 
        #g_list=[]
        item_list=[]
        total_list=[]
    unique_g_list=set(gst_list)
    gst_list=list(unique_g_list)
    gst_list.sort()
    x=len(gst_list)
    '''for item in new_list:
        #g_list.append(item.pop(1))
        if previous_invno=="":
            item_list.extend(item)
            previous_invno=item[0]
        elif previous_invno==item[0]:
            previous_invno=item[0]
            item.pop(0)
            item_list.extend(item)
        else:
            print(item_list)
            total_list.append(item_list)
            item_list=[]
            item_list.extend(item)
            previous_invno=item[0]'''
    '''for item in new_list:
        if previous_invno=="":
            position=gst_list.index(item[1])
            if len(item_list)==0:
                for counter in range(position+1):
                    item_list.extend(list_to_be_stuffed)
            item_list.extend(item)
            previous_invno=item[0]
        elif previous_invno==item[0]:
            previous_invno=item[0]
            position=gst_list.index(item[1])
            if len(item_list)==0:
                for counter in range(position+1):
                    item_list.extend(list_to_be_stuffed)
            item.pop(0)
            item_list.extend(item)
        else:
            print(item_list)
            total_list.append(item_list)
            item_list=[]
            item_list.extend(item)
            previous_invno=item[0]  '''  
    for item in new_list:
        if previous_invno=="":
            position=gst_list.index(item[1])
            item_list.insert(0,item[0])
            if len(item_list)!=position*4:
                for counter in range(position):
                    item_list.extend(list_to_be_stuffed)
            previous_invno=item[0]
            item.pop(0)
            item.pop(0)
            item_list.extend(item)
            
        elif previous_invno==item[0]:
            previous_invno=item[0]
            position=gst_list.index(item[1])
            if len(item_list)!=(position*4)+1:
                for counter in range(position-1):
                    item_list.extend(list_to_be_stuffed)
            item.pop(0)
            item.pop(0)
            item_list.extend(item)
        else:
            #print(item_list)
            total_list.append(item_list)
            item_list=[]
            previous_invno=item[0]
            position=gst_list.index(item[1])
            item_list.insert(0,item[0])
            if len(item_list)!=position*4:
                for counter in range(position):
                    item_list.extend(list_to_be_stuffed)
            item.pop(0)
            item.pop(0)
            item_list.extend(item)
            #previous_invno=item[0]
    heading_list=["SlNo","InvNo","InvDate","  Supplier  ","GSTIN","   4   ","   5   ","   17   "," Total "]
    total_list.insert(0,heading_list)
    print(total_list)
        #print(item.purchase_no.invoice_date,item.purchase_no.supplier,item.purchase_no,item.gst_rate,item.taxable_amnt,item.CGST,item.SGST,item.IGST)
        #new_set.setdefault(k)
    if request.method=="GET":
        context={"GSTwiseList":gst_list,"ItemList":total_list}
        return render(request,template_name,context)

'''def purchase_returnsform(request):
    template_name="billingapp/purchase_returns.html"
    purchase_formset=inlineformset_factory(Purchase,Purchase_Items_Bridge,fields=("purchase_no","item","item_hsncode","item_quantity","item_rate","uom","item_disc","item_taxable","item_tax","item_CGST","item_SGST","item_IGST","item_amnt"),extra=1,can_delete=True)
    if request.method=="GET":
        purchasemodel=purchasemodel_configuration()
        purchase_formsetmodel=purchaseformset_configuration(purchase_formset)
        context={"PurchaseForm": purchasemodel,"BridgeForm":purchase_formsetmodel}
        return render(request,template_name,context)'''
def purchasemodel_return_configuration():
    purchasemodel=Purchase_returns_modelform()
    purchasemodel.fields["purchase_subtotal"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_SGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_CGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_IGSTAmnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_GTotal"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_taxableamnt"].widget.attrs.update({"readonly":"readonly","value":'0'})
    purchasemodel.fields["purchase_Discount"].widget.attrs.update({"value":'0'})
    return purchasemodel

def return_gst_wise_table(latest_purchase,mode):
    purchase_item_list=Purchase_Items_Returns_Bridge.objects.filter(purchase_returns_no=latest_purchase)
    if mode=="edit":
        GST_wise.objects.filter(purchase_no=latest_purchase).delete()
    calculate_gstwise=purchase_item_list.values('item_tax').annotate(cgst=Sum('item_CGST'),sgst=Sum('item_SGST'),igst=Sum('item_IGST'),amount=Sum('item_amnt'))
    gst_wisemodel=Purchase_Returns_GST_wise()
    for item in calculate_gstwise:
        gst_wisemodel.purchase_returns_no=latest_purchase
        gst_wisemodel.purchase_receiptno=latest_purchase.return_invoice_no
        gst_wisemodel.gst_rate=item['item_tax']
        gst_wisemodel.taxable_amnt=item['amount']
        gst_wisemodel.CGST=item['cgst']
        gst_wisemodel.SGST=item['sgst']
        gst_wisemodel.IGST=item['igst']
        gst_wisemodel.save()
    
def purchase_returnsform(request):
    template_name="billingapp/purchase_returns.html"
    purchase_return_formset=inlineformset_factory(Purchase_Returns,Purchase_Items_Returns_Bridge,
    fields=("purchase_returns_no","item","item_hsncode","item_quantity","item_rate","uom","item_disc","item_taxable","item_tax","item_CGST","item_SGST","item_IGST","item_amnt"),extra=1,can_delete=True)
    if request.method=="GET":
        purchasemodel=purchasemodel_return_configuration()
        purchasemodel.fields["purchase_Discount"].widget.attrs.update({"readonly":"readonly"})
        purchase_returns_formsetmodel=purchaseformset_configuration(purchase_return_formset)
        #print(purchasemodel)
        context={"PurchaseReturnForm": purchasemodel,"BridgeReturnForm": purchase_returns_formsetmodel}
        return render(request,template_name,context)
    elif request.method=="POST":
        purchase_returns_master=Purchase_returns_modelform(request.POST)
        #print(purchase_returns_master.errors)
        if purchase_returns_master.is_valid():
            purchase_returns_master.save()
            latest_purchase=Purchase_Returns.objects.last()
            latest_purchaseobj=Purchase_Returns.objects.get(purchasereturns_id=latest_purchase.purchasereturns_id)
            purchase_return_formsetmodel=purchase_return_formset(request.POST)
            #print(purchase_return_formsetmodel.errors)
            #print(purchase_return_formsetmodel)
            if  purchase_return_formsetmodel.is_valid():
                instances=purchase_return_formsetmodel.save(commit=False)
                print(instances[0].uom,"1237")
                for instance in instances:
                    #print(instance,"1238")
                    stockobj=Stock.objects.get(stock_item=instance.item)
                    #print(stockobj.stock_UOM)
                    instance.base_uom=stockobj.stock_UOM
                    instance.purchase_returns_no=latest_purchaseobj
                    base_quantity=stock_update(instance.item,instance.item_quantity,instance.uom,op="subtraction")
                    instance.base_item_quantity=base_quantity
                    #print(x)
                    instance.save()
                return_gst_wise_table(latest_purchase,mode='create')
            purchasemodel=Purchase_returns_modelform()
            purchase_reurns_formsetmodel=purchaseformset_configuration(purchase_return_formset)
        context={"PurchaseReturnForm": purchasemodel,"BridgeReturnForm":purchase_reurns_formsetmodel}
        return render(request,template_name,context)

def purchasereturninfo(request):
    cinvoice_no=request.GET.get('invoice_no')
    #print(cinvoice_no)
    objdict={}
    if request.method=="GET":
        #print("hi")
        purchaseinfoobj=Purchase.objects.filter(invoice_no=cinvoice_no).values('purchase_state__state_name','supplier__party_name','invoice_date','purchase_type','remarks','purchase_Discount','purchase_Paymode__payment_method')
        #purchaseinfoobj=Purchase.objects.filter(invoice_no=cinvoice_no)
        #print(purchaseinfoobj)
        purchase=Purchase.objects.get(invoice_no=cinvoice_no)
        purchaseitemlist=Purchase_Items_Bridge.objects.filter(purchase_no=purchase).values('item__product_id','item__product_name')
        #mydic={(id) for item in purchaseitemlist for id in item}
        '''my_dict={{item['item__product_id']:item['item__product_name']} for item in purchaseitemlist }
        for item in my_dict:
            print(item)'''
        my_dict1={}
        item_dict={}
        return_dict={}
        '''for item in purchaseitemlist:
            for counter,value in enumerate(item.items()):
                if counter==0:
                    my_key=value[1]
                if counter==1:
                    my_dict1[my_key]=value[1]
        print(my_dict1)'''
        for item in purchaseitemlist:
            item_dict[item.get('item__product_id')]=item.get('item__product_name')
        return_dict['purchase_details']=purchaseinfoobj[0]
        return_dict['item_details']=item_dict
        
        #purchaseitemlist1=dict(purchaseitemlist[0])
        #print(purchaseitemlist)
        '''for name in dir(purchaseinfolist):
            objdict[name]=getattr(purchaseinfolist, name)'''
        return JsonResponse(return_dict,safe=False)

def item_bridge_fields(request):
    all_dict={}
    item_dict={}
    invoice_no=request.GET.get('invoice_no')
    citem=request.GET.get('item')
    if request.method=="GET":
        purhase_obj=Purchase.objects.get(invoice_no=invoice_no)
        itemobj=Product.objects.get(product_id=citem)
        itembridgelist=Purchase_Items_Bridge.objects.filter(item=itemobj).filter(purchase_no=purhase_obj).values('item_quantity','item_hsncode','uom__unit_shortname','item_rate','item_disc','item_taxable','item_tax','item_CGST','item_SGST','item_IGST','item_amnt')
        returned_quantitylist=Purchase_Items_Returns_Bridge.objects.filter(item=itemobj).filter(purchase_returns_no__return_invoice_no=purhase_obj).values('item_quantity').aggregate(Sum('item_quantity'))
        print(returned_quantitylist)
        #sum_quantity=returned_quantitylist.aggregate(Sum('item_quantity'))
        
        #print(sum_quantity)
        for item in itembridgelist:
            
            prev_quantity=item.get('item_quantity')
            if returned_quantitylist['item_quantity__sum']!=None:
                current_quantity=prev_quantity-returned_quantitylist.get('item_quantity__sum')
            else: 
                current_quantity=prev_quantity
            item_dict['quantity']=current_quantity
            item_dict['hsn_code']=item.get('item_hsncode')
            item_dict['uom']=item.get('uom__unit_shortname')
            item_dict['rate']=item.get('item_rate')
            item_dict['disc']=item.get('item_disc')
            item_dict['taxable']=item.get('item_taxable')
            item_dict['tax']=item.get('item_tax')
            item_dict['CGST']=item.get('item_CGST')
            item_dict['IGST']=item.get('item_IGST')
            item_dict['SGST']=item.get('item_SGST')
            item_dict['amount']=item.get('item_amnt')
    return JsonResponse(item_dict,safe=False)

def purchase_return_summary_report(request):
    template_name="billingapp/purchasereturn_summaryreport.html"
    purchasereturn_summarylist=Purchase_Returns.objects.all()
    if request.method=="GET":
        context={"SummaryList":purchasereturn_summarylist}
        return render(request,template_name,context)

def purchasereturn_registerreport(request):
    template_name="billingapp/purchasereturn_registerreport.html"
    purchase_reportlist=Purchase_Items_Returns_Bridge.objects.all().order_by('purchase_returns_no__invoice_date','purchase_returns_no__supplier__party_name')
    print(purchase_reportlist)
    if request.method=="GET":
        context={"PurchaseReportList":purchase_reportlist}
        return render(request,template_name,context)

'''def change_to_dictionary(purchasemenulist):
    purchase_dict=[item for item in purchasemenulist]
    dict_to_return={}
    for purchase_info in purchase_dict:'''

'''def purchase_summary_report(request):
    template_name="billingapp/purchase_summaryreport.html"
    query=Q()
    if request.method=="GET":
        
        supplier=request.GET.get('supplier','')
        invoice_date=request.GET.get('invoice_date','')
        intpage_num=int(page_num)
        start_num=(intpage_num-1)*2
        end_num=start_num+2
        if supplier!='':
            query&=Q(supplier__party_name__contains=supplier)
        if invoice_date!='':
            query&=Q(invoice_date__exact=invoice_date)
        if query!='(AND: )':
            purchasesummarylist=Purchase.objects.filter(query).values('purchase_id','invoice_no','supplier__party_name','invoice_date','purchase_state__state_name','purchase_type','purchase_taxableamnt','purchase_IGSTAmnt','purchase_SGSTAmnt','purchase_CGSTAmnt','purchase_subtotal','purchase_Discount','purchase_GTotal')
            total_count=purchasesummarylist.count()
            purchasesummarylist=purchasesummarylist[start_num:end_num]
        else:
            purchasesummarylist=Purchase.objects.all()
        new_purchasemenulist=change_to_dictionary(purchasesummarylist)
        new_purchasesummarylist['tota_count']={'queryset_count':total_count}
        return JsonResponse(new_purchasesummarylist,safe=False)'''


