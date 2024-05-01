import csv
from entidades.models import TipoOrganizacion

def feed_tipos_org():
    TipoOrganizacion.objects.all().delete()
    
    with open('data/tipos_organizaciones.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            tipo_org = TipoOrganizacion(id=item['id'], nombre=item['nombre'])
            tipo_org.save()
            print(f'TipoOrganizacion creada: {tipo_org}')
        

def run():
    feed_tipos_org()
