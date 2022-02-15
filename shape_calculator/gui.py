import tkinter as tk
from tkinter import ttk, messagebox

from shapes_control import ShapesControl, SelectedShapeData


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self['background'] = '#ebebeb'
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.font = 'Helvetica 18'
        self.geometry('600x500')
        self.minsize(600, 500)
        self.maxsize(600, 500)

        self.frame_control = tk.Frame(self)
        self.frame_output = tk.Frame(self)
        self.frame_input = tk.Frame(self)
        self.frame_input.configure(bg='red')
        self.frame_output.configure(bg='yellow')
        self.frames_pask()
        
        self.frame_control_configure(self.frame_control)
        self.frame_control_pack(self.frame_control)

        self.canvas = tk.Canvas(self)
        self.label_list = [ttk.Label(self),]
        self.entry_list = [ttk.Entry(self),]

    def frames_pask(self):
        self.frame_control.place(relx=.6, rely=.3, relwidth=.4, relheight=.7)
        self.frame_output.place(relx=0, rely=0, relwidth=1, relheight=.3)
        self.frame_input.place(relx=0, rely=.3, relwidth=.6, relheight=.7)

    def frame_control_configure(self, root):
        root.configure(bg='green')
        root.lebel_select = ttk.Button(root, text='Select shape', command=self.select_button_use)
        root.choose_bar = ttk.Combobox(root, font=self.font, state="readonly",
                                  values=tuple(ShapesControl().get_shapes_all().keys()))
        root.choose_bar.current(0)
        root.calculate_button = ttk.Button(root, text='calculate', command=self.calculate_button_use)
        root.draw_button = ttk.Button(root, text='draw', command=self.draw_button_use)

    def frame_control_pack(self, root):
            root.lebel_select.place(relx=.1, rely=.1, relwidth=.8, relheight=.08)
            root.choose_bar.place(relx=.1, rely=.2, relwidth=.8, relheight=.1)
            root.calculate_button.place(relx=.1, rely=.4, relwidth=.8, relheight=.2)
            root.draw_button.place(relx=.1, rely=.7, relwidth=.8, relheight=.2)

    def frame_input_configure(self, root):
        self.canvas.destroy()
        self.input_widget_destroy()
        attributes = self.get_attributes_name()
        self.label_list = [ttk.Label(root, width=10, font=self.font, text=el+' is') for el in attributes]
        self.entry_list = [ttk.Entry(root, width=10, font=self.font) for _ in attributes]
        self.frame_input_pack()

    def frame_input_pack(self):
        attributes = self.get_attributes_name()
        for el in range(len(attributes)):
            self.label_list[el].grid(row=el, column=0, padx=20, pady=20)
            self.entry_list[el].grid(row=el, column=1, padx=20, pady=20)  

    def get_attributes_name(self) -> list:
        obj = ShapesControl.str_to_object(self.choice)
        return ShapesControl.get_arguments(obj)
   
    def frame_output_configure(self, root):
        self.canvas.destroy()
        self.get_arg_shape()
        area, perimetr_or_volume, method_name = self.get_area_and_volume_or_perimetr()

        label_perimetr = ttk.Label(root, font=self.font, width=20, text=method_name)
        label_area = ttk.Label(root, font=self.font, width=20, text='area is')
        label_out_perimetr = ttk.Label(root, font=self.font, width=20)
        label_out_area = ttk.Label(root, font=self.font, width=20)       
            
        label_out_area.configure(text=str(area))
        label_out_perimetr.configure(text=str(perimetr_or_volume))
        self.frame_output_pack(label_area, label_perimetr, label_out_area, label_out_perimetr)

    def frame_output_pack(self, root_area, root_perimetr, root_out_area, root_out_perimetr):
        root_perimetr.grid(row=0, column=0, padx=30, pady=20)
        root_area.grid(row=1, column=0, padx=30, pady=20)
        root_out_perimetr.grid(row=0, column=1)
        root_out_area.grid(row=1, column=1)
    
    def get_area_and_volume_or_perimetr(self) -> list:
        obj = ShapesControl.str_to_object(self.choice)
        if obj.get_name() in ShapesControl().get_shapes_3d().keys():
            method_name =' volume is'
            perimetr_or_volume = obj(*self.arg).volume()
        else:
            method_name = 'perimetr is'
            perimetr_or_volume = obj(*self.arg).perimetr()
        area = obj(*self.arg).area()
        return area, perimetr_or_volume, method_name
    
    def get_arg_shape(self) -> bool:
        obj = ShapesControl.str_to_object(self.choice)
        try:
            self.arg = [float(el.get()) for el in self.entry_list]
        except ValueError:
            self.get_error_messages()
        except:
            print('', end='')
            

    def input_widget_destroy(self):
        [el.destroy() for el in self.label_list]
        [el.destroy() for el in self.entry_list]

    def select_button_use(self):
        self.choice = self.frame_control.choose_bar.get()
        self.frame_input_configure(self.frame_input)

    def calculate_button_use(self):
        try:
            self.choice
        except AttributeError:
            self.get_info_messages()
        else:
            self.frame_output_configure(self.frame_output)
    
    def draw_button_use(self):
        self.input_widget_destroy()
        self.canvas = MyCanvas(self.frame_input)
        try:
            self.choice
            self.arg
        except AttributeError:
            self.get_info_messages()
        else:
            if self.choice in ShapesControl().get_shapes_3d().keys():
                self.canvas.my_create_text()
            if self.choice == 'Circle':
                self.canvas.my_create_oval(*self.arg)
            if self.choice == 'Trapezoid':
                self.canvas.my_trapezoid(*self.arg)
            if self.choice == 'Triangle':
                self.canvas.my_tringle(*self.arg)
            if self.choice in ['Square', 'Rectangle']:
                self.canvas.my_create_rectangle(*self.arg)
            self.canvas.place(relheight=1, relwidth=1)

    def get_info_messages(sefl):
        messagebox.showinfo(
            'INFO',
            '1. Select a shape in list\n2. Press button "selected shape"\n' +
            '3. Input data\n4. Press button "calculete"\n5. Press button "draw"'
        )
    
    def get_error_messages(self):
        messagebox.showerror(
            'ERROR',
            'Insert the number'
        )


