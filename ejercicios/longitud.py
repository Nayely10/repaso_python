#LONGITUD
Frutas = ["pera","durazno","fresa"]
print(Frutas[-2])

#RANGO DE INDICES
nombres =["Juli","Juan2","Catalina","Sandra","Gabriel"]
print(nombres[2:4])#CUENTA EL 2 Y EL 3 ,NO INCLUYE EL 4 solo CUENTA HASTA ANTES DE EL 4


#COMPROBAR SI EL ELEMENTO EXISTE
Articulos_casa = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]
if "escoba" in Articulos_casa:
    print("si,'escoba',es un articulo de la lista ")
else:
    print("no,'celular',no es un articulo de la lista")
    #CAMBIAR ELEMENTOS DE LA LISTA
Articulos_casa  = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]  
Articulos_casa[3] = "espejos"
print(Articulos_casa)
  
  #CAMBIAR VARIOS ELEMENTOS DE LA LISTA
Articulos_casa  = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]  
Articulos_casa[2:5] = ["escaleras","baños","olla"]
print(Articulos_casa)
  
#INSERTAR  UN ELEMENTO EN EL INDICE ESPECIFICO EN UNA LISTA
Articulos_casa  = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]  
Articulos_casa.insert(1,"patio")
print(Articulos_casa)

#INSERTAR ELEMENTOS AL FINAL-APPEND
Articulos_casa  = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]  
Articulos_casa.append( "trapero")
print(Articulos_casa)


#AMPLIAR LISTA -EXTEND
Articulos_casa  = ["mesa","muebles","escoba","ventanas","puertas","cama","televisor"]  
Eletrodomesticos = ["cafetera","nevera","arrocera","micoondas"]
Articulos_casa.extend(Eletrodomesticos)
print(Articulos_casa)


#ELIMINAR ELEMENTOS DE UNA LISTA
Eletrodomesticos = ["cafetera","nevera","arrocera","microondas"]
Eletrodomesticos.remove("microondas")
print(Eletrodomesticos)

#ELIMINAR INDICE ESPECIFICADO-POP - SI NO SE ESPECIFICA BORRA EL ULTIMO

Eletrodomesticos = ["cafetera","nevera","arrocera","microondas"]
Eletrodomesticos.pop(2)
print(Eletrodomesticos)