from hello_program import chai

chai('hello this is ginger tea')


# source code --> byte code (__pycache__ folder madhe aste) --> python VM (virtual machine)

# 1. Compiled to Byte code (but python is interpreted language)

# 2. python is low level and platform independent

# 3. byte code runs faster 
#    .pyc files --> (frozen binaries) --> compiled python byte code by interpreter 

# 4. __pycache__ folder : 
#       Source Change and python Version
#       program1.cpython-311.pyc
#       works only for the imported files
#       not for top level files


# 5. Python Virtual Machine : (PVM)
#       code loop to iterate byte code
#       run time engine
#       also known as python interpreter


# 6. Byte code is NOT machine code
#       python specific interpretation
#      cpython, jython, IronPython, Stackless,PyPy
#       cpython --. Standard Implimentation
