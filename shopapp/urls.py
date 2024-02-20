# myapp/urls.py

from django.urls import path
from .views import index, ProductProfitAPIView,ProductSalesAPIView,AverageProfitMarginBySeasonAPIView,TopSellingProductsByCategoryAPIView,LowStockHighDemandProductsAPIView

urlpatterns = [
    path('test/', index, name='index'),
    path('product-profit/', ProductProfitAPIView.as_view(), name='product-profit'),
    path('product-sales/', ProductSalesAPIView.as_view(), name='product-sales'),
    path('top-selling-products/', TopSellingProductsByCategoryAPIView.as_view(), name='top-selling-products'),
    path('average-profit-margin/', AverageProfitMarginBySeasonAPIView.as_view(), name='average-profit-margin'),
    path('low-stock-high-demand-products/', LowStockHighDemandProductsAPIView.as_view(), name='low-stock-high-demand-products'),

]
