# V1 AirBnB Clone - The Console
![The Logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20180613%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180613T220049Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fcc9ffab23ac53f0118d4424952caf0f48a2cd41568b0601195e075242925db0)

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
* [Testing](#testing)
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

#### Access into the directory:
```
cd AirBnB_clone
```

#### Start up the console interactively:
```
./console
```

#### Use the console non-interactives:
```
echo "command" | ./console.py 
```


## File Descriptions
console.py - this is the entry point for our command interpreter.

#### Console Commands
* quit: quit out of console
* EOF: quit out of console
* create: Creates a new instance of class, saves it to the JSON file before printing the id
* destroy: Deletes an instances from the storage
show
* show: Prints the string representation of an instance based on the class name and id.
* all: Prints string representation of all instances. Can specify class as option
* update: Updates an instance using the class name and id


## Usage 

#### Interative Mode:
```
(hbnb) help

Documented commands (type help <topic>):
========================================

EOF  all  count  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) create BaseModel
18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) all BaseModel
(hbnb) [BaseModel] (18bb97af-f3fc-4213-946a-c9a3d77cd508) {'created_at': datetime.datetime(2018, 6, 13, 22, 27, 16, 194963), 'updated_at': datetime.datetime(2018, 6, 13, 22, 27, 16, 195000), 'id': '18bb97af-f3fc-4213-946a-c9a3d77cd508'}
(hbnb) show BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) create User
71a36988-d044-4471-a2b2-ea5f78a7acec
(hbnb) User.all()
[User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'created_at': datetime.datetime(2018, 6, 13, 22, 27, 56, 902596), 'updated_at': datetime.datetime(2018, 6, 13, 22, 27, 56, 902642), 'id': '71a36988-d044-4471-a2b2-ea5f78a7acec'}
(hbnb) update User 71a36988-d044-4471-a2b2-ea5f78a7acec first_name Mama
(hbnb) User.show(71a36988-d044-4471-a2b2-ea5f78a7acec)
[User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'id': '71a36988-d044-4471-a2b2-ea5f78a7acec', 'created_at': datetime.datetime(2018, 6, 13, 22, 27, 56, 902596), 'first_name': 'Mama', 'updated_at': datetime.datetime(2018, 6, 13, 22, 45, 20, 107855)}
(hbnb) destroy BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) show BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
** no instance found **
(hbnb) quit
```

#### Non-interactive Mode:
```
echo "User.all()" | ./console.py
(hbnb) [User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'updated_at': datetime.datetime(2018, 6, 13, 22, 48, 15, 587000), 'id': '71a36988-d044-4471-a2b2-ea5f78a7acec', 'first_name': 'Bob', 'created_at': datetime.datetime(2018, 6, 13, 22, 27, 56, 902596)}
(hbnb)
```


## Testing
To run all the tests, run the following command:
```
python3 -m unittest discover tests
```

To run tests by folder, run the following command:
```
python3 -m unittest tests/test_models/<file>.py
```

## Bugs
* When updating, it can only take one attribute at a time. Future versions may improve that

* Otherwise, no know bug. Send us a message if you stumble upon one! :)


## Authors
Amy Tai | [GitHub](https://github.com/Wyrd00) | [Twitter](https://twitter.com/flyaway0120) | [LinkedIn](https://www.linkedin.com/in/Wyrd00/)

Adriel Tolentino | [GitHub])(https://github.com/adrielt07) | [Twitter](https://twitter.com/am__adriel) | [LinkedIn](https://www.linkedin.com/in/adriel-tolentino)


## License
You are free to use this console without our permission. Have fun, be safe!~
