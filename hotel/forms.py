from django import forms

from .models import Cliente, Habitacion, Empleado


class PruebaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Cliente
        fields = ('nombre', 'dpi', 'nit',)

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'dpi','nit',)

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('nombre', 'dpi','nit', 'direccion',)

class HabitacionForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Habitacion
        fields = ('nombre', 'numero', 'clientes',)

    def __init__ (self, *args, **kwargs):
        super(HabitacionForm, self).__init__(*args, **kwargs)
        self.fields["clientes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["clientes"].help_text = "* Ingrese los Huéspedes que se hospedarán en la habitación"
        self.fields["clientes"].queryset = Cliente.objects.all()
