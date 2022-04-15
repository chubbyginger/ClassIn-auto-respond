#!/usr/bin/env python3
import pyautogui as autogui
import pygame
from pygame.locals import *
import threading
import sys
if sys.platform == "win32":
    # For Windows, import the CTypes library.
    import ctypes
    from ctypes import wintypes
# else:
    # For non-Windows OSes, import the PIL ImageGrab.
    import PIL.ImageGrab

# Init variables
leftTopX = 0
leftTopY = 0
rightBotX = 0
rightBotY = 0
PixelR = 0
PixelG = 0
PixelB = 0
stopThread = False

# For Windows, Register USER32.DLL for getting RGB values of the screen.
if sys.platform == "win32":
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    user32.GetDC.restype = wintypes.HDC
    user32.GetDC.argtypes = (wintypes.HWND,)

    gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)
    gdi32.GetPixel.restype = wintypes.COLORREF
    gdi32.GetPixel.argtypes = (wintypes.HDC, ctypes.c_int, ctypes.c_int)

# Init pygame
pygame.init()
# screen = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_caption("这是个没卵用的窗口")

# Print hello messages
print("Classin Automove\n\
==============================\n\
posLeftTop: 确定左上角位置    posRightBot: 确定右下角位置\n\
getPixelData: 取色          start: 开始\n\
stop: 结束\n")

# Get colour on Windows. See https://blog.51cto.com/u_15127566/4229590
def getPixelColour(x, y):
    if sys.platform == "win32":
        hdc = user32.GetDC(None)
        color = gdi32.GetPixel(hdc, x, y)
        r = color & 0xFF
        g = color >> 8 & 0xFF
        b = color >> 16 & 0xFF
        return (r, g, b)
    else:
        # TODO: get pixel colour on non-Windows platforms.
        rgb = PIL.ImageGrab.grab().getpixel((x, y))
        return rgb


def scanScreen():
    # TODO: scan function
    pass

# Main loop
while True:
    # pygame.display.update()
    inCommand = input("> ")
    
    if inCommand == "posLeftTop":
        leftTopX, leftTopY = autogui.position()
        print(f"获取左上角坐标成功，坐标为({leftTopX}, {leftTopY})")
    
    if inCommand == "posRightBot":
        rightBotX, rightBotY = autogui.position()
        print(f"获取右下角坐标成功，坐标为({rightBotX}, {rightBotY})")

    if inCommand == "getPixelData":
        currX, currY = autogui.position()
        PixelR, PixelG, PixelB = getPixelColour(currX, currY)
        print(f"获取像素成功，RGB值为({PixelR}, {PixelG}, {PixelB})")
    
    if inCommand == "start":
        thr = threading.Thread(target=scanScreen)
        thr.start()
        print("已启动扫描屏幕线程")
    
    if inCommand == "stop":
        stopThread = True
        print("已停止扫描屏幕线程")