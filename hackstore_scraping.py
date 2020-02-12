#!/usr/bin/python
# -*- coding: utf-8 -*-
#obtener años
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
import sql

datos1 = sql.Datos()
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	 # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 -Peliculas")
	print ("\t2 -Series")
	print ("\t3 -Animes")
	print ("\t4 -Mostrar Busqueda")
	print ("\t9 - Salir")
 
 

def busqueda(nombre):
	titulos = []
	refs = []
	idiomas = []
	url = 'https://hackstore.net/'+nombre+'/'
	if url == 'https://hackstore.net/'+nombre+'/':
		response = get(url)
		res = BeautifulSoup(response.text,"html5lib");
		tags = res.findAll("div",{"class":"movie-back"})
		for tag in tags:
			titulo = tag.h3.getText()
			titulos.append(titulo)
		tags2 = res.findAll("div", {"class": "movie-back"})
		for tag in tags2:
			ref = tag.a.get("href")
			refs.append(ref)
		tags3 = res.findAll("div",{"class":"audios"})
		for tag in tags3:
			idioma = tag.getText()
			idiomas.append(idioma)
		for titulo,ref,idioma in zip(titulos,refs,idiomas):
			datos=(titulo,ref,idioma) 
			datos1.alta(datos)

		numeros = [str(i) for i in range(2,5)]
		for numero in numeros:
			url = 'https://hackstore.net/'+nombre+'/page/'+numero+'/'
			response = get(url)
			res = BeautifulSoup(response.text,"html5lib");
			tags = res.findAll("div", {"class": "movie-back"})
			for tag in tags:
				titulo = tag.h3.getText()
				titulos.append(titulo)
			tags2 = res.findAll("div", {"class": "movie-back"})
			for tag in tags2:
				ref = tag.a.get("href")
				refs.append(ref)
			
			tags3 = res.findAll("div",{"class":"audios"})
			for tag in tags3:
				idioma = tag.getText()
				idiomas.append(idioma)
			for titulo,ref,idioma in zip(titulos,refs,idiomas):
				datos=(titulo,ref,idioma) 
				datos1.alta(datos)			


while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
		busqueda("peliculas")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
		busqueda("series")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		busqueda("animes")
	elif opcionMenu=="4":
		print ("")
		nombre = str(input("Ingresa el nombre a buscar: "))
		
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



	

