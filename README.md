# ros_package_template_python
## Overview
Repository template for a ROS package written in Python.

### License
TBC

### Structure
This template follows a "one package to one repository" architecture.
Typically this is best employed after a time when interface layers between packages becomes well defined.
In early stage development multiple packages maybe under development together and, in this case, it might be better to group multiple ROS packages in a single repository.

Source code is broken into two distinct parts:
1. a ROS independent Pythonic part that should be used for handling core functionality
2. a ROS interfacing layer that exposes the underlying core functionality to ROS

This is done for several reasons:
- to enable better code re-use
- to allow for easy changes in middle-ware in the future
- to allow more modular testing
- to provide flexibilty in application of core functionality

## Installation
TBC

## Usage
TBC

### Config Files
TBC

### Launch Files
TBC

### Nodes
#### Node
TBC

##### Topics, Services and Actions Offerred
TBC

### ROSbags
TBC


## Bugs and Feature Requests

TBC