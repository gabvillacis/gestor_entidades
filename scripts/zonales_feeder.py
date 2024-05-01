import csv
from entidades.models import Zonal

def feed_zonales():
    Zonal.objects.all().delete()
    
    with open('data/zonales.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            zonal = Zonal(id=item['id'], nombre=item['nombre'])
            zonal.save()
            print(f'Zonal creado: {zonal}')
        

def run():
    feed_zonales()
