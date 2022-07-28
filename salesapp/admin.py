from django.contrib import admin
from salesapp.models import Sales,Sales_Items_Bridge,Sales_GST_Wise,Sales_Returns,Sales_Items_Return_Bridge,Sales_Returns_GST_Wise

admin.site.register(Sales)
admin.site.register(Sales_Items_Bridge)
admin.site.register(Sales_GST_Wise)
admin.site.register(Sales_Returns)
admin.site.register(Sales_Items_Return_Bridge)
admin.site.register(Sales_Returns_GST_Wise)

# Register your models here.
