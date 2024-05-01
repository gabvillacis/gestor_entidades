import csv
from entidades.models import TipoGad

def feed_tipos_gad():
    TipoGad.objects.all().delete()
    
    with open('data/tipos_gad.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            tipo_gad = TipoGad(id=item['id'], nombre=item['nombre'])
            tipo_gad.save()
            print(f'TipoGad creado: {tipo_gad}')
        

def run():
    feed_tipos_gad()
