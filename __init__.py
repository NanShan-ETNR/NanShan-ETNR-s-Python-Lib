'''
==========================MyGUI=====================
Welcome to MyGUI!
This module has a lot of branch module,
It can make it easy for you to use GUI. 
==================NanShan_Python_Modules============
We have advanced technology and excellent development environment.
We can make many Python modules according to your needs.
'''
import tkinter as tk
import tkinter.messagebox as mes
import tkinter.simpledialog as sim
import tkinter.colorchooser as col
import tkinter.filedialog as fil
import os
import sys

E = tk.E

class new_window(tk.Tk):
     pass

def button(win,text='',command=None,anchor=None,width=None,height=None,color=None,bitmap=None,cursor=None,font=None,image=None,state=None):
     return tk.Button(win,text=text,command=command,anchor=anchor,width=width,height=height,bg=color,bitmap=bitmap,cursor=cursor,font=font,image=image,state=state)

def label(win,text='',justify=None,anchor=None,width=None,height=None,bg=None,fg=None,image=None,exportselection=None):
     return tk.Label(win,text=text,anchor=anchor,width=width,height=height,bg=bg,fg=fg,justify=justify,image=image,exportselection=exportselection)

def text(win,autoseparators=None,bg=None,bd=None,cursor=None,exportselection=None,fg=None,font=None,height=None,padx=None,pady=None,state=None,width=None,highlightthickness=None,highlightcolor=None,highlightbackground=None,text=''):
     pass
