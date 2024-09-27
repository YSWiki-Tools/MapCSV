import csv
import json
from itertools import chain


def is_in_rectangle(pos:tuple[float, float],
					selector1:tuple[float, float],
					selector2:tuple[float, float]) -> bool:
	a = selector1[0] > selector2[0]
	b = selector1[1] > selector2[1]
	match a, b:
		case True, True:
			return selector1[0] > pos[0] > selector2[0] and selector1[1] > pos[1] > selector2[1]
		case False, True:
			return selector1[0] < pos[0] < selector2[0] and selector1[1] > pos[1] > selector2[1]
		case True, False:
			return selector1[0] > pos[0] > selector2[0] and selector1[1] < pos[1] < selector2[1]
		case False, False:
			return selector1[0] < pos[0] < selector2[0] and selector1[1] < pos[1] < selector2[1]


def location_at(pos:tuple[float, float]) -> str:
	with open("locations.json", encoding="utf-8") as locations_file:
		locations = json.load(locations_file)
		for place, boundaries in locations.items():
			if type(boundaries[0]) == int: 
				continue
			elif is_in_rectangle(pos, *boundaries):
				return place
		return f"({pos[0]}, {pos[1]})"
	

with (open("schedules_in&out/output.csv", "w", encoding="utf-8") as output_file,
	  open("schedules_in&out/sample_map.json") as map_file,
	  open("groups.json", encoding="utf-8") as groups_file):
	output = csv.writer(output_file, lineterminator="\n")
	map_json = json.load(map_file)
	groups = json.load(groups_file)
	is_1980_mode = map_json["mapImage"].find("1980") > 0
	markers = map_json["markers"]

	places = {}
	for marker in markers:
		location = location_at(marker["position"])
		try:
			if not places[location]:
				places[location] = {}
		except KeyError:
			places[location] = {}
		description = marker["popup"]["description"].strip("\n").split("\n")
		timeframe = "" 
		for i in description:
			if not i:
				continue
			if i[0] == "*":
				i = i[1:].strip()
				if i in groups["210928X0"[is_1980_mode::2]].keys():
					for member in groups["210928X0"[is_1980_mode::2]][i]: 
						places[location][timeframe].append(member)
				else:
					places[location][timeframe].append(i)
			else:
				timeframe = i
				places[location][timeframe] = []

	students = set(chain(*[places[place][time] for place in places.keys() for time in places[place].keys()]))
	visits = {student:list() for student in students}
	for student in students:
		for place in places.keys():
			for time in places[place].keys():
				if student in places[place][time]:
					visits[student].append((time, place))

	maxsites = max(map(len, visits.values()))
	output.writerow(["Имя и фамилия", "Имя", "Местоимение", *list(map(lambda x: " ".join(x), zip(["Время", "Место", "Занятие"] * maxsites, map(str, sorted(list(range(1, maxsites+1)) * 3)))))])
	lines = []
	for name, sites in visits.items():
		line = [None] * (3 + 3*maxsites)
		line[0] = name.strip()
		line[1] = name.split()[0]
		for i, site in enumerate(sites):
			line[3 + 3*i] = site[0]
			line[4 + 3*i] = site[1]
		lines.append(line)
	output.writerows(lines)
	