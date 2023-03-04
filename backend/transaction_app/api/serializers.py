from rest_framework import serializers
from transaction_app.models import Account, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name', 'amount', 'date', 'category', 'created', 'updated']