# Los generados son funciones que recuerdan el estado en el que están entre ejecuciones 
# La idea es que no va a guardar todo en memoria sino que va a recordar lo último que le pasó a uno y luego le devolverá otra cosa 

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i+=1
        
g = hundred_numbers()
print(next(g)) # acá muestra 0
print(next(g)) # acá muestra 1 
print(list(g)) # acá genera una lista que va desde 2 hasta 99 porque el recuerda en que número se quedó 
        
        
# Un iterator no es lo mismo que un iterable 

class FirstHundredGenerator: # esta clase es un iterator , pero no se puede iterar en un for loop 
    def __init__(self):
        self.number = 0
        
    def __next__(self):# Todas las clases que tengan este dunder method son iterators 
        if self.number < 100:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()    
        
my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))


class FirstHundredIterable:
    def __iter__(self): # con este metodo ya se puede iterar sobre un objeto 
        return FirstHundredGenerator()
    
print(sum(FirstHundredIterable()))    


# Un iterable se puede definir con el dunder __iter__  o con los dunder __len__ , __getitem__
class AnotherIterable: 
    def __init__(self) -> None:
        self.cars =['Fiesta','Focus']
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return self.cars[i] 
    
    
friends = ['Rolf', 'Jose','Randy','Ana','Mary']
star_filter_with_r = filter(lambda friend: friend.startswith('R'),friends) # el primer argumento de filter es una función que devuelve un booleano y el segundo argumento es un iterable 
star_with_r = (f for f in friends if f.startswith('R')) # esto crea un generador con el cual podemos hacer uso de la función next 

#%%%
class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
    
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'],data['password'])
    
users = [
    {'username': 'rolf', 'password':'123'},
    {'username':'teclado','password':'456'}
]        

for user in users:
    print (user)   
    
users = [User.from_dict(user) for user in users]
users = map(User.from_dict,users) # map mapea una funcion con un iterable y como que los relaciona 
# la función map genera un generador     

#%%

# La función any devuelve True si hay almenos uno verdadero y false de lo contrario
# La función all devuelve True si todos son verdaderos               