import tkinter as tk

class Frame_Rule(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        img = tk.PhotoImage(file='background2.png')
        bg = tk.Label(self, image=img)
        bg.image = img
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        app_name = tk.Label(self, 
                            text='使い方', 
                            font=("MS ゴシック", "25"), 
                            bg="sandy brown")
        app_name.pack(pady=30)

        usage = tk.Message(self,
                           aspect=1000,
                           text='1.ホーム画面で「START」をクリック\n2.質問に答えていく\n3.貴方に合った音楽を再生',
                           font=("MSゴシック", "10"),
                           bg="sandy brown")
        usage.pack()

        button0 = tk.Button(self,
                            text='START',
                            font=("MS ゴシック", "25"),
                            command=lambda: self.scenechange(master.frame0),
                            bg="sandy brown")
        button0.pack(pady=30)

    def scenechange(self, page):
        page.tkraise()