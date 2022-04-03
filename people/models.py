from django.db import models

# Create your models here.
class Person(models.Model):
    prefix_en_choices = (
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
        ("Ms.", "Ms."),
        ("Master", "Master"),
    )
    prefix_th_choices = (
        ("นาย", "นาย"),
        ("นาง", "นาง"),
        ("นางสาว", "นางสาว"),
        ("เด็กชาย", "เด็กชาย"),
    )

    prefix_en = models.CharField(max_length=10, choices=prefix_en_choices)
    prefix_th = models.CharField(max_length=10, choices=prefix_th_choices)
    first_name_th = models.CharField(max_length=50)
    last_name_th = models.CharField(max_length=50)
    middle_name_th = models.CharField(max_length=50)
    first_name_en = models.CharField(max_length=50)
    last_name_en = models.CharField(max_length=50)
    middle_name_en = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField()
    citizen_id = models.CharField(max_length=13)
    # contact = models.ManyToManyField("Contact", blank=True)
