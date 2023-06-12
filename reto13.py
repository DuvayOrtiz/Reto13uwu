def ordnum(A):# defino una función que tenga como variable el diccionario
    nums = list(A.values())   # Se hace una lista con los numeritos :D
    nums.sort()  # Ordenamos de manera ascendente
    for i in nums: # printeo todas las i
        print(i)
A = {"calamardo": 5,"fortuna": 3,"factor": 6, "falcao": 2, "tio": 9, "tamarindo": 8} # Ingreso un diccionario
print(ordnum(A)) # Imprimo la función