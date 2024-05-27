from django.urls import path
from home import views

urlpatterns = [
    path ('view' , views.Outlet_view.as_view() , name="Outlet_view"),
    path ('<int:pk>' , views.Outlet_detail.as_view() , name="Outlet_detail"),
]
