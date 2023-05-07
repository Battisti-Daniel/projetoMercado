from django.contrib import admin
from products.models import Product_model,Types_model

class Product_model_admin(admin.ModelAdmin):
    list_display = ("name","quant","expired","code","type_product",)
    search_fields = ("name",)

class Types_model_admin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Product_model,Product_model_admin)
admin.site.register(Types_model,Types_model_admin)