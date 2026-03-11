from fastapi import FastAPI
from pydantic import BaseModel
import json

app= FastAPI(
	title="API de Programación Agéntica - EPII Diurno",
        description="Elaborado por Fabian de la cruz",
        version="1.0.0.",
        contact={
                "name": "Fabian de la cruz perez",
                "email": "fjdelacruzp22@ul.edu.co",
        })

@app.get("/")
def initialEndpoint():
	return{"Message":"Hola mundo"}

@app.get("/exercise1")
def exercise1():
	nombre="Fabian"
	edad=21
	activo="True"
	return{"exercise":1,
		"nombre":nombre,
		"edad":edad,
		"activo":activo}

@app.get("/exercise2")
def exercise2(a:int=0,mb:int=0):
	return{"exercise":2,"resultado":a+b}


@app.get("/exercise3")
def exercise3(num:int):
	return{"exercise":3,"numero":num,"es par": num %2==0}

@app.get("/exercise4")
def exercise4():
	lista[1,2,3,4,5]
	recorrido=[n for n in lista]
	return{"exercise":4,"lista":recorrido}


@app.get("/exercise5")
def exercise5(a:int,b:int):
	return{"exercise":5,"resultado":a*b}

@app.get("/exercise6")
def exercise6():
	persona ={
			"nombre":"Fabian",
			"Edad": 21,
			"ciudad":"Barranquilla",
		}

	return{"exercise":6, "persona":persona}


@app.get("/exercise7")
def exercise7():
	persona = {
			"nombre":"Fabian",
			"Edad": 21,
			"Ciudad": "Barranquilla",
}
	claves = list (persona.keys())
	return{"exercise":7,"claves":claves}
