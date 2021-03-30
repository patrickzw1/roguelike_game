from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from actions import EscapedAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

class Engine:
	def __init__(self, entities: set[Entity], event_handler: EventHandler, player:Entity):
		self.entities = entities
		self.event_handler = event_handler
		self.player = player

	def handle_event(self, events:Iterable[Any]) -> None:
		for event in events:
			action = self.event_handler.dispatch(event)

			if action is None:
				continue
			if isinstance(action, MovementAction):
				self.player.move(dx=action.dx, dy=action.dy)
			if isinstance(action, EscapedAction):
				raise SystemExit()

	def render(self, console:Console, context:Context) -> None:
		for entity in self.entities:
			console.print(entity.x, entity.y, entity.char, fg=entity.color)
		context.present(console)
		console.clear()