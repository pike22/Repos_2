#imports
from PIL import ImageTk, Image
# from alpha import Alpha
from LevelDesigner import *
from z_Pictures import *
from colored import fg
from tkinter import *
from tkinter import filedialog
from Weapons import *
from Engine import *
from Entity import *
import keyboard
import mouse

class Alpha_LVD():
	BGcolor = 'Grey'
	def __init__(self, ):
		self.__screenWidth	 = 1280
		self.__screenHeight = 800
		self.__version	 = "Level Designer [ALPHAv0.5]"
		self.__color 	 = 'Grey'

		"""Class Call's"""
		self.__mainApp	= Tk()
		self.__cLogic	= Collision_Logic()
		self.__cNode	= Collision_Node(self.__cLogic)
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__iNode	= Image_Node() #NOTHING TO NOTE
		self.__kNode	= Kinetics_Node()
		self.__mainMenu = Menu_Main(self.__mainApp, self.__color)
		self.__GUI		= GUI_Main(self.__cLogic, self.__iNode, self.__cNode, self.__mainApp, 'Grey', self.__mainMenu)

		"""Widget Names"""
		#frames
		self.__projWindow = None
		self.__imageList  = None

		#buttons
		self.__Import = None

		"""Variables"""
		#Wumpas = None
		self.__t = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth+260) + 'x' + str(self.__screenHeight))
		self.__mainMenu.Menu_SetUP()

	def set_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__screenHeight, self.__screenWidth, color=self.__color)

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.quit()

	def GUI_run(self):
		self.__GUI.windowSETUP()
		self.__GUI.gridSETUP(True)

	def windowLoop(self):

		#closes the window
		self.close_window()

		#--------------------------#
		#-more might be added soon-#
		#--------------------------#


		#repeats the func after so long
		self.__mainApp.after(int(self.__tNode.get_FPS()), self.windowLoop)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp

	def get_projWindow(self):
		return self.__projWindow

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...



print('\n-------Initial Set UP--------\n')
LVD = Alpha_LVD()
LVD.tk_windowSETUP()
LVD.set_MainCanvas()
LVD.GUI_run()
print('\n-----Level Designer Loop-----\n')
LVD.windowLoop()
LVD.get_mainAPP().mainloop()
print('\n')
print('<------------------------------->')
print('<--------------END-------------->')
print('<------------------------------->')
