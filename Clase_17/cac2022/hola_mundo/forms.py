from django import forms
from django.core import validators
from django.forms import ValidationError


def messi_validate(value):
    if not value or str(value).upper() != "MESSI":
        raise ValidationError("No puede no ser Messi", code="error_messi",)


class ContactoForm(forms.Form):
    TORNEO_CHOICES = (
        (1, "Champions"),
        (2, "Supercopa"),
        (3, "Copa Argentina"),
        (4, "LPF"),
    )

    nombre = forms.CharField(label="Contacto:", required=False, max_length=10)
    apellido = forms.CharField(label="Apellido de contacto", required=False)
    email = forms.EmailField()
    sitio_favorito = forms.URLField(label="Sitio Favorito")
    nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=['1980', '1981', '1982']))
    jugador_favorito = forms.CharField(label="Jugador Favorito:", validators=(messi_validate,))
    torneo_favorito = forms.ChoiceField(label="Torneo Favorito:", choices=TORNEO_CHOICES)

    def clean_torneo_favorito(self):
        data = self.cleaned_data['torneo_favorito']
        if data != "1":
            raise ValidationError("No podes no elegir a la Champions")

        return data
