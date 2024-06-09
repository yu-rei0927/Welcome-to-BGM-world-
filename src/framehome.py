import tkinter as tk


class Frame_Home(tk.Frame):
    def __init__(self, master=None):
        
        super().__init__(master)

        #backgraound
        img = tk.PhotoImage(file="background2.png")
        bg = tk.Label(self, image=img)
        bg.image = img
        bg.place(x=0, y=0)


        
        #タイトル
        label0 = tk.Label(self, text='ようこそBGMの世界へ!!', font=("MSゴシック", "20"), bg="sandy brown", fg="white")
        label0.pack(pady=40)

        #説明
        button0 = tk.Button(self, text='説明', font=("MSゴシック", "15"), command=lambda: self.scenechange(master.framerule), bg="sandy brown", fg="white")
        button0.pack()

        #質問1へ
        button1 = tk.Button(self, text='質問にいく', font=("MSゴシック", "15"), command=lambda: self.scenechange(master.frame0), bg="sandy brown", fg="white")
        button1.pack()

        #終わる
        buttonex = tk.Button(self, text='終わる', font=("MSゴシック", "10"), command=lambda: master.destroy(), bg="sandy brown", fg="white")
        buttonex.pack(pady=20)

        
        


    def scenechange(self, page):
        page.tkraise()
