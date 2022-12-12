#Project 4 - Jacqueline Cole - December 12th, 2022

import math
from font2420 import *

my_name = "Jacqueline"

def Distance (X0,Y0,X1,Y1): 
    DeltaX = X1-X0
    DeltaY = Y1-Y0
    return math.sqrt(DeltaX*DeltaX + DeltaY*DeltaY)

black = [0,0,0] 
blue = [0,0,255] 
green = [0,255,0] 
cyan = [0,255,255] 
red = [255,0,0]
magenta = [255,0,255] 
yellow = [255,255,0] 
white = [255,255,255] 
gray = [128,128,128]

def getRed (Pixel): return Pixel[0] 
def getGreen (Pixel): return Pixel[1] 
def getBlue (Pixel): return Pixel[2]
def setRed (Pixel,Value): 
    Pixel[0] = Value 
    return
def setGreen (Pixel,Value): 
    Pixel[1] = Value 
    return
def setBlue (Pixel,Value): 
    Pixel[2] = Value 
    return

def make_empty_picture (Width,Height,Color=white): 
    return {"Width":Width, "Height":Height, "Default":Color}
def get_width (Canvas): return Canvas["Width"] 
def get_height (Canvas): return Canvas["Height"] 
def get_default (Canvas): return Canvas["Default"]

def onScreen (Canvas, X, Y): 
    X = int(round(X)) 
    Y = int(round(Y))
    if (X < 0) or (Y < 0): return False 
    if (X >= Canvas["Width"]): return False 
    if (Y >= Canvas["Height"]): return False 
    return True
def set_pixel (Canvas, X, Y, Color=black): 
    if not onScreen(Canvas,X,Y): return 
    Index = (int(round(X)),int(round(Y))) 
    if Color == Canvas["Default"]: 
        if Index in Canvas: del Canvas[Index]
    else: 
        Canvas[Index] = Color 
    return 
def get_pixel (Canvas, X, Y):
    Index = (int(round(X)),int(round(Y)))  
    if Index in Canvas:
        Result = Canvas[Index] 
    else: 
        Result = Canvas["Default"] 
    return Result

def write_string(Outfile,S): 
    L = [ord(CH) for CH in S] 
    Outfile.write(bytes(L))
    return

def write_bytes (Outfile,N,TotalBytes=1): 
    L = []
    for I in range(TotalBytes): 
        L = L + [N % 256] 
        N = N // 256
    Outfile.write(bytes(L))
    return

def write_bmp (Canvas, FileName):
    Width = get_width(Canvas)
    Height = get_height(Canvas)
    FileHeaderSize = 14
    ImageHeaderSize = 40
    BytesPerPixel = 3
    BitsPerPixel =  BytesPerPixel * 8
    Pad = 4 - (Width * BytesPerPixel) % 4
    if Pad == 4: Pad = 0
    BytesPerRaster = Width * BytesPerPixel + Pad
    ImageSize = Height * BytesPerRaster
    Offset = FileHeaderSize + ImageHeaderSize
    FileSize = ImageSize + Offset
    Outfile = open(FileName, "wb")
    try:
        write_string (Outfile, "BM")
        write_bytes (Outfile, FileSize, 4)
        write_bytes (Outfile, 0, 2)
        write_bytes (Outfile, 0, 2)
        write_bytes (Outfile, Offset, 4)
        write_bytes (Outfile, ImageHeaderSize, 4)
        write_bytes (Outfile, Width, 4)
        write_bytes (Outfile, Height, 4)
        write_bytes (Outfile, 1, 2)
        write_bytes (Outfile, BitsPerPixel, 2)
        write_bytes (Outfile, 0, 4)
        write_bytes (Outfile, ImageSize, 4)
        write_bytes (Outfile, 0, 4)
        write_bytes (Outfile, 0, 4)
        write_bytes (Outfile, 0, 4)
        write_bytes (Outfile, 0, 4)
        for Y in range(Height-1, -1, -1):
            for X in range(Width):
                Pixel = get_pixel(Canvas,X,Y)
                write_bytes (Outfile, getBlue(Pixel), 1)
                write_bytes (Outfile, getGreen(Pixel), 1)
                write_bytes (Outfile, getRed(Pixel), 1)
            if Pad > 0: write_bytes(Outfile, 0, Pad)
    finally:
        Outfile.close()
    return

