from django.db import models


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_date_of_birth = models.DateField()
    customer_excel_file = models.FileField(upload_to='files/')
