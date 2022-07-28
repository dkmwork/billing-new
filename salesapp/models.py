from django.db import models
from billingapp.models import (State,City,Unit,Financial_Year,UOM,Category_GST,UOM_Conversion,Company,Branch,User,Product,Party,Payment_Mode,Purchase,Payment_Details,Stock,
Warehouse_Bin_Stock,Purchase_Returns,Purchase_Items_Bridge,GST_wise,Purchase_Items_Returns_Bridge,Purchase_Returns_GST_wise)
 
class Sales(models.Model):
    sales_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_type_choices=(("B2B","B2B"),("B2C","B2C"))
    credit_choice=(("Yes","Yes"),("No","No"))
    sales_invoiceno=models.CharField(max_length=40,null=False,verbose_name="Billing No")
    sales_state=models.ForeignKey(State,null=False,on_delete=models.CASCADE,related_name="sales",verbose_name="State")
    customer=models.ForeignKey(Party,null=False,on_delete=models.CASCADE,related_name="sales")
    invoice_date=models.DateField(null=True,blank=True)
    sales_type=models.CharField(max_length=40,choices=sales_type_choices,null=True,blank=True,verbose_name="Sales Type")
    sales_credit=models.CharField(max_length=40,choices=credit_choice,null=True,blank=True)
    sales_taxableamount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_IGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_CGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_SGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_subtotal=models.DecimalField(max_digits=18,decimal_places=3)
    sales_Discount=models.DecimalField(max_digits=18,decimal_places=3)
    sales_GTotal=models.DecimalField(max_digits=18,decimal_places=3)
    sales_Paymode=models.ForeignKey(Payment_Mode,on_delete=models.CASCADE,related_name='sales')
    def __str__(self):
        return (self.sales_invoiceno)

class Sales_Items_Bridge(models.Model):
    salesdetails_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_no=models.ForeignKey(Sales,null=False,on_delete=models.CASCADE,related_name="sales_items_bridge")
    sales_item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="sales_items_bridge")
    sales_item_code=models.CharField(max_length=20,null=True,blank=True)
    salesitem_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_hsncode=models.CharField(max_length=20,null=True,blank=True)
    sales_uom=models.ForeignKey(UOM,on_delete=models.CASCADE,related_name='sales_items_bridge',default=1)
    salesitem_rate=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_disc=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_taxable=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_tax=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_CGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_SGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_IGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_amnt=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return str (self.salesdetails_id)

class Sales_GST_Wise(models.Model):
    salesgst_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_no=models.ForeignKey(Sales,null=False,on_delete=models.CASCADE,related_name="sales_gst_wise")
    salesgst_rate=models.IntegerField()
    sales_receiptno=models.CharField(max_length=15,null=True,blank=True)
    sales_taxable_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_CGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_SGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_IGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    def __str__(self):
        return str (self.salesgst_rate)

class Sales_Returns(models.Model):
    salesreturns_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_type_choices=(("B2B","B2B"),("B2C","B2C"))
    credit_choice=(("Yes","Yes"),("No","No"))
    return_salesinvoiceno=models.ForeignKey(Sales,null=False,on_delete=models.CASCADE,related_name='sales_returns',verbose_name="Billing No")
    sales_state=models.ForeignKey(State,max_length=40,null=False,on_delete=models.CASCADE,related_name='sales_returns')
    customer=models.ForeignKey(Party,max_length=40,null=False,on_delete=models.CASCADE,related_name='sales_returns')
    invoice_date=models.DateField(null=False)
    sales_type=models.CharField(choices=sales_type_choices,max_length=40,null=False)
    sales_credit=models.CharField(max_length=40,choices=credit_choice,null=True,blank=True)
    sales_taxableamnt=models.DecimalField(max_digits=18,decimal_places=3,verbose_name="Taxbl Amt")
    sales_IGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_CGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_SGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    sales_subtotal=models.DecimalField(max_digits=18,decimal_places=3)
    sales_Discount=models.DecimalField(max_digits=18,decimal_places=3)
    sales_GTotal=models.DecimalField(max_digits=18,decimal_places=3)
    sales_Paymode=models.ForeignKey(Payment_Mode,on_delete=models.CASCADE,related_name='sales_returns')
    def __str__(self):
        return str(self.return_salesinvoiceno.sales_invoiceno)

class Sales_Items_Return_Bridge(models.Model):
    salesreturns_details_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_returns_no=models.ForeignKey(Sales_Returns,null=False,on_delete=models.CASCADE,related_name="sales_returns_items_bridge")
    sales_item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="sales_returns_items_bridge")
    sales_item_code=models.CharField(max_length=20,null=True,blank=True)
    salesitem_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    base_salesitem_quantity=models.DecimalField(max_digits=15,decimal_places=3,null=True,blank=True)
    salesitem_hsncode=models.CharField(max_length=20,null=True,blank=True)
    sales_uom=models.ForeignKey(UOM,on_delete=models.CASCADE,related_name='sales_returns_items_bridge',default=1)
    sales_base_uom=models.CharField(max_length=20,null=True,blank=True)
    salesitem_rate=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_disc=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_taxable=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_tax=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_CGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_SGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    salesitem_IGSTamnt=models.DecimalField(max_digits=15,decimal_places=3,default=0)
    salesitem_amnt=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return str(self.salesreturns_details_id)

class Sales_Returns_GST_Wise(models.Model):
    sales_returns_gst_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    sales_returns_no=models.ForeignKey(Sales,null=False,on_delete=models.CASCADE,related_name="sales_returns_gst_wise")
    salesgst_rate=models.IntegerField()
    sales_receiptno=models.CharField(max_length=15,null=True,blank=True)
    sales_taxable_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_CGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_SGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    sales_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    sales_IGST_amount=models.DecimalField(max_digits=15,decimal_places=3)
    def __str__(self):
        return str (self.salesgst_rate)





# Create your models here.
