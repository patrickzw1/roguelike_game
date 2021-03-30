#!/usr/bin/env python3
import tcod
from engine import Engine
from entity import Entity
from actions import EscapedAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    # loading the font image
    tileset = tcod.tileset.load_tilesheet(
    	"../picture/font.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255,255,255))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), "#", (255,255,0))
    entities = {npc, player}
    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(screen_width,screen_height,tileset=tileset,title="Roguelike Game",vsync=True)as context:
    	root_console = tcod.Console(screen_width, screen_height, order="F")
    	
    	while True:
	    	engine.render(console=root_console, context=context)
	    	events = tcod.event.wait()
	    	engine.handle_event(events)


if __name__ == "__main__":
    main()