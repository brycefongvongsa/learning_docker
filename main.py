from helper_functions import hello_docker_image, function_practice

if __name__ == "__main__":
    print(hello_docker_image.print_message())
    print(function_practice.performOperation(20, 5, 2, operation='add'))
    # output should be 24
    print(function_practice.performOperation(20, 5, 2, operation='subtract'))
    # output should be 13
    print(function_practice.performOperation(20, 5, 2, operation='multiply'))
    # output should be 200
    print(function_practice.performOperation(20, 5, 2, operation='divide'))
    # output should be 2.0
    print(function_practice.performOperation(20, operation='divide'))
    