from django import forms

class Student_Form(forms.Form):
    Sname=forms.CharField()
    Email=forms.EmailField()
    ReenterEmail=forms.EmailField()
    Password=forms.CharField()
    Reenterpassword=forms.CharField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        Pa=self.cleaned_data['Password']
        RPa=self.cleaned_data['Reenterpassword']
        if Pa!=RPa:
            raise forms.ValidationError('Both are not match')
        
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>=1:
            raise forms.ValidationError('Bot')