datecalc
========

rcube is created by Vi Grey (https://vigrey.com) <vi@vigrey.com> and is licensed under a BSD 2-Clause License. Read LICENSE for more license text.

Python module to solve Rubik's Cubes

####Dependencies

* Python (>= 2.4)

To install, open the terminal and `cd to the root directory of this program, then enter the command:
```
sudo python setup.py install
```

You could also install this module using pip (Recommended Method) by entering the command:
```
sudo pip install rcube
```

####Importing the Module

Simply type:
```
import rcube
```

####Using the Module

To use this module to solve a rubik's cube, use *rcube.solve(cube_list)* where cube_list is a list with the format:

```
cube_list = [
    [U1, U2, U3, U4, U5, U6, U7, U8, U9],
    [L1, L2, L3, L4, L5, L6, L7, L8, L9],
    [F1, F2, F3, F4, F5, F6, F7, F8, F9],
    [R1, R2, R3, R4, R5, R6, R7, R8, R9],
    [B1, B2, B3, B4, B5, B6, B7, B8, B9],
    [D1, D2, D3, D4, D5, D6, D7, D8, D9]
]
```
The variables can be anything you want, as long as they are consistant.  Below is how to determine what variale should go in which position of the cube_list:

=-=-=-=-=-=-=-=-=-=

Back side is above

U1 U2 U3

U4 U5 U6 - When looking directly at Up side

U7 U8 U9

Front side is below

=-=-=-=-=-=-=-=-=-=

Up side is above

L1 L2 L3

L4 L5 L6 - When looking directly at Left side

L7 L8 L9

Down side is below

=-=-=-=-=-=-=-=-=-=

Up side is above

F1 F2 F3

F4 F5 F6 - When looking directly at Front side

F7 F8 F9

Down side is below

=-=-=-=-=-=-=-=-=-=

Up side is above

R1 R2 R3

R4 R5 R6 - When looking directly at Right side

R7 R8 R9

Down side is below

=-=-=-=-=-=-=-=-=-=

Up side is above

B1 B2 B3

B4 B5 B6 - When looking directly at Back side

B7 B8 B9

Down side is below

=-=-=-=-=-=-=-=-=-=

Front is above

D1 D2 D3

D4 D5 D6 - When looking directly at Down side

D7 D8 D9

Back is below

=-=-=-=-=-=-=-=-=-=

####Example Uses

```
import rcube

cube_list = [
    ['Red', 'Green', 'Yellow', 'Yellow', 'White', 'White', 'Orange', 'Green', 'Green'],
    ['Blue', 'Orange', 'Green', 'Orange', 'Red', 'Yellow', 'Green', 'Red', 'Blue'],
    ['White', 'Yellow', 'Red', 'Red', 'Blue', 'Orange', 'Orange', 'Green', 'White'],
    ['White', 'Green', 'Green', 'White', 'Orange', 'Red', 'Orange', 'Blue', 'Blue'],
    ['Orange', 'Orange', 'Yellow', 'Blue', 'Green', 'Blue', 'Red', 'Blue', 'Yellow'],
    ['Yellow', 'Red', 'Blue', 'White', 'Yellow', 'White', 'Red', 'Yellow', 'White']
]

print(rcube.solve(cube_list))
```
prints out:
```
L' B L B' M2 B L' B' L B' R2 B M2 B' R2 B R' U R U' M2 U R' U' R M2 U R' U' M2 U R U2 L' U M2 U' L U B L B' M2 B L2 B' M2 B L B2 R' B M2 B' R B M2 D U R2 U' M' U R2 U' M D' M U2 M U2 D' L2 D M2 D' L2 D' R U' R' U' R U R' F' R U R' U' R' F R D R2 U' R' U' R U R' F' R U R' U' R' F D F' R U' R' U' R U R' F' R U R' U' R' F R F D' F' R U' R' U' R U R' F' R U R' U' R' F R F D F2 D R U' R' U' R U R' F' R U R' U' R' F R D' F2 R D' R U' R' U' R U R' F' R U R' U' R' F R D R' D2 F' R U' R' U' R U R' F' R U R' U' R' F R F D2 F U' R' U' R U R' F' R U R' U' R' F R2 F' R' U' R' U' R U R' F' R U R' U' R' F R'
```
