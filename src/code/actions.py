class Action:
	pass

# subclass of Action
class EscapedAction(Action):
	pass
	
# subclass of Action
class MovementAction(Action):
	def __init__(self, dx:int, dy:int):
		super().__init__()
		self.dx = dx
		self.dy = dy