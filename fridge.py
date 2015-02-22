import time as T

class Container(object):

	def __init__(self):
		pass

	def add_item(self, item):
		pass

	def rmv_item(self, item):
		pass

	def wow(self, item):
		pass

class FoodItem(object):

	def __init__(self, name, quantity):
		pass

	def pas(self):
		pass

	def __add__(self, other):
		if type(other) == FoodItem:
			if self.name == other.name:
				return FoodItem(self.name, self.quantity + other.quantity)

class PerishableFood(FoodItem):

	def __init__(self, name, quantity, expiry = None):
		FoodItem.__init__(name, quanitity)
		# Week as default one
		self.expiry = expiry or T.timedelta()

	def get_expiry(self):
		return self.expiry

	def is_alive(self):
		# Compare today's time with expiry time
		return True

	def pas(self):
		pass



fridge = Container()

bananas = PerishableFood('banana', 2)
other_bananas = PerishableFood('banana', 2)
bunch = bananas + other_bananas

fridge.add_item(bunch)
