from tkinter import *
from .si_files import SI_Files
from .gui_events import GUI_Events
from .menu_events import Menu_Events

class Menu_Main():
	def __init__(self, mainApp, color):
		self.__color	= color
		self.__mainApp  = mainApp
		self.__mainMenu = Menu(mainApp)
		self.__Events	= Menu_Events()
		self.__eGUI 	= None
		self.__siFILES  = None

		"""#MENU TABS#"""
		self.__fileMenu = Menu(self.__mainMenu)
		self.__editMenu = Menu(self.__mainMenu)
		self.__nextMenu = Menu(self.__mainMenu)#place holder/quick copy

		mainApp.config(menu=self.__mainMenu)

	def Menu_SetUP(self, ):
		#calls the below methods to set up the menu.
		self.File_Menu()
		self.Edit_Menu()


	def File_Menu(self, ):
		self.__mainMenu.add_cascade(label='File', menu=self.__fileMenu)
		self.__fileMenu.add_command(label='--Maps--', )
		self.__fileMenu.add_command(label='New File' , command=self.__Events.New_File)
		self.__fileMenu.add_command(label='Open File', command=self.__siFILES.Read_File)
		self.__fileMenu.add_command(label='Save File', command=lambda:self.__siFILES.Save_File(self.__eGUI.get_imageDICT()))
		self.__fileMenu.add_command(label='--Buttons--')
		self.__fileMenu.add_command(label='New Button Set' ,)# command="")
		self.__fileMenu.add_command(label='Clear Button Set', command=self.__siFILES.Clear_ButtonSet)
		self.__fileMenu.add_command(label='Open Button Set', command=lambda:self.__siFILES.Clear_ButtonSet(True))
		self.__fileMenu.add_command(label='Save Button Set', command=lambda:self.__siFILES.Save_ButtonSet(self.__eGUI.get_buttonDICT()))
		self.__fileMenu.add_command(label='-----')
		self.__fileMenu.add_command(label='Exit', command=self.__mainApp.quit)

	def Edit_Menu(self, ):
		self.__mainMenu.add_cascade(label='Edit', menu=self.__editMenu)
		self.__editMenu.add_command(label='plcHOLD', )#command=COMMANDHERE)

	def Next_Menu(self): #place holder
		self.__mainMenu.add_cascade(label='next', menu=self.__nextMenu)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_eGUI(self, gui):
		self.__eGUI = gui

	def set_siFILES(self, siFILES):
		self.__siFILES = siFILES
