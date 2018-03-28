from grid_rect import show_grid_rect 

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
#from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
"""
def _quit(root):
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)
canvas.mpl_connect('key_press_event', on_key_event)
"""


class SampleApp(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.wm_title("Grand Rectangle")       
        

        self.label_graphic = Tk.LabelFrame(self, text="Graphic")
        self.label_graphic.pack(side=Tk.TOP, fill="both")
    
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        x,y,sigmin,time = show_grid_rect(2, 0.3, 100)    
        self.ax.contour(x,y,sigmin,0.3)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label_graphic)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        
        self.label_toolbar = Tk.LabelFrame(self, text="Toolbar")
        self.label_toolbar.pack(side=Tk.BOTTOM, fill="both")
        toolbar = NavigationToolbar2TkAgg(self.canvas, self.label_toolbar)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        
        self.label_msize = Tk.LabelFrame(self, text="Matrix's size:")
        self.label_msize.pack(side=Tk.LEFT)
        self.entry_msize = Tk.Entry(self.label_msize)
        self.entry_msize.pack() 
        
        self.label_epsilon = Tk.LabelFrame(self, text="Epsilon:")
        self.label_epsilon.pack(side=Tk.LEFT)
        self.entry_epsilon = Tk.Entry(self.label_epsilon)
        self.entry_epsilon.pack()
        
        self.label_precision = Tk.LabelFrame(self, text="Precision:")
        self.label_precision.pack(side=Tk.LEFT)
        self.entry_precision = Tk.Entry(self.label_precision)
        self.entry_precision.pack()
        
        self.button2 = Tk.Button(self, text="Quit", command=self._quit)
        self.button2.pack(side=Tk.RIGHT)
        self.button = Tk.Button(self, text="Go", command=self._go)
        self.button.pack(side=Tk.RIGHT)
        

    def _go(self):
        #print(self.entry_msize.get())
        #print(self.entry_epsilon.get())
        #print(self.entry_precision.get())
        arg1 = self.entry_msize.get()
        arg2 = self.entry_epsilon.get()
        arg3 = self.entry_precision.get()
        self.ax.clear()
        x,y,sigmin,time = show_grid_rect(int(arg1), float(arg2), int(arg3))   
        self.ax.contour(x,y,sigmin,int(arg3))
        self.canvas.draw()
        
        
    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()

app = SampleApp()
app.mainloop()