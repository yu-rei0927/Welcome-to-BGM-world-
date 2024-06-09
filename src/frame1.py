#frame1.py
import tkinter as tk
from getdata import GetData
from question import Question

class Frame_1(Question):
	def __init__(self, master=None):
		self.question_num = 1  # ここ
		self.master=master  # ここ
		question = '今しているのはクリエイティブな事ですか。'  # ここ
		option0 = "はい"  # ここ
		option1 = "いいえ"  # ここ
		super().__init__(	question_num=self.question_num,
							question=question,
							option0=option0, 
							option1=option1)

	def scenechange1(self):
		self.master.data.set_q_list(index=self.question_num, option=0)
		self.master.frame2.tkraise()  # ここ

	def scenechange2(self):
		self.master.data.set_q_list(index=self.question_num, option=1)
		self.master.frame2.tkraise()  # ここ