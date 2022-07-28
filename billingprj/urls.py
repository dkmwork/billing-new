"""billingprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from billingapp import views
from salesapp import views as s_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('state',views.stateform,name='state'),
    path('city',views.citymodelform,name='city'),
    path('category',views.categorymodelform,name='category'),
    path('uom',views.uommodelform,name='uom'),
    path('uom_conversion',views.uomconversion_modelform,name='uom_conversion'),
    path('financial_year',views.financialyear_modelformset,name='financial_year'),
    path('company',views.companymodelform,name='company'),
    path('branch',views.branchmodelform,name='branch'),
    path('user',views.usermodelform,name='user'),
    path('product',views.productmodelform,name='product'),
    path('gst_and_hsn_select',views.gst_and_hsn_select,name="gst_and_hsn_select"),
    path('party',views.partymodelform,name='party'),
    path('payment',views.Paymentmode_modelform,name='payment'),
    path('check_duplicate',views.check_duplicate,name='check_duplicate'),
    path('statelist',views.statelist,name='statelist'),
    path('state_edit/<int:stateid>',views.state_edit,name='state_edit'),
    path('citylist',views.citylist,name='citylist'),
    path('city_edit/<int:cityid>',views.city_edit,name='city_edit'),
    path('categorylist',views.categorylist,name="categorylist"),
    path('category_edit/<int:categoryid>',views.category_edit,name='category_edit'),
    path('financial_yearlist',views.financial_yearlist,name='financial_yearlist'),
    path('financial_year_edit/<int:yearid>',views.financial_year_edit,name='financial_year_edit'),
    path('uomlist',views.uomlist,name='uomlist'),
    path('uom_edit/<int:uomid>',views.uom_edit,name='uom_edit'),
    path('uom_conversionlist',views.uom_conversionlist,name='uom_conversionlist'),
    path('uom_conversion_edit/<int:conversionid>',views.uom_conversion_edit,name='uom_conversion_edit'),
    path('companylist',views.companylist,name='companylist'),
    path('company_edit/<int:companyid>',views.company_edit,name='company_edit'),
    path('branchlist',views.branchlist,name='branchlist'),
    path('branch_edit/<int:branchid>',views.branch_edit,name='branch_edit'),
    path('userlist',views.userlist,name='userlist'),
    path('user_edit/<int:userid>',views.user_edit,name='user_edit'),
    path('productlist',views.productlist,name='productlist'),
    path('product_edit/<int:productid>', views.product_edit, name='product_edit'),
    path('partylist',views.partylist,name='partylist'),
    path('party_edit/<int:partyid>',views.party_edit,name='party_edit'),
    path('payment_modelist',views.payment_modelist,name='payment_modelist'),
    path('payment_mode_edit/<int:payid>',views.payment_mode_edit,name='payment_mode_edit'),
    path('statesearch',views.statesearch,name='statesearch'),
    path('categorysearch',views.categorysearch,name='categorysearch'),
    path('productsearch',views.productsearch,name='productsearch'),
    path('partysearch',views.partysearch,name='partysearch'),
    path('purchase',views.purchaseform,name="purchase"),
    path('purchase_hsn_gst_select',views.purchase_hsn_gst_select,name='purchase_hsn_gst_select'),
    path('purchaselist',views.purchase_list,name='purchaselist'),
    path('purchaselist_edit/<int:purchaseid>',views.purchaselist_edit,name='purchaselist_edit'),
    path('purchase_registerreport',views.purchase_register_report,name='purchase_registerreport'),
    path('purchase_summaryreport',views.purchase_summary_report,name='purchase_summaryreport'),
    path('purchase_report',views.purchase_report,name='purchase_report'),
    path('purchase_returns',views.purchase_returnsform,name='purchase_returns'),
    path('purchasereturninfo',views.purchasereturninfo,name='purchasereturninfo'),
    path('item_bridge_fields',views.item_bridge_fields,name='item_bridge_fields'),
    path('purchasereturn_summaryreport',views.purchase_return_summary_report,name='purchasereturn_summaryreport'),
    path('purchasereturn_registerreport',views.purchasereturn_registerreport,name='purchasereturn_registerreport'),
    path('sales',s_view.salesform,name='sales'),
    path('set_state_code',s_view.set_state_code,name='set_state_code'),
    path('get_contactno',s_view.get_contactno,name='get_contactno'),
    path('sales_hsn_gst_select',s_view.sales_hsn_gst_select,name='sales_hsn_gst_select'),
    path('sales_register_report',s_view.sales_register_reoprt,name='sales_register_report'),
    path('sales_summary_report',s_view.sales_summary_report,name='sales_summary_report'),
    path('sales_returns',s_view.sales_returnsform,name='sales_returns'),
    path('salesreturninfo',s_view.salesreturninfo,name='salesreturninfo'),
    path('salesitem_bridge_fields',s_view.salesitem_bridge_fields,name='salesitem_bridge_fields'),
]
