from django.urls import path
from django.conf.urls import url
from . import views
from .views import CustomerViewSet

#configure APIs views requests
customer_list = CustomerViewSet.as_view({
    'get': 'list',

})
customer_detail = CustomerViewSet.as_view({
    'get': 'retrieve',
})

#configure urls
urlpatterns = (
    path('', customer_list, name='customer-list'),
    path('<int:pk>', customer_detail, name='customer-detail'),
)
