# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


conexion=sqlite3.connect("hackstore.db")
try:
    conexion.execute("""create table informacion (
                              codigo integer primary key AUTOINCREMENT,
                              nombre text,
                              url text,
                              idioma text


                        )""")
    print("se creo la tabla paciente")                        
except sqlite3.OperationalError:
    print("La tabla paciente ya existe")                    
conexion.close()

class Datos:

    def abrir(self):
        conexion=sqlite3.connect("hackstore.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into informacion(nombre, url,idioma) values (?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, url from informacion where nombre=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()