# Automating Blender
# Creates a grid of cubes
# Uses the Blender Array Modifier. 
# Created on June 4, 2015
# Created by Rick Henderson
# Available for use and distribution as long as you retain 
# these comments.
# Feel free to modify this code for your own applications.
#==============================================================
# Instruction:
#=================
# Either copy and paste this code into the Blender Scripting
# window, or open this file as a text block.

import bpy

# Change these values to the number of rows and columns you want for a
# a grid or matrix of cubes

nRows = 12
nCols = 12

# You can also change these values if you want to alter the offset between the cubes
xOffset = 1
yOffset = 1
zOffset = 0     # You would have to alter the code more if you want a 3D array of cubes

# Add a cube with options
bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, 
                                location=(-6, -5, 0), 
                                layers=(True, False, False, False, False, 
                                        False, False, False, False, False, False, 
                                        False, False, False, False, False, False, 
                                        False, False, False))
                                        
# Add the ARRAY modifier
bpy.ops.object.modifier_add(type='ARRAY')

# Create the first Column
bpy.context.object.modifiers["Array"].count = nRows

# Set the offset to use
bpy.context.object.modifiers["Array"].relative_offset_displace[0] = xOffset

#Apply the offset to create the first column of objects
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array")

# Add a second array modifier
bpy.ops.object.modifier_add(type='ARRAY')

# Create the rest of the columns
bpy.context.object.modifiers["Array"].count = nCols

# Set the yOffset for the columns but change x-offset value back to 0
bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 0 
bpy.context.object.modifiers["Array"].relative_offset_displace[1] = yOffset

#Apply the offset to finish
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array")

