import requests
import json

class Lectura:
    def __init__(self):
        pass

    def leer_archivo(self):
        url = "http://localhost:8080/apiv1/clientes/add"

        with open("source/Archivos/Clientes.txt") as file:
            for line in file:
                result = line.split(",")
                myList = [i.split('\n')[0] for i in result]
                myList = [i.rstrip() for i in myList]
                myList = [i.lstrip() for i in myList]

                _json = {"surname": str(myList[0]),
                         "firstname": str(myList[1]),
                         "name_coun": str(myList[2]),
                         "name_lang": str(myList[3]),
                         "name_air": str(myList[4])}

                _headers = {"Content-Type": "application/json"}

                response = requests.post(url,data=json.dumps(_json), headers=_headers)

                print("respuesta", _json)
