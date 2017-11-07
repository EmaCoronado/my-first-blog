from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import HabitacionForm, ClienteForm, EmpleadoForm, PruebaForm
from hotel.models import Habitacion, Cliente, Empleado, Reservacion


# Create your views here.


def reservacion_list(request):
    habitaciones=Habitacion.objects.filter()
    return render(request, 'hotel/reservacion.html', {'posts': habitaciones})


def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm()
    return render(request, 'hotel/cliente_edit.html', {'form': form})

def cliente_list(request):
    cliente=Cliente.objects.filter()
    return render(request, 'hotel/cliente.html', {'posts': cliente})


def cliente_detail(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    return render(request, 'hotel/cliente_detail.html', {'post':post})


def cliente_edit(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm(instance=post)
    return render(request, 'hotel/cliente_edit.html', {'form': form})

def cliente_remove(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    post.delete()
    return redirect('cliente_list')

def empleado_new(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('empleado_detail', pk=post.pk)
    else:
        form = EmpleadoForm()
    return render(request, 'hotel/empleado_edit.html', {'form': form})

def empleado_list(request):
    empleado=Empleado.objects.filter()
    return render(request, 'hotel/empleado.html', {'posts': empleado})

def empleado_detail(request, pk):
    post = get_object_or_404(Empleado, pk=pk)
    return render(request, 'hotel/empleado_detail.html', {'post':post})

def empleado_edit(request, pk):
    post = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('empleado_detail', pk=post.pk)
    else:
        form = EmpleadoForm(instance=post)
    return render(request, 'hotel/empleado_edit.html', {'form': form})

def empleado_remove(request, pk):
    post = get_object_or_404(Empleado, pk=pk)
    post.delete()
    return redirect('empleado_list')


def reservacion_nueva(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            habitacion = Habitacion.objects.create(nombre=form.cleaned_data['nombre'], numero = form.cleaned_data['numero'])
            for cliente_id in request.POST.getlist('clientes'):
                reservacion = Reservacion(cliente_id=cliente_id, habitacion_id = habitacion.id)
                reservacion.save()
                return redirect('reservacion_list')
    else:
        form = HabitacionForm()
    return render(request, 'hotel/reservacion_editar.html', {'form': form})

def reservacion_editar(request, pk):
    post = get_object_or_404(Habitacion, pk=pk)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reservacion_detail', pk=post.pk)
    else:
        form = HabitacionForm(instance=post)
    return render(request, 'hotel/reservacion_editar.html', {'form': form})

def reservacion_detail(request, pk):
    post = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'hotel/reservacion_detail.html', {'post':post})

def reservacion_remove(request, pk):
    post = get_object_or_404(Habitacion, pk=pk)
    post.delete()
    return redirect('reservacion_list')
