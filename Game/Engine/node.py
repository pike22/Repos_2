from .kinetics_node import Kinetics_Node

#Parent: None
#Children:
	#PathFind_Node
	#Main_Node

class Node():
	def __init__(self, mainApp=None, cLogic=None, cNode=None, iNode=None, tNode=None, pfNode=None):
		#---Classes---#
		"""#The Classes that the objects need#"""
		self._mainApp = mainApp
		self._pfNode = pfNode
		self._cLogic = cLogic
		self._cNode  = cNode
		self._iNode  = iNode
		self._tNode  = tNode
		self._kNode  = Kinetics_Node()

	# def yes(self, ):
	# 	stuffs

	def Create_ObjectName(self, acronym, numb, LVLD=False):
		if LVLD == True:
			if numb <= 9:
				ID = str(acronym)+"#000"+str(numb)
			elif numb > 9 and numb <= 99:
				ID = str(acronym)+"#00"+str(numb)
			elif numb > 99 and numb <= 999:
				ID = str(acronym)+"#0"+str(numb)
			elif numb > 999 and numb <= 9999:
				ID = str(acrounym)+"#"+str(numb)
			else:
				print('To manny!!')
			# print(ID)
			return ID
		else:
			if numb <= 9:
				ID = str(acronym)+"#00"+str(numb)
			elif numb > 9 and numb <= 99:
				ID = str(acronym)+"#0"+str(numb)
			elif numb > 99 and numb <= 999:
				ID = str(acronym)+"#"+str(numb)
			else:
				print('To manny!!')
			# print(ID)
			return ID


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_
