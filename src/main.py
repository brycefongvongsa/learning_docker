import utils
from Dog import Dog
from breeds import *
import utils
import hello_docker_image

if __name__ == "__main__":
    print(hello_docker_image.print_message())
    
    print('----------Dog class start -----------')
    taro = Pomeranian('Taro', 0, 'BF')
    rui = Dog('Rui', 4, "SF")
    finn = Dog('Finn', 4, "CF")
    miso = Dog('Miso', 4, 'AH')
    dogs = [taro, rui, finn, miso]
    print(taro.bark())
    print('----------Dog class over -----------')
    
    with open('../data/dog_sheet.txt', 'w') as f:
        for dog in dogs:
            f.write(dog.getName() + '|' + str(dog.getAge()) + '|' + dog.getOwner() + '\n')