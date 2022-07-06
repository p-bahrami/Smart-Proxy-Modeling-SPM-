import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class Data:
    def __init__(self):
        self.layer = tk.IntVar()


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = tk.Frame(self)
        container.pack()

        self.data = Data()

        self.frames = {}
        for F in (page1,):
            frame = F(container, self.data)
            self.frames[F] = frame
            frame.pack()

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


class page1(tk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.data = data

        frame1 = tk.Frame(self, width=200)
        frame1.pack()

        self.button = tk.Button(frame1, text="plot")
        self.button.grid(row=1, column=0, columnspan=2, pady=20)

        np.random.seed(2)
        self.num = list(np.random.randint(low=1, high=10, size=3000000))

        self.button['command'] = self.open

    def plot(self, var, window):
        global ax, newcmp, nx, ny, x, y, num_reshaped
        nx = 500
        ny = 600
        var = 1
        num_reshaped = np.array(self.num).reshape(10, nx * ny)
        layer = num_reshaped[var - 1:var, :]
        layer = layer.reshape(nx, ny)
        x, y = np.mgrid[slice(0, nx + 1, 1), slice(0, ny + 1, 1)]

        self.figure = Figure(figsize=(4, 4))
        ax = self.figure.add_subplot(111)
        col_type = cm.get_cmap('rainbow', 256)
        newcolors = col_type(np.linspace(0, 1, 1000))
        white = np.array([1, 1, 1, 1])
        newcolors[:1, :] = white
        newcmp = ListedColormap(newcolors)

        c = ax.pcolormesh(x, y, layer, cmap=newcmp)
        ax.figure.colorbar(c)
        self.canvas = FigureCanvasTkAgg(self.figure, window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def open(self):
        self.toplevel = tk.Toplevel()
        self.toplevel.geometry('+500+100')

        self.h_slider1 = tk.Scale(self.toplevel, from_=1, to=10, orient="horizontal", length=100, resolution=1, variable=self.data.layer)
        self.h_slider1.pack()

        self.h_slider1['command'] = self.update

        self.plot(self.data.layer.get(), self.toplevel)

    def update(self, *args):
        var = self.data.layer.get()
        layer = num_reshaped[var - 1:var, :]
        layer = layer.reshape(nx, ny)
        ax.pcolormesh(x, y, layer, cmap=newcmp)
        self.canvas.draw()


app = SampleApp()
app.mainloop()