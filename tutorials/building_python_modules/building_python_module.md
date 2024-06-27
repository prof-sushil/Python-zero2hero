## Building Python Modules
* Creating Python modules allows you to structure your code efficiently, promote code reuse, and make it easier to manage large codebases. 
* A Python module is simply a Python file with a .py extension that contains Python code.
* It can define functions, classes, and variables, and it can also include runnable code.

### What is a Python Module?

A Python module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. For example, the file mymodule.py is a module, and its module name is mymodule.

**Using a module**

* To use the module, we need to import it in another python file.

**The \_\_name__ Variable**

* Every Python module has a special attribute called\_\_name__. 

* The value of \_\_name__ is set to '\_\_main__' when the module is run directly, and it is set to the module's name when it is imported.

**Packages and \_\_init__.py** 

* A package is a directory containing multiple modules (i.e. multiple python files) and an \_\_init__.py file (this file can be empty).

* Package Structure:  
        ├── mypackage  
        │   ├── \_\_init__.py  
        │   ├── module1.py  
        │   ├── module2.py  


**Module Search Path**  

Python looks for modules in the following places:
* The directory containing the input script (or the current directory if no file is specified).  
* The directories listed in the PYTHONPATH environment variable.  
* The installation-dependent default path.  

**Relative Imports**
* We can use relative imports within a package.  
* For example, if module1.py wants to import function2 from module2.py, you can do it as follows:  
> from .module2 import function2

 

