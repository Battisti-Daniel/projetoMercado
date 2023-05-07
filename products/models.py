from django.db import models

class Types_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    expired = models.DateField()
    quant = models.IntegerField()
    code = models.IntegerField()
    type_product = models.ForeignKey(Types_model,on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    