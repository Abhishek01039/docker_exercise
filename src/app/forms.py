from django import forms
# from django.core import validators
from app.models import person
# def check_name(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("Name start with z")
#     return value

class detail(forms.ModelForm):
    id=forms.IntegerField(disabled=True,widget=forms.HiddenInput(),required=False)
    name=forms.CharField()
    email=forms.EmailField()
    salary=forms.IntegerField(max_value=500)
    
    class Meta:
        # db_table = person
        model=person
        fields=['id','name','email','salary']
        # # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
    
    # clean is a keyword to validate the form
    # def clean_address(self):
    #     address=self.cleaned_data['address']
    #     if len(address)==0:
    #         raise forms.ValidationError("Please Enter Right Address")
    #     return address

    # def clean_name(self):
    #     Name=self.cleaned_data['name']
    #     if Name[0]!="B":
    #         raise forms.ValidationError("Please Enter right Name")
    #     return Name

    def clean_name(self):
        Name=self.cleaned_data['name']
        if Name[0]!="B":
            raise forms.ValidationError("Please Enter Name starts with B")
        return Name