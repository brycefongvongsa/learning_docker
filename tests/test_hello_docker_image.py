import pytest
import sys
import os
from src import hello_docker_image

def test_hello_docker_image():
    assert hello_docker_image.print_message() == 'Hello docker image!'
    print("test_hello_docker_image passed")
    