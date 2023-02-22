from django import forms

from app.models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = 'name','email','subject','message'