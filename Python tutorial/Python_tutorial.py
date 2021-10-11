# Sacado de W3 schools 

# Esto es para hacer un comentario 

"Esto es para crear un string"
'Esto también es para crear un string'

y = "Jhon" 
y_1 = 'Jhon'

# Los anteriores dos son string, ambos son válidos


#%% Para definir una celda 
## PYTHON VARIABLES 

# Las variables son sensibles a si se usa con mayúscula o minúscula 
# Las variables no pueden iniciar con números
# Las variables solo pueden tomar valores alphanumericos o _ 

x_1 = str(3) # lo pone en formato de string '3'
print(x_1) 
x_2= int(3) # lo pone en formato de entero 3 
print(x_2)
x_3 = float(3) # lo pone en formato de decimal 3.0 
print(x_3)

# Función type para saber de que tipo es la variable que estoy ejecutando 
print(type(x_1)) 
print(type(x_2))
print(type(x_3))

# TIPOS DE ESCRIBIR LAS VARIABLES 

# Camel case (todas las palabras de la variable comienzan con mayúscula menos la primera)

myVariableName = "John"

# Pascal Case ( Todas las palabras comienzan con mayúscula )

MyVariableName = "John"

# Snake case ( todas las palabras separadas por )
my_variable_name = "John"

# Asignación multiple en una misma línea 
x, y, z = "Orange", "Banana", "Cherry" 

# Asignación de un mismo valor a varias variables 

x = y = z = "Orange"

# Desempacar una lista 
fruits = ["apple", "banana", "cherry"]

x = y = z = fruits

# TODAS LAS VARIABLES QUE SE CREARON ANTERIORMENTE SON GLOBALES, ESTO QUIERE DECIR QUE LAS PODEMOS LLAMAR
# DENTRO O FUERA DE UNA FUNCIÓN 
 




#%% 
x = "awesome" # esta variable es global 

def myfunc():
  x = "fantastic" # esta variable es local 
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x # se define la variable dentro de la función como global 
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#%% PYTHON NUMBERS 

# hay tres tipos que son el int, float y complex 

# Float son números decimales con doble precisión. 

# Si quiero un número aleatorio 

import random

print(random.randrange(1, 10))

# Se le puede hacer cast a un string para convertirlo a int o float

x= int( "3")
y = float("4")
print(x)
print(y)
#%% PYTHON STRINGS 

# String multilinea se declara con 3 comillas 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(type(a))


#%% Los strings se pueden tratar como un array 
a = "Hello, World!"
print(a[1])

for x in a: # Para cada elemento en a (osea nuestro string)
  print(x)

# longitud de un string 
# Los espacios y las comas cuentan en la longitud de un string 
print(len(a))

# Revisar si hay cierto caracter dentro de nuestro string 

txt = "The best things in life are free!"
print("free" in txt)  # se encuentra la palabra free en el caracter txt 

# ReviSAR si no existe el string 

txt = "The best things in life are free!"
print("expensive" not in txt)

# Obtener partes del string 
a = txt[4]
b = txt[:5]
c = txt[::-1]
d = txt[1:6]
print(a)
print(" este es b "+ b)
print(c)
print( " este es d " +d)

#%%
a = " Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "# quita el espacio pequeño que hay entre las comillas y la H 
print(a.strip()) # returns "Hello, World!

a = "Hello, World!" # reemplazar un caracter dentro de otro 
print(a.replace("H", "J"))

a = "Hello_World!" # separa cada elemento del string como elementos de una lista haciendo uso del separador que le pasamos como parámetro 
print(a.split("_")) # returns ['Hello', ' World!']

d = " hello"
e = "world"

# Para concatenar strings
f = d+e
print(f)

f_1 = d+ " "+ e
print(f_1)

# La función format sirve para juntar strings y numeros 
#%%
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."# el orden que está acá es el que se le pasa a la función format 
print(myorder.format(itemno, price, quantity)) 

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

