import re
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .placed_imagemain import Placed_ImageMain

#for save and import information
class SI_Files():
	def __init__(self, iNode, mainApp, color, eGUI):
		#class Calls
		self.__mainApp = mainApp
		self.__iNode = iNode
		self.__color = color
		self.__eGUI  = eGUI

		#SI_FILES VARS
		self.__columnMax = 4
		self.__column = 0
		self.__rowMax = 10
		self.__row	  = 1

		self.__imageFrame	= None
		self.__saveLevel	= None
		self.__importLevel	= None

		self.__mapFiles = 'E:\Github\Repos_2\Game\LevelDesigner\MapSave_Files'
		self.__loadFile = 'E:\Github\Repos_2\Game\LevelDesigner\ButtonSet_Files'
		self.__pngFiles = 'E:\Github\Repos_2\Game\z_Pictures\Walls'

		#WRITE FILE VARS
		self.__buttonDICT = {} #this is for the buttons
		self.__imageDICT  = {} #this is for the images

		'''#READ FILE VARS'''

		#imageVARS
		self.__placedImageTag = []
		self.__placedImageTK  = []

		#mapSaves
		self.__imageFileID	= []
		self.__imageFileLoc	= {}
		self.__imageFileRot	= {}
		self.__imageFilePos	= {}

		#buttonSaves
		self.__buttonFileID  = []
		self.__buttonFileLoc = {}

		#OTHER VARS
		self.list 		   = [] #when in need of a random list, clear before use.
		self.__tkImage	   = None
		self.__isRotate	   = False
		self.__stepCount   = 0
		self.__lastRotate  = 0
		self.__imageCount  = 1
		self.__buttonCount = 1


	def Save_File(self, imageDICT):
		self.__imageDICT = imageDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)
		if file == '' or file == None:
			print('No File Selected')
			return

		self.__saveLevel = open(str(file.name), 'w')

		self.__stepCount = 0
		self.Save_Line(file=self.__saveLevel, funct=self.Save_List, dict=self.__imageDICT)
		self.Save_Line(file=self.__saveLevel, funct=self.Save_Dict, dict=self.__imageDICT)
		self.Save_Line(file=self.__saveLevel, funct=self.Save_Dict, dict=self.__imageDICT)
		self.Save_Line(file=self.__saveLevel, funct=self.Save_Dict, dict=self.__imageDICT)

		self.__saveLevel.close() #DON'T FORGET ABOUT THIS

	def Read_File(self, mainGame=None):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		if mainGame == None:
			file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
			if file == '':
				print('No File Selected')
				return
			self.__importLevel = open(file, 'r')
		else:
			self.__importLevel = open(mainGame, 'r')

		self.__stepCount = 0
		self.__imageFileID 	 = []
		self.__imageFileLoc   = {}
		self.__imageFileRot   = {}
		self.__imageFilePos   = {}
		#clear all list/dict used below
		self.Read_Line(file=self.__importLevel, funct=self.Read_List, listName=self.__imageFileID)
		self.Read_Line(file=self.__importLevel, funct=self.Read_Dict, fileTypes='LVD Maps')
		self.Read_Line(file=self.__importLevel, funct=self.Read_Dict, fileTypes='LVD Maps')
		self.Read_Line(file=self.__importLevel, funct=self.Read_Dict, fileTypes='LVD Maps')

		self.__importLevel.close()
		self.File_ToLevel(mainGame)
		#this splits for easy use of the second half during boot up

	#Takes the info read from files and actually creates the games side of them.
	def File_ToLevel(self, mainGame):
		# print(self.__imageFileID)
		# print(self.__imageFileLoc)
		# print(self.__imageFileRot)
		# print(self.__imageFilePos)
		for tag in self.__imageFileID:
			#PULLS IN IMAGE AND ROTATES IF NEEDED
			image = self.__iNode.Image_Add(self.__imageFileLoc[tag])
			tkImage = self.__iNode.Image_Rotate(image[0], int(self.__imageFileRot[tag]))

			#COORDS & CORNERS FROM FILE
			coord = self.__imageFilePos[tag]
			firstNumb = re.search("([0-9]*[^(,)])", coord)
			if firstNumb != None:
				new_firstNumb = firstNumb.group(1)
			secondNumb = re.search(str(new_firstNumb)+", ([0-9]*[^(,)])", coord)
			if secondNumb != None:
				new_secondNumb = secondNumb.group(1)
			x = int(new_firstNumb)
			y = int(new_secondNumb)
			self.__imageFilePos[tag] = (x, y)

			#PLACES THE IMAGES
			self.__imageDICT[tag] = Placed_ImageMain(tag, None)
			self.__imageDICT[tag].Image_Info(self.__imageFileLoc[tag], image[1], (x, y), self.__imageFileRot[tag])
			self.__iNode.Image_Place(x, y, tkImage, tag=[tag, self.__imageDICT[tag].get_groupID()])
			self.__placedImageTag.append(tag)
			self.__placedImageTK.append(tkImage)


		#INFO TO GUI_EVENT
		if self.__imageFileID != []:
			lastID  = re.search("^LVDW#(.{4})", self.__imageFileID[-1])
			lastID2 = lastID.group(1)
			self.__imageCount += int(lastID2)+1

		# lastBID  = re.search("^LVDB#(.{4})", self.__bIDfile[len(self.__bIDfile)-1])
		# lastBID2 = lastBID.group(1)
		# self.__buttonCount += int(lastBID2)+1

		self.__eGUI.File_Images(self.__buttonDICT, self.__imageDICT, self.__placedImageTag, self.__placedImageTK, self.__buttonCount, self.__imageCount)
		self.__eGUI.set_RowColumn(self.__row, self.__column)



	def Save_ButtonSet(self, buttonDICT):
		self.__buttonDICT = buttonDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Load Out', filetypes=filetype, defaultextension=filetype, initialdir=self.__loadFile)
		if file == '':
			print('No File Selected')
			return
		self.__saveButton = open(str(file.name), 'w')

		self.__stepCount = 0
		self.Save_Line(self.__saveButton, self.Save_List, self.__buttonDICT)
		self.Save_Line(self.__saveButton, self.Save_Dict, self.__buttonDICT)

		self.__saveButton.close() #DON'T FORGET ABOUT THIS
	def Clear_ButtonSet(self, change=False): #make this a clean only, add parameter to switch between (clear only) and (clear then new)
		#this clears the current buttons to make way for the new set.
		for widget in self.__imageFrame.grid_slaves():
			widget.destroy()
		self.__buttonDICT.clear()
		self.__row = 0
		self.__column = 0
		self.__buttonCount = 0

		if change == True:
			self.Read_ButtonSet()
		#this splits for easy use of the second half during boot up

	def Read_ButtonSet(self, DefaultBS=None):
		if DefaultBS == None:
			filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
			file = filedialog.askopenfilename(title='Button Import', filetypes=filetypes, initialdir=self.__loadFile)
			if file == '':
				print('No File Selected')
				return
			else:
				self.__importButtons = open(file, 'r')
		else:
			self.__importButtons = open(DefaultBS, 'r')

		#clear all list/dict used below
		self.__stepCount 	 = 0
		self.__buttonFileID	 = []
		self.__buttonFileLoc = {}
		#this reads the file and puts the data into lists/dictionaries.
		self.Read_Line(file=self.__importButtons, funct=self.Read_List, listName=self.__buttonFileID)
		self.Read_Line(file=self.__importButtons, funct=self.Read_Dict, fileTypes='Button Sets')

		self.__importButtons.close()

		#this creates the button set from the created dictionaries and lists.
		for tag in self.__buttonFileID:
			# print(tag, 'button')

			#CREATES BUTTON FROM SAVE FILE
			self.Create_Button(self.__buttonFileLoc[tag], self.__imageFrame, buttonID=tag)
			# print(self.__buttonFileLoc[tag])

		if self.__buttonFileID != []:
			lastBID  = re.search("^LVDB#(.{3})", self.__buttonFileID[-1])
			lastBID2 = lastBID.group(1)
			self.__buttonCount += int(lastBID2)+1

			# print(self.__buttonCount, 'button id #')
			self.__eGUI.set_buttonCount(self.__buttonCount)

	'''<========================================================================>
	#*************************#ShortCut functions#******************************#
	<========================================================================>'''
	def Create_Button(self, fileLoc, parent, buttonID, mainGame=None):
		image = self.__iNode.Image_Add(fileLoc)
		if mainGame == None:
			widgetID = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.__eGUI.Drag_Drop(buttonID))
		else:
			widgetID = None
		self.__buttonDICT[buttonID] = Button_Main(buttonID, widgetID)
		self.__buttonDICT[buttonID].Image_Data(fileLoc=fileLoc, tkImage=image[2], pilImage=image[0], size=image[1])

		#Place Button
		if mainGame == None:
			widgetID.grid(row=self.__row, column=self.__column)
			if self.__column <= self.__columnMax:
				self.__column += 1
			else:
				self.__column = 0
				self.__row	  +=1
			self.__eGUI.set_RowColumn(column=self.__column, row=self.__row)
		self.__eGUI.set_buttonDICT(self.__buttonDICT)

	'''===================READ LINE function==================='''
	#fileType is defaulted in the function called before this one
	def Read_List(self, curLine, listName):
		listName.append(curLine)

	#fileType is defaulted in the function called before this one
	def Read_Dict(self, curLine, step, type):
		if type == 'LVD Maps':
			if re.search("(^LVDW#.{4})", curLine) != None:
				if step == 1:
					if re.search("=(.*/.*/.*$)", curLine) != None:
						self.__imageFileLoc[re.search("(^LVDW#.{4})", curLine).group(1)] = re.search("=(.*/.*/.*$)", curLine).group(1)
						# print(self.__imageFileLoc)
				elif step == 2:
					if re.search("=z(.*$)", curLine) != None:
						self.__imageFileRot[re.search("(^LVDW#.{4})", curLine).group(1)] = re.search("=z(.*$)", curLine).group(1)
						# print(self.__imageFileRot)
				elif step == 3:
					if re.search("=z(.*$)", curLine) != None:
						self.__imageFilePos[re.search("(^LVDW#.{4})", curLine).group(1)] = re.search("=z(.*$)", curLine).group(1)
						# print(self.__imageFilePos)
		else:
			if re.search("(^LVDB#.{3})", curLine) != None:
				if step == 1:
					if re.search("=(.*/.*/.*$)", curLine) != None:
						self.__buttonFileLoc[re.search("(^LVDB#.{3})", curLine).group(1)] = re.search("=(.*/.*/.*$)", curLine).group(1)

	def Read_Line(self, file, funct, fileTypes=None, listName=None):
		for line in file:
			line = line.rstrip('\n')
			# print(line)

			step = re.search("(^<.*$)", line)
			if step != None:
				self.__stepCount += 1
				# print('step:', self.__stepCount)
				return
			else:
				if self.__stepCount == 0:
					if line != '':
						if listName != None:
							funct(line, listName)
				elif self.__stepCount == 1 or self.__stepCount == 2 or self.__stepCount == 3:
					if line != '':
						if fileTypes != None:
							funct(line, self.__stepCount, fileTypes)
				# print(line)

	def Save_List(self, file, key):
		info = str(key)+'\n'
		file.write(info)
		if key == self.list[-1]:
			print('lastKEY', key)
			self.__stepCount += 1
			return

	def Save_Dict(self, file, key, dict, step):
		# print('saveDICT call', key)
		#Location
		if step == 1:
			info = str(key)+'='+str(dict[key].get_fileLoc())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY', key)
				self.__stepCount += 1
				return
		#Rotation
		elif step == 2:
			info = str(key)+'=z'+str(dict[key].get_rotation())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return
		#Position
		elif step == 3:
			info = str(key)+'=z'+str(dict[key].get_myCoords())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return

	def Save_Line(self, file, funct, dict):
		for key in dict.keys():
			self.list.append(key)
		for key in dict.keys():
			# print('step:', self.__stepCount)
			if self.__stepCount == 0:
				funct(file, key)
			else:
				funct(file, key, dict, self.__stepCount)
		file.write('\n<=======================================================>\n\n')

	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imageDICT(self):
		return self.__imageDICT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_imageFrame(self, frame):
		self.__imageFrame = frame
