from django.db import models
import re
from django.core.exceptions import ValidationError
from django.db.models import Q

def validate_mobileno(value):
    rule=re.compile("^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
    if not rule.match(value):
        raise ValidationError(f"{value} is not a valid mobile number")
def validate_email(value):
    print(value)
    rule=re.compile("^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$")
    if not rule.match(value):
        raise ValidationError(f"{value} is not a valid email address")

class State(models.Model):
    state_id=models.IntegerField(primary_key=True,auto_created=True)
    state_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    state_code=models.CharField(max_length=2,null=False,blank=False,unique=True,verbose_name="State Code")
    state_shortname=models.CharField(max_length=5,null=False,blank=False,unique=True)
    def __str__(self):
        return self.state_name
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=Q(state_code__lte=99), 
                name="state_code_constarint"
                )]

class City(models.Model):
    city_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    state_id=models.ForeignKey(State,max_length=40,null=False,on_delete=models.CASCADE,related_name='city')
    city_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    city_shortname=models.CharField(max_length=40,null=False,blank=False,unique=True)
    def __str__(self):
        return self.city_name

class Unit(models.Model):
    unit_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    unit_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    #unit_abrevation=models.CharField(max_length=10,null=False,unique=True)
    def __str__(self):
        return self.unit_name
class Financial_Year(models.Model):
    year_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    finacial_year=models.CharField(max_length=40,null=False,unique=True)
    def __str__(self):
        return self.finacial_year
    
class Category_GST(models.Model):
    category_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    category_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    gst_percent=models.CharField(max_length=40,null=False,blank=False,unique=True)
    hsn_code=models.CharField(max_length=20,null=True,blank=True)
    financial_year=models.ForeignKey(Financial_Year,on_delete=models.CASCADE,related_name='category_gst')
    def __str__(self):
        return self.category_name

class UOM(models.Model):
    unit_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    unit_shortname=models.CharField(max_length=40,null=False,blank=False,unique=True)
    unit_longname=models.CharField(max_length=40,null=False,blank=False,unique=True)
    def __str__(self):
        return self.unit_shortname

class UOM_Conversion(models.Model):
    conversion_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    operation_choices=(('Addition','Addition'),('Sutraction','Subtraction'),('Multiplication','Multiplication'),('Division','Division'))
    fromunit=models.ForeignKey(UOM,null=False,on_delete=models.CASCADE,related_name='uom_conversion_fromunit')
    tounit=models.ForeignKey(UOM,null=False,on_delete=models.CASCADE,related_name='uom_conversion_tounit')
    operations=models.CharField(max_length=40, choices=operation_choices,null=False,blank=False)
    conversion_value=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return f"{self.fromunit}{self.tounit}"

class Company(models.Model):
    company_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    company_name=models.CharField(max_length=40,null=False,unique=True)
    company_shortname=models.CharField(max_length=5,null=True,blank=True,unique=True)
    company_street=models.CharField(max_length=100,null=False)
    company_state=models.ForeignKey(State,null=False,on_delete=models.CASCADE,related_name='company')
    company_city=models.ForeignKey(City,null=False,on_delete=models.CASCADE,related_name='company')
    company_pin=models.CharField(max_length=100,null=False)
    company_email=models.CharField(validators=[validate_email],max_length=100,null=False,unique=True)
    company_url=models.CharField(max_length=100,null=False,unique=True)
    contact_no=models.CharField(validators=[validate_mobileno],max_length=100,null=False)
    def __str__(self):
        return self.company_name
    
class Branch(models.Model):
    branch_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    branch_name=models.CharField(max_length=100,null=False)
    branch_street=models.CharField(max_length=100,null=False,blank=False)
    branch_city=models.ForeignKey(City,null=False,on_delete=models.CASCADE,related_name='branch')
    branch_state=models.ForeignKey(State,null=False,on_delete=models.CASCADE,related_name='branch')
    branch_poc=models.CharField(max_length=100,null=False,blank=False)
    branch_pin=models.CharField(max_length=100,null=False,blank=False)
    poc_contact_no=models.CharField(validators=[validate_mobileno],max_length=100,null=False,blank=False)
    def __str__(self):
        return self.branch_name

