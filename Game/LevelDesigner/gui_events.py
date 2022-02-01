import re
import os
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .placed_imagemain import Placed_ImageMain

class GUI_Events():
	def __init__(self, iNode, cLogic, mainApp, color):
		self.__columnMax = 4
		self.__column = 0
		self.__rowMax = 10
		self.__row	  = 1

		#other classes
		self.__mainApp	= mainApp
		self.__cLogic	= cLogic
		self.__iNode	= iNode
		self.__color	= color
		self.__kNode	= Kinetics_Node()

		#GUI vars
		self.__isIMG		= False
		self.__isDrag		= False
		self.__isRotate		= False
		self.__isMoving		= False
		self.__hoverWidget	= None
		self.__hoverSquare	= None
		self.__lastRotate	= 0
		self.__gridCoords	= []
		self.__gridCorners	= []

		self.__mapFiles = 'E:\Github\Repos_2\Game\levelDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Repos_2\Game\z_Pictures\Walls'

		'''#_IMAGE VARIABLES_#'''
		#Button Vars
		self.__buttonCount	= 0
		self.__buttonDICT	= {}

		#PLC_images
		self.__placedImagesTK	= [] #List for tkinter
		self.__placedImages 	= [] #Organizational reasons
		self.__imageDICT			= {}
		self.__IDcount			= 0
		self.__CurIMG			= None
		self.__tkIMG			= None


		#RAND VARS
		#self.var = None

	def Create_Button(self, parent):
		filetypes = (("PNG", "*.png"), ("All Files", "*.*"))
		file = filedialog.askopenfilename(title='Picture Import', filetypes=filetypes, initialdir=self.__pngFiles)
		if file == '':
			print('No File Selected')
		newFile = re.search('.*/(.*/.*/.*$)', file)
		if newFile != None:
			file = newFile.group(1)
		else:
			return

		#Create Buttons Name
		if self.__buttonCount <= 9:
			button_ID = 'LVD#B00'+str(self.__buttonCount)
		elif self.__buttonCount > 9 and self.__buttonCount <= 99:
			button_ID = 'LVD#B0'+str(self.__buttonCount)
		elif self.__buttonCount > 99 and self.__buttonCount <= 999:
			button_ID = 'LVD#B'+str(self.__buttonCount)
		else:
			print('ERROR: To Manny Buttons')
		self.__buttonCount += 1
		print(button_ID)

		#Create Button
		image = self.__iNode.Img_Add(file)
		widget_ID = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.Drag_Drop(button_ID))
		self.__buttonDICT[button_ID] = Button_Main(button_ID, widget_ID)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=file, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		widget_ID.grid(row=self.__row, column=self.__column)
		if self.__column <= self.__columnMax:
			self.__column += 1
		else:
			self.__column = 0
			self.__row	  +=1

	def Drag_Drop(self, button_ID):
		if self.__isDrag == False:
			print("!#_ON_#!")
			self.__isDrag = True
			self.__CurIMG = self.__iNode.Img_Place(-50, -50, image=self.__buttonDICT[button_ID].get_tkIMG(), LVD='yes')
			self.__mainApp.bind(('<Motion>'), lambda event, arg=button_ID: self.Move_Image(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=button_ID: self.Rotate_Image(event, arg))
		else:
			print('!#_OFF_#!')
			self.__isDrag = False
			self.__isRotate = False
			self.__lastRotate = 0
			self.__tkIMG	= None
			Image_Node.Render.delete(self.__CurIMG)
			self.__mainApp.unbind(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))
			Image_Node.Render.unbind(('<Button-1>'))


	def Rotate_Image(self, event, button_ID):
		self.__lastRotate += 90
		if self.__lastRotate == 360:
			self.__lastRotate = 0
		self.__isRotate = True
		oldIMG = self.__CurIMG
		self.__tkIMG = self.__iNode.Img_Rotate(self.__buttonDICT[button_ID].get_pilIMG(), self.__lastRotate)
		x, y = self.__gridCoords[self.__hoverSquare]
		self.__CurIMG = self.__iNode.Img_Place(x, y, self.__tkIMG, LVD='yes')
		Image_Node.Render.delete(oldIMG)

	def Move_Image(self, event, button_ID):
		self.__isMoving = True
		self.Find_Square(event)
		self.Find_Widget()

		if self.__hoverWidget == Image_Node.Render:
			if self.__isDrag == True:
				canvID = Image_Node.Render.find_withtag(self.__CurIMG)[0]
				x, y = self.__gridCoords[self.__hoverSquare]
				Image_Node.Render.coords(canvID, x, y)
				Image_Node.Render.bind(('<Button-1>'), lambda event, arg=button_ID: self.Place_Image(event, arg))

	def Place_Image(self, event, button_ID):
		self.Del_Image(event)
		if self.__IDcount <= 9:
			ID = 'LVD#W000'+str(self.__IDcount)
		elif self.__IDcount > 9 and self.__IDcount <= 99:
			ID = 'LVD#W00'+str(self.__IDcount)
		elif self.__IDcount > 99 and self.__IDcount <= 999:
			ID = 'LVD#W0'+str(self.__IDcount)
		elif self.__IDcount > 999 and self.__IDcount <= 9999:
			ID = 'LVD#W'+str(self.__IDcount)
		else: #add more elif's above if needed
			print('ERROR: To Manny Walls')
		self.__IDcount += 1

		self.Find_Square(event)
		x, y = self.__gridCoords[self.__hoverSquare]

		self.__placedImages.append(ID)
		self.__placedImagesTK.append(self.__tkIMG)
		self.__imageDICT[ID] = PLC_ImgMain(ID, button_ID)
		self.__imageDICT[ID].Image_Info(self.__buttonDICT[button_ID].get_fileLoc(),
									  self.__buttonDICT[button_ID].get_Size(),
									  (x, y), self.__lastRotate)
		if self.__tkIMG == None:
			self.__tkIMG = self.__buttonDICT[button_ID].get_tkIMG()

		self.__iNode.Img_Place(x, y, self.__tkIMG, LVD='yes', tag=[ID, self.__imageDICT[ID].get_group_ID()])

	def Find_Image(self):
		if self.__isIMG == False:
			print("!#_ON_#!")
			self.__isIMG = True
			self.__mainApp.bind_all("((<Button-1>))", self.Find_imgTag)
		else:
			print('!#_OFF_#!')
			self.__isIMG = False
			self.__mainApp.unbind_all("((<Button-1>))")

	def Find_ImageTag(self, event):
		self.Find_Square(event)

		x1, y1, x2, y2 = self.__gridCorners[self.__hoverSquare]
		Canvas_ID = Image_Node.Render.find_overlapping(x1+5, y1+5, x2-5, y2-5)
		ID == Image_Node.find_withtag(Canvas_ID)
		print(ID)

	def Map_Wipe(self):
		item = len(self.__placedImages)-1
		while self.__placedImages != []:
			item -= 1
			if item == 0:
				item = len(self.__placedImages)-1
			ID = Image_Node.Render.find_withtag(self.__placedImages[item])
			if ID != ():
				print(self.__placedImages[item])
				Image_Node.Render.delete(self.__placedImages[item])
				del self.__imageDICT[self.__placedImages[item]]
				del self.__placedImages[item]
			print(self.__placedImages)


	def Del_Image(self, event):
		self.Find_Square(event)

		x1, y1, x2, y2 = self.__gridCorners[self.__hoverSquare]
		Canvas_ID = Image_Node.Render.find_overlapping(x1+5, y1+5, x2-5, y2-5)
		ID = None
		if self.__placedImages != []:
			for item in range(len(self.__placedImages)-1, -1, -1):
				ID = Image_Node.Render.find_withtag(self.__placedImages[item])
				if ID != ():
					for tuple in Canvas_ID:
						if ID[0] == tuple:
							print(self.__placedImages[item])
							Image_Node.Render.delete(self.__placedImages[item])
							del self.__imageDICT[self.__placedImages[item]]
							del self.__placedImages[item]

	def Del_File(self):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Select to Be Deleted', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		os.remove(file)
		print(file, ':File Removed')

	def PASS(self):
		pass

	def Find_Widget(self):
		x, y = self.__mainApp.winfo_pointerxy()
		self.__hoverWidget = self.__mainApp.winfo_containing(x, y)

	def Find_Square(self, event):
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__gridCorners)):
			if event.x > self.__gridCorners[item][0] and event.y > self.__gridCorners[item][1]:
				if event.x < self.__gridCorners[item][2] and event.y < self.__gridCorners[item][3]:
					self.__hoverSquare = item


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imageDICT(self):
		return self.__imageDICT

	def get_buttonDICT(self):
		return self.__buttonDICT

	def get_grid(self):
		return self.__gridCorners


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_gridSETUP(self, grid, coord):
		self.__gridCorners = grid #The Corners of an availible square in the grid.
		self.__gridCoords = coord #The Coords of an availible square in the grid.

	def set_imageDICT(self, dict):
		self.__imageDICT = dict

	def set_buttonDICT(self, dict):
		self.__buttonDICT = dict

	def set_RowColumn(self, row, column):
		self.__column = column
		self.__row 	  = row

	def set_buttonCount(self, count):
		self.__buttonCount = count

	#SUBJECT TO CHANGE
	def File_Images(self, buttonDICT, imageDICT, placedImages, placedImagesTK, buttonCount, IDcount):
		self.__placedImagesTK = placedImagesTK
		self.__placedImages	  = placedImages
		self.__buttonCount	  = buttonCount
		self.__buttonDICT	  = buttonDICT
		self.__IDcount		  = IDcount
		self.__imageDICT		  = imageDICT
