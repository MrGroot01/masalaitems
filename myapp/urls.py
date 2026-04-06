from django.urls import path
from .views import MasalItemsView

urlpatterns = [
    path('products/', MasalItemsView.as_view()),
]