class User(models.Model):
    user_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    user_name=models.CharField(max_length=100,null=False)
    user_designation=models.CharField(max_length=100,null=False)
    user_branch=models.ForeignKey(Branch,null=False,on_delete=models.CASCADE,related_name='user')
    user_location=models.CharField(max_length=100,null=False)
    user_email=models.CharField(validators=[validate_email],max_length=100,null=False,unique=True)
    user_contact_no=models.CharField(validators=[validate_mobileno],max_length=100,null=False)
    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    category=models.ForeignKey(Category_GST,on_delete=models.CASCADE,related_name='product',null=True,blank=True)
    product_name=models.CharField(max_length=100,null=False,unique=True)
    product_code=models.CharField(max_length=100,null=False,unique=True)
    base_unit=models.ForeignKey(UOM,null=False,on_delete=models.CASCADE,related_name='product')
    def __str__(self):
        return self.product_name
    
class Party(models.Model):
    party_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    party_name=models.CharField(max_length=100,null=False,unique=True)
    party_street=models.CharField(max_length=100,null=False)
    party_city=models.ForeignKey(City,max_length=40,null=False,on_delete=models.CASCADE,related_name='party')
    party_state=models.ForeignKey(State,max_length=40,null=False,on_delete=models.CASCADE,related_name='party')
    contact_no=models.CharField(validators=[validate_mobileno],max_length=40,null=False,verbose_name="Mobile No")
    party_email=models.CharField(validators=[validate_email],max_length=40,unique=True,null=False)
    party_GST=models.CharField(max_length=40,null=False,unique=True)
    party_category=models.CharField(max_length=100,null=False)
    party_type=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.party_name

class Payment_Mode(models.Model):
    pay_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    payment_method=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.payment_method

class Purchase(models.Model):
    purchase_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    invoice_no=models.CharField(max_length=40,null=False)
    purchase_state=models.ForeignKey(State,max_length=40,null=False,on_delete=models.CASCADE,related_name='purchase')
    supplier=models.ForeignKey(Party,max_length=40,null=False,on_delete=models.CASCADE,related_name='purchase')
    invoice_date=models.DateField(null=False)
    purchase_type=models.CharField(max_length=40,null=False)
    remarks=models.CharField(max_length=40,null=False)
    purchase_taxableamnt=models.DecimalField(max_digits=18,decimal_places=3,verbose_name="Taxbl Amt")
    purchase_IGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_CGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_SGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_subtotal=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_Discount=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_GTotal=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_Paymode=models.ForeignKey(Payment_Mode,on_delete=models.CASCADE,related_name='purchase')
    #purchase_Item=models.ManyToManyField(Product,through="Purchase_Items_Bridge",related_name="purchase",blank=True)
    def __str__(self):
        #return f"{self.supplier.party_name}{self.invoice_no}"
        return (self.invoice_no)

class Payment_Details(models.Model):
    payment_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    purchase_no=models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='payment_details')
    payment_method=models.ForeignKey(Payment_Mode,on_delete=models.CASCADE, related_name='payment_details')
    bank_name=models.CharField(max_length=40,null=True,blank=True)
    ifsc_code=models.CharField(max_length=20,null=True,blank=True)
    cheque_no=models.CharField(max_length=50,unique=True,null=True,blank=True)
    card_no=models.CharField(max_length=40,unique=True,null=True,blank=True)
    card_expiry_date=models.DateField(null=True,blank=True)
    cvc_code=models.IntegerField(null=True,blank=True)
    referrence_no=models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return f"{self.purchase_no}{self.payment_method}"

class Stock(models.Model):
    stock_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    stock_item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="stock")
    stock_UOM=models.ForeignKey(UOM,null=False,on_delete=models.CASCADE,related_name="stock")
    stock_quantity=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return self.stock_item.product_name
class Warehouse_Bin_Stock(models.Model):
    warehouse_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    Warehouse=models.CharField(max_length=20,null=True,blank=True)
    Bin=models.CharField(max_length=20,null=True,blank=True)
    Item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="warehouse_bin_stock")
    base_unit=models.ForeignKey(UOM,null=False,on_delete=models.CASCADE,related_name="warehouse_bin_stock")
    quantity=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return f"{self.warehouse}{self.item.product_name}"