txt = "We are the so-called \"Vikings\" from the north." # Para poner algo entre comillas dentro de un string 
print(txt)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
#%%

txt = "The best things in life are free!"
print("free" in txt)  # se encuentra la palabra free en el caracter txt (TRUE OR FALSE)


#%%
txt_1 = "Hello,man to my world."
x = txt_1.find("firu") # si no lo encuentra pone -1 
print(x) # encuentra la primera posición de ese string 

txt_2 = "Hello,man to my world."
x_2 = txt_2.find("man")
print(x_2) # encuentra la primera posición de ese string 

#%%
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

# https://www.w3schools.com/python/python_strings_methods.asp
#%%

# tenemos el operador de modulo que nos devuelve el residuo de la división 

x = 5%2
print(x)
#%%
x = 15
y = 2
print(x // y)

# Esto daría 7.5 pero acá se lleva hacia el entero más cercano por debajo. 
#%% Python operators 


# == equal != not equal (comparasion)

# and, or y not  (logicos)

x = 5

print(x > 3 and x < 10)

x_1 = 5 
print (not(x_1 > 3 and x_1< 10)) # lo que hace not es que devuelve el resultado de la condición de manera opuesta

# is y también is not 


#%%
x = ["apple", "banana"]
y = ["apple", "banana"]
x = z 

print(x is z )

# Devuelve true porque x y z son el mismo objeto 

print(x is y)

# Devuelve False porque x y y no son el mismo objeto pero si tienen el mismo contenido

print(x == y)

# Devuelve true porque x es igual a y , más no son el mismo objeto. 


x_1 = ["apple", "banana"]

print("banana" in x_1)

# returns True because a sequence with the value "banana" is in the list


x_2 = ["apple", "banana"]

print("pineapple" not in x_2)

# returns True because a sequence with the value "pineapple" is not in the list

#%% PYTHON LIST 

## TIPOS DE ARRAYS EN PYTHON 

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

my_List = [1,5,67,89,34,100]
 
print(len(my_List))
print(type(my_List))

my_caracter = " hola soy juanchito"
print(len(my_caracter))
print(type(my_caracter))

tuplita = ("apple", "banana", "cherry")
print(len(tuplita))
print(type(tuplita))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#%%
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # nunca se incluye el último término. 

#%%
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#%% FORMAS DE INSERTAR UN ELEMENTO EN UNA LISTA 
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(0, "watermelon") # inserte este valor en ese indice 
print(thislist)  

thislist_2 = ["apple", "banana", "cherry"]
thislist_2.append("orange")
print(thislist_2)

# MERE UNA LISTA DENTRO DE OTRA EXTENDIENDO LA PRIMERA 
thislist_3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist_3.extend(tropical)
print(thislist_3)

# se extiende la lista con una tupla 
thislist_4 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist_4.extend(thistuple)
print(thislist_4)
#%%
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#%% REMOVER ELEMENTOS DE UNA LISTA 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # remueve ese elemento de la lista 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # quita el elemento de ese indice 
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] # lo mismo que pop pero con el comando del 
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear() # deja a la lista vacia 
print(thislist) 
#%% FOR LOOP EN UNA LISTA 

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # esto crea un iterable ( una lista de números [0,1,2])
  print(thislist[i])  


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



## TODOS ESTOS METODOS HACEN LO MISMO 

#%%
x = range(3, 20, 2) # una secuencia que comienza en 3 va hasta 20 sin incluirlo y va de dos en dos
print( "el cuarto número de esta lista es :" , x[3])  # ASI PARA METER UN NÚMERO DENTRO DE UN PRINT 

for n in x:
  print(n)

#%% list comprenhension  newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] # a la nueva lista asignele el valor de x  para cada x en frutas si x comienza con la letra a 

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits] # devuelvame x si x es distinto de banana, de no serlo devuelva orange 

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#%% ORDENAR UNA LISTA DE FORMA ASCENDENTE 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# ORDENA UNA LISTA DE FORMA DESCENDENTE 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#%% reversa de una lista 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist.reverse())

