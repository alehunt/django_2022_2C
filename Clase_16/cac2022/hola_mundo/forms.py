from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Contacto:", required=False, max_length=10)
    apellido = forms.CharField(label="Apellido de contacto", required=False)
    email = forms.EmailField()
    
