from .image_node import Image_Node

class Info_Node():
	def __init__(self, ID=None, groupID=None, buttonID=None):
		#---Tkinters_Parameters---#
		self._ID		= ID		#Individual Tag
		self._groupID	= groupID	#Groups Tag
		self._buttonID	= buttonID	#Buttons Individual Tag
		self._myCorners	= None #(x1, y1, x2, y2)
		self._myCoords	= None #(x, y)
		self._pilImage	= None
		self._rotation	= None
		self._tkImage	= None
		self._fileLoc	= None
		self._size		= None #(width, height)

		#---Games_Parameters---#
		self._baseDefense	= None
		self._baseHealth	= None
		self._baseAttack	= None
		self._durability	= None
		self._rarity		= None
		self._speed			= None

	def Image_Data(self, size=None, pilImage=None, tkImage=None, fileLoc=None):
		self._pilImage	= pilImage
		self._tkImage	= tkImage
		self._fileLoc	= fileLoc
		self._size		= size


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_ID(self):
		return self._ID

	def get_groupID(self):
		return self._groupID

	def get_buttonID(self):
		return self._buttonID

	def get_myCorners(self):
		return self._myCorners

	def get_myCoords(self):
		return self._myCoords

	def get_pilImage(self):
		return self._pilImage

	def get_tkImage(self):
		return self._tkImage

	def get_rotation(self):
		return self._rotation

	def get_fileLoc(self):
		return self._fileLoc

	def get_size(self):
		return self._size

	def get_durability(self):
		return self._durability

	def get_rarity(self):
		return self._rarity

	def get_speed(self):
		return self._speed

	#-Attack, health, defense_#
	def get_attack(self):
		return self._baseAttack

	def get_health(self):
		return self._baseHealth

	def get_defense(self):
		return self._baseDefense



	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_rotation(self, rotation):
		self._rotation = rotation

	def set_canCollide(self, yes):
		self._canCollide = yes

	def set_myCorners(self, objectName):
		if Image_Node.Render.bbox(objectName) != None:
			self._myCorners = Image_Node.Render.bbox(objectName)
		else:
			self._myCorners = objectName

	def set_myCoords(self, coords):
		self._myCoords = coords

	def set_tkImage(self, tkImage):
		self._tkImage = tkImage

	def set_rarity(self, rarity):
		self._rarity = rarity

	def set_speed(self, speed):
		self._speed = speed
