from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['CI', 'nombre', 'apellido', 'email', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
    # Validación personalizada para CI

    def clean_CI(self):
        ci = self.cleaned_data.get('CI')
         # Verificar que el CI tenga exactamente 10 dígitos
        if len(ci) != 10:
            raise forms.ValidationError(
                "El número de cédula debe tener 10 dígitos.")
        # Verificar que el CI contenga solo números
        if not ci.isdigit():
            raise forms.ValidationError(
                "El número de cédula solo debe contener dígitos númericos.")
        # Verificar que el CI sea único, a menos que estemos actualizando la misma persona
        if Persona.objects.filter(CI=ci).exists() and not self.instance.pk:
            raise forms.ValidationError(
                "El número de cédula ya está registrado.")
        return ci

    # Validación personalizada para Email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Este campo es obligatorio.")
        if not "@" in email or not "." in email:
            raise forms.ValidationError(
                "Ingrese un correo electrónico válido.")
        return email
