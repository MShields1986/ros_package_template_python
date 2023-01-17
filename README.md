# ros_package_template_python
## Overview
Repository template for a ROS package written in Python.

This repository includes a simple ROS package with several key functionalities already boiler plated.
These include:
- A split between the ROS interface and the core underlying logic
- Subsriber
- Custom message publisher
- Service Server
- `TODO: Add a Service Client Proxy`
- `TODO: Add an Action Server`
- `TODO: Add an Action Client Proxy`
- Launch File with Logging Options

### License
`TODO: Complete as appropriate for your package`

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
`TODO: Complete as appropriate for your package`

Clone this repository into your catkin workspace src directory.
```shell
cd path_to_your/catkin_ws/src
git clone https://github.com/MShields1986/ros_package_template_python.git
```

Build your project using catkin make.
```shell
cd path_to_your/catkin_ws/
catkin_make
```

## Usage
`TODO: Complete as appropriate for your package`

Run the package using roslaunch.
```shell
roslaunch ros_package init.launch
```

Logging ROSbags to the ros_package/bags directory is enabled by default, but can be disabled using the log arguement. 
```shell
roslaunch ros_package init.launch log:=false
```

### Config Files
`TODO: Complete as appropriate for your package`

Default configuration parameters are stored in ros_package/config/default.yaml

Included parameters are as follows:

Name          | Description                       | Default Value
--------------|-----------------------------------|---------------------------
example_param | An example parameter              | "I'm a parameter in a config file"


### Nodes
#### Node
`TODO: Complete as appropriate for your package`

##### Topics, Services and Actions Offerred
`TODO: Complete as appropriate for your package`

### ROSbags
`TODO: Complete as appropriate for your package`
Bags are logged into the ros_package/bags directory.
Topics recorded are as follows:
- /output
- /should_i_die

## Bugs and Feature Requests
`TODO: Complete as appropriate for your package`

Please report bugs and request features using the [Issue Tracker](https://github.com/MShields1986/ros_package_template_python/issues).
