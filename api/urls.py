from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products.as_view(), name='products'),
    path('products/<str:pk>/', views.ProductsRUD.as_view()),
    path('products/<str:pk>/reviews/', views.ProductReview.as_view()),
    path('category/', views.Category.as_view(), name='category'),
    path('category/<str:name>/', views.CategoryRU.as_view()),
    path('category/<str:name>/products/', views.CategoryProducts.as_view())
]