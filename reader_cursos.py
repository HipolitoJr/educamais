import csv
import os
path =  "/home/hipolito/Documentos/dados2/"
os.chdir(path)
from sisu.models import *

with open('Sisu 2017_1 Notas de corte.csv', encoding='ISO-8859-1') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		try:
			ies = Ies.objects.get(codigo=row['CÓD. IES'])
		except:
			ies = Ies(codigo=row['CÓD. IES'], nome=row['NOME IES'], sigla=row['SIGLA IES'])
			ies.save()
		try:
			campus = Campus.objects.get(nome=row['CAMPUS'])
		except:
			campus = Campus(nome=row['CAMPUS'], ies=ies)
			campus.save()
		try:
			curso = Curso.objects.get(codigo=row['CÓD CURSO'])
		except:
			curso = Curso(codigo=row['CÓD CURSO'], nome=row['NOME CURSO'], turno=row['TURNO'], grau=row['GRAU'], campus=campus)
			curso.save()
		curso = Curso.objects.get(codigo=row['CÓD CURSO'])
		modalidades = ModalidadeCurso(tipo=row['TIPO MODALIDADE'], descricao = row['MODALIDADE CONCORRÊNCIA'], nota_corte=row['NOTA DE CORTE'], curso=curso)
		modalidades.save()


with open('Sisu 2017_1 Notas de corte.csv', encoding='ISO-8859-1') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		try:
			modalidade = ModalidadeCurso.objects.get(curso__codigo=row['CÓD CURSO'], nota_corte=row['NOTA DE CORTE'])
			modalidade.descricao = row['MODALIDADE CONCORRÊNCIA']
			modalidade.save()
		except:
			continue