import csv
import os
path =  "/home/hipolito/Documentos/dados/"
os.chdir(path)
from enem.models import *

with open('BASE_TOTAL_FINAL.csv', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        try:
            tipo_perfil = TipoPerfil.objects.get(renda_familiar=row['Q006'], tipo_escola=row['TP_ESCOLA'], cor_raca=row['TP_COR_RACA'])
        except:
            tipo_perfil = TipoPerfil.objects.create(renda_familiar=row['Q006'], tipo_escola=row['TP_ESCOLA'], cor_raca=row['TP_COR_RACA'])
        try:
            area = Area.objects.get(perfil=tipo_perfil, prova=row['area'])
        except:
            area = Area(perfil=tipo_perfil, prova=row['area'], frequencia=row['frequencia'], media=row['media'])
            if int(area.frequencia) > 1:
                area.variancia = row['variancia']
            area.save()
with open('BASE_FINAL.csv', encoding='ISO-8859-1') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')
	for row in reader:
		tipo_perfil = TipoPerfil.objects.get(renda_familiar=row['Q006'], tipo_escola=row['TP_ESCOLA'], cor_raca=row['TP_COR_RACA'])
		area = Area.objects.get(perfil=tipo_perfil, prova=row['area'])
		try:
			percentil = Percentil.objects.get(area=area, valor=row['pct'])
		except:
			percentil = Percentil(area=area, valor=row['pct'], frequencia=row['frequencia'], media=row['media'])
			percentil.save()




