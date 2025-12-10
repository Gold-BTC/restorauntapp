from django.urls import path
from . import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('',views.DishListView.as_view(),name='dish-list'),
]