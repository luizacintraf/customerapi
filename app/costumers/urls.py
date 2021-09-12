from django.urls import path
from django.conf.urls import url

from . import views

from .views import CostumerViewSet

costumer_list = CostumerViewSet.as_view({
    'get': 'list',

})
costumer_detail = CostumerViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = (
    path('', costumer_list, name='customer-list'),
    path('<int:pk>', costumer_detail, name='customer-detail'),
)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:id>/', views.get_costumer, name='costumer'),
# ]
