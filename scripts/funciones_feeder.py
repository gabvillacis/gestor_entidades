import csv
from entidades.models import Funcion

def feed_funciones():
    Funcion.objects.all().delete()
    
    with open('data/funciones.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            funcion = Funcion(id=item['id'], nombre=item['nombre'])
            funcion.save()
            print(f'Funcion creada: {funcion}')
        

def run():
    feed_funciones()
