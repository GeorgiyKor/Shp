from django.contrib import admin
from .models import Item,Company, Deliveries, Categories, Purchases, Cheque


admin.site.register(Company)
admin.site.register(Deliveries)
admin.site.register(Item)
admin.site.register(Categories)
admin.site.register(Purchases)
admin.site.register(Cheque)
# Register your models here.
