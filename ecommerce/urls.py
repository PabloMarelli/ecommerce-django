from django.urls import path
from ecommerce import views


urlpatterns = [
    # Customers URLs
    path("customers/", views.CustomerList.as_view(), name="customer-list"),
    path("customers/<int:pk>/", views.CustomerDetail.as_view(), name="customer-detail"),
    # Product URLs
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
    # Transactions URLs
    path("transactions/", views.TransactionList.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", views.TransactionDetail.as_view(), name="transaction-detail"),
    # Categorys URLs
    path("categorys/", views.category_list, name="category-list"),
    path("categorys/<int:pk>/", views.category_detail, name="category-detail"),
    # Tags URLs
    path("tags/", views.TagList.as_view(), name="tag-list"),
    path("tags/<int:pk>/", views.TagDetail.as_view(), name="tag-detail"),
    
]
