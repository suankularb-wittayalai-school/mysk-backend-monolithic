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

    def test_contact_repr(self):
        contact = Contact.objects.get(name="Phone")
        self.assertEqual(repr(contact), "Phone")

    def test_update_contact(self):
        contact = Contact.objects.get(name="Phone")
        contact.value = "0987654321"
        contact.save()
        self.assertEqual(contact.value, "0987654321")

    def test_delete_contact(self):
        contact = Contact.objects.get(name="Phone")
        contact.delete()
        self.assertEqual(Contact.objects.count(), 0)
