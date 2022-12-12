#Project 4 - Jacqueline Cole - December 12th, 2022
from graphics import *

canvas = make_empty_picture(320,200,yellow) 
write_bmp(canvas,"Test1.bmp") 

canvas = make_empty_picture(320,200,yellow) 
add_horizontal_line(canvas, 10, 50, 20, red) 
add_vertical_line(canvas, 100, 50, 150, blue) 
add_line(canvas, -20, 180, 300, -20, green) #Some pixels cut off-screen 
write_bmp(canvas,"Test2.bmp")

canvas = make_empty_picture(320,200,yellow) 
Color = red 
for X in range(10,51,10): 
   add_rectangle_filled_sized(canvas,X,10,10,20,Color) 
   add_rectangle_outline_sized(canvas,X,40,10,20,black) 
   if Color == red: 
       Color = blue 
   else: 
       Color = red 
write_bmp(canvas,"Test3.bmp") 

canvas = make_empty_picture(320,200,yellow) 
add_bresenham_filled_circle(canvas,160,100,75,cyan) 
add_bresenham_circle(canvas,160,100,75,blue) 
write_bmp(canvas,"Test4.bmp")

#------------------------------------------------------------ 
# TEST PROGRAM FOR GRAPHICS LIBRARY 
# Copyright (C) 2020-2022 -- Dr. William T. Verts 
#-------------------------------------------------------------
#------------------------------------------------------------ 
# Build the canvas and define variables for later use. 
#------------------------------------------------------------ 
canvas = make_empty_picture(641, 481, cyan) 
XMid = get_width(canvas) // 2 
YMid = get_height(canvas) // 2 
Radius = 150 
Band = 40 
#------------------------------------------------------------ 
# Draw horizontal blue lines from screen left to screen 
# right, starting at line 40 and stepping down 10 rows at 
# a time. 
#------------------------------------------------------------ 
for Y in range(Band, get_height(canvas), 10): 
    add_horizontal_line(canvas, 0, get_width(canvas)-1, Y, blue) 
#------------------------------------------------------------ 
# Draw vertical blue lines from line 40 to screen bottom, 
# starting at screen left and stepping right 10 columns at 
# a time. 
#------------------------------------------------------------ 
for X in range(0, get_width(canvas), 10): 
    add_vertical_line(canvas, X, Band, get_height(canvas)-1, blue) 
#------------------------------------------------------------ 
# Draw a green filled box from screen left to screen right 
# for the first 40 lines, surrounded by a black outline. #------------------------------------------------------------ 
add_rectangle_filled_sized (canvas, 0, 0, get_width(canvas), Band, green) 
add_rectangle_outline_sized(canvas, 0, 0, get_width(canvas)-1, Band-1, black) 
#------------------------------------------------------------ 
# Draw a big yellow filled circle at screen center, with
# a bunch of red circle outlines starting at radius 10 and 
# stepping by 5 per circle. Finally, draw a red spot at 
# the center, and draw a black outline. 
#------------------------------------------------------------ 
add_bresenham_filled_circle(canvas, XMid, YMid, Radius, yellow) 
for R in range(10, Radius, 5): 
    add_bresenham_circle(canvas, XMid, YMid, R, red) 
    add_bresenham_filled_circle(canvas, XMid, YMid, 5, red) 
    add_bresenham_circle(canvas, XMid, YMid, Radius, black) 
#------------------------------------------------------------ 
# Draw my signature in the green area. 
#------------------------------------------------------------ 
add_line(canvas, 10, 10, 20, 30) # V 
add_line(canvas, 20, 30, 30, 10) 
add_line(canvas, 40, 10, 30, 30) # E 
add_line(canvas, 40, 10, 60, 10) 
add_line(canvas, 35, 20, 45, 20) 
add_line(canvas, 30, 30, 50, 30) 
add_line(canvas, 70, 10, 60, 30) # R 
add_line(canvas, 70, 10, 80, 10) 
add_line(canvas, 65, 20, 75, 20) 
add_line(canvas, 80, 10, 85, 15) 
add_line(canvas, 85, 15, 75, 20) 
add_line(canvas, 75, 20, 80, 30) 
add_line(canvas, 90, 10,110, 10) # T 
add_line(canvas,100, 10, 90, 30) 
add_line(canvas,120, 10,130, 10) # S 
add_line(canvas,130, 10,132, 12) 
add_line(canvas,120, 10,115, 15) 
add_line(canvas,115, 15,120, 20) 
add_line(canvas,120, 20,125, 20) 
add_line(canvas,125, 20,128, 25) 
add_line(canvas,128, 25,125, 30) 
add_line(canvas,125, 30,115, 30) 
add_line(canvas,115, 30,112, 25) 
#------------------------------------------------------------ 
# Add your signature (Extra Credit) and Save the image to file. 
# #------------------------------------------------------------ 
add_text(canvas, XMid // 2, Band - 8,  my_name, blue) 
print ("Pixels in canvas = ", get_width(canvas)*get_height(canvas)) 
print ("Items in canvas = ",len(canvas)) 
write_bmp(canvas, "TestGraphics.bmp") 
print ("All Done")
