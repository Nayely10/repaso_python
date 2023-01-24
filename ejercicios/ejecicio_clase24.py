#RECORRER TUPLA
"""Letras =("a","b","c","d","e","f")
for l in Letras:
    print(l)
    
#OPERADORES DE PERTENENCIA
T1 =("a","b","c","d","e","f")
if "c"in T1:
    print("si se encuentra en la lista")
else:
    print("La letra no se encuentra en la lista")

#CONCATENACION
T1 = (1,2,3,4,5)
print(T1 +(6,7,8,9))"""
#REPETICION
"""Letras =("a","b","c","d","e","f")
print(Letras*4)"""
#INDEXACION
"""T1 = (1,2,3,4,5)
print(T1[1])"""
 
 
#INDEXACION NEGATIVA
"""T1 =(1,2,3,4,5)
print(T1[-2])"""

#SORTED : Ordena una lista de forma acendente-MENOR A MAYOR
T1 = (1,2,8,10,3,4,5)
print (sorted(T1))

#MAX MIN - MUESTRA EL NUMERO MAYOR Y EL NUMERO MENOR DE LA DUPLA
T1 = (1,2,8,10,3,4,5)
print(max(T1))
print(min(T1))

#SUMANDO LOS ELEMENTOS DE LA LISTA
T1 = (1,2,8,10,3,4,5)
print(sum(T1))

#COUNT: ME CUENTE CUANTAS VECES ME APARECE EL (2)
T2=(1,2,3,4,6,7,9,0,2)
Z = T2.count(2)
print(Z)


#INDEX:ME VA A ARROJAR EN QUE LUGAR ESTA EL INDICE O ELEMENTO EN ESTE CAS EL(2) 
T2=(1,2,3,3,4,6,7,9,0,2)
Z = T2.index(2)
print(Z)

#RECORRER 2 DUPLAS O LISTAS (zip)
PAISES = ("Colombia","Peru","Ecuador","Argentina","Mexico")
CAPITALES =("Bogota","Lima","Quito","Buenos Aires","Mexico")

for pais,capi in zip(PAISES,CAPITALES):
    print(pais,capi)