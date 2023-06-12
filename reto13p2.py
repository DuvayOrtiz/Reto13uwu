def mezdic(A1, A2):
    nuevod = A1.copy() # El nuevo diccionario es la copia del 1
    for letras, nums in A2.items(): # Se compara con los elementos del segundo
        if letras not in nuevod: # si no está se agrega en el diccionario nuevo
            nuevod[letras] = nums
    return nuevod
A1 = {"calamardo": 5,"fortuna": 3,"factor": 6, "falcao": 2, "tio": 9, "tamarindo": 8} # Ingreso un diccionario
A2 = {"patricio": 5,"mala suerte": 3,"comun": 6, "falcao": 2, "tia": 9, "limon": 8} # Ingreso un diccionario
print(mezdic(A1, A2)) # Se imprime el nuevo diccionario