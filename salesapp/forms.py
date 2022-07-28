from django import forms
from django.forms import ModelForm
from salesapp.models import (Sales,Sales_Items_Bridge,Sales_GST_Wise,Sales_Returns,Sales_Items_Return_Bridge,Sales_Returns_GST_Wise)
from billingapp.models import (State,City,UOM,Unit,Category_GST,UOM_Conversion,Financial_Year,Company,
Branch,User,Product,Party,Payment_Details,Payment_Mode,Purchase,Stock)

class Sales_modelform(ModelForm):
    
    class Meta:
        model=Sales
        exclude=('sales_id',)
class Sales_items_bridge_modelform(ModelForm):
    class Meta:
        model=Sales_Items_Bridge
        exclude=('salesdetails_id',)
    
class Sales_GST_Wise_modelform(ModelForm):
    class Meta:
        model=Sales_GST_Wise
        exclude=('salesgst_id',)

class Sales_Returns_modelform(ModelForm):
    class Meta:
        model=Sales_Returns
        exclude=('salesreturns_id',)

class Sales_Items_Return_Bridge_modelform(ModelForm):
    class Meta:
        model=Sales_Items_Return_Bridge
        exclude=('salesreturns_details_id',)

class Sales_Returns_GST_Wise_modelform(ModelForm):
    class Meta:
        model=Sales_Returns_GST_Wise
        exclude=('sales_returns_gst_id',)
