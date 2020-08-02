import csv
import os
path =  "/home/hipolito/Documentos/dados2/"
os.chdir(path)
from sisu.models import *

with open('Sisu 2017_1 Pesos notas de corte.csv', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        try:
            curso_id = Curso.objects.get(campus__ies__sigla=row['SG_IES'],campus__nome=row['NO_CAMPUS'],nome=row['NO_CURSO'],turno=row['DS_TURNO'],grau=row['DS_GRAU'])
            pesocurso = PesoCurso(disciplina=row['NO_DISCIPLINA'],
                      curso=curso_id,
                      peso=float(row['NU_PESO']))
            pesocurso.save()
        except:
            continue
