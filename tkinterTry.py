from tkinter import *
import time
from random import randrange, randint

canvasConfig = {
	"width": 400,
	"height": 400,
	"bg": "#bbada0"
}
# #cdc1b4
positionConfig = {
	"marginAround": 10,
	"marginBetween": 5,
	"width_count": 4,
	"height_count": 4
}

cell = {
	"map" : [],
	"bg": {
		0: 		"#cdc1b4",
		2: 		"#eee4da",
		4: 		"#ede0c8",
		8: 		"#f2b179",
		16: 	"#f59563",
		32: 	"#f67c5f",
		64: 	"#f65e3b",
		128: 	"#edcf72",
		256: 	"#edcc61",
		512: 	"#edc850",
		1024: 	"#edc53f",
		2048: 	"#edc22e"
		# TODO: continue colors
	},
	"fontColor" : {
		0 : 	"#776e65",
		2 : 	"#776e65",
		4 : 	"#776e65",
		8 : 	"#f9f6f2",
		16 : 	"#f9f6f2",
		32 : 	"#f9f6f2",
		64 : 	"#f9f6f2",
		128 : 	"#f9f6f2",
		256 : 	"#f9f6f2",
		512 : 	"#f9f6f2",
		1024 : 	"#f9f6f2",
		2048 : 	"#f9f6f2"
		# TODO: recreate colors
	}
	# TODO: add font color
}


"""
.--------------------->X
|  (0,0) (1,0) (2,0)  // (X,Y)
|  (0,1) (1,1) (2,1)
|  (0,2) (1,2) (2,2)
\/
Y
"""

# coord: X or Y value
# side: "width" or "height"
def coord_calc(coord, side, boxsize):
	return positionConfig["marginAround"] + coord * positionConfig["marginBetween"] + coord * boxsize

def size_calc(coord, side):
	return ( canvasConfig[side]
			- positionConfig["marginAround"] * 2
			- (positionConfig[side+"_count"]-1) * positionConfig["marginBetween"] ) / positionConfig[side+"_count"]

def coords_calc(Xpos, Ypos):
	width = size_calc(Xpos, "width")
	height = size_calc(Xpos, "height")
	return {
		"width" 	: width,
		"height" 	: height,
		"x"			: coord_calc(Xpos, "width", width),
		"y"			: coord_calc(Ypos, "height", height)
	}


def canvas_init(master):
	canvas = Canvas(master, 
				width=canvasConfig["width"],
				height=canvasConfig["height"],
				bg=canvasConfig["bg"])
	canvas.pack()
	return canvas

def rectangles_generation():
	for X in range(0,positionConfig["width_count"]):
		for Y in range(0,positionConfig["height_count"]):
			coords = coords_calc(X, Y)
			value = cell["map"][X][Y]

			canvas.create_rectangle(coords["x"], 
				coords["y"], 
				coords["x"]+coords["width"], 
				coords["y"]+coords["height"], 
				fill=cell["bg"][value])

			text = (value if value else "")
			canvas.create_text(coords["x"]+coords["width"]/2, 
				coords["y"]+coords["width"]/2, 
				fill=cell["fontColor"][value], 
				text=text)
				# font=tkFont.Font(family='Helvetica', size=36, weight='bold'))

def map_init():
	cell["map"] = []
	for X in range(0, positionConfig["width_count"]):

		row = []
		for Y in range(0, positionConfig["height_count"]):
			row.append(0)
		
		cell["map"].append(row)


def moveUp():
	for _ in range(0,int(max(positionConfig["width_count"], positionConfig["height_count"])*1.5)):
		for X in range(0, positionConfig["width_count"]):
			for Y in range(0, positionConfig["height_count"]-1):
				if cell["map"][X][Y] == 0 and cell["map"][X][Y+1] != 0:
					cell["map"][X][Y] = cell["map"][X][Y+1]
					cell["map"][X][Y+1] = 0
				elif cell["map"][X][Y] != 0 and cell["map"][X][Y+1] == cell["map"][X][Y]:
					cell["map"][X][Y+1] = 0
					cell["map"][X][Y] *= 2

def moveDown():
	for _ in range(0,int(max(positionConfig["width_count"], positionConfig["height_count"])*1.5)):
		for X in range(0, positionConfig["width_count"]):
			for Y in reversed(range(1, positionConfig["height_count"])):
				if cell["map"][X][Y] == 0 and cell["map"][X][Y-1] != 0:
					cell["map"][X][Y] = cell["map"][X][Y-1]
					cell["map"][X][Y-1] = 0
				elif cell["map"][X][Y] != 0 and cell["map"][X][Y-1] == cell["map"][X][Y]:
					cell["map"][X][Y-1] = 0
					cell["map"][X][Y] *= 2

def moveLeft():
	for _ in range(0,int(max(positionConfig["width_count"], positionConfig["height_count"])*1.5)):
		for X in range(0, positionConfig["width_count"]-1):
			for Y in range(0, positionConfig["height_count"]):
				if cell["map"][X][Y] == 0 and cell["map"][X+1][Y] != 0:
					cell["map"][X][Y] = cell["map"][X+1][Y]
					cell["map"][X+1][Y] = 0
				elif cell["map"][X][Y] != 0 and cell["map"][X+1][Y] == cell["map"][X][Y]:
					cell["map"][X][Y] = 0
					cell["map"][X+1][Y] *= 2

def moveRight():
	for _ in range(0,int(max(positionConfig["width_count"], positionConfig["height_count"])*1.5)):
		for X in reversed(range(1, positionConfig["width_count"])):
			for Y in range(0, positionConfig["height_count"]):
				if cell["map"][X][Y] == 0 and cell["map"][X-1][Y] != 0:
					cell["map"][X][Y] = cell["map"][X-1][Y]
					cell["map"][X-1][Y] = 0
				elif cell["map"][X][Y] != 0 and cell["map"][X-1][Y] == cell["map"][X][Y]:
					cell["map"][X][Y] = 0
					cell["map"][X-1][Y] *= 2

def show_table():
	print("Table")
	for Y in range(0, positionConfig["height_count"]):
		for X in range(0, positionConfig["width_count"]):
			print(cell["map"][X][Y], end="")
		print()

def get_rand_coord(side):
	return randint(0, positionConfig[side+"_count"]-1)

def get_rand_empthy_cell():
	x = get_rand_coord("width")
	y = get_rand_coord("height")
	while cell["map"][x][y] != 0:
		x = get_rand_coord("width")
		y = get_rand_coord("height")
	return {
		"x": x,
		"y": y
	}

def is_table_full():
	for X in range(0, positionConfig["width_count"]):
		for Y in range(0, positionConfig["height_count"]):
			if cell["map"][X][Y] == 0:
				return False
	return True

def generete_new():
	for _ in range(0, 2):
		if is_table_full():
			return
		coords = get_rand_empthy_cell()
		value = randrange(2, 5, 2)
		cell["map"][coords["x"]][coords["y"]] = value

def repaint():
	canvas.delete("all")
	rectangles_generation()
	canvas.pack()

def key_pressed(event):

	if event.char == "w":
		moveUp()
	elif event.char == "a":
		moveLeft()
	elif event.char == "s":
		moveDown()
	elif event.char == "d":
		moveRight()
	else:
		return

	if is_table_full():
		time.sleep(3)
		map_init()

	generete_new()
	# show_table() # TODO: delete
	
	repaint()

def event_init(master):
	master.bind("<Key>", key_pressed)



master = Tk()
canvas = canvas_init(master)

map_init()
repaint()

event_init(master)

master.mainloop()