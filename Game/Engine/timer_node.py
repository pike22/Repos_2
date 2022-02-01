
class Timer_Node():
	GameTime = 0
	def __init__(self, mainApp):
		self.__mainApp		  = mainApp
		self.__seconds		  = 0
		self.__FPS			  = 1000 / 30
		self.__frameCount 	  = 33


	def Game_Clock(self, OFF=False):
		Timer_Node.GameTime += 1
		if Timer_Node.GameTime == self.__frameCount:
			self.__seconds += 1
			if OFF == True:
				print(self.__seconds, 'seconds')
			self.__frameCount += 33

		self.__mainApp.after(int(self.__FPS), self.Game_Clock)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_seconds(self):
		return self.__seconds

	def get_FPS(self):
		return self.__FPS


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
