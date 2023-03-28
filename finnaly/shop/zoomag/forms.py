from django import forms

class OrderForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)