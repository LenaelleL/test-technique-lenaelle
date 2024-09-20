## Objectives

This project is used to get measurements data from this url : 'http://localhost:3000/measurements', store it and display it again through two routes.

## Technologies

This project uses python 3.11.1, fastAPI, pandas for data management and pytest for testing. 
It was also created and run using a python virtual environment directly from VS Code.

## Get started

Measurements API needs to be running.
If using VSCode venv, can be run easily using the debug feature.

Otherwise start by creating a virtual environment using this command : ```python -m venv .venv```. 
Then activate it (commands differ based on OS, see https://fastapi.tiangolo.com/virtual-environments/).
Then install fastapi and uvicorn using pip.
You can now run the program using the following command : ```fastapi dev main.py```

## Testing

To run the tests, once the virtual environment is activated and pytest is installed, run ```pytest```.