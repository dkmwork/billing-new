from django.contrib import admin
from billingapp.models import (State,City,Unit,Category_GST,UOM,UOM_Conversion,Financial_Year,Company,Branch,User,Product,
Party,Payment_Mode,Purchase,Payment_Details,Stock,Purchase_Items_Bridge,GST_wise,Warehouse_Bin_Stock,Purchase_Returns,Purchase_Items_Returns_Bridge,
Purchase_Returns_GST_wise)

admin.site.register(State)
admin.site.register(City)
admin.site.register(Unit)
admin.site.register(Category_GST)
admin.site.register(UOM)
admin.site.register(UOM_Conversion)
admin.site.register(Financial_Year)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Party)
admin.site.register(Payment_Mode)
admin.site.register(Purchase)
admin.site.register(Payment_Details)
admin.site.register(Stock)
admin.site.register(Purchase_Items_Bridge)
admin.site.register(GST_wise)
admin.site.register(Purchase_Returns)
admin.site.register(Purchase_Items_Returns_Bridge)
admin.site.register(Purchase_Returns_GST_wise)

# Register your models here.
