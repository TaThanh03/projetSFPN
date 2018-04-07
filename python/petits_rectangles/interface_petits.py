import matplotlib
matplotlib.use('TkAgg')
from grid_petits_rect2 import grid_petits_rect 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import sys
if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk

def matrice_gen(n):
    if n == 2:    
        A = np.array([[1,20],[-10,-1]])
    elif n == 3:
        A = np.array([[-0.55,-0.04,-0.5],[-0.41,0.036,0.19],[0.28,-0.31, 0.20]])
    elif n == 4:
        A = np.array([[5,0,0,-1],[1,0,-100,1],[-1.5,1,-200,1],[-1,100,3,-3]])
    elif n == 5:
        A = np.array([[1,0,0,0,0],[2,10,0,0,1],[2,2,70,0,8],[2,4,1,2,6],[2,1,1,1,20]])
    elif n == 6:
        A = np.array([[1,0,-1,3,1,5],[-2,100,4,5,1,2],[1,8,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,1,2,5],[-6,1,2,5,6,70]])
    elif n == 7:
        A = np.array([[1,0,4,-1,3,1,5],[-2,100,9,400,5,1,2],[1,8,7,1,4,9,4],[-2,-7,6,-100,3,4,9],[-2,-1,3,-8,4,2,5],[-6,100,-5,2,5,6,7],[-2,-4,-6,3,5,7,900]])
    elif n == 8:
        A = np.array([[1,0,144,-1,3,4,1,5],[-100,-3,1,100,4,5,1,2],[8,8,-9,87,1,4,9,4],[-2,-57,5,6,-100,35,4,9],[-2,3,-4,3,-8,57,2,5],[-7,1,-5,7,-7,500,5,7],[-2,8,-4,-6,3,100,7,9],[3,4,6,8,-100,4,-3,89]])
    else:
        A = np.array([[1,20],[-10,-1]])
    return A

class SampleApp(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.wm_title("Grand Rectangle")       
        self.label_graphic = Tk.LabelFrame(self, text="Graphic")
        self.label_graphic.pack(side=Tk.TOP, fill="both")
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        m = 100
        A = matrice_gen(2)
        x,y,sigmin,s = grid_petits_rect(A, 0.3, m)
        
        print("s", s) 
        for i in range(s):
            tmp1 = x[1+i*m:(i+1)*m]
            tmp2 = y[1+i*m:(i+1)*m]
            tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m]
            self.ax.contour(tmp1,tmp2,tmp3,0.3)
            
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
        self.ax.clear()
        A = matrice_gen(int(self.entry_msize.get()))
        eps = float(self.entry_epsilon.get())
        m = int(self.entry_precision.get())
        x,y,sigmin,s = grid_petits_rect(A, eps, m)
        print("s", s) 
        """
        for i in range(s):
            tmp1 = x[1+i*m:(i+1)*m]
            tmp2 = y[1+i*m:(i+1)*m]
            tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m]
            self.ax.contour(tmp1,tmp2,tmp3,eps)
        """
        self.canvas.draw()
        #self.canvas.show()
        
    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()
        
app = SampleApp()
app.mainloop()
