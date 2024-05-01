import csv
from entidades.models import Canton, Parroquia

def feed_parroquias():
    Parroquia.objects.all().delete()
    
    with open('data/parroquias.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            print(item)
            canton = Canton(id=item['id_canton'])
            parroquia = Parroquia(id=item['id_parroquia'], nombre=item['nombre_parroquia'], canton=canton)
            parroquia.save()
            print(f'Parroquia creada: {parroquia}')
        

def run():
    feed_parroquias()
