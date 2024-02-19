# Chapter 4: Factory patterns

## Simple Factory 🚧

> A class which chooses which product class to instantiate and return, based upon method parameters.

### Use in Python

The Python standard library contains multiple references to factory objects, for instance
[namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) 
and [dataclasses](https://docs.python.org/3/library/dataclasses.html#module-dataclasses)
are factories for creating classes.

The [Factory Boy](https://github.com/FactoryBoy/factory_boy) package provides easy object creation for Django and for other ORMs.

## Factory Method 📋

> Defines an interface for creating an object, but lets subclasses decide which class to
> instantiate. The Factory method lets a class defer instantiation to subclasses.

For instance the `PizzaStore` abstract class in this repo provides an abstract `create_pizza` interface for creating one
product.

### Use in Python

The [python-qrcode](https://github.com/dancergraham/python-qrcode) module uses the factory method pattern nicely to
separate only the part of the code that changes (generating png, svg, etc.) from the underlying logic of the code
generation and to allow extension through the creation of new factory methods without modification of the existing code.
I took advantage of this to add a new class for the creation of 3D QR codes with my favourite NURBS modelling software
Rhino - it was super simple once I understood the pattern.

## Abstract Factory 🏭

> Provides an interface for creating families of related or dependent objects without specifying
> their concrete classes.

For instance the `PizzaIngredientFactory` abstract class defines an interface for a family of products.

## Builder 👷🏻‍♀️🏗️

When the object creation gets more complex with a number of distinct steps then the Builder pattern comes in, 
esseantially using a Template method to put all of the creation steps together.

## Running the code

```bash
python pizza_abstract_factory.py
```
