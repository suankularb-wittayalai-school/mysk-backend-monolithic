from django.test import TestCase

from .models import Contact, Person, Student, Teacher

# Create your tests here.


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(name="Phone", type="P", value="0912345678")

    def test_contact_name(self):
        contact = Contact.objects.get(name="Phone")
        self.assertEqual(contact.name, "Phone")

    def test_contact_type(self):
        contact = Contact.objects.get(name="Phone")
        self.assertEqual(contact.type, "P")

    def test_contact_value(self):
        contact = Contact.objects.get(name="Phone")
        self.assertEqual(contact.value, "0912345678")

    def test_contact_str(self):
        contact = Contact.objects.get(name="Phone")
        self.assertEqual(str(contact), "Phone")

    def test_update_contact(self):
        contact = Contact.objects.get(name="Phone")
        contact.value = "0987654321"
        contact.save()
        self.assertEqual(contact.value, "0987654321")

    def test_delete_contact(self):
        contact = Contact.objects.get(name="Phone")
        contact.delete()
        self.assertEqual(Contact.objects.count(), 0)


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            prefix_en="Mr.",
            prefix_th="นาย",
            first_name_th="สมชาย",
            last_name_th="สมบัติ",
            first_name_en="Somchai",
            last_name_en="Sombut",
            birthdate="2000-01-01",
            citizen_id="1234567890123",
        )

    def test_person_prefix_en(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.prefix_en, "Mr.")

    def test_person_prefix_th(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.prefix_th, "นาย")

    def test_person_first_name_th(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.first_name_th, "สมชาย")

    def test_person_last_name_th(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.last_name_th, "สมบัติ")

    def test_person_middle_name_th(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.middle_name_th, None)

    def test_person_first_name_en(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.first_name_en, "Somchai")

    def test_person_last_name_en(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(person.last_name_en, "Sombut")

    def test_person_add_contact(self):
        person = Person.objects.get(first_name_en="Somchai")
        contact = Contact.objects.create(name="Phone", type="P", value="0912345678")
        person.contacts.add(contact)
        self.assertEqual(person.contacts.count(), 1)

    def test_person_str(self):
        person = Person.objects.get(first_name_en="Somchai")
        self.assertEqual(str(person), "Mr. Somchai Sombut")

    def test_person_update(self):
        person = Person.objects.get(first_name_en="Somchai")
        person.first_name_en = "Somchai2"
        person.save()
        self.assertEqual(person.first_name_en, "Somchai2")

    def test_person_delete(self):
        person = Person.objects.get(first_name_en="Somchai")
        person.delete()
        self.assertEqual(Person.objects.count(), 0)

    def test_person_delete_with_contact(self):
        person = Person.objects.get(first_name_en="Somchai")
        contact = Contact.objects.create(name="Phone", type="P", value="0912345678")
        person.contacts.add(contact)
        person.delete()
        self.assertEqual(Person.objects.count(), 0)
        self.assertEqual(Contact.objects.count(), 1)


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            student_id="1234567890123",
            person=Person.objects.create(
                prefix_en="Mr.",
                prefix_th="นาย",
                first_name_th="สมชาย",
                last_name_th="สมบัติ",
                first_name_en="Somchai",
                last_name_en="Sombut",
                birthdate="2000-01-01",
                citizen_id="1234567890123",
            ),
        )

    def test_student_id(self):
        student = Student.objects.get(student_id="1234567890123")
        self.assertEqual(student.student_id, "1234567890123")

    def test_student_person(self):
        student = Student.objects.get(student_id="1234567890123")
        self.assertEqual(student.person.first_name_en, "Somchai")

    def test_student_str(self):
        student = Student.objects.get(student_id="1234567890123")
        self.assertEqual(str(student), "1234567890123: Mr. Somchai Sombut")

    def test_student_update(self):
        student = Student.objects.get(student_id="1234567890123")
        student.student_id = "1234567890124"
        student.save()
        self.assertEqual(student.student_id, "1234567890124")

    def test_student_delete(self):
        student = Student.objects.get(student_id="1234567890123")
        student.delete()
        self.assertEqual(Student.objects.count(), 0)

    def test_student_delete_with_person(self):
        student = Student.objects.get(student_id="1234567890123")
        student.person.delete()
