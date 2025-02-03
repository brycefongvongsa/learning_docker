import pytest
from ..hello_docker_image import print_message

def test_hello_docker_image():
    assert print_message() == 'Hello docker image!'
    print("test_hello_docker_image passed")
    