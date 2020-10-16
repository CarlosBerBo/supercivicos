from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data.get('nombre' )
        responsable = form.cleaned_data.get('responsable') #dic
        email = form.cleaned_data.get('email' )
        telefono = form.cleaned_data.get('telefono')
        password = form.cleaned_data.get('password' )
        direccion = form.cleaned_data.get('direccion')
        empresa = User.objects.create_user(nombre, responsable, email, password,
                                            telefono, direccion, empresa)
        if empresa:
            login(request, empresa)
            messages.success(request, 'Empresa registrada exitosamente')
            return redirect('')
    return render(request, 'register_empresa.html', {'form': form

    })
