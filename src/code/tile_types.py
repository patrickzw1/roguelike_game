import numpy as np
from typing import Tuple

# tile graphics structure type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
	[
		("character", np.int32), # Unicode codepoint
		("foreground", "3B"),	# 3 unsigned bytes for RBG color
		("background", "3B")
	]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
	[
		("walkable", np.bool), # True if this tile can be walk over
		("transparent", np.bool), # True if this tile doesn't block the Field of view
		("dark", graphic_dt)	# Tile struct used for statically defined tile data
	]
)

def new_tile(*, walkable:int, transparent:int, 
			dark:Tuple[int, Tuple[int,int,int], Tuple[int,int,int]]
			) -> np.ndarray:
	# Helper function for defining individual tile types"
	return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
	walkable=True, transparent=True, dark=(ord(" "), (255,255,255), (50,50,150)))

wall = new_tile(
	walkable=False, transparent=False, dark=(ord(" "), (255,255,255), (0,0,100)))

