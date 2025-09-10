# Employee Class README

## Overview

The `Employee` class models an employee with attributes such as first name, last name, and salary (`pay`). It provides various methods to access and modify employee data, including class-level controls like salary raise percentages. The class also keeps track of total number of employees and all instances created.

Two subclasses, `Developer` and `Manager`, extend `Employee` to model specialized roles with additional attributes and behaviors.

---

## Classes and Inheritance

### Employee

- **Attributes**:

  - `first`, `last`: Employee's first and last names.
  - `pay`: Salary of the employee.
  - `raiseAmt` (class-level): Default raise multiplier (e.g., 1.08).
  - `numEmp` (class-level): Counter tracking total employees created.
  - `instances` (class-level): List storing all employee instances.

- **Methods**:
  - `__init__(self, first, last, pay=30000)`: Initializes employee, increments `numEmp`, and adds instance to `instances`.
  - `details(self)`: Prints full name.
  - `__str__(self)`: Returns readable string representation including name and pay.
  - `__repr__(self)`: Returns a developer-friendly string representation for debugging.
  - `__len__(self)`: Returns length of full name (sum of first and last name lengths).
  - `applyRaise(self)`: Applies raise by multiplying pay with `raiseAmt`.
  - `email` (property): Returns a company email in the format `first.last@company.in`.
  - `fullname` (property): Returns full name (first + last).
  - `fullname` (setter): Allows setting `first` and `last` by assigning a full name string.
  - `raise_amt(cls, amt)` (classmethod): Sets the class-wide raise amount.
  - `fromStr(cls, stri)` (classmethod): Alternative constructor to create an employee from a hyphen-separated string `"first-last-pay"`.
  - `printInstances(cls)` (classmethod): Prints all instances stored in `instances`.
  - `isWeekday(day)` (staticmethod): Returns True if a given `datetime.date` object is a weekday.

### Developer (inherits from Employee)

- **Additional attribute**:
  - `progLang`: Programming language of the developer.
- **Method**:
  - Extends `__str__` to include the programming language.

### Manager (inherits from Employee)

- **Additional attribute**:
  - `emps`: List of employees managed.
- **Methods**:
  - Extends `__str__` to include employees managed.
  - `addEmp(obj)`: Add an employee to the managed list.
  - `removeEmp(obj)`: Remove an employee from the managed list.

---

## Key Learnings and Notes

- **Class variables vs. instance variables**: `raiseAmt`, `numEmp`, and `instances` are shared across instances while `first`, `last`, and `pay` are instance-specific.
- **Instance tracking**: Keeping a list of all instances (`instances`) allows operations on all employees, such as mass printing.
- **Property decorators**: `@property` and `@setter` enable controlled access/modification of derived or combined data attributes like `email` and `fullname`.
- **Classmethods for alternate constructors**: `fromStr` demonstrates a flexible way to create objects from formatted strings.
- **Staticmethods for utility functions**: `isWeekday` effectively encapsulates functionality related to the Employee but independent of instance or class state.
- **Inheritance and method overriding**: `Developer` and `Manager` demonstrate extending functionality and how subclass `__str__` can augment or customize parent behavior with `super()`.
- **Using magic methods**: Customizing `__str__`, `__repr__`, and `__len__` aids in debugging and provides expected behavior for built-in functions.

---

## Example Usage:

---

## Conclusion

Implementing this employee class hierarchy has strengthened understanding of Python's object-oriented features such as class and instance variables, inheritance, method overriding, and use of decorators for properties and class/static methods. It demonstrates practical use cases like tracking objects, defining alternate constructors, and building extensible class structures.
