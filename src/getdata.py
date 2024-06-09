# getdata.py

class GetData:
    def __init__(self):
        self.q_list = [None] * 4
        self.music = None

    def set_q_list(self,index:int,option:int):
        self.q_list[index]=option

    def get_q_list(self):
        return self.q_list
