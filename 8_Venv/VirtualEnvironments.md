# Python virtual environments

Useful links:
- [Pyenv](https://github.com/pyenv/pyenv)
- [An introduction to Python virtual environments](https://docs.python.org/3/tutorial/venv.html)
- [What are dependecies](https://www.fullstackpython.com/application-dependencies.html)
- [Installing Tensorflow (TF) in a virtual environment](https://www.tensorflow.org/install/pip)
- [How to use git and virtual environemnts](https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde)
- [Managing different Python versions and dependencies](https://www.youtube.com/watch?v=Jfc5aCCQlg0)

## Quick start
Set the desired version, say 3.9.1, of Python for your project with `pyenv` using:
> `pyenv local 3.9.1`
We might be happy with the current global version, though in any case we may want to document our chosen version for later, perhaps in the README. 

Start a new virtual environment using your chosen version of Python (assumes version > 3.3):
> `python -m venv .venv`

Activate the environment using `source .venv/bin/activate`, install the desired libraries using `pip` and then save the versions of the libraries using `pip freeze > requirements.txt`. These libraries can then be re-installed using `pip install -r requirements.txt`. 

## Introduction

Ideally, we would like to revisit a coding project later in life and be able to run the code and admire our past self's work. However, it might not be easy to pick up where we left off. The Python libraries used in a project (e.g. NumPy, TensorFlow), called the project's *dependencies*, might have been updated since the project was created. Additionally, the version of Python that we used when we created the project might be differnt from the one that we currently use. 

The purpose of this project is to introduce `pyenv` which allows us to create projects with different versions of python, and *virtual environments* which allows us to isolate our project's dependencies. 

## Pyenv
`Pyenv` makes it easy to switch between multiple versions of Python and define which version of Python you want to use for different contexts. For instance, you may want a global version of Python, and then a different project specific version of Python. To find out more about `pyenv` and how it works, [see here](https://github.com/pyenv/pyenv) 

To install a version of Python, say 3.9.1, type:
> `pyenv install 3.9.1`

To set the global version of Python, defined in the `$(pyenv root)/version` file, type:
> `pyenv global 3.9.1`

To set the version of Python for a specific directory and all its subdirectories type:
> `pyenv local 3.9.1`

This specifies the version in a hidden `.project-version` file. 

One can check which version of Python is 'active' using `python -V`, and where this program is located using `which python`. 

## Virtual environments

From Python3.3+, the `venv` package is included and provides an easy way for creating virtual environments.

To start a Python virtual environment, type: 
>`python -m venv .venv` 

Here, `.venv` is just a popular directory name for the virtual environment.

To activate the virtual environment, type: 
>`source .venv/bin/activate`

To deactivate the virtual environment, type: `deactivate`

Once in the virtual environment, install the desired libraries and their desired versions using [pip](https://docs.python.org/3/installing/index.html#installing-index) - the benefit of doing this in a virtual environment is that these libraries will be isolated and won't infere with other projects' dependencies. I believe it also recommended to upgrade pip before installing dependencies using `pip install --upgrade pip`. 

To document the versions of all the libraries used in a project, type: 
>`pip freeze > requirements.txt` 

This produces a list of the installed libraries and their versions, and creates and saves them to the `requirements.txt` file. In order to re-install these specific libraries, type:
>`pip install -r requirements.txt`
