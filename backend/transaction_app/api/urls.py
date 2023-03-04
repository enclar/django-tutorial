from django.urls import path, include
from transaction_app.api.views import TransactionAV

urlpatterns = [
    path('list/', TransactionAV.as_view(), name='transaction-list'),
    # path('<int:pk>/', transaction_details, name='transaction-details'),
]