#%% COPIA DE UNA LISTA 

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#%% UNIR DOS LISTAS 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#%% TUPLAS 
# tienen los mismos metodos que las listas 
# SON ORDENADAS PERO NO SE PUEDEN CAMBIAR (ACEPTAN VALORES DUPLICADOS)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Para crear una tupla de un solo elemento se debe añadir una coma depués de este 
thistuple = ("apple",) # se le añade la coma 
print(type(thistuple))

# SI QUIERO CAMBIAR ALGUN ELEMENTO DE UNA TUPLA LA DEBO CONVERTIR A LISTA Y AHÍ SI HACER EL CAMBIO Y LUEGO VOLVER A CONVERTIRLO 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# desempacar una tupla haciendo uso del asterisco para que meta lo restante en una lista

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

a = range(1, len(fruits))
print(a)

for i in a:
  print(i)

#%% PYTHON SETS  A set is a collection which is both unordered and unindexed.

# no se pueden cambiar los elementos de un set pero si se pueden añadir nuevos 

# no se permiten duplicados 

thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = set(("apple", "banana", "cherry")) # esto se hace ya sea para tuplas, sets o listas con los dobles paréntesis 
print(thisset)

# ADICIONAR ELEMENTOS A UN SET 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# ADICIONAR UN SET CON OTRO  con el método update o con el método union 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# SE PUEDE ADICIONAR A UN SET CUALQUIER OBJETO QUE SEA ITERABLE Y VA A QUEDAR COMO SET 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# ELIMINAR UN ELEMENTO DE UN SET  ( se puede hacer con remove, discord - este no envía error si no lo encuentra o con pop, pero pop elimina el último elemento del set. )

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)



#%% DICCIONARIOS  los items no permiten duplicados 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# no se permiten los duplicados y por lo tanto se sobreescribe el año 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


#%% PARA OBTENER EL VALOR ALOJADO DENTRO DE UNA LLAVE 
print(thisdict["model"])
x = thisdict.get("model") 
print(x)
#%% obtener las llaves del diccionario 
K = thisdict.keys()
v = thisdict.values()
i = list(thisdict.items())
print(K)
print(v)
print((i[0][0]))

#  VERIFICAR SI EXISTE UNA LLAVE DENTRO DE ESE DICCIONARIO 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# actualizar el valor de un diccionario
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# eliminar un item del diccionario 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#%% LOOPS SOBRE DICCIONARIOS 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# imprime las llaves 
for x in thisdict:
  print(x)

# imprime los valores de las llaves 
for x in thisdict:
  print(thisdict[x])

# también se puede así para imprimir los valores de las llaves 
for x in thisdict.values():
  print(x)  

# recorrer tanto en llaves como en valores del diccionario 
for x, y in thisdict.items():
  print(x, y)

#%% Copiar un diccionario 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# también se puede así 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#%% diccionarios anidados 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

# otra forma de crear diccionarios anidados 
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"]["name"])

#%% PYTHON IF , ELIF , ELSE 

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# EL ELIF SIGNIFICA : SI LA CONDICIÓN ANTERIOR NO ES VERDADERA ENTONCES TRATA ESTA 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#%% EL ELSE TOMA LO QUE NO HAYA SIDO ACEPTADO POR ALGUNA DE LAS CONDICIONES PASADAS 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  


#%%
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#%% NOT USADO CON EL IF 
x = 5
print((x > 3 and x < 10)) # ESTO DEVUELVE TRUE 
x = 5
print(not(x > 3 and x < 10)) # ESTO DEVUELVE false porque es el reverso de la otra operación 

a = False
if not a:
	print('a is false.')

b = True 
if not b: # como los if's solo se ejecutan si son verdaderos, al negar b este se vuelve falso por lo tanto no se ejecuta el if 
	print('a is false.')


