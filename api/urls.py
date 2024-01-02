from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [
    path('products/', views.Products.as_view(), name='products'),
    path('products/<str:pk>/', views.ProductsReadUpdateDelete.as_view()),
    path('products/<str:pk>/reviews/', views.ProductReview.as_view()),
    path('', include('api.routers')),
    path('category/', views.Category.as_view(), name='category'),
    path('category/<str:name>/', views.CategoryReadUpdate.as_view(), name='category_read_update'),
    path('cart/', views.UserCart.as_view()),
    path('cart/delete/<str:pk>/', views.DeleteCartItem.as_view()),
    path('cart/delete', views.DeleteCartItems.as_view()),
]
