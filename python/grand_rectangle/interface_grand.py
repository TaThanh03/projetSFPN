import matplotlib
matplotlib.use('TkAgg')
from grid_rect import show_grid_rect, show_grid_rect_zoom
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import numpy as np
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

zoom_x_max = 0
zoom_x_min = 0
zoom_y_max = 0
zoom_y_min = 0
zoom_x_tmp = 0
zoom_y_tmp = 0
class my_toolbar(NavigationToolbar2TkAgg):
    def __init__(self, canvas_, parent_):
        self.toolitems = (
            ('Home', 'Reset original view', 'home', 'home'),
            ('Back', 'Go back', 'back', 'back'),
            ('Forward', 'Move forward', 'forward', 'forward'),
            ('Pan', 'Move around', 'move', 'pan'),
            ('Zoom', 'Zoom', 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ('Subplots', 'Configure', 'subplots', 'configure_subplots'),
            ('Save', 'Save instance', 'filesave', 'save_figure'),
            )
        NavigationToolbar2TkAgg.__init__(self,canvas_,parent_)
    
    def press_zoom(self, event):
        global zoom_x_tmp, zoom_y_tmp
        zoom_x_tmp, zoom_y_tmp = event.xdata, event.ydata
        print("press", zoom_x_tmp, zoom_y_tmp)
        NavigationToolbar2TkAgg.press_zoom(self, event)
        
    def release_zoom(self, event):
        global zoom_x_tmp, zoom_y_tmp, zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max
        if (zoom_x_tmp < event.xdata):
            zoom_x_min = zoom_x_tmp
            zoom_x_max = event.xdata
        else:
            zoom_x_max = zoom_x_tmp
            zoom_x_min = event.xdata
        if (zoom_y_tmp < event.ydata):
            zoom_y_min = zoom_y_tmp
            zoom_y_max = event.ydata
        else:
            zoom_y_max = zoom_y_tmp
            zoom_y_min = event.ydata
        zoom_x_tmp, zoom_y_tmp = event.xdata, event.ydata
        print('release', zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max)
        NavigationToolbar2TkAgg.release_zoom(self, event)
        
        
class SampleApp(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.wm_title("Grand Rectangle")       
        self.label_graphic = Tk.LabelFrame(self, text="Graphic")
        self.label_graphic.pack(side=Tk.TOP, fill="both")
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        A = matrice_gen(2)
        x,y,sigmin,time = show_grid_rect(A, 0.3, 100)    
        self.ax.contour(x,y,sigmin,0.3)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label_graphic)
        self.canvas.show()
        
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.label_toolbar = Tk.LabelFrame(self, text="Toolbar")
        self.label_toolbar.pack(side=Tk.BOTTOM, fill="both")
        
        toolbar = my_toolbar(self.canvas, self.label_toolbar)
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
        
        self.button_quit = Tk.Button(self, text="Quit", command=self._quit)
        self.button_quit.pack(side=Tk.RIGHT)
        self.button_go = Tk.Button(self, text="Go", command=self._go)
        self.button_go.pack(side=Tk.RIGHT)
        self.button_recalculate = Tk.Button(self, text="Recalculate", command=self._recalculate)
        self.button_recalculate.pack(side=Tk.RIGHT)
        
    def _go(self):
        arg1 = matrice_gen(int(self.entry_msize.get()))
        arg2 = self.entry_epsilon.get()
        arg3 = self.entry_precision.get()
        self.ax.clear()
        x,y,sigmin,time = show_grid_rect(arg1, float(arg2), int(arg3))   
        self.ax.contour(x,y,sigmin,float(arg2))
        #self.canvas.draw()
        self.canvas.show()
        
    def _recalculate(self):
        arg1 = matrice_gen(int(self.entry_msize.get()))
        arg2 = self.entry_epsilon.get()
        arg3 = self.entry_precision.get()
        self.ax.clear()
        x,y,sigmin,time = show_grid_rect_zoom(arg1,float(arg2),int(arg3), zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max)   
        self.ax.contour(x,y,sigmin,float(arg2))
        #self.canvas.draw()
        self.canvas.show()
        
    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()
        
            

app = SampleApp()
app.mainloop()
