import csv
import json
import configparser
from itertools import chain


def time_sortkey(a: list[str, list]) -> int:
	score = int(a[0][:4].replace(":", ""))  # "7:05 AM" → 705
	if a[0][-2] == "P":
		score += 1000
	return score


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


options = configparser.ConfigParser()
options.read('options.ini')	

t = None
with open(f"locales/schedules_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as t_file:
	t = json.load(t_file)


def location_at(pos:tuple[float, float], patrol:bool) -> str:
	with open(f"locales/locations_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as locations_file:
		locations = json.load(locations_file)
		for place, boundaries in locations.items():
			if patrol: 
				if place[:6] == t["patrol"] and is_in_rectangle(pos, *boundaries):
					return place
			else:
				if is_in_rectangle(pos, *boundaries):
					return place
		print(f"({pos[0]}, {pos[1]})")
		return f"({pos[0]}, {pos[1]})"


with (open("schedules_in&out/output.csv", "w", encoding="utf-8") as output_file,
	  open("schedules_in&out/sample_map.json") as map_file,
	  open(f"locales/groups_{options["MAIN"]["language"]}.json", "r", encoding="utf-8") as groups_file):
	output = csv.writer(output_file, lineterminator="\n")
	map_json = json.load(map_file)
	groups = json.load(groups_file)
	markers = map_json["markers"]

	places = {}
	for marker in markers:
		location = location_at(marker["position"], marker["categoryId"] == "1")
		try:
			if not places[location]:
				places[location] = {}
		except KeyError:
			places[location] = {}
		description = marker["popup"]["description"].strip("\n").split("\n")
		timeframes = []
		for i in description:
			if not i:
				continue
			if i[0] == "*":
				i = i[1:].strip()
				for timeframe in timeframes:
					if i in groups[options["MAIN"]["mode"]].keys():
						for member in groups[options["MAIN"]["mode"]][i]: 
							places[location][timeframe].append(member)
					else:
						places[location][timeframe].append(i)
			else:
				timeframes = i.split(", ")
				for timeframe in timeframes:
					places[location][timeframe] = []

	students = set(chain(*[places[place][time] for place in places.keys() for time in places[place].keys()]))
	visits = {student:list() for student in students}
	for student in students:
		for place in places.keys():
			for time in places[place].keys():
				if student in places[place][time]:
					visits[student].append((time, place))
		visits[student].sort(key=time_sortkey)

	maxsites = max(map(len, visits.values()))
	output.writerow([t["full_name"], t["name"], t["pronoun"], *list(map(lambda x: " ".join(x), zip([t["time"], t["place"], t["activity"]] * maxsites, map(str, sorted(list(range(1, maxsites+1)) * 3)))))])
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
	