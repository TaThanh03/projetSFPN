import matplotlib
matplotlib.use('TkAgg')
from grid_rect import show_grid_rect, show_grid_rect_zoom
from grid_petits_rect2 import grid_petits_rect
from proj_corr import proj_corr, proj_corr_zoom
from grid_par_comp import grid_par_comp

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
        A = np.array([[1,20*1j],[-10,-1]])
    elif n == 3:
        A = np.array([[-1, 4, -5*1j],[-1, 3, 9*1j],[8, -3, 2]])
    elif n == 4:
        A = np.array([[1, 1, 1, 1],[2, 60, 2, 2],[1, 1, 20, 1],[1, 2, 5, 20*1j]])
    elif n == 5:
        A = np.array([[1,0,0,0,0],[2,10*1j,0,0,1],[2,2,70,0,8],[2,4,1,2,6],[2,1,1,1,20]])
    elif n == 6:
        A = np.array([[1,0,-1,3,1,5],[-2,100,4,5,1,2],[1,8*1j,7,4,9,4],[-7,6,-1,3,4,9],[-2,-4,3,1,2,5],[-6,1,2,5,6,70]])
    elif n == 7:
        A = np.array([[1,0,4,-1,3,1,5],[-2,100,9*1j,400,5,1,2],[1,8,7*1j,1,4,9,4],[-2,-7,6,-100,3,4,9],[-2,-1,3,-8,4,2,5],[-6,100,-5,2,5,6,7],[-2,-4,-6,3,5,7,900]])
    elif n == 8:
        A = np.array([[1,0,144,-1,3,4,1,5],[-100*1j,-3,1,100,4,5,1,2],[8,8,-9,87*1j,1,4,9,4],[-2,-57,5,6,-100,35,4,9],[-2,3,-4,3,-8,57,2,5],[-7,1,-5,7,-7,500,5,7],[-2,8,-4,-6,3,100,7,9],[3,4,6,8,-100,4,-3,89]])
    else:
        A = np.array([[1,20*1j],[-10,-1]])
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
        #print("press", zoom_x_tmp, zoom_y_tmp)
        NavigationToolbar2TkAgg.press_zoom(self, event)
        
    def release_zoom(self, event):
        global zoom_x_tmp, zoom_y_tmp, zoom_x_max, zoom_x_min, zoom_y_max,  zoom_y_min
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
        #print('release', zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max)
        NavigationToolbar2TkAgg.release_zoom(self, event)
        
        
