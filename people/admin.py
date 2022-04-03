from django.contrib import admin
from .models import Contact, Person, Student, Teacher

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "value")


class PersonAdmin(admin.ModelAdmin):
    list_display = ("prefix_en", "first_name_en", "last_name_en")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "person")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_id", "person")


admin.site.register(Contact, ContactAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
