import csv
from entidades.models import Provincia

def feed_provincias():
    Provincia.objects.all().delete()
    
    with open('data/provincias.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            provincia = Provincia(id=item['id'], nombre=item['nombre'])
            provincia.save()
            print(f'Provincia creada: {provincia}')
        

def run():
    feed_provincias()
