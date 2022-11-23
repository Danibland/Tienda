from django import forms

from inventario.models import productos


class productos_form(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'