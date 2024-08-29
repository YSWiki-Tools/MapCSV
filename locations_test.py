from random import random
from PIL import Image, ImageDraw, ImageColor
from json import load
from itertools import chain

akademi_map = Image.open("locations_test/Карта_Akademi_(1980).png",)
p, v = Image.new('RGBA', (9208, 6208), 'rgba(0, 0, 0, 0)'), akademi_map.copy()
draw_zones = ImageDraw.Draw(p)

with open("locations.json") as locations_file:
	locations = load(locations_file)

	for zone in locations.values():
		hue = random() * 360
		fillcolor = (*ImageColor.getrgb(f"hsb({hue}, 100%, 100%)"), 60)
		outlinecolor = (*ImageColor.getrgb(f"hsb({hue}, 100%, 80%)"), 100)
		match zone:
			case [list(), list()]:
				zone[0][1] = 6208 - zone[0][1]
				zone[1][1] = 6208 - zone[1][1]
				draw_zones.rectangle(list(chain(*zone)), fillcolor, outlinecolor)
			case [int(), int()]:
				zone[1] = 6208 - zone[1]
				draw_zones.ellipse([zone[0]+50, zone[1]+50, zone[0]-50, zone[1]-50], outlinecolor)
v.alpha_composite(p)
v.save("locations_test/output2.png")
	
