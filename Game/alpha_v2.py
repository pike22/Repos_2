from LevelDesigner import *
from PIL import ImageTk, Image
from z_Pictures import *
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard
import re


class Alpha_v2():
	def __init__(self):
		#<--\Tkinter window information\-->#
		self.__screenWidth	= 1280
		self.__screenHeight	= 800
		self.__loopCount	= 33
		self.__seconds		= 0
		self.__version		= "Stab Simulator [ALPHA v0.2.944]"

		#<--\Rosters Of All Entities\-->#
		self.__staticRoster	= [] #Statics can't move alone.
		self.__playerRoster	= []
		self.__weaponRoster	= []
		self.__everyRoster	= []
		self.__enemyRoster	= ['#stalfos', '#slime', ]
		self.__wallRoster	= ['#wall', '#floor', ] #Walls don't move period.
		self.__projRoster	= ['#arrow', ]

		#<--\Class Creation/Assignments\-->#
		self.__mainApp 		= Tk()
		#Engine#
		self.__Maps 		= Maps_GetFile()
		self.__Node 		= Node(self.__mainApp)
		self.__cLogic		= Collision_Logic_v2()
		self.__cNode		= Collision_Node_v2(self.__cLogic)
		self.__iNode 		= Image_Node()
		self.__tNode 		= Timer_Node(self.__mainApp)
		self.__pfNode 		= PathFind_Node(self.__cLogic, self.__cNode, self.__iNode)
		#Entities#
		self.__Player 		= Player_Main(self.__cLogic, self.__iNode)
		self.__Sword 		= Sword_Main(cLogic=self.__cLogic, iNode=self.__iNode)
		self.__Bow			= Bow_Main(cLogic=self.__cLogic, cNode=self.__cNode, iNode=self.__iNode, tNode=self.__tNode)
			#more latter is needed. Weapons may go here
		#Level Designer#
		self.__GUI 			= GUI_Main(self.__cLogic, self.__iNode, self.__cNode, self.__mainApp, color=None, mainMenu=None)
		self.__eGUI 		= self.__GUI.get_eGUI()
		self.__siFiles 		= self.__GUI.get_siFILE()
		self.__imageDICT 	= None
			#__Import-Maps__#
		self.__levelONE   	= self.__Maps.get_levelONE()
		self.__levelTWO  	= self.__Maps.get_levelTWO()
		self.__levelTHREE	= self.__Maps.get_levelTHREE()
		self.__levelFOUR  	= self.__Maps.get_levelFOUR()

		#<--\Path Finder Setup\-->#
		self.__pfNode.System_Grid()


		#<--\Collision Setups\-->#
		self.__collision_OnOff = 'On' #Defults to On.

		#<-Temporary Variables->#
		self.is_g = False

	def Window_Setup(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))

	def Create_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__screenHeight, self.__screenWidth)
		self.__cLogic.Create_Grid()


	def Close_Window(self):
		if keyboard.is_pressed('q') == True:
			self.__mainApp.quit()
			return True


	def Game_Setup(self, showTime=False, collision_OnOff='On'):
		self.__collision_OnOff = collision_OnOff
		self.__siFiles.Read_File(self.__levelFOUR)
		self.__imageDICT = self.__siFiles.get_imageDICT()
		# print(self.__imageDICT)

		#<--\Entity Setups\-->#
		self.__Player.Player_Setup(self.__screenWidth, self.__screenHeight)
		# self.__Player.set_weapons(self.__Sword, self.__Bow)


		#<--\Weapon Setups\-->#
		print("Weapons Need rework with collision")
		print("They have anchent code.")
		print()
		# self.__Sword.Sword_Setup()
		# self.__Bow.Bow_Setup()

		#<--\Collision Setup\-->#
		#Add_Collision(self, pos, obj, tag)
		self.__cLogic.Add_Collision(pos=self.__Player.get_myCoords(), obj=self.__Player, tag=self.__Player.get_ID())
		for key, value in self.__imageDICT.items():
			self.__cLogic.Add_Collision(pos=value.get_myCoords(), obj=value, tag=key)
			# print()
		# self.__cLogic.Check_ifUsed()


		#<--\Clock Setup\-->#
		self.__tNode.Game_Clock(showTime)


	def Game_Loop(self):
		#Window Kill:
		kill = self.Close_Window()
		if kill == True:
			return

		#<--\Stuffs\-->#
		self.__cLogic.Is_Collision(self.__Player.get_ID())


		#<--\Entity\-->#
		#
		#Player
		self.__Player.Movement_Controll()
		#
		#

		#<--\Combat\-->#
		#
		#
		#
		#
		#


		self.__mainApp.after(int(self.__tNode.get_FPS()), self.Game_Loop)



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_ForT(self, ForT):#ForT == False or True, ForT
		self.__ForT = ForT


	"""#|--------------Extra Functions--------------|#"""
	def Find_AllTags(self):
		listOfTags = Image_Node.Render.find_all()
		# print(listOfTags, 'list of tags')
		for item in listOfTags:
			tag = Image_Node.Render.gettags(item)
			if len(tag) > 0:
				print(color + "Item", item, 'Has tag:', tag)




print('|You wanted to theroise creating functions within one of the collision classes to make setting up entities much easier|')
print("|I hope you run this tomorrow, probably will due to writing this. DON'T FORGET")
print("\n<<-----Initial Setup----->>\n")
Game = Alpha_v2()
Game.Create_MainCanvas()
Game.Window_Setup()
Game.Game_Setup(False, 'On')
print("\n<<-------Game Loop------->>\n")
Game.Game_Loop()
Game.get_mainAPP().mainloop()
print('\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')
print('\n')
