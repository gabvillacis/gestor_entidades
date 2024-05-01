from django.shortcuts import render
from entidades.models import *
from django.http import JsonResponse
from entidades.forms import EntidadForm

def home(request):
    
    if request.method == 'POST':
        # Aquí se va a procesar el formulario
        
        try:
            form = EntidadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({'resultado': 'ok'})
            else:
                errores = form.errors.as_json()
                return JsonResponse({'resultado': 'nok', 'msg_error': errores}, status=400)
        except Exception as e:
            return JsonResponse({'resultado': 'nok', 'msg_error': str(e)}, status=500)
            
    
    tipos_organizaciones = TipoOrganizacion.objects.all()
    tipos_entidades = TipoEntidad.objects.all()
    funciones = Funcion.objects.all()
    ambitos_accion = AmbitoAccion.objects.all()
    zonales = Zonal.objects.all()
    provincias = Provincia.objects.all()
    tipos_gad = TipoGad.objects.all()
    
    return render(request, 'index.html',{'tipos_organizaciones': tipos_organizaciones,
                                          'tipos_entidades': tipos_entidades,
                                          'funciones': funciones,
                                          'ambitos_accion': ambitos_accion,
                                          'zonales': zonales,
                                          'provincias': provincias,
                                          'tipos_gad': tipos_gad,
                                        })    

def get_cantones(request, provincia_id):   
    cantones = Canton.objects.filter(provincia__id=provincia_id).values('id', 'nombre')
    cantones_dict_list = list(cantones)  # Convierte los objetos QuerySet en una lista de diccionarios
    return JsonResponse(cantones_dict_list, safe=False)


def get_parroquias(request, canton_id):   
    parroquias = Parroquia.objects.filter(canton__id=canton_id).values('id', 'nombre')
    parroquias_dict_list = list(parroquias)  # Convierte los objetos QuerySet en una lista de diccionarios
    return JsonResponse(parroquias_dict_list, safe=False)