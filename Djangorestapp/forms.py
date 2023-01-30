from django import forms
from Djangorestapp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal= self.cleaned_data['EmpSal']
        if inputsal<15000:
            raise forms.ValidationError('The minimum salary should be 15000')
        return inputsal
    class Meta:
        model=Employee
        fields= '__all__'   