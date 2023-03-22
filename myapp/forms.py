from django import forms
from django.core.validators import RegexValidator
from .models import Student
import re

class StudentForm(forms.ModelForm):
    # name=forms.CharField()
    # email=forms.EmailField()
    # phone=forms.CharField()
    class Meta:
        model = Student
        fields = ['name','email','phone']
        # labels ={'name':'Enter Name','email':'Enter Email','phone':'Mobile No.'}
        
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if not re.match(r'^[A-Za-z ]+$', name):
    #         raise forms.ValidationError('Name can only contain letters')
    #     return name

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not re.match(r'^\d{10}$', phone):
    #         raise forms.ValidationError('Mobile number must be a 10-digit ')
    #     return phone


