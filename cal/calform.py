from django import forms

class CalForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={"style": "resize: none; border: none;","id":"hi"}))
    box = forms.CharField(widget=forms.Textarea(attrs={"style": "resize: none; border: none;","id":"hi"}))
    day = forms.TimeField()
    #description = forms.CharField()
    #views = forms.IntegerField()
    #available = forms.BooleanField()





# from django.forms import ModelForm, Textarea
# from myapp.models import MyModel
#
# class CalForm(ModelForm)
#     class Meta:
#         model = MyModel
#         widgets = {
#           'summary': Textarea(attrs={'rows':80, 'cols':20}),
#         }
