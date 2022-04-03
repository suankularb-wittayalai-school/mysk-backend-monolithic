from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_type_choices = (
        ("P", "Phone"),
        ("E", "Email"),
        ("F", "Facebook"),
        ("L", "Line"),
        ("T", "Twitter"),
        ("I", "Instagram"),
        ("W", "Website"),
        ("D", "Discord"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=contact_type_choices)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    middle_name_th = models.CharField(max_length=50, blank=True, null=True)
    first_name_en = models.CharField(max_length=50)
    last_name_en = models.CharField(max_length=50)
    middle_name_en = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField()
    citizen_id = models.CharField(max_length=13)
    contact = models.ManyToManyField(Contact, blank=True, null=True)

    def __str__(self):
        return f"{self.prefix_en} {self.first_name_en} {self.last_name_en}"


class Student(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="student"
    )
    student_id = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student_id}: {self.person.prefix_en} {self.person.first_name_en} {self.person.last_name_en}"


class Teacher(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, related_name="teacher"
    )
    teacher_id = models.CharField(max_length=5)
    # subject_group = models.ManyToManyField("SubjectGroup", blank=True, null=True)

    def __str__(self):
        return f"{self.teacher_id}: {self.person.prefix_en} {self.person.first_name_en} {self.person.last_name_en}"
