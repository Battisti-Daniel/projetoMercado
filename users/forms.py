from django import forms
from users.models import  Employed_register

class Register_model_form(forms.ModelForm):
    class Meta:
        model = Employed_register
        fields = "__all__"
        exclude = [
            "register_time"
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if(len(name) < 3):
            self.add_error("name","O Nome do usuario deve ter no minimo 3 caracteres")
        return name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if(len(last_name) < 3):
            self.add_error("last_name","O sobrenome do usuário deve ter no minimo 3 caracteres")
        return last_name
    
    def clean_born(self):
        born = self.cleaned_data.get("born")
        if(born.year > 2005):
            self.add_error("born","O funcionario que deseja cadastrar nao tem a idade minima")
        return born
    
    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        if( len(telephone) != 11):
            self.add_error("telephone","Por favor verificar o numero de telefone se esta correto")
        return telephone
    
    def clean_pessoal_id(self):
        pessoal_id = self.cleaned_data.get("pessoal_id")
        if(len(pessoal_id)!= 11) :
            self.add_error("pessoal_id","CPF inserido de forma incorreta, verifique tente novamente")
        return pessoal_id