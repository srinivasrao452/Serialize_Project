
from Serialize_App.models import Employee
from django import forms

# from local to server

# from server to local

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
