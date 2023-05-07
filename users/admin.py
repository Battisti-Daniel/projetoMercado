from django.contrib import admin
from users.models import Employed_register,Gender,Job_type

class Employed_register_admin(admin.ModelAdmin):
    list_display = ("name","last_name","gender","born"
                    ,"employed_function","telephone",
                    "email","register_time","photo")
    search_fields = ("name","last_name")

class Gender_admin(admin.ModelAdmin):
    list_display = ("gender_type",)
  
class Job_type_admin(admin.ModelAdmin):
    list_display = ("name","salary","quantity")
    search_fields = ("name",)

admin.site.register(Employed_register,Employed_register_admin)
admin.site.register(Gender,Gender_admin)
admin.site.register(Job_type,Job_type_admin)