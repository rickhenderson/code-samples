# read_hadamard_file.py
# Reads data from a text file to create a 3D
#    version of a given Hadamard Matrix.
# Created by Rick Henderson
# Created on June 4, 2015
# Completed June 5, 2015
# Note: A "Hadamard File" is a text file containing rows
#       rows of + and - where the + indicates a 1 or a cube
#       and the - represents a 0 or a space.

import bpy

# Set the order (size) of the matrix

nOrder = 12

# You can also change these values if you want to alter the offset between the cubes
xOffset = 1.0
yOffset = 1.0
zOffset = 0     # You would have to alter the code more if you want a 3D array of cubes

xpos = 0
ypos = 0
char_number = 0

# Open the file to read from
# Modified technique from DiveIntoPython3.net/files.html
line_number = 0
with open('c:/had12.txt', encoding='utf-8') as a_file:
    for each_row in a_file:
        line_number += 1
		# Just print the current row to the console as a test
        print(each_row.rstrip())
        for a_char in each_row:
            char_number += 1
            # If the current character is +, generate a cube then position it
            if a_char == '+':
                bpy.ops.mesh.primitive_cube_add(radius=0.5)
                bpy.context.object.location[0] = line_number * xOffset
                bpy.context.object.location[1] = char_number * yOffset
                   
        # Now an entire row has been read, so reset char_number to 0
        char_number = 0
        
# Program Ends
            
            
        
        
