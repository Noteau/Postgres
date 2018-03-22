#!/usr/bin/env/python
# coding: utf-8
import os
import gzip
import time

print("Bienvenue sur cet assistant de base de données SQL.\nSi vous voulez sauvegarder toutes les bases dans une archive compressée tapez 1.\nSi vous voulez sauvegarder une base de données en particulier tapez 2.\nSi vous voulez restaurer les bases de données à partir d'une sauvegarde spécifique tapez 3.\nSi vous voulez supprimer les sauvegardes datant de 7 jours ou plus tapez 4.\n")
is_number = True
while  is_number == True:
	try:
		choix = raw_input("Votre choix :\n")
		choix = int(choix)		
		choix = choix / 1
		if choix >= 5 or choix <= 0:
			print("Le nombre n'est pas valide.")			
		else:
			is_number = False
	except:
		print("Vous n'avez pas entré un nombre")
if choix == 1:
	if not os.path.exists("bdd_save"):
		os.makedirs("bdd_save")
	my_fichier_destination = raw_input("Le fichier de destination : ")
	my_user = raw_input("Votre nom d'utilisateur Mysql : ")	
	os.system('mysqldump -u%s -p --all-databases | gzip > ./bdd_save/%s.sql.gz'% (my_user, my_fichier_destination ) )
	print("Sauvegarde effectuée dans l'archive ./bdd_save/%s.sql.gz"% my_fichier_destination)
elif choix == 2:
	if not os.path.exists("bdd_save"):
		os.makedirs("bdd_save")
	my_fichier_destination = raw_input("Le fichier de destination : ")
	my_databases = raw_input("La base de données à sauvegarder : ")
	my_user = raw_input("Votre nom d'utilisateur Mysql : ")	
	os.system('mysqldump -u%s -p --databases %s | gzip > ./bdd_save/%s.sql.gz'% (my_user,my_databases,my_fichier_destination ))
	print("Sauvegarde effectuée dans l'archive ./bdd_save/%s.sql.gz"% my_fichier_destination)
elif choix == 3:
	my_fichier_source = raw_input("Votre fichier source : ")
	my_file = gzip.open('./bdd_save/%s.sql.gz'% my_fichier_source, 'rb')
	my_file_content = my_file.read()
	my_file.close()
	fichier = open("data.sql","a")
	fichier.write(my_file_content)
	fichier.close()
	my_user = raw_input("Votre nom d'utilisateur Mysql : ")
	os.system("mysql -u%s -p < data.sql"% my_user)
	print("Restauration effectuée.")
	os.remove("data.sql")
elif choix == 4:
	for element in os.listdir('./bdd_save/'):
		if element.endswith('sql.gz'):
			current_time = int(round(time.time()))
			file_time = os.path.getmtime("./bdd_save/%s"% element)
			if (current_time - file_time ) > 10 :
				os.remove("./bdd_save/%s"% element)
				print("Fichier %s supprimé avec succés"% element)
		else :
				print("%s est nop" % element)