class MyCanvas(tk.Canvas):

    def __init__(self, root):
        super().__init__(root)
        self.font = 'Helvetica 18'
        self.max_wight = 600 * .6
        self.max_hight = 500 * .7
        self.center = (self.max_hight // 2, self.max_wight // 2)

    def my_create_rectangle(self, height, width):
        height = height // 2 if height < self.max_hight else (self.max_hight - 10) // 2
        width = width // 2 if width < self.max_wight else (self.max_wight - 10) // 2
        self.create_rectangle(
            self.center[0] - height, self.center[1] - width,
            self.center[0] + height, self.center[1] + width,
            outline="#fb0", fill="red"   
        )
    
    def my_create_oval(self, radius):
        radius = radius  if radius < self.max_hight // 2 else (self.max_hight - 10) // 2
        self.create_oval(
            self.center[0] - radius, self.center[1] - radius,
            self.center[0] + radius, self.center[1] + radius,
            outline="#fb0", fill="red"   
        )

    def get_intercetions(self, x0, y0, r0, x1, y1, r1):
        # circle 1: (x0, y0), radius r0
        # circle 2: (x1, y1), radius r1

        d=((x1-x0)**2 + (y1-y0)**2) ** .5

        # non intersecting
        if d > r0 + r1 :
            return None
        # One circle within other
        if d < abs(r0-r1):
            return None
        # coincident circles
        if d == 0 and r0 == r1:
            return None
        else:
            a=(r0**2-r1**2+d**2)/(2*d)
            h=(r0**2-a**2) ** .5
            x2=x0+a*(x1-x0)/d   
            y2=y0+a*(y1-y0)/d   
            x3=x2+h*(y1-y0)/d     
            y3=y2-h*(x1-x0)/d 

            x4=x2-h*(y1-y0)/d
            y4=y2+h*(x1-x0)/d

            return (x3, y3, x4, y4)

    def my_tringle(self, side_a, side_b, side_c):
        self.create_polygon(
            self.center[0]-side_a//2, self.center[1],
            self.center[0]+side_a//2, self.center[1],
            self.get_intercetions(self.center[0]-side_a//2, self.center[1], side_b,
                                    self.center[0]+side_a//2, self.center[1], side_c)[0],
            self.get_intercetions(self.center[0]-side_a//2, self.center[1], side_b,
                                    self.center[0]+side_a//2, self.center[1], side_c)[1],
            outline="#fb0", fill="red"
        )

    def my_trapezoid(self, top_side: float, bottom_side: float,
                    left_side: float, right_side: float):
        self.create_polygon(
            self.center[0]+bottom_side, self.center[1],
            self.center[0]-bottom_side//2, self.center[1],

            self.get_intercetions(self.center[0]-bottom_side//2, self.center[1], left_side,
                                    self.center[0]-bottom_side//2+top_side, self.center[1], right_side)[0],
            self.get_intercetions(self.center[0]-bottom_side//2, self.center[1], left_side,
                                    self.center[0]-bottom_side//2+top_side, self.center[1], right_side)[1],
            self.get_intercetions(self.center[0]-bottom_side//2, self.center[1], left_side,
                                    self.center[0]-bottom_side//2+top_side, self.center[1], right_side)[0] + top_side,
            self.get_intercetions(self.center[0]-bottom_side//2, self.center[1], left_side,
                                    self.center[0]-bottom_side//2+top_side, self.center[1], right_side)[1],
        )

    def my_create_text(self):
        self.create_text(
            self.center[0], self.center[1], 
            text="Only 2D shapes",
            font=self.font
        )


if __name__ == '__main__':
    app = App()
    app.mainloop()
