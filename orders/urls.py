from django.urls import path

from .views import OrdersPageView

urlpatterns = [

path("", OrdersPageView.as_view(), name="orders")

]
