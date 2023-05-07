from django.shortcuts import render,redirect
from users.forms import Register_model_form
from users.models import Employed_register

def register_view(request):

    if request.method == "POST":
        register = Register_model_form(request.POST,request.FILES)
        if register.is_valid():
            register.save()
            register = Register_model_form()
            redirect("register_view")
    else:
        register = Register_model_form()
    
    db_values = Employed_register.objects.all()        
    return render(request,"register.html",{"register" : register, "db_values" : db_values})