def add_line (Canvas, X1, Y1, X2, Y2, Color=black): 
    D = int(round(Distance(X1,Y1,X2,Y2))) + 1 
    Ax = X2 - X1 
    Ay = Y2 - Y1
    for I in range(D+1):
        T = I / float(D)
        X = Ax * T + X1  
        Y = Ay * T + Y1
        set_pixel(Canvas, X, Y, Color)
    return

def add_horizontal_line (Canvas, X1, X2, Y, Color=black): 
    if (Y < 0) or (Y >= get_height(Canvas)): return 
    if (X1 > X2): X1,X2 = X2,X1
    for X in range(X1,X2+1): set_pixel(Canvas,X,Y,Color) 
    return

def add_vertical_line (Canvas, X, Y1, Y2, Color=black): 
    if (X < 0) or (X >= get_width(Canvas)): return 
    if (Y1 > Y2): Y1,Y2 = Y2,Y1
    for Y in range(Y1,Y2+1): set_pixel(Canvas,X,Y,Color) 
    return

def add_rectangle_filled (Canvas, X1, Y1, X2, Y2, Color=black): 
    if (Y1 > Y2): Y1,Y2 = Y2,Y1  # Required
    if (X1 > X2): X1,X2 = X2,X1  # Optional
    for Y in range(Y1,Y2+1):
        add_horizontal_line(Canvas,X1,X2,Y,Color) 
    return

def add_rectangle_outline (Canvas, X1, Y1, X2, Y2, Color=black): 
    if (Y1 > Y2): Y1,Y2 = Y2,Y1 # Optional
    if (X1 > X2): X1,X2 = X2,X1 # Optional
    add_horizontal_line (Canvas, X1, X2, Y1, Color) # Top 
    add_horizontal_line (Canvas, X1, X2, Y2, Color) # Bottom 
    add_vertical_line (Canvas, X1, Y1, Y2, Color) # Left 
    add_vertical_line (Canvas, X2, Y1, Y2, Color) # Right 
    return

def add_rectangle_filled_sized (Canvas, X, Y, W, H, Color=black): 
    add_rectangle_filled(Canvas,X,Y,X+W-1,Y+H-1,Color) 
    return
def add_rectangle_outline_sized (Canvas, X, Y, W, H, Color=black): 
    add_rectangle_outline(Canvas,X,Y,X+W,Y+H,Color) 
    return

def add_bresenham_circle (Canvas, Xc, Yc, R, Color=black): 
    X = R 
    Y = 0 
    E = -R
    while (X >= Y):
        set_pixel (Canvas, Xc - X, Yc + Y, Color) 
        set_pixel (Canvas, Xc + X, Yc + Y, Color) 
        set_pixel (Canvas, Xc - X, Yc - Y, Color) 
        set_pixel (Canvas, Xc + X, Yc - Y, Color) 
        set_pixel (Canvas, Xc - Y, Yc + X, Color) 
        set_pixel (Canvas, Xc + Y, Yc + X, Color) 
        set_pixel (Canvas, Xc - Y, Yc - X, Color) 
        set_pixel (Canvas, Xc + Y, Yc - X, Color) 
        E = E + Y + Y + 1 
        Y = Y + 1 
        if (E > 0): 
            E = E - X - X + 2 
            X = X - 1
    return

def add_bresenham_filled_circle (Canvas, Xc, Yc, R, Color=black): 
    X = R 
    Y = 0 
    E = -R
    while (X >= Y):
        add_horizontal_line(Canvas,Xc - X, Xc + X, Yc + Y, Color) 
        add_horizontal_line(Canvas,Xc - X, Xc + X, Yc - Y, Color) 
        add_horizontal_line(Canvas,Xc - Y, Xc + Y, Yc + X, Color) 
        add_horizontal_line(Canvas,Xc - Y, Xc + Y, Yc - X, Color) 
        E = E + Y + Y + 1 
        Y = Y + 1 
        if (E > 0): 
            E = E - X - X + 2 
            X = X - 1
    return

def add_text (canvas, X, Y, S, Color=black):
    #Code will eventually go here
    return