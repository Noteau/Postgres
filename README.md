# Postgres
Projet Postgres

__Etape 1 :__  Installer une machine virutelle Ubuntu 64 bits disponible à l'addresse : *https://ubuntu-fr.org/telechargement*

__Etape 2 :__ Installer Mysql serveur avec la commande : sudo apt install mysql-server

__Etape 3 :__ Dans le terminal Mysql (ouvrable avec mysql -u root -p) et tapez "CREATE USER 'appli_web'@'localhost' IDENTIFIED BY 'password';" pour creer un utilisateur
Nous utilisons ensuite "GRANT ALL PRIVILEGES ON * . * TO 'appli_web'@'localhost';" pour donner les permissions à notre utilisateur. Enfin "FLUSH PRIVILEGES;" permet de valider et mettre à jour les priviléges.

__Etape 4 :__ Toujours dans le terminal Mysql tapez "CREATE DATABASE appli_web;"

__Etape 5 :__ Installer PhpMyAdmin avec la commande "sudo apt install phpmyadmin" et il faut sélectionner Apache 2 comme serveur HTTP en appuyant sur espace

__Etape 6 :__ Allez sur le site : http://www.generatedata.com/?lang=fr et creer de la données à votre guise pour le télécharger au format SQL et un type de base de données MySQL, ne pas oublier de décocher la case "Inclure une requete DROP TABLE" si votre table n'existe pas encore.

__Etape 7 :__ Faite un import du fichier précendent dans PhpMyAdmin

__Etape 8 :__ Telecharger le script à partir du dépôt Github : https://github.com/Noteau/Postgres

__Etape 9 :__ Pour éxécuter le script python il est nécessaire d'utiliser Python 3.6 (téléchargable ici : https://www.python.org/downloads/)
Et de l'éxécuter par la commande python mysql.py
Une fois à cette étape le script vous accompagnera pour réaliser les dernières étapes en vous demandant les informations requises pour réaliser les interactions avec la base de données.