class SampleApp(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.wm_title("Calcul de pseudospectres")       
        #self.geometry('{}x{}'.format(800, 600))
        
        self.label_ENTRY = Tk.LabelFrame(self, width=100, height=900, pady=3)
        
        self.label_TIME = Tk.Label(self.label_ENTRY, text = "Welcome!")
        self.label_TIME.pack()
        
        self.label_msize = Tk.LabelFrame(self.label_ENTRY, text="Matrix's size:")
        self.label_msize.pack()
        self.entry_msize = Tk.Entry(self.label_msize)
        self.entry_msize.pack() 
        self.label_epsilon = Tk.LabelFrame(self.label_ENTRY, text="Epsilon:")
        self.label_epsilon.pack()
        self.entry_epsilon = Tk.Entry(self.label_epsilon)
        self.entry_epsilon.pack()    
        self.label_precision = Tk.LabelFrame(self.label_ENTRY, text="Precision:")
        self.label_precision.pack()
        self.entry_precision = Tk.Entry(self.label_precision)
        self.entry_precision.pack()
        
        self.checkbutton_algo = Tk.LabelFrame(self.label_ENTRY, text="Algorithm:" )
        self.CheckVar1 = Tk.IntVar()
        C1 = Tk.Radiobutton(self.checkbutton_algo, text = "Grid grand rectangle", variable = self.CheckVar1, value=1)
        C2 = Tk.Radiobutton(self.checkbutton_algo, text = "Grid petits rectangles", variable = self.CheckVar1, value=2)
        C3 = Tk.Radiobutton(self.checkbutton_algo, text = "Prediction Correction", variable = self.CheckVar1, value=3, command= self._popup_proj_corr)
        C4 = Tk.Radiobutton(self.checkbutton_algo, text = "Grid par Composition", variable = self.CheckVar1, value=4)
        C1.pack(anchor = 'w' )
        C2.pack(anchor = 'w' )
        C3.pack(anchor = 'w' )
        C4.pack(anchor = 'w' )
        self.checkbutton_algo.pack()
        
        self.checkbutton_mode = Tk.LabelFrame(self.label_ENTRY, text="Mode:" )
        self.CheckVar2 = Tk.IntVar()
        C5 = Tk.Radiobutton(self.checkbutton_mode, text = "Sequentiel", variable = self.CheckVar2, value=1)
        C6 = Tk.Radiobutton(self.checkbutton_mode, text = "Parallel", variable = self.CheckVar2, value=2)
        C5.pack(anchor = 'w' )
        C6.pack(anchor = 'w' )
        self.checkbutton_mode.pack()
        
        self.button_go = Tk.Button(self.label_ENTRY, text="Go", command=self._go)
        self.button_go.pack(fill='x', expand=True)
        self.button_recalculate = Tk.Button(self.label_ENTRY, text="Recalculate", command=self._recalculate)
        self.button_recalculate.pack(fill='x', expand=True)
        self.button_quit = Tk.Button(self.label_ENTRY, text="Quit", command=self._quit)
        self.button_quit.pack(fill='x', expand=True)
        
        self.label_ENTRY.pack(side=Tk.LEFT)
        
        self.label_graphic = Tk.LabelFrame(self, text="Graphic", width=650, height=900, pady=3)
        self.fig = Figure(figsize=(5, 5), dpi=130)
        self.ax = self.fig.add_subplot(111)
        """
        A = matrice_gen(2)
        x,y,sigmin,time = show_grid_rect(A, 0.3, 100)    
        self.ax.contour(x,y,sigmin,0.3)
        """
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label_graphic)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.label_toolbar = Tk.LabelFrame(self, text="Toolbar")
        self.label_toolbar.pack(side=Tk.BOTTOM, fill="both")
        toolbar = my_toolbar(self.canvas, self.label_toolbar)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        self.label_graphic.pack(side=Tk.RIGHT)
        
    def _go(self):
        arg1 = matrice_gen(int(self.entry_msize.get()))
        arg2 = float(self.entry_epsilon.get())
        arg3 = int(self.entry_precision.get())
        algo = self.CheckVar1.get()
        mode = int(self.CheckVar2.get())
        self.ax.clear()
        time = 0
        if (algo == 1):
            x,y,sigmin,time = show_grid_rect(arg1, arg2, arg3, mode)   
            self.ax.contour(x,y,sigmin,arg2)
            #self.canvas.draw()
            self.canvas.show()
        elif (algo == 2):
            x,y,sigmin,time,s,m = grid_petits_rect(arg1, arg2, arg3, mode)   
            for i in range(s):
                tmp1 = x[1+i*m:(i+1)*m];
                tmp2 = y[1+i*m:(i+1)*m];
                tmp3 = sigmin[1+i*m:(i+1)*m,1+i*m:(i+1)*m];
                self.ax.contour(tmp1,tmp2,tmp3,[arg2])
            self.canvas.show()
        elif (algo == 3):
            K = int(self.entry_K.get())
            tol = float(self.entry_tol.get())
            taille, zx, zy, time = proj_corr(arg1, arg2, K, tol, mode)
            for i in range(taille):
                self.ax.plot(zx[i], zy[i])
            self.canvas.show()
        elif (algo == 4):
            x,y,p,time = grid_par_comp(arg1, arg2, arg3, mode)
            self.ax.contour(x,y,p,[arg2])
            self.canvas.show()
        strg = "Time: " + str(time)
        self.label_TIME.config(text = strg)
        
        
    def _recalculate(self):
        time = 0
        arg1 = matrice_gen(int(self.entry_msize.get()))
        arg2 = float(self.entry_epsilon.get())
        arg3 = int(self.entry_precision.get())
        algo = self.CheckVar1.get()
        mode = int(self.CheckVar2.get())
        self.ax.clear()
        if ( algo == 1 or algo == 2):
            x,y,sigmin,time = show_grid_rect_zoom(arg1,arg2,arg3, zoom_x_max, zoom_x_min, zoom_y_max, zoom_y_min, mode)   
            self.ax.contour(x,y,sigmin,float(arg2))
            #self.canvas.draw()
            self.canvas.show()
        if ( algo == 3):
            K = int(self.entry_K.get())
            tol = float(self.entry_tol.get())
            taille, zx, zy, time = proj_corr_zoom(arg1,arg2,K,tol, zoom_x_max, zoom_x_min, zoom_y_max, zoom_y_min) 
            for i in range(taille):
                self.ax.plot(zx[i], zy[i])
            self.canvas.show()
        
        strg = "Time: " + str(time)
        self.label_TIME.config(text = strg)
        
    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()
        
    def _popup_proj_corr(self):
        self.toplevel = Tk.Toplevel()
        self.label_K = Tk.LabelFrame(self.toplevel, text="K:")
        self.label_K.pack()
        self.entry_K = Tk.Entry(self.label_K)
        self.entry_K.pack()    
        self.label_tol = Tk.LabelFrame(self.toplevel, text="Tol:")
        self.label_tol.pack()
        self.entry_tol = Tk.Entry(self.label_tol)
        self.entry_tol.pack()   
        
app = SampleApp()
app.mainloop()
