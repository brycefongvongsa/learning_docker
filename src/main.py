import function_practice
from Dog import Dog
from breeds import *
import hello_docker_image

if __name__ == "__main__":
    print(hello_docker_image.print_message())
    
    taro = Pomeranian('Taro', 0)
    rui = Dog('Rui', 4)
    finn = Dog('Finn', 4)
    dogs = [taro, rui, finn]
    print(taro.bark())
    print(Dog.calculate_average_age(dogs))
    