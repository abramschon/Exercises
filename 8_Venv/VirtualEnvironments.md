# Python virtual environments

Useful links:
- [Installing Tensorflow (TF) in a virtual environment](https://www.tensorflow.org/install/pip)
- [An introduction to Python virtual environments](https://docs.python.org/3/tutorial/venv.html)
- [How to use git and virtual environemnts](https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde)

To start a Python virtual environment, type: 
>`python3 -m venv .venv` 

Here, `.venv` is just a popular directory location for the virtual environment.

To activate the virtual environment, type: 
>`source .venv/bin/activate`

To deactivate the virtual environment, type: `deactivate`

Once in the virtual environment, install the desired packages and their desired versions using [pip](https://docs.python.org/3/installing/index.html#installing-index) - the benefit of doing this in a virtual environment is that these packages will be isolated and won't infere with other projects.

To document the versions of all the packages used in a project, type: 
>`pip freeze > requirements.txt` 

This produces a list of the installed packages and their versions, and creates and saves them in the `requirements.txt` file. In order to install these saved packages elsewhere, type:
>`pip install -r requirements.txt`

### Some Bash Tips
- `>>` appends to an existing file, whereas `>` will overwite the contents of a file.