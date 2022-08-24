class Car:
    def __init__(self, make, model) -> None:
        self.make = make 
        self.model = model 
        
    def __repr__(self) -> str:
        return f'Car {self.make}{self.model}'


class Garage:
    def __init__(self) -> None:
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to the garage but you can only add Car type objets")
        self.cars.append(car)

       
if __name__ == "__main__":
    ford = Garage()
    car = Car(make='ford', model= 'Fiesta')
    ford.add_car(car= car)
    print(len(ford))