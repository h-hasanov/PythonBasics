import importlib.util
import os
import sys

dirPath = os.path.dirname(os.path.realpath(__file__))
path = dirPath+"/utils/importedFunctions.py"
moduleName = "Foo"

# Load the module from the specified location
moduleSpec = importlib.util.spec_from_file_location(moduleName, path)
module = importlib.util.module_from_spec(moduleSpec)

# Add the module to the system modules list
sys.modules[moduleSpec.name] = module

# Load the module into the interpreter
moduleSpec.loader.exec_module(module)

# Now, create the class from the module
c = module.Foo()
print("Foo.var = {0}".format(c.var))

# Set up the path so other things get processed properly
sys.path.append(dirPath)