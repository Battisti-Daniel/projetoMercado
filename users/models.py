from django.db import models


class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    gender_type = models.CharField(max_length=50)

    def __str__(self):
        return self.gender_type

class Job_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    salary = models.FloatField()

    def __str__(self):
        return self.name
    

class Employed_register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    pessoal_id = models.CharField(max_length=11)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    born = models.DateField()
    employed_function = models.ForeignKey(Job_type,on_delete=models.PROTECT)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    register_time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null= True,blank=True)

    def __str__(self):
        return self.name