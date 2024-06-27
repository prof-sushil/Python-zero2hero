## Working with Libraries in Python  
Libraries in Python are collections of modules and packages that provide pre-written code to help you perform common tasks, saving time and effort. Python has a rich ecosystem of standard libraries, as well as third-party libraries, which we can use to extend the functionality of your programs.  

### Standard Libraries

Python's standard library is a collection of modules and packages that come with Python, providing a wide range of functionalities. We do not need to install standard libraries separately.

**Commonly Used Standard Libraries**  

* os: Provides functions to interact with the operating system.  
* sys: Provides access to some variables used or maintained by the interpreter.  
* datetime: Supplies classes for manipulating dates and times.  
* random: Implements pseudo-random number generators.  
* json: Provides methods for working with JSON data.  

**Importing and Using Standard Libraries**
```
    import math  

    print(math.sqrt(16))  
    print(math.pi)  
```
We can also import specific functions or classes from a module:

```
from datetime import datetime

now = datetime.now()
print(now)  # Output: current date and time
```

### Third-Party Libraries
Third-party libraries are packages that are not included in the standard library but can be installed using the Python package manager, pip.

Command to install third party libraries
```
pip install pakage_name
```
Example:  
NumPy is a library for numerical operations and working with arrays.  
Let's install numpy.
```
pip install numpy
```
Once installed, we can import and use the library just like any other module:

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  
```

### Virtual Environment

A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system

```
pip install virtualenv
```
If virutalenv could not be installed then try installing with apt.
```
sudo apt install python<version>-venv
```

Create a virtual environment
```
 python<version> -m venv <virtual-environment-name>
 ```

 Example:
 ```
 python3.8 -m venv myvenv
 ```

 Once the virtual env has been created then, we can install libraries inside that virtual environment.

 ```
 source path_to_virtual_env/bin/activate
 ```

 To check the packages installed inside our virtual environment:
 ```
 pip list
 ```

 To deactivate the virtual environment use following command
 ```
 deactivate
 ```
