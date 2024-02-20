from django.shortcuts import render
import csv
import os
# Create your views here.
from django.http import HttpResponse, JsonResponse
from shopapp.models import Product 
from django.db.models import F, Sum, Case, When, Value, IntegerField, Avg
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):

    # Calculate the total profit for each product
    product_profit_query = Product.objects.annotate(
        total_profit=Sum(
            F('SELLING_PRICE') * F('QUANTITY_SOLD') * F('PROFIT_MARGIN') - F('COST_PRICE') * F('QUANTITY_SOLD'),
            output_field=IntegerField()
        )
    )
    print(product_profit_query)
    print('//////////////////////////////////////////////////////////////////')
    # Calculate the total sales for each product
    product_sales_query = Product.objects.annotate(
        total_sales=Sum('QUANTITY_SOLD')
    )

    print(product_sales_query)
    print('//////////////////////////////////////////////////////////////////')
   

    # Identify Top Selling Products by Category
    top_selling_products_by_category = Product.objects.values('PRODUCT_CATEGORY').annotate(
        total_sales=Sum('QUANTITY_SOLD')
    ).order_by('-total_sales')

    print(top_selling_products_by_category)
    print('//////////////////////////////////////////////////////////////////')
    
    # Calculate Average Profit Margin by Season
    average_profit_margin_by_season = Product.objects.values('SEASON').annotate(
        average_profit_margin=Avg('PROFIT_MARGIN')
    )

    print(average_profit_margin_by_season)
    print('//////////////////////////////////////////////////////////////////')
    

    # Products with low stock and high demand
    low_stock_high_demand_products = Product.objects.filter(
        QUANTITY_SOLD__lt=F('SPACE_OCCUPIED') * 0.5,  # Example threshold for low stock
        RATING__gte=4.5  # Example threshold for high demand
    )
    print(low_stock_high_demand_products)

    return HttpResponse("Query processed successfully.") 


class ProductProfitAPIView(APIView):
    def get(self, request):
        product_profit_data = Product.objects.annotate(
            total_profit=Sum(
                F('SELLING_PRICE') * F('QUANTITY_SOLD') * F('PROFIT_MARGIN') - F('COST_PRICE') * F('QUANTITY_SOLD'),
                output_field=IntegerField()
            )
        ).values('PRODUCT_ID', 'PRODUCT_NAME', 'total_profit')
        return Response(product_profit_data)

    
class ProductSalesAPIView(APIView):
    def get(self, request):
        product_sales_data = Product.objects.annotate(
            total_sales=Sum('QUANTITY_SOLD')
        ).values('PRODUCT_ID', 'PRODUCT_NAME', 'total_sales')
        return Response(product_sales_data)

    
class TopSellingProductsByCategoryAPIView(APIView):
    def get(self, request):
        top_selling_products_data = Product.objects.values('PRODUCT_CATEGORY').annotate(
            total_sales=Sum('QUANTITY_SOLD')
        ).order_by('-total_sales')
        return Response(top_selling_products_data)


class AverageProfitMarginBySeasonAPIView(APIView):
    def get(self, request):
        average_profit_margin_data = Product.objects.values('SEASON').annotate(
            average_profit_margin=Avg('PROFIT_MARGIN')
        )
        return Response(average_profit_margin_data)


class LowStockHighDemandProductsAPIView(APIView):
    def get(self, request):
        low_stock_high_demand_products_data = Product.objects.filter(
            QUANTITY_SOLD__lt=F('SPACE_OCCUPIED') * 0.5,
            RATING__gte=4.5
        ).values('PRODUCT_ID',  
            'PRODUCT_NAME', 
            'QUANTITY_SOLD',
            'SPACE_OCCUPIED',
            'RATING')
        return Response(low_stock_high_demand_products_data)