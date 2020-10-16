from django import forms

class RegisterForm(forms.Form):
    nombre = forms.CharField(required=True, min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'nombre'
                                }))
    responsable = forms.CharField(required=True, min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'responsable',
                                }))
    telefono = forms.CharField(required=True, min_length=10, max_length=10,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'telefono'
                                }))
    direccion = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'direccion'
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@email.com'
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'password'
                                }))
