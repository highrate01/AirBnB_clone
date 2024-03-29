# The AirBnb_clone
# #This is a group project completed by GODWIN ESSIEN and ADEBISI OLUFEMI.

This project is a prerequisite for the completion of our month 5 in the ALX Software Engineering Course. It is aimed at demonstrating all of the concepts we have learned so
far in the course of studying the python progrmming language.

# PROJECT DESCRIPTION & OVERVIEW

The project is aimed at building a cloned version of the AriBnb web application but to be used on a command intepreter.

in this regard, a command interpreter is used to manipulate data without a visual interface, like a shell (for development and debugging)

As we go through the implementation of this project, the following concepts are considered.

- Using the concept of Object Oriented Programming to implement the project 
- Creating a Python package
- Creating a command interpreter in Python using the cmd module
- Creating unit tests and module testing to ensure a smooth implementation of this project
- Serialization and deserialization of JSON files
- Using Datetime module to genrate current time for each created and updated account
- using UUID module to assign a unique id for each created account
- Managing file storage
- Using *args and **kwargs for input commands
- E.t.c

# THE PROCESS / DESCRIPTION OF COMMAND INTERPRETER 


# HOW TO START

The console.py file contains program for interactive and non-interactive part of the command line interpreter. 
It is implemented using the cmd module to instantiate and access the webapp through an interactive terminal.
Upon execution, it prompts (hbnb) and  options of help on default, as contained in the cmd module. Further more, Quit / EOF is implemented to terminate the interpreter. An empty line + Enter doesnt execute anything.

The console was further updated to show other options like "Create, Show, Destroy, Update"

# HOW TO USE IT

Execute the interpreter by typing
./console.py

enter command "help" to display available command line that are accessible
type any of the commands from the listed options on "help" and press Enter


# EXAMPLE
./console.py
(hbnb) help

Documented commands (type help <\topic>):
========================================
EOF  help  quit

(hbnb)
 
(hbnb) help quit

Quit command to exit the program

(hbnb)

(hbnb) 

(hbnb) quit 

# OTHER PROCESS INVOLVED

models/base_model.py file is the base class of all the models. It contains common elements as follows:
Attributes: id, created_at and updated_at
methods: save() and to_json()

To achieve this Project, A parent class (called BaseModel) is created to handle initialization, serialization and deserialization of all future instances.
we created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
and also created all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
we further created the first storage engine of the project: File storage.

All unittests are considered to validate all our classes and storage engine
At the end of this project, we hope to have successfuly build our first full web application to run on command interpreter.

# The AirBnB clone.
