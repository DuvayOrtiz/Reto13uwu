# Reto13uwu
## El ultimo retooooooooooooou
## :star: Punto 1 :boom:

```ruby
def ordnum(A):# defino una función que tenga como variable el diccionario
    nums = list(A.values())   # Se hace una lista con los numeritos :D
    nums.sort()  # Ordenamos de manera ascendente
    for i in nums: # printeo todas las i
        print(i)
A = {"calamardo": 5,"fortuna": 3,"factor": 6, "falcao": 2, "tio": 9, "tamarindo": 8} # Ingreso un diccionario
print(ordnum(A)) # Imprimo la función
```
## :star: Punto 2 :boom:

```ruby
def mezdic(A1, A2):
    nuevod = A1.copy() # El nuevo diccionario es la copia del 1
    for letras, nums in A2.items(): # Se compara con los elementos del segundo
        if letras not in nuevod: # si no está se agrega en el diccionario nuevo
            nuevod[letras] = nums
    return nuevod
A1 = {"calamardo": 5,"fortuna": 3,"factor": 6, "falcao": 2, "tio": 9, "tamarindo": 8} # Ingreso un diccionario
A2 = {"patricio": 5,"mala suerte": 3,"comun": 6, "falcao": 2, "tia": 9, "limon": 8} # Ingreso un diccionario
print(mezdic(A1, A2)) # Se imprime el nuevo diccionario
```
## :star: Punto 3 :boom:

```ruby
import json

# Función para leer el archivo JSON
def leer_json(archivo):
    with open(archivo, 'r') as file:
        data = json.load(file)
    return data
# Función para imprimir los nombres completos de personas que practican un deporte específico
def imprimir_nombres_deporte(data, deporte):
    for usuario, info in data.items():
        if deporte in info['deportes']:
            nombre = info['nombres']
            apellido = info['apellidos']
            todo = f"{nombre} {apellido}"
            print(todo)
# Función para imprimir los nombres completos de personas en un rango de edades
def imprimir_nombres_rango_edades(data, edad_min, edad_max):
    for usuario, info in data.items():
        edad = info['edad']
        if edad_min <= edad <= edad_max:
            nombres = info['nombres']
            apellidos = info['apellidos']
            nombre_completo = f"{nombres} {apellidos}"
            print(nombre_completo)

# Programa principal
archivo_json = 'datos.json'
data = leer_json(archivo_json)
# Solicitar al usuario el deporte y mostrar los nombres de personas que lo practican
deporte_ingresado = input("Ingrese el deporte: ")
print("Nombres de personas que practican", deporte_ingresado)
imprimir_nombres_deporte(data, deporte_ingresado)

# Solicitar al usuario el rango de edades y mostrar los nombres de personas dentro de ese rango
edadmin = int(input("Ingrese la edad mínima: "))
edadmax = int(input("Ingrese la edad máxima: "))
print("Nombres de personas en el rango de edades", edadmin, "-", edadmax)
imprimir_nombres_rango_edades(data, edadmin, edadmax)
```
## :star: Punto 4 :boom:

```ruby

```
## :star: Punto 5 :boom:

```ruby
import requests
def obtener_datos(api_url):
    response = requests.get(api_url)
    json_data = response.json()

    print("JSON:")
    print(json_data)
    print()

    print("Pares de llave-valor:")
    for key, value in json_data.items():
        print(f"Llave: {key}, Valor: {value}")
    print()

obtener_datos("https://api.publicapis.org/entries")
obtener_datos("https://catfact.ninja/fact")
obtener_datos("https://api.coindesk.com/v1/bpi/currentprice.json")
```
