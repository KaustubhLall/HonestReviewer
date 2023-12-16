from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('classify_reviews/', views.review_classification_view, name='classify_reviews'),

]
