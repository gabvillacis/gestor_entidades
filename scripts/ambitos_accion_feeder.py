import csv
from entidades.models import AmbitoAccion

def feed_funciones():
    AmbitoAccion.objects.all().delete()
    
    with open('data/ambitos_accion.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            ambito_accion = AmbitoAccion(id=item['id'], nombre=item['nombre'])
            ambito_accion.save()
            print(f'AmbitoAccion creado: {ambito_accion}')
        

def run():
    feed_funciones()
