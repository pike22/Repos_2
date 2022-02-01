from .kinetics_node import Kinetics_Node

#Parent: None
#Children:
	#Main_Node

class Node():
	def __init__(self, mainApp=None, cLogic=None, cNode=None, iNode=None, tNode=None):
		#---Classes---#
		"""#The Classes that the objects need#"""
		self._cLogic = cLogic
		self._cNode  = cNode
		self._iNode  = iNode
		self._tNode  = tNode
		self._kNode  = Kinetics_Node()

	# def yes(self, ):
	# 	stuffs

	def Create_ObjectName(self, acronym, numb):
		if numb <= 9:
			ID = str(acronym)+"#00"+str(numb)
		elif numb > 9 and numb <= 99:
			ID = str(acronym)+"#0"+str(numb)
		elif numb > 99 and numb <= 999:
			ID = str(acronym)+"#"+str(numb)
		else:
			print('To manny!!')
		return ID


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_
