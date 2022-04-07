from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

	path('admin_login/', views.adminlogin, name="adminlogin"),
	path('admin_home/', views.adminhome, name="adminhome"),
	path('admin_allorder/', views.adminallorder, name="adminallorder"),
	path('product/', views.productcreate, name="product"),
	path('admin_home/<int:transaction_id>/',views.adminhomeid, name="adminhomeid"),
	path('admin_home/<int:transaction_id>.changestatus/',views.adminchangestatus, name="adminchangestatus"),
]