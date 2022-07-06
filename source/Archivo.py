import requests
import json

class Lectura:
    def __init__(self):
        pass

    def leer_archivo(self):
        lista = []
        i=1
        url = "http://localhost:8080/view/creaemployee"


        with open("source/Archivos/Clientes.txt") as file:
            for line in file:
                result = line.split(",")
                myList = [i.split('\n')[0] for i in result]
                myList = [i.rstrip() for i in myList]
                myList = [i.lstrip() for i in myList]

                _json = {"surname": str(myList[0]), "firstname": str(myList[1]) }

                _headers = {"Content-Type": "application/json"}

                response = requests.post(url,data=json.dumps(_json), headers=_headers)

                print("respuesta",response)
