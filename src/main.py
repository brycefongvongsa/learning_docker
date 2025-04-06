from Dog import Dog
from breeds import *
import utils
import hello_docker_image
import json
import csv

if __name__ == "__main__":

    print(hello_docker_image.print_message())
    print("--------------------")
    print("Welcome to the Dog Management System!" + '\n')
    
    # Convert CSV to JSON
    csv_file_path = '../data/dog_sheet.csv'
    json_file_path = '../data/dog_sheet.json'
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader] # Read CSV data into a list of dictionaries
    
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file) # Write the list of dictionaries to a JSON file
    
    # Load dogs from JSON file
    print("Loading dogs from JSON file...")
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        dogs = []
        for row in json_data:
            dog = Dog(name=row['Name'], age=int(row['Age']), owner=row['Owner'])
            dogs.append(dog)
    
    print("\nAll dogs loaded successfully!")
    for d in dogs:
        print(f"Name: {d.getName()}, Age: {d.getAge()}, Owner: {d.getOwner()}")
            