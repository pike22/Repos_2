from ..entity_main import Entity_Main

#Parenet: Entity_Main
#Children:
	#Stalfos_Main
	#CPU_Stalfos_Main

class Enemy_Main(Entity_Main):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Entity_Main.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
