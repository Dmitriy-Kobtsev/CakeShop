from django.urls import path

from bakery.apps import BakeryConfig
from bakery.views import ProductView, ProductFilterView, CategoryCreate, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = BakeryConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('products/<int:pk>/', ProductFilterView.as_view(), name='product_filter'),
    path('create_category/', CategoryCreate.as_view(), name='category'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create_product/', ProductCreateView.as_view(), name='product_create'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]