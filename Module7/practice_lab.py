'''Added doc string so pylinter stops complaining about missing doc string.'''
class Car():
    '''basic class to represent a car.'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0


    def accelerate(self):
        '''Speeds the car up by 5 mph.'''
        self.speed += 5


    def brake(self):
        '''Slows the car down by 5 mph.'''
        self.speed -= 5


    def get_speed(self):
        '''Returns the current speed of the car.'''
        return self.speed


if __name__ == "__main__":
    car = Car("Ford", "F-150", 2006)
    for i in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()} mph")
    for i in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()} mph")
