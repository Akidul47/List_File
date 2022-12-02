from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import CompilerModel

class ReviewForm(ModelForm):
    #Id_num = forms.IntegerField(label='ID')
    #last_name = forms.CharField(label='Last Name', max_length= 100)
    #code = forms.CharField(label="Code", widget=forms.Textarea())
    #email = forms.EmailField(label='Email'fr
    class Meta:
        model = CompilerModel
        fields = ('code',)