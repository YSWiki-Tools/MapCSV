import csv
import json
from itertools import chain
from copy import deepcopy


def time_sortkey(a: list[str, list]) -> int:
	score = int(a[0][:4].replace(":", ""))
	if a[0][-2] == "P":
		score += 1000
	return score


def average_point(a: tuple[float, float], b: tuple[float, float]):
	return (a[0]+b[0]) // 2, (a[1]+b[1]) // 2


start = None
markers = None
pattern = None
with (open("cartographer_in&out/start.json") as start_file,
	  open("cartographer_in&out/markers.csv", "r", encoding='utf-8') as markers_file,
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
	  open("locations.json", encoding="utf-8") as locations_file):
	locations = json.load(locations_file)
	id = 0
	for place in places:
		start["markers"].append(deepcopy(pattern))
		start["markers"][id]["id"] = id
		start["markers"][id]["popup"]["title"] = "Посещения"
		if place in locations.keys():
			start["markers"][id]["position"] = average_point(*locations[place])
		else:
			print(f'Внимание, указанная вами локация "{place}" отсутствует в списке. Убедитесь, что вы не допустили опечатку.\nСписок локаций находится в файле locations.json')
			start["markers"][id]["position"] = (6680, 5308)
		start["markers"][id]["popup"]["description"] = "\n".join(chain(*sorted([[time, *people] for time, people in markers[place].items()], key=time_sortkey)))
		id += 1
	json.dump(start, output, indent=4)
input("Готово.")
