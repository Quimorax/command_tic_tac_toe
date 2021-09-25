# Command tic-tac-toe

## Description:

It's command version of tic-tac-toe with pretty colored print. The table, players, commas and result are colored.

Initially user have table with coordinates from one to desk size _(include)_. And user can enter coordinate, where he
wants go. After selecting a coordinate, a cross or zero takes its place.</br>
**Example**:

Initially: </br>![](images/exp1.png)</br>
_Some time later.._</br>
![](images/example2.png)

### Command line parameters

Since the project is on the command line, it has some command line parameters:</br>
(parameters in unix style)

- `-h` or `--help`: return help message
- `-ds` or `--desk-size`: configure desk size _(default 3)_
- `-p` or `--player`: identify player, who will go first _(default chose random)_

### Technical information

All program run from function `main` from `main.py`, which is located at the root of the project. Module `main.py` 
uses instruments from package `utilities`. Function `main` - it's function with infinite 
cycle, which ended if one of players win or if draw.

### Some other information

Program work on Windows, Unix, macOS and Linux. Necessary Python is 3.9+.</br>
Required external libraries to this program:
- `pytest`: uses in tests
- `colorama`: uses to Windows support
- `termcolor`: The main library for color output
