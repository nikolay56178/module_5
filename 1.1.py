class StringVar():

	def __init__(self,text):
		self.text = text 

	def get(self):
		 print('Your text : ',self.text)

	def set(self):

		b = self.text.center(20, "-")
		print(b)
		 
text1 = 'hello world!'

a = StringVar(text1)

a.get()
a.set()