class Purchase_Items_Bridge(models.Model):
    purchasedetails_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    purchase_no=models.ForeignKey(Purchase,null=False,on_delete=models.CASCADE,related_name="purchade_items_bridge")
    item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="purchade_items_bridge")
    #base_item_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    item_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    item_hsncode=models.CharField(max_length=20,null=True,blank=True)
    uom=models.ForeignKey(UOM,on_delete=models.CASCADE,related_name='purchase_items_bridge',default=1)
    #base_uom=models.CharField(max_length=20,null=True,blank=True)
    item_rate=models.DecimalField(max_digits=15,decimal_places=3)
    item_disc=models.DecimalField(max_digits=15,decimal_places=3)
    item_taxable=models.DecimalField(max_digits=15,decimal_places=3)
    item_tax=models.DecimalField(max_digits=15,decimal_places=3)
    item_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_amnt=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return str (self.purchasedetails_id)
    
class GST_wise(models.Model):
    gst_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    purchase_no=models.ForeignKey(Purchase,null=False,on_delete=models.CASCADE,related_name="gst_wise")
    gst_rate=models.IntegerField()
    purchase_receiptno=models.CharField(max_length=15,null=True,blank=True)
    taxable_amnt=models.DecimalField(max_digits=15,decimal_places=3)
    CGST=models.DecimalField(max_digits=15,decimal_places=3)
    SGST=models.DecimalField(max_digits=15,decimal_places=3)
    IGST=models.DecimalField(max_digits=15,decimal_places=3)
    def __str__(self):
        return str (self.gst_rate)

class Purchase_Returns(models.Model):
    purchasereturns_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    return_invoice_no=models.ForeignKey(Purchase,null=False,on_delete=models.CASCADE,related_name='purchase_returns')
    purchase_state=models.ForeignKey(State,max_length=40,null=False,on_delete=models.CASCADE,related_name='purchase_returns')
    supplier=models.ForeignKey(Party,max_length=40,null=False,on_delete=models.CASCADE,related_name='purchase_returns')
    invoice_date=models.DateField(null=False)
    purchase_type=models.CharField(max_length=40,null=False)
    remarks=models.CharField(max_length=40,null=False)
    purchase_taxableamnt=models.DecimalField(max_digits=18,decimal_places=3,verbose_name="Taxbl Amt")
    purchase_IGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_CGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_SGSTAmnt=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_subtotal=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_Discount=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_GTotal=models.DecimalField(max_digits=18,decimal_places=3)
    purchase_Paymode=models.ForeignKey(Payment_Mode,on_delete=models.CASCADE,related_name='purchase_returns')
    def __str__(self):
        return str (self.return_invoice_no.invoice_no)

class Purchase_Items_Returns_Bridge(models.Model):
    purchase_returnsdetails_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    purchase_returns_no=models.ForeignKey(Purchase_Returns,null=False,on_delete=models.CASCADE,related_name="purchase_items_returns_bridge")
    item=models.ForeignKey(Product,null=False,on_delete=models.CASCADE,related_name="purchase_items_returns_bridge")
    item_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    base_item_quantity=models.DecimalField(max_digits=15,decimal_places=3)
    item_hsncode=models.CharField(max_length=20,null=True,blank=True)
    uom=models.ForeignKey(UOM,on_delete=models.CASCADE,related_name='purchase_items_returns_bridge',default=1)
    # its not a display field but to make a query easier.
    base_uom=models.CharField(max_length=20,null=True,blank=True)
    item_rate=models.DecimalField(max_digits=15,decimal_places=3)
    item_disc=models.DecimalField(max_digits=15,decimal_places=3)
    item_taxable=models.DecimalField(max_digits=15,decimal_places=3)
    item_tax=models.DecimalField(max_digits=15,decimal_places=3)
    item_CGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_SGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_IGST=models.DecimalField(max_digits=15,decimal_places=3)
    item_amnt=models.DecimalField(max_digits=18,decimal_places=3)
    def __str__(self):
        return str (self.purchase_returnsdetails_id)
    
class Purchase_Returns_GST_wise(models.Model):
    purchase_returns_gst_id=models.IntegerField(primary_key=True,auto_created=True,unique=True)
    purchase_returns_no=models.ForeignKey(Purchase_Returns,null=False,on_delete=models.CASCADE,related_name="purchase_returns_gst_wise")
    gst_rate=models.IntegerField()
    purchase_receiptno=models.CharField(max_length=15,null=True,blank=True)
    taxable_amnt=models.DecimalField(max_digits=15,decimal_places=3)
    CGST=models.DecimalField(max_digits=15,decimal_places=3)
    SGST=models.DecimalField(max_digits=15,decimal_places=3)
    IGST=models.DecimalField(max_digits=15,decimal_places=3)
    def __str__(self):
        return str (self.gst_rate)














# Create your models here.
