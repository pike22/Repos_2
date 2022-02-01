from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow

#__Render == Canvas

class Image_Node():
	Render = None
	def __init__(self):
		self.__gridSizeX = 64
		self.__gridSizeY = 64
		self.__imageList    = [] #0 = PIL_img | #1 = size | #2 = TK_img
		self.__placedImage  = None #this will replace the list varient
		self.__placedCoord  = None #this will replace the list varient

	def Image_Add(self, img_Location):
		#takes in the initail img
		self.__imageList = []
		PIL_img = Image.open(str(img_Location))
		self.__imageList.append(PIL_img)
		self.__imageList.append(PIL_img.size)

		#converts im to an ImageTk
		self.__imageList.append(ImageTk.PhotoImage(PIL_img))
		#Eventually a method of storage will be implimented

		## NOTE: self.Img_list == [PIL, size, TK image] in order of 0, 1, 2
		# print(self.__imageList, 'PIL_img | size | TK_img')
		return self.__imageList

	def Image_Rotate(self, pilImg, angle, LVD=False):
		# angle %= angle
		if LVD == True:
			pilImg = pilImg.rotate(angle, Image.NEAREST)
			tkImg  = ImageTk.PhotoImage(pilImg)
			return tkImg
		else:
			pilImg = pilImg.rotate(angle, Image.NEAREST)
			tkImg  = ImageTk.PhotoImage(pilImg)
			return tkImg

	def Image_Place(self, x, y, image, LVD='no', tag=None): # !!returns a tuple!! #Tag needs to be a list
		if LVD == 'no':
			canvasID = Image_Node.Render.create_image((x, y), image=image, anchor="nw")
			if tag != None:
				if len(tag) > 1:
					for item in range(len(tag)):
						Image_Node.Render.addtag_withtag(tag[item], canvasID)
				else:
					Image_Node.Render.addtag_withtag(tag, canvasID)
			self.__placedImage = canvasID
			self.__placedCoord = (x, y)
			#Why does this need to return anything? maybe the canvasID, that would be it.
			# return self.__placedCoord

		elif LVD != 'no': #this is for the level designer
			canvasID = Image_Node.Render.create_image((x, y), image=image, anchor="nw")
			if tag != None:
				if len(tag) > 1:
					for item in range(len(tag)):
						Image_Node.Render.addtag_withtag(tag[item], canvasID)
				else:
					Image_Node.Render.addtag_withtag(tag, canvasID)
			self.__placedImage = canvasID
			self.__placedCoord = (x, y)
			#Why does this need to return anything? maybe the canvasID, that would be it.
			# return self.__placedImage


	def Create_Canvas(self, mainApp, height, width, color='Grey'):
		Image_Node.Render = Canvas(mainApp, height=height, width=width, bg=str(color))
		Image_Node.Render.grid(row=0, column=0, rowspan=10)
		Image_Node.Render.grid_propagate(0)
