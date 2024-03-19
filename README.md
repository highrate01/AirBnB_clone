# The AirBnb_clone
# #This is a group project completed by GODWIN ESSIEN and ADEBISI OLUFEMI.

This project is a prerequisite for the completion of our month 5 in the ALX Software Engineering Course. It is aimed at demonstrating all of the concepts we have learned so
far in the course of studying the python progrmming language.

#CONCEPT OVERVIEW

The project is aimed at building a cloned version of the AriBnb web application but to be used on a command intepreter.

in this regard, a command interpreter is used to manipulate data without a visual interface, like a shell (for development and debugging)

As we go through the implementation of this project, the following concepts are considered.

- Using the concept of Object Oriented Programming to implement the project 
- Creating a Python package
- Creating a command interpreter in Python using the cmd module
- Creating unit tests and module testing to ensure a smooth implementation of this project
- Serialize and deserialize of JSON files
- Using Datetime module
- Creating UUID
- Managing file storage
- Using *args and **kwargs
- E.t.c

#THE PROCESS

The console.py file is the entry point of our command interpreter, models/base_model.py file is the base class of all the models. It contains common elements as follows:
Attributes: id, created_at and updated_at
methods: save() and to_json()

To achieve this, A parent class (called BaseModel) is created to handle initialization, serialization and deserialization of all future instances.
we have created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
and also created all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

we further created the first abstracted storage engine of the project: File storage.
All unittests are considered to validate all our classes and storage engine

At the end of this project, we hope to have successfuly build our first full web application to run on command interpreter.

#The AirBnB clone.