#%% pass statement ( esto es como decir si tal cosa pasa no haga nada )

a = 33
b = 200

if b < a:
  pass


#%% WHILE LOOP 

i = 1
while i < 6: # mientras que i sea menor que 6 imprima i 
  print(i)
  i += 1

#%% Break termina con la iteración  aún si la condición de la iteración es verdadera 
i = 1
while i < 6:
  print(i)
  if i == 3: # si i llega a ser igual a 3 termine el loop 
    break
  i += 1  


#%% EL CONTINUE ES COMO, SI SE ENCUENTRA CON ESTA CONDICIÓN SIGA A LA SIGUIENTE ITERACIÓN. 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#%% LO QUE ESTÉ DENTRO DE ESE ELSE SE EJECUTARÁ CUANDO LA CONDICIÓN DEL WHILE NO SEA MÁS VERDAD 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#%% FOR LOOP 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": # si x es igual a banana entonces continue a la siguiente iteración 
    continue
  print(x) 

# el código del print se ejecuta cuando el recorrido ya haya acabado, sin embargo hay que tener en cuenta que si hay un break este no se ejecutará
for x in range(6):
  print(x)
else:
  print("Finally finished!")  

#%%
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
  if fruits[i] == "banana":
    continue
  print(fruits[i])

# RANGE range(start, stop, step)
# start por default es 0 
# el stop siempre se requiere, irá hasta ese valor menos -1 
# de a cuanto vamos a avanzar 

#%%

b = range(0,11,2)
for i in b:
  print(i)

#%%
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# se ejecuta primero lo que está dentro del loop interno y luego si pasa al siguiente loop       

  
#%% FUNCIONES 

# en caso de que no sepa cuantos argumentos se van a pasar a la función, ese * lo recibirá en forma de tupla 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# parámetros es lo que se declara a la hora de escribir la función
# los argumentos es lo que se pone a la hora de llamar la función 

#%% RECURSIÓN DE FUNCIONES 
def tri_recursion(k):
  if(k > 0): # si k es mayor a 0 
    result = k + tri_recursion(k - 1)# el resultado será igual a k + el nuevo (k-1) pasado a la función 
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#%% FUNCIÓN LAMBDA lambda arguments : expression 
# solo puede haber una expresión después de los dos puntos, pero puede tomar cualquier número de argumentos 
x = lambda a : a + 10
print(x(5))

# no sabemos cual número entra a myfunc
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)# acá se declara que a myfunc le entra el 2 
mytripler = myfunc(3)

print(mydoubler(11)) # ese dos luego con el lambda se multiplica por 11 
print(mytripler(11))

#%% PYTHON ARRAYS 

a = [1,2,4,5]
b = 8
a.append(b)
print(a)

# a la hora de usar extend se le debe pasar a la lista original otro objeto que sea iterable, una lista, una tupla un diccionario o un set. 
c = [1,2,4,5]
d = [8,6,7,9]

c.extend(d)
print(c)

#%%PYTHON CLASSES

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# para declarar un método de un objeto se hace con una función 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#%%
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#%%
import datetime

x = datetime.datetime.now()
print(x)

#%%
username = input("Enter username:")
print("Username is: " + username)

#%% MODULO MATH THE PYTHON 

X = 5%2
print(X)

import math

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = pow(4, 3)
print(x)

x = math.sqrt(64)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

x = math.pi
print(x)
#%%
txt = "The best things in life are free!"
print("free" in txt)  # se encuentra la palabra free en el caracter txt

#%% Positional and Keyword arguments 
def hello(*args,**kwargs):
  print(args)
  print(kwargs)

## Keyword arguments are the ones defined by a = sign like  age and dob this is known as a key value pair.  
hello('Krish','Naik',age=29,dob=1990)  
  
#%%
def hello(name,age=29):
  print('My name is {} and age is {}'.format(name,age))

hello('Juan',30)  

#%%
