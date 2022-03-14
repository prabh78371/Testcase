from django import forms
from testing.models import Student
class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


