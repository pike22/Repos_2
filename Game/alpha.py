from LevelDesigner import *
from PIL import ImageTk, Image
from z_Pictures import *
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard
import re


class Alpha():
	def __init__(self):
		self.__screenWidth	= 1280
		self.__screenHeight = 800
		self.__version	 = "Stab Simulator [ALPHAv0.2.894]"

		#Don't append till after SetUP is called
		self.__everyRoster 		= [] #Allobject IDs
		#---Entity ID Rosters---#
		self.__stalfosRoster	= [] #Stalfos tags
		self.__playerRoster		= [] #Player tags
		self.__slimeRoster		= [] #Slime tags
		self.__wallRoster		= [] #Wall tags

		#---Entity Amount to Create---#
		self.__stalfosCount = 1

		#---Entity groupID Rosters---#
		self.__weaponRoster	= ["#sword", "#bow", ]
		self.__staticRoster = ['#wall', '#floor', ]
		self.__enemyRoster	= ["#stalfos", "#slime"]
		self.__projRoster	= ['#arrow', ]

		#---Class Calls---#
		self.__mainApp = Tk()
		#__Engine__#
		self.__Maps		= Maps_GetFile()
		self.__Node		= Node(self.__mainApp) #other nodes are initialised in node.py: __init__()
		self.__cLogic	= Collision_Logic() #cLogic has to be made before other Game_Classes.
		self.__cNode	= Collision_Node(self.__cLogic)
		self.__iNode	= Image_Node()
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__pfNode	= PathFind_Node(self.__cLogic, self.__cNode, self.__iNode) #Path Finder
		#__Entites__#
		self.__Player	= Player_Main(self.__cLogic, self.__iNode)
		#__Tools-Weapons__#
		self.__Sword	= Sword_Main(cLogic=self.__cLogic, iNode=self.__iNode)
		self.__Bow		= Bow_Main(cLogic=self.__cLogic, cNode=self.__cNode, iNode=self.__iNode, tNode=self.__tNode)
		#__Level-Designer__#
		self.__GUI		= GUI_Main(self.__cLogic, self.__iNode, self.__cNode, self.__mainApp, color=None, mainMenu=None)
		self.__eGUI		= self.__GUI.get_eGUI()
		self.__siFILES	= self.__GUI.get_siFILE()

		#__Additional-Parameter-SetUP__#
		self.__GUI.gridSETUP()
		self.__cLogic.set_grid(self.__eGUI.get_grid())

		#__Import-Maps__#
		self.__levelONE   = self.__Maps.get_levelONE()
		self.__levelTWO   = self.__Maps.get_levelTWO()
		self.__levelTHREE = self.__Maps.get_levelTHREE()
		self.__levelFOUR  = self.__Maps.get_levelFOUR()

		#---Collision SETUP---#
		"""Fills out the Collision_Logic and Collision_Node Classes"""
		#__Player__#
		self.__cLogic.Add_CollisionDict(tagOrId=self.__Player.get_ID(), obj=self.__Player)
		self.__playerRoster.append(self.__Player.get_ID())
		self.__cNode.set_playerRoster(self.__playerRoster)
		#__Statics__#
		self.__imageDICT = None
		self.__cNode.set_staticRoster(self.__staticRoster)
		#__Enemies__#
		self.__cNode.set_enemyRoster(self.__enemyRoster)
		#__Stalfos__#
		for item in range(self.__stalfosCount):
			ID = self.__Node.Create_ObjectName("ST", item)
			self.__stalfosRoster.append(ID)
			stalMain = Stalfos_Main(ID=ID, cLogic=self.__cLogic, iNode=self.__iNode)
			self.__cLogic.Add_CollisionDict(tagOrId=ID, obj=stalMain)
		self.__cNode.set_stalfosRoster(self.__stalfosRoster)
		#__Slime__#
		for item in range(self.__stalfosCount):
			ID = self.__Node.Create_ObjectName("SL", item)
			self.__slimeRoster.append(ID)
			slime = Slime_Main(ID=ID, cLogic=self.__cLogic, pfNode=self.__pfNode, iNode=self.__iNode)
			self.__cLogic.Add_CollisionDict(tagOrId=ID, obj=slime)
		self.__cNode.set_slimeRoster(self.__slimeRoster)
		#__Weapons__#
		self.__cLogic.Add_CollisionDict(self.__Sword.get_ID(), self.__Sword)#Subject to Change
		self.__cLogic.Add_CollisionDict(self.__Bow.get_ID(), self.__Bow) 	 #Subject to Change
		self.__cNode.set_weaponRoster(self.__weaponRoster)
		#__Projectiles__#
		self.__cNode.set_projRoster(self.__projRoster)

		self.__cNode.set_everyRoster(self.__everyRoster)

		#---Path Finder Setups---#
		self.__pfNode.System_Grid()
		self._collision_OnOff = 'On'

		#---Temperary Variables---#
		self.__loopCount = 33
		self.__seconds   = 0
		self.is_g = False


	def Window_SetUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__screenWidth)+'x'+str(self.__screenHeight))

	def Create_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__screenHeight, self.__screenWidth)


	def Close_Window(self):
		if keyboard.is_pressed('q') == True:
			self.__mainApp.quit()
			return True

	def Game_SetUP(self, GC_OFF=False, collision_OnOff='On'):
		# #__Statics SETUP__#
		self._collision_OnOff = collision_OnOff
		self.__siFILES.Read_File(self.__levelFOUR)
		self.__imageDICT = self.__siFILES.get_imageDICT()

		# print('image keys\n\t', self.__imageDICT.keys())
		for key in self.__imageDICT.keys():
			self.__cLogic.Add_CollisionDict(tagOrId=key, obj=self.__imageDICT[key])
			self.__wallRoster.append(key)
		self.__cLogic.Add_Collision(lvdCorners=self.__imageDICT)
		self.__cNode.set_wallRoster(self.__wallRoster)

		#Bellow is Entity set up
		self.__Player.Player_SetUP(self.__screenWidth, self.__screenHeight)
		self.__everyRoster.append(self.__Player.get_ID())
		# self.__Player.Info_Print('PLayer')
		self.__Sword.Sword_SetUP()
		self.__everyRoster.append(self.__Sword.get_ID())
		# self.__Sword.Info_Print('Sword')
		self.__Bow.Bow_SetUP()
		self.__everyRoster.append(self.__Bow.get_ID())
		# self.__Bow.Info_Print('Bow')
		self.__Player.set_weapons(sword=self.__Sword, bow=self.__Bow, )

		#_Path Finding_#
		self.g = -1
		self.__pfNode.Map_Grid(self.__cLogic.get_collisionDict())

		#__ENEMY Setup__#
		COLDICT = self.__cLogic.get_collisionDict()
		for item in range(len(self.__stalfosRoster)):
			if self.__stalfosRoster[item] in COLDICT.keys():
				if re.search("(^ST#.{3})", self.__stalfosRoster[item]) != None:
					Stal = COLDICT[re.search("(^ST#.{3})", self.__stalfosRoster[item]).group(1)]
					Stal.Stalfos_SetUP(self.__screenWidth, self.__screenHeight)
					self.__everyRoster.append(Stal.get_ID())
					# dum_Stal.Info_Print('Stalfos')

		COLDICT = self.__cLogic.get_collisionDict()
		for item in range(len(self.__slimeRoster)):
			if self.__slimeRoster[item] in COLDICT.keys():
				if re.search("(^SL#.{3})", self.__slimeRoster[item]) != None:
					Slime = COLDICT[re.search("(^SL#.{3})", self.__slimeRoster[item]).group(1)]
					Slime.Slime_SetUP(self.__screenWidth, self.__screenHeight)
					self.__everyRoster.append(Slime.get_ID())
					self.__pfNode.Breadth_Search(startOBJ=Slime, endOBJ=self.__Player)
					# Slime.Info_Print('Slime')
					Slime.Misc_Any()
					# self.__pfNode.Show_Ends(32)


		#_Weapon SETUP_#

		#_Sets Every Roster_#
		self.__cNode.set_everyRoster(self.__everyRoster)

		#_CLOCK SETUP_#
		self.__tNode.Game_Clock(GC_OFF)



	#gameLoop def is for the classes use.
	def Game_Loop(self):
		#to kill the window
		a = self.Close_Window()
		if a == True:
			return
		# self.new_Player()

		# if self._collision_OnOff == 'Off':
		# if keyboard.is_pressed('g'):
		# 	self.is_g = True
		while self.g != 2000:
			self.g += 1
			self.__pfNode.Show_Breadth(self.g)

		#_loop Debug_#
		# self.debug_collisionDict() #workes

		#_Entity Loop Calls_#
			#_PLAYER_#
		if self.__Player.get_attack() == True:
			self.__Player.Player_MeleeAttack()
			self.__Player.Player_RangedAttack()
			# self.__cLogic.Check_forCollision(self.__Player)
		if self.__Player.get_isAlive() == True:
			if self.__Player.Player_MeleeAttack() == False and self.__Player.Player_RangedAttack() == False:
				if self._collision_OnOff == 'On':
					self.__Player.Movement_Controll()
				pass
		else:
			# print("dead? A#192")
			pass

			#_STALFOS_#
		collisionDict = self.__cLogic.get_collisionDict()
		for key in self.__stalfosRoster:
			if key in collisionDict:
				stalfos = collisionDict[key]
				if stalfos.get_isAlive() == True:
					if self._collision_OnOff == 'On':
						# stalfos.Movement_Controll()
						# stalfos.Stal_Attack()
						pass
			#_SLIME_#
		for key in self.__slimeRoster:
			if key in collisionDict:
				slime = collisionDict[key]
				if slime.get_isAlive() == True:
					# if self._collision_OnOff == 'On':
					reDraw = slime.Movement_Controll(self.__Player.get_myCoords())
					# print(reDraw, 'redraw?')
					# if reDraw == True:
					# 	self.__pfNode.Clear_Path()
					# 	self.__pfNode.Breadth_Search(startOBJ=slime, endOBJ=self.__Player)
					pass

		#_Collision Logic functions_#
		#_collisionDict is set up inside the alpha.__init__()

		#only one Player should be here (IGNORE MULTIPLAYER)
		list1 = []
		list1 = [self.__Player.get_myCorners()]
		for item in range(len(self.__stalfosRoster)):
			stal = self.__cLogic.Tag_toObject(self.__stalfosRoster[item])
			if stal != None:
				list1.append(stal.get_myCorners())
		for item in range(len(self.__slimeRoster)):
			slime = self.__cLogic.Tag_toObject(self.__slimeRoster[item])
			if slime != None:
				list1.append(slime.get_myCorners())

		if self.__Sword.get_isActive() == True:
			list1.append(self.__Sword.get_myCorners())
		if self.__Bow.get_isActive() == True:
			list1.append(self.__Bow.get_myCorners())
		for item in range(len(self.__Bow.get_projID())):
			# print(self.__Bow.get_projID(item), 'proj ID, A#189')
			if self.__Bow.get_projActive(item) == True:
				list1.append(self.__Bow.get_projCorners(item))

		self.__cLogic.Add_Collision(bfsCorners=self.__pfNode.get_shownList())


		self.__cLogic.Add_Collision(list1)
		self.__cNode.Use_Collision(len(list1))



		#_Combat_#
		if self.__Sword.get_isActive() == True:
			self.__Sword.Weapon_Active()

		if self.__Bow.get_isActive() == True:
			self.__Bow.Weapon_Active()

		for item in range(len(self.__Bow.get_projID())):
			# print('Active?', 'l#235')
			if self.__Bow.get_projActive(item) == True:
				self.__Bow.Proj_Active(item)

		if self.__Player.get_isHit() == True:
			self.__Player.Reset_Hit(Name='Player')

		collisionDict = self.__cLogic.get_collisionDict()
		for item in range(len(self.__stalfosRoster)):
			if self.__stalfosRoster[item] in collisionDict.keys():
				result = collisionDict[self.__stalfosRoster[item]]
				if result.get_isHit() == True:
					print('got hit')
					result.Reset_Hit(Name='Stalfos')

		for item in range(len(self.__slimeRoster)):
			if self.__slimeRoster[item] in collisionDict.keys():
				result = collisionDict[self.__slimeRoster[item]]
				if result.get_isHit() == True:
					print('got hit')
					result.Reset_Hit(Name='Slime')


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

	def Debug_CollisionDICT(self):
		if keyboard.is_pressed('t'):
			self.__cLogic.print_collisionDict()
			self.__cLogic.del_collisionDict(self.__Player.get_ID())
			self.__cLogic.print_collisionDict()

	#this is a function call for test prints to make sure things work
	def Testing_Debug(self):
		# self.find_all_Tags()
		# self.debug_collisionDict()
		# print(Image_Node.Render, 'Render')
		pass


#puts the above class to action
print('\n<<-----Initial Set UP------>>\n') #to make it easier to read in the command promt
Game = Alpha()
Game.Create_MainCanvas()
Game.Window_SetUP()
Game.Game_SetUP(False, 'On')
# Game.Testing_Debug()
print('\n<<-----Game Main Loop------>>\n')
Game.Game_Loop()
Game.get_mainAPP().mainloop()
print('\n')
print('<<----------------------------->>')
print('<<-------------END------------->>')
print('<<----------------------------->>')
