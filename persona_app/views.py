from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Persona
from .forms import PersonaForm
#Vista Principal
def listar_personas(request):
    search = request.GET.get('search')  # Obtiene el parámetro de búsqueda
    if search:
        personas = Persona.objects.filter(
            Q(CI__icontains=search) | 
            Q(nombre__icontains=search) | 
            Q(apellido__icontains=search)| 
            Q(nombre__icontains=search.split()[0]) & Q(apellido__icontains=' '.join(search.split()[1:]))
        )
    else:
        personas = Persona.objects.all()  # Obtiene todas las personas si no hay búsqueda
    
    paginator = Paginator(personas, 5)  # Muestra 5 personas por página
    page_number = request.GET.get('page')  # Obtiene el número de la página actual
    page_obj = paginator.get_page(page_number)  # Obtiene las personas para esa página

    return render(request, 'listar_personas.html', {'page_obj': page_obj})
    
    
#Vista de Crear Persona 
def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm()
    return render(request, 'crear_persona.html', {'form': form})

#Vista de Actualizar Persona
def actualizar_persona(request, CI):
    persona = get_object_or_404(Persona, CI=CI)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'crear_persona.html', {'form': form})

#Vista de Eliminar Persona
def eliminar_persona(request, CI):
    persona = get_object_or_404(Persona, CI=CI)
    if request.method == 'POST':
        persona.delete()
        return redirect('listar_personas')
    return render(request, 'eliminar_persona.html', {'persona': persona})
