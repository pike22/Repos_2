from .placed_imageinfo import Placed_ImageInfo
from Engine.main_node import Main_Node
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import *

class Placed_ImageMain(Main_Node):
	def __init__(self, ID, buttonID):
		Main_Node.__init__(self, info=Placed_ImageInfo(ID, buttonID))

	def Image_Info(self, fileLoc, size, coords, rotation, canCollide=None):
		self._info.Image_Data(fileLoc=fileLoc, size=size)
		self._info.set_myCoords(coords)
		self._info.set_canCollide(canCollide)
		self._info.set_rotation(rotation)

	# def ...(self, ):
	# 	This will be for future functions that may need to be
	# 	Created.


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_
