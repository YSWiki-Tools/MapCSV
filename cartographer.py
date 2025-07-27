import csv
import json
import configparser
from itertools import chain
from copy import deepcopy


def time_sortkey(a: list[str, list]) -> int:
	score = int(a[0][:4].replace(":", ""))  # "7:05 AM" → 705
	if a[0][-2] == "P":
		score += 1000
	return score


def average_point(a: tuple[float, float], b: tuple[float, float]):
	return (a[0]+b[0]) // 2, (a[1]+b[1]) // 2


options = configparser.ConfigParser()
options.read('options.ini')

start = None
markers = None
pattern = None
with (open(f"locales/start_{options["MAIN"]["language"]}.json") as start_file,
	  open("cartographer_in&out/markers.csv", encoding='utf-8') as markers_file,
	  open("cartographer_in&out/pattern.json") as pattern_file):
	start = json.load(start_file)
	markers = list(csv.reader(markers_file))
	pattern = json.load(pattern_file)

	places = {i[2] for i in markers}
	markers = {place: list(filter(lambda x: x[2] == place, markers)) for place in places}
	for place in places:
		times = {i[0] for i in markers[place]}
		markers[place] = {time: list(filter(lambda x: x[0] == time, markers[place])) for time in times}
		for time in markers[place].keys():
			markers[place][time] = ["*"+entry[1] for entry in markers[place][time]]

# markers: {
#     place: {
#         time: [
#             person,
#         ],
#     },
# }

with (open("cartographer_in&out/output.json", "w") as output,
	  open("locations.json", "r", encoding="utf-8") as locations_file,
	  open(f"cartographer_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as t_file):
	
	t = json.load(t_file)
	locations = json.load(locations_file)
	id = 0

	for place in places:
		start["markers"].append(deepcopy(pattern))
		start["markers"][id]["id"] = id
		start["markers"][id]["popup"]["title"] = t["visits"]

		if place in locations.keys():
			
			start["markers"][id]["position"] = average_point(*locations[place])
		else:
			print(t["location_not_present"].format(place=place))
			start["markers"][id]["position"] = (6680, 5308)

		start["markers"][id]["popup"]["description"] = "\n".join(chain(*sorted([[time, *people] for time, people in markers[place].items()], key=time_sortkey)))

		if len(start["markers"][id]["popup"]["description"]) > 300:
			print(t["description_too_long"].format(id=id))

		id += 1

	json.dump(start, output, indent=4)
input("Done.")
