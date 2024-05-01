import csv
from entidades.models import Provincia, Canton

def feed_cantones():
    Canton.objects.all().delete()
    
    with open('data/cantones.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            provincia = Provincia(id=item['id_provincia'])
            canton = Canton(id=item['id'], nombre=item['nombre_canton'], provincia=provincia)
            canton.save()
            print(f'Canton creado: {canton}')
        

def run():
    feed_cantones()
