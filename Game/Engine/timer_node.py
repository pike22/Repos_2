
class Timer_Node():
	GameTime = 0
	def __init__(self, mainApp):
		self.__mainApp		  = mainApp
		self.__seconds		  = 0
		self.__FPS			  = 1000 / 30
		self.__frameCount 	  = 33

		#Time_Delay Parameters
		self._nextTime = 0



	def Game_Clock(self, showTime=False):
		Timer_Node.GameTime += 1
		if Timer_Node.GameTime == self.__frameCount:
			self.__seconds += 1
			if showTime == True:
				print(self.__seconds, 'seconds')
			self.__frameCount += 33

		self.__mainApp.after(int(self.__FPS), self.Game_Clock)


	def Time_Delay(self, delay=None, ): ## NOTE: Delay is in mil-seconds. 33 delay == 1 second
		if delay != None:
			self._nextTime = Timer_Node.GameTime + delay
			print(Timer_Node.GameTime)
			print(self._nextTime)



		if Timer_Node.GameTime == self._nextTime:
			print("Times UP!!")
			return True


		self.__mainApp.after(int(self.__FPS), self.Time_Delay)



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_seconds(self):
		return self.__seconds

	def get_FPS(self):
		return self.__FPS


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
