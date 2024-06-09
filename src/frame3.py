import tkinter as tk
from getdata import GetData
from question import Question

class Frame_3(Question):
	def __init__(self, master=None):
		self.question_num = 3  # ここ
		self.master=master
		question = '今焦っている状況ですか？'  # ここ
		option0 = "焦っている"  # ここ
		option1 = "焦っていない"  # ここ
		super().__init__(	question_num=self.question_num,
							question=question,
							option0=option0, 
							option1=option1)

	def scenechange1(self):
		self.master.data.set_q_list(index=self.question_num, option=0)
		print("q_list:", self.master.data.q_list)  # テスト用
		self.master.framemusic.tkraise()  # ここ

	def scenechange2(self):
		self.master.data.set_q_list(index=self.question_num, option=1)
		print("q_list:", self.master.data.q_list)  # テスト用
		self.master.framemusic.tkraise()  # ここ

