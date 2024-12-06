import importlib

module_name = "#"

while module_name != "":
	module_name = input("enter day: ")
	try:
		module = importlib.import_module(module_name, package=None)
	except :
	    print(f"could not find {module_name}")
