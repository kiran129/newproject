from django import forms
from Practiceapp.models import Employee

class Employee(forms.ModelForm):
      class Meta:
          model=Employee
          fields='__all__'