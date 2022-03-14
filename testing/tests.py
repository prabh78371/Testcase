from django.test import TestCase
from testing.models import Student

# Create your tests here.
class StudentTest(TestCase):
    def setUp(self):
         Student.objects.create(first_name= "prabhjot",last_name="kaur",reg_number="123" )

# test the fields of model
    
    def test_first_name_label(self):
        student = Student.objects.get(id=1)
        field_name = student._meta.get_field('first_name').verbose_name
        self.assertEqual(field_name,'first name')

    
    def test_reg_number_label(self):
        student = Student.objects.get(id=1)
        field_name = student._meta.get_field('reg_number').verbose_name
        self.assertEqual(field_name,'reg number')


    def test_last_name_label(self):
        student = Student.objects.get(id=1)
        field_name = student._meta.get_field('last_name').verbose_name
        self.assertEqual(field_name,'last name')

# test the string function of model

    def test_string_method(self):
        student= Student.objects.get(id=1)
        expected_string = f"name:{student.first_name} {student.last_name} {student.reg_number}"
        self.assertEqual(str(student),expected_string)


# test the django views

    def test_index(self):
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code,404)

    def test_view(self):
        response = self.client.get('view/')
        self.assertEqual(response.status_code,404)