import tkinter as tk
import pygame.mixer as pgm


class Frame_Music(tk.Frame):
    def __init__(self, master=None):
        pgm.init()
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        img = tk.PhotoImage(file='background2.png')
        bg = tk.Label(self, image=img, bg='sandy brown', fg='white')
        bg.image = img
        bg.place(x=0, y=0)
        self.flg=0

        self.dic = {
            '00000': 'ヴィヴァルディ_「四季」より「春」第1楽章',
            '00001': 'バッハ_ゴルトベルク変奏曲',
            '00010': 'モーツァルト_ディヴェルティメント K.136第一楽章',
            '00011': 'ヨハン・シュトラウス2世_美しく青きドナウ',
            '00100': 'モーツァルト_ピアノソナタ第11番 イ長調 K.331 - 第3楽章「トルコ行進曲」',
            '00101': 'バッハ_平均律クラヴィーア曲集 第1巻 プレリュード第1番 ハ長調 BWV 846',
            '00110': 'モーツァルト_交響曲第40番 第4楽章「アレグロ・アッサイ」',
            '00111': 'バッハ_無伴奏チェロ組曲 第1番 ト長調 BWV 1007',
            '01000': 'ベートーヴェン_行進曲 第6番田園第1楽章',
            '01001': 'ベートーヴェン_交響曲第7番 イ長調作品92第2楽章アレグレット',
            '01010': 'ヘンデル_水上の音楽第2曲 アラホーンパイプ',
            '01011': 'ラヴェル_ボレロ',
            '01100': 'ベートーヴェン_ピアノソナタ14番',
            '01101': 'ショパン_ノクターン第2番 変ホ長調 作品9-2',
            '01110': 'ショパン_ワルツ 第7番 嬰ハ短調 Op.64-2',
            '01111': 'サティ_ジムノペディ 第1番'
        }
        self.music=None

       
        label0 = tk.Label(self, text='再生画面', font=("MSゴシック", "40"), bg='sandy brown', fg='white')
        label0.pack(pady=30)
        self.label1 = tk.Label(self, text='music', font=("MSゴシック", "15"), bg='sandy brown', fg='white',wraplength=350)
        self.label1.pack()
        buttonpl = tk.Button(self, text='再生', font=("MSゴシック", "20"), command=lambda: self.musicstart(), bg='sandy brown', fg='white')
        buttonpl.pack(side=tk.LEFT, padx=50)
        buttonpa = tk.Button(self, text='停止', font=("MSゴシック", "20"), command=lambda: self.music.stop(), bg='sandy brown', fg='white')
        buttonpa.pack(side=tk.RIGHT, padx=50)

        button = tk.Button(self, text='戻る', font=("MSゴシック", "20"), command=lambda: self.scenechange(master.framehome), bg='sandy brown', fg='white')
        button.pack(side=tk.BOTTOM, pady=30)

    def musicstart(self):
        if self.flg==0:
            self.qi = self.master.data.q_list
            self.q = '0'
            for i in range(len(self.qi)):
                self.q += str(self.qi[i])

            self.music = pgm.Sound('music/{}.mp3'.format(self.dic[self.q]))
            self.flg=1


        self.music.play(loops=-1)
        self.label1.config(text=self.dic[self.q])

    


    def scenechange(self, page):
        self.flg=0
        page.tkraise()
        self.music.stop()
        self.label1.config(text='music')
        
