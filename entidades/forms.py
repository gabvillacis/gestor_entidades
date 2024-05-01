from django import forms
from entidades.models import Entidad

class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        exclude = ['fecha_registro', 'fecha_ult_act']