from django import forms
from student.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'email', 'password', 'age']