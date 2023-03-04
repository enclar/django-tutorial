from django.contrib import admin
from transaction_app.models import Account, Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)