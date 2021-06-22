# Conway's Game of Life
This project is an implementation of Conway's Game of Life.

## About the code
The source code of this project was written in Python. Here is a high-level overview of the sources:
* The script `Life.py` can be used to run the game
* The package `life` contains two classes, `Game` and `World`. These classes are 
well-documented in their source files, so no more details about them will be provided here.

### Dependencies

The project has two main Python dependencies:
* A Python 3 interpreter
* A set of Python packages listed in requirements.txt

The set of Python packages is not included in the repo to save space. To run this project after
it has been cloned, these packages may need to be installed. 

This is a set of directions for installing these packages. Note that these directions assume a 
Python 3 interpreter exists and that it has been associated with the shell command `python3`.
* Start a shell session and navigate to the root directory of the project/cloned repo
* Run the command `python3 -m venv venv` to create a Python 3 virtual environment (venv) using your
Python 3 setup
* Run the command `source venv/bin/activate` to activate the venv
* Run the command `pip install --upgrade pip` to upgrade pip (the Python package manager)
* Run the command `python -m pip install -r requirements.txt` to install the required 
packages

Now you should be able to run the game by running `Life.py`. When you are done, you can deactivate
the venv using the command `deactivate`. If you want to run the game again after deactivating the
venv, first reactivate the venv using the command above.

## About Conway's Game of Life
Conway's Game of Life (or Life for short) is a cellular automation created by the English 
mathematician John Conway. As a cellular automation, Life has the following elements:
* A two-dimensional grid of cells, where each cell in the grid has an attribute called a state
* A set of states that a cell can be in
* A transition function that maps a cell's state and the states of its neighbours to a new state

For Life in particular:
* A cell can be in one of two states: dead or live
* The transition function consists of the following rules:
    * If a cell is live and has 2 or 3 live neighbours, the cell's next state is live
    * If a cell is dead but has 3 live neighbours, the cell's next state is live
    * All other cells have a next state of dead
    
Note that for Life, a cell's neighbours are defined using the 
[Moore neighbourhood](https://en.wikipedia.org/wiki/Moore_neighborhood) definition.

The game is played by setting an initial state, and then repeatedly applying the rules of the game 
to generate successive states.

Life is interesting for several reasons:
* Emergence: repeated application of simple rules to a simple initial state can result in very 
complex and intricate future states
* Undecidability: no algorithm can take two states and determine if application of the rules
to one of the states will yield the other state
* Turing completeness: the game can theoretically simulate any Turing machine
* Self-similarity: the game can be implemented in itself 
(see [Life in Life](https://www.youtube.com/watch?v=xP5-iIeKXE8))

## About John Conway
John Horton Conway (1937 – 2020) was an English mathematician. Born in Liverpool, Conway resolved 
at the young age of 11 to become a mathematician at Cambridge. He graduated with his Ph.D. from 
Cambridge in 1964, and he retired in 2013. In addition to his long and influential career as 
a researcher, Conway was lauded for being a kind and eccentric character and a gifted expositor of 
mathematics. For a full account of Conway’s life, see the book Genius at Play: The Curious Mind of 
John Horton Conway by Siobhan Roberts. Conway passed away on Saturday, April 11, 2020, from 
COVID-19. He was 82. 

