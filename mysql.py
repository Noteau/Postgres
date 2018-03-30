#!/usr/bin/env/python
# coding: utf-8
import os
import gzip
import time
import re
import sys

def verif(my_fichier_destination):
	my_file = gzip.open('./bdd_save/%s.sql.gz'% my_fichier_destination, 'rb')
	my_file_content = my_file.read()
	my_file.close()
	if my_file_content != '':
		return True
	else:
		return False

def getAllData():
	try :
		ip = input("L'adresse ip du serveur auquel vous voulez accéder (laissez vide pour le localhost):")
		if ip == '':
			ip = '127.0.0.1'
		if not os.path.exists("bdd_save"):
			os.makedirs("bdd_save")
		my_fichier_destination = input("Le fichier de destination : ")
		my_user = input("Votre nom d'utilisateur Mysql : ")	
		os.system('mysqldump -u%s -p -h %s --all-databases | gzip > ./bdd_save/%s.sql.gz'% (my_user, ip, my_fichier_destination ) )
		is_verif = verif(my_fichier_destination)
		if is_verif == True:
			print("Sauvegarde effectuée dans l'archive ./bdd_save/%s.sql.gz"% my_fichier_destination)
		else:
			os.remove('./bdd_save/%s.sql.gz'% my_fichier_destination)
			raise
	except :
		print("Une erreur est survenu lors de la sauvegarde des bases de données")

def getOneData():
	try :
		ip = input("L'adresse ip du serveur auquel vous voulez accéder (laissez vide pour le localhost):")
		if ip == '':
			ip = '127.0.0.1'
		if not os.path.exists("bdd_save"):
			os.makedirs("bdd_save")
		my_fichier_destination = input("Le fichier de destination : ")
		my_databases = input("La base de données à sauvegarder : ")
		my_user = input("Votre nom d'utilisateur Mysql : ")	
		os.system('mysqldump -u%s -p -h%s --databases %s | gzip > ./bdd_save/%s.sql.gz'% (my_user, ip, my_databases,my_fichier_destination ))
		is_verif = verif(my_fichier_destination)
		if is_verif == True:
			print("Sauvegarde effectuée dans l'archive ./bdd_save/%s.sql.gz"% my_fichier_destination)
		else:
			os.remove('./bdd_save/%s.sql.gz'% my_fichier_destination)
			raise
	except :
		print("Une erreur est survenu lors de la sauvegarde de la base de données")

def restoreData():
	try :
		my_fichier_source = input("Votre fichier source : ")
		my_file = gzip.open('./bdd_save/%s.sql.gz'% my_fichier_source, 'rb')
		my_file_content = my_file.read()
		my_file.close()
		fichier = open("data.sql","a")
		fichier.write(my_file_content)
		fichier.close()
		my_user = input("Votre nom d'utilisateur Mysql : ")
		os.system("mysql -u%s -p < data.sql"% my_user)
		print("Restauration effectuée.")
		os.remove("data.sql")
	except :
		print("Une erreur est survenu lors de la restauration")

def removeSave():
	try :
		for element in os.listdir('./bdd_save/'):
			if element.endswith('sql.gz'):
				current_time = int(round(time.time()))
				file_time = os.path.getmtime("./bdd_save/%s"% element)
				if (current_time - file_time ) > 10 :
					os.remove("./bdd_save/%s"% element)
					print("Fichier %s supprimé avec succés"% element)
			else :
					print("%s est nop" % element)
	except :
		print("Une erreur est survenu lors de la suppresion des sauvegardes")

print("Bienvenue sur cet assistant de base de données SQL.\nSi vous voulez sauvegarder toutes les bases dans une archive compressée tapez 1.\nSi vous voulez sauvegarder une base de données en particulier tapez 2.\nSi vous voulez restaurer les bases de données à partir d'une sauvegarde spécifique tapez 3.\nSi vous voulez supprimer les sauvegardes datant de 7 jours ou plus tapez 4.\n")
is_number = True
while  is_number == True:
	try :
		choix = input("Votre choix :\n")
		choix = int(choix)		
		choix = choix / 1
		if choix >= 5 or choix <= 0:
			print("Le nombre n'est pas valide.")			
		else:
			is_number = False
	except:
		print("Vous n'avez pas entré un nombre")

if choix == 1:
	getAllData()
elif choix == 2:
	getOneData()
elif choix == 3:
	restoreData()
elif choix == 4:
	
