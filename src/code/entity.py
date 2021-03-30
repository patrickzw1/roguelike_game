from typing import Tuple

class Entity:
	"""
	A generic object to represent players, enemies, and other items
	"""

	# char parameter is the character to represent entity, like player is "@"
	def __init__(self, x:int, y:int, char:str, color:Tuple[int,int,int]):
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, dx:int, dy:int) -> None:
		# moving the entity by a given amount
		self.x += dx
		self.y += dy