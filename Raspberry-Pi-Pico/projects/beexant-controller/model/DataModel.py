from itertools import count
from pyclbr import Class
import this
from typing_extensions import Self

class DataModel:
    def __init__(self,count):
        self.count=count
    
    @property
    def counter(self):
        self.count +=1