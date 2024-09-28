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
		zone[0][1] = 6208 - zone[0][1]
		zone[1][1] = 6208 - zone[1][1]
		draw_zones.rectangle(list(chain(*zone)), fillcolor)
v.alpha_composite(p)
v.save("locations_test/output.png")
	
