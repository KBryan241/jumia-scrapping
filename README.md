test-scrapping-jumia


comment lier une base de donne MySQL SERVER lancer MICROSOFT SQL SERVER MANAGEMENT STUDIO Creer une nouvelle requête et inscrivez les code sql ci-dessous:

################ CREATION DE LA BASE DE DONNEES ################################ CREATE DATABASE <votre_base>

#################### CREATION DES TABLES ###############################

USE <votre_base>

CREATE TABLE <nom_de_la table>(
id INT IDENTITY(1,1) PRIMARY KEY, (permet de definir une clé primaire qui s'incrementera de maniere automatique)
nom_variable type_variable ) (creer autant de champ que necessaire pour votre projet)


installer pyodbc  : pip install pyodbc  (package permettant la liaison avec la base de donnee)

puis dans votre script.py 

import pyodbc

  conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' (n'oublier pas d'installer le gestionnaire 
            'Server= localhost;'
                  'Database= nom_de_votre base;'
                  'Trusted_Connection=yes;')
                  
    (tester la connexion en executant ce code) 