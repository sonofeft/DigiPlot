
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

from tkinter.ttk import Combobox, Progressbar, Separator, Treeview, Notebook

from tkinter import *
from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, LabelFrame
from tkinter import Listbox, Message, Radiobutton, Spinbox, Text
from tkinter import OptionMenu
import tkinter.filedialog
from tkinter import _setit as set_command

import os, sys, zipfile, json
try:
    from StringIO import StringIO as MemoryIO
except:
    from io import BytesIO as MemoryIO
    
from PIL import Image
    
from digiplot.plot_area import PlotArea
from digiplot.tk_digiplot import Point

from digiplot.auto_detect_Dialog import _auto_detect
here = os.path.abspath(os.path.dirname(__file__))

proj_path = os.path.join( here, 'examples', "test.digiplot.zip" )
zf = zipfile.ZipFile( os.path.abspath(proj_path) , 'r')

PA = PlotArea(w_canv=600, h_canv=600) # will hold PlotArea() when it is opened
img_data = zf.read( 'img.jpg' )
fh = MemoryIO(img_data)
img = Image.open(fh)
PA.set_img( img )

# ========== process json data ==============
json_data = zf.read('digiplot_info.json')
J = json.loads( json_data )

PA.fi_origin = J['fi_origin']
PA.fj_origin = J['fj_origin']
PA.fimax = J['fimax']
PA.fjmax = J['fjmax']
PA.fi_offset = J['fi_offset']
PA.fj_offset = J['fj_offset']
PA.x_origin = J['x_origin']
PA.y_origin = J['y_origin']
PA.xmax = J['xmax']
PA.ymax = J['ymax']
PA.log_x = J['log_x']
PA.log_y = J['log_y']
PA.log10_x_origin = J['log10_x_origin']
PA.log10_y_origin = J['log10_y_origin']
PA.log10_xmax = J['log10_xmax']
PA.log10_ymax = J['log10_ymax']

pointL = []
pLL = J['list_of_points']
for pL in pLL:
    #print(pL)
    x,y,fi,fj = pL
    pointL.append( Point(x,y,fi,fj) )
            
zf.close()


class _Testdialog:
    def __init__(self, master):
        frame = Frame(master, width=300, height=300)
        frame.pack()
        self.master = master
        self.x, self.y, self.w, self.h = -1,-1,-1,-1
        
        self.Button_1 = Button(text="Test Dialog", relief="raised", width="15")
        self.Button_1.place(x=84, y=36)
        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    def Button_1_Click(self, event): #click method for component ID=1
        dialogOptions = {'PA':PA, 'pointL':pointL}
        
        
        dialog = _auto_detect(self.master, "GaussianBlur Used for Curve Edge Detection",
                              dialogOptions=dialogOptions)
        print( '===============Result from Dialog====================' )
        print( dialog.result )
        print( '=====================================================' )

def main():
    root = Tk()
    app = _Testdialog(root)
    root.mainloop()

if __name__ == '__main__':
    main()
