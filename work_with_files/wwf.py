import csv
import json

def read_file(doc: str) -> None:
    """Reads line by line on the file passed"""
    with open(doc, "r") as file:
        for line in file:
            print(line.strip())
            
def write_file(doc: str, msg: str) -> None:
    """Writes the message passed in the file. Warnning this overwrite all the contet on the file"""
    with open(doc, "w") as file:
        file.write(msg + "\n")         

def append_file(doc: str, msg: str) -> None:
    """Appends a new massege passed in the file"""
    with open(doc, "a") as file:
        file.write(msg + "\n")
        
def read_csv(doc: str) -> None:
    """Read the content of a csv doc row by row"""
    with open(doc, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def write_csv(doc: str, data: list[list]) -> None:
    """write the data passed in the csv file"""
    with open (doc, "w", newline='') as file:
        write = csv.writer(file)
        write.writerows(data)
        
def read_json(doc: str) -> None:
    """Reads the data of the json file"""
    with open(doc, "r") as file:
        data = json.load(file)
        print(data)
        
def write_json(doc: str, data: dict) -> None:
    """Write the data passed in the json file"""
    with open(doc, "w") as file:
        json.dump(data, file, indent=4)
    

read_file("test.txt")
write_file("test.txt", "i am working perfect")
read_file("test.txt")
append_file("test.txt", "its now appending a new message")
print("-----")
read_file("test.txt")

print("-----")
data: list[list] = [["name", "age"], ["Alice", 18], ["vitor", 20]]
write_csv("data.csv", data)
read_csv("data.csv")

print("-----")
dataj: dict = {"name": "Alice", "Age": 18, "City": "Never Land"}
write_json("data.json", dataj)
read_json("data.json")

