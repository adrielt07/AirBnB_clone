# V1 AirBnB Clone - The Console


## Basic Usage

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Getting Started](#getting-started)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Usage Example](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project was created using Ubuntu 14.04 LTS with Python3

## Getting Started

#### Clone the repo:
```
https://github.com/adrielt07/AirBnB_clone.git
```

#### Access into the directory
```
cd AirBnB_clone
```

#### Start up the console interactively:
```
./console
```

#### Use the console non-interactives
```
echo "command" | ./console.py 
```


## File Descriptions
console.py - the console contains the entry point of the command interpreter. List of commands this console current supports:

* quit - quit out of console
* EOF - quit out of console
* create - Creates a new instance of class, saves it to the JSON file before printing the id
* destroy - Deletes an instances from the storage
show - Prints the string representation of an instance based on the class name and id.
* all - Prints string representation of all instances. Can specify class as option
* update - Updates an instance using the class name and id

