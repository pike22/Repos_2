from .button_info import Button_Info
from Engine import Main_Node

class Button_Main(Main_Node):
	def __init__(self, buttonID, widgetID):
		Main_Node.__init__(self, info=Button_Info(buttonID))
		self.__widgID = widgetID
		print("any functions in gui_events that are related to the buttons here\n might need to be moved here, unless can't")
		print('in button_main.py')

	def Image_Data(self, fileLoc, tkImage, pilImage, size):
		self._info.Image_Data(	pilImage=pilImage,
		 						tkImage=tkImage,
								fileLoc=fileLoc,
								size=size
							)


	"""|--------------Getters--------------|#"""
	#this is where a list of getters will go...
	def get_widgID(self):
		return self.__widgID

	def get_tkImage(self):
		return self._info.get_tkImage()

	def get_pilImage(self):
		return self._info.get_pilImage()
