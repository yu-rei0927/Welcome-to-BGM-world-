import tkinter as tk
from getdata import GetData

class Question(tk.Frame):
    def __init__(self, master=None, question_num=None, question=None, option0=None, option1=None):
        super().__init__(master)
        #self.question_num = question_num
        self.grid(row=0, column=0, sticky="nsew")

        # Load the background image
        self.background_image = tk.PhotoImage(file="background2.png")

        # Create a canvas and set the background image
        self.canvas = tk.Canvas(
            self,
            width=self.background_image.width(),
            height=self.background_image.height(),
        )
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)
        self.canvas.pack(fill="both", expand=True)

        # Create the label and buttons on the canvas
        self.label = tk.Label(
            self.canvas,
            text="~ Q{0} ~\n{1}".format(question_num+1, question),
            font=("Courier", "15"),
            foreground="black", 
            background="sandy brown", 
            justify="center", 
            height=4, 
            width=25, 
            wraplength=300,
            borderwidth=0,
        )
        self.label_window = self.canvas.create_window(
            self.canvas.winfo_width() // 2, 50, anchor="n", window=self.label
        )

        # ボタンを配置するためのフレームを作成
        self.button_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.button_frame_window = self.canvas.create_window(
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() - 70,  # Lowered by 30 pixels from -100 to -70
            anchor="s",
            window=self.button_frame,
        )

        # ボタンのサイズを統一
        button_width = 10
        button_height = 2

        # 各ボタンを作成してフレームに配置
        self.button1 = tk.Button(
            self.button_frame,
            text=option0,
            font=("Courier", "16"),
            width=button_width,
            height=button_height,
            command=lambda: self.scenechange1(),
        )
        self.button2 = tk.Button(
            self.button_frame,
            text=option1,
            font=("Courier", "16"),
            width=button_width,
            height=button_height,
            command=lambda: self.scenechange2(),
        )

        # ボタンにマウスイベントをバインド
        self.button1.bind("<Enter>", self.on_enter_no)
        self.button1.bind("<Leave>", self.on_leave_no)
        self.button2.bind("<Enter>", self.on_enter_yes)
        self.button2.bind("<Leave>", self.on_leave_yes)

        # ボタンを左右に並べる
        self.button1.grid(row=0, column=0, padx=10)
        self.button2.grid(row=0, column=1, padx=10)

        # Bind the canvas resize event to a method to update widget positions
        self.canvas.bind("<Configure>", self.on_resize)

    def on_enter_no(self, event):
        event.widget.config(bg="#a1ecbf")

    def on_leave_no(self, event):
        event.widget.config(bg="SystemButtonFace")

    def on_enter_yes(self, event):
        event.widget.config(bg="#ffcccc")

    def on_leave_yes(self, event):
        event.widget.config(bg="SystemButtonFace")

    def on_resize(self, event):
        # Update the positions of the widgets on the canvas
        self.canvas.coords(self.label_window, self.canvas.winfo_width() // 2, 50)
        self.canvas.coords(
            self.button_frame_window,
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() - 70,  # Lowered by 30 pixels from -100 to -70
        )

    def scenechange1(self, question_num, page):
        # main.pyでself.data = GetData()とし、質問画面からmaster.data.set_q_list(...)を呼び出す
        #data = GetData()
        #data.set_q_list(0,0)
        self.master.data.set_q_list(index=self.question_num, option=0)
        page.tkraise()

    def scenechange2(self, question_num, page):
        #data = GetData()
        #data.set_q_list(0,1)
        self.master.data.set_q_list(index=self.question_num, option=1)
        page.tkraise()
