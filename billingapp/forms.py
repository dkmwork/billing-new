from django import forms
from django.forms import ModelForm
from billingapp.models import (State,City,UOM,Unit,Category_GST,UOM_Conversion,Financial_Year,Company,
Branch,User,Product,Party,Payment_Details,Payment_Mode,Purchase,Stock,Purchase_Items_Bridge,GST_wise,Purchase_Returns,
Purchase_Items_Returns_Bridge,Purchase_Returns_GST_wise)

class State_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # get the cursor focus on 'state_name' text box when the page loads.
        self.fields['state_name'].widget.attrs.update({'autofocus':'autofocus'})
        self.fields['state_code']=forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    class Meta:
        model=State
        exclude=('state_id',)

class City_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['state_id'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=City
        exclude=('city_id',)

class Unit_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['unit_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Unit 
        exclude=('unit_id',)

class Category_GST_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Category_GST
        exclude=('category_id',)

class UOM_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['unit_shortname'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=UOM
        exclude=('unit_id',)

class UOM_conversion_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['fromunit'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=UOM_Conversion
        exclude=('conversion_id',)

class Financial_year_modelform(ModelForm):
    class Meta:
        model=Financial_Year
        exclude=('year_id',)

class Company_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['company_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Company
        exclude=('company_id',)

class Branch_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['branch_name'].widget.attrs.update({'autofocus':'autofocuse'})
    class Meta:
        model=Branch
        exclude=('branch_id',)

class User_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=User
        exclude=('user_id',)

class Product_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['product_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Product
        exclude=('product_id',)

class Party_modelform(ModelForm):
    class Meta:
        model=Party 
        exclude=('party_id',)

class Payment_mode_modelform(ModelForm):
    class Meta:
        model=Payment_Mode
        exclude=('pay_id',)
        
class Purchase_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["remarks"]=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":10}))
    class Meta: 
        model=Purchase
        exclude=('purchase_id',)
# using this function for validation(saving purchase with atleast one item)
# Now, when form.is_valid() is called from view, the form's clean method is called implicitly and this validation is executed.
    def clean(self):
        cd=self.cleaned_data
        if cd.get('purchase_taxableamnt')<=0:
            self.add_error("purchase_taxableamnt", "Add at least one item to the purchase !!")
        return cd
class Payment_details_modelform(ModelForm):
    class Meta:
        model=Payment_Details 
        exclude=('payment_id',)

class Stock_modelform(ModelForm):
    class Meta:
        model=Stock
        exclude=('stock_id',)

class Purchase_items_bridge_modelform(ModelForm):
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['item_rate'].widget.attrs.update({'class':"to_be_calculated"})
    #     self.fields['item_disc'].widget.attrs.update({'class':"to_be_calculated"})
    #     self.fields['item_quantity'].widget.attrs.update({'class':"to_be_calculated"})
    class Meta:
        model=Purchase_Items_Bridge
        exclude=('purchasedetails_id',)
    
class GST_wise_modelform(ModelForm):
    class Meta:
        model=GST_wise 
        exclude=('gst_id',)

class Purchase_returns_modelform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["remarks"]=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model=Purchase_Returns
        exclude=('purchasereturns_id',)

class Purchase_items_returns_bridge_modelform(ModelForm):
    class Meta:
        model=Purchase_Items_Returns_Bridge
        exclude=('purchase_returnsdetails_id',)

class Purchase_returns_GST_wise_modelform(ModelForm):
    class Meta:
        model=Purchase_Returns_GST_wise
        exclude=('purchase_returns_gst_id',)
    

