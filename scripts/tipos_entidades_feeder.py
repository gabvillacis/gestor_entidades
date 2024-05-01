import csv
from entidades.models import TipoEntidad

def feed_entidades():
    TipoEntidad.objects.all().delete()
    
    with open('data/tipos_entidades.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            tipo_entidad = TipoEntidad(id=item['id'], nombre=item['nombre'])
            tipo_entidad.save()
            print(f'TipoEntidad creada: {tipo_entidad}')
        

def run():
    feed_entidades()
