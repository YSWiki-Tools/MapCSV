import csv
import json
import itertools as irt

def is_in_rectangle(pos:tuple[float, float],
					selector1:tuple[float, float],
		    		selector2:tuple[float, float]) -> bool: # type: ignore
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
	labyrinth = is_in_rectangle(pos, (5532, 2548), (5718, 2204))
	confession_tree = is_in_rectangle(pos, (4396, 5832), (4802, 6194))
	east_fountain = is_in_rectangle(pos, (3234, 1972), (3596, 1718))
	west_fountain = is_in_rectangle(pos, (5602, 1714), (6014, 1978))
	east_japanese_garden = is_in_rectangle(pos, (5890, 3440), (5646, 3726))
	east_japanese_garden_inside = is_in_rectangle(pos, (5914, 3916), (6444, 3258))
	west_japanese_garden = is_in_rectangle(pos, (3574, 3720), (3372, 3330))
	west_japanese_garden_inside = is_in_rectangle(pos, (3310, 3300), (2760, 3892))
	inner_garden = is_in_rectangle(pos, (7748, 1810), (7930, 1632))
	inner_garden_east = is_in_rectangle(pos, (7656, 1554), (7238, 1862))
	inner_garden_west = is_in_rectangle(pos, (7976, 1564), (8322, 1844))
	south_roof = is_in_rectangle(pos, (16, 4050), (2698, 3122))
	between_gym_and_pool = is_in_rectangle(pos, (4508, 5215), (4723, 4256))
	between_showers = is_in_rectangle(pos, (4731, 4200), (4485, 3787))
	male_shower_south = is_in_rectangle(pos, (4432, 3767), (3781, 3976))
	female_shower_south = is_in_rectangle(pos, (4746, 3996), (5492, 3812))
	gardening_club = is_in_rectangle(pos, (2814, 2706), (3495, 2016))
	lockers = is_in_rectangle(pos, (7553, 954), (8110, 248))
	class_11 = is_in_rectangle(pos, (7071, 659), (7551, 429))
	class_12 = is_in_rectangle(pos, (8601, 650), (8123, 429))
	class_21 = is_in_rectangle(pos, (7558, 3494), (7070, 3730))
	class_22 = is_in_rectangle(pos, (8610, 3492), (8116, 3726))
	class_31 = is_in_rectangle(pos, (1092, 444), (602, 666))
	class_32 = is_in_rectangle(pos, (2146, 444), (1652, 670))
	south_east_stairway_1 = is_in_rectangle(pos, (9155, 941), (8827, 613))
	south_west_stairway_1 = is_in_rectangle(pos, (6528, 933), (6861, 610))
	north_east_stairway_1 = is_in_rectangle(pos, (6857, 2548), (6528, 2870))
	north_west_stairway_1 = is_in_rectangle(pos, (9145, 2872), (8807, 2542))
	south_east_stairway_2 = is_in_rectangle(pos, (9141, 3675), (8806, 3996))
	south_west_stairway_2 = is_in_rectangle(pos, (6865, 3672), (6526, 4004))
	north_west_stairway_2 = is_in_rectangle(pos, (6865, 5607), (6526, 5935))
	north_east_stairway_2 = is_in_rectangle(pos, (9140, 5924), (8810, 5603))
	north_east_stairway_3 = is_in_rectangle(pos, (2677, 2549), (2339, 2880))
	south_east_stairway_3 = is_in_rectangle(pos, (2672, 944), (2352, 622))
	south_west_stairway_3 = is_in_rectangle(pos, (397, 626), (61, 954))
	north_west_stairway_3 = is_in_rectangle(pos, (400, 2890), (64, 2559))
	english_class = is_in_rectangle(pos, (2668, 1460), (2344, 976))
	biology_lab = is_in_rectangle(pos, (2674, 1508), (2346, 2002))
	art_room = is_in_rectangle(pos, (2672, 2036), (2344, 2512))
	science_club = is_in_rectangle(pos, (1648, 2812), (2156, 3064))
	newspaper_club = is_in_rectangle(pos, (1128, 2729), (1620, 3040))
	photography_club = is_in_rectangle(pos, (591, 2811), (1100, 3060))
	audiovisual_room = is_in_rectangle(pos, (62, 2027), (401, 2528))
	computer_class = is_in_rectangle(pos, (59, 1996), (398, 1504))
	announcement_room = is_in_rectangle(pos, (62, 970), (398, 1470))
	headmaster_room = is_in_rectangle(pos, (1125, 271), (1623, 743))
	cooking_club = is_in_rectangle(pos, (7567, 2797), (7055, 3046))
	drama_club = is_in_rectangle(pos, (8087, 2720), (7588, 3044))
	occult_club = is_in_rectangle(pos, (8622, 2780), (8113, 3046))
	meeting_room = is_in_rectangle(pos, (8844, 2025), (9144, 2511))
	sewing_room = is_in_rectangle(pos, (8858, 1496), (9144, 1985))
	homecare_room = is_in_rectangle(pos, (8816, 964), (9144, 1453))
	infirmary = is_in_rectangle(pos, (6861, 964), (6530, 1465))
	teacher_room = is_in_rectangle(pos, (6861, 1499), (6530, 1979))
	guidance_councelor_room = is_in_rectangle(pos, (6830, 2019), (6530, 2514))
	science_lab = is_in_rectangle(pos, (8807, 4026), (9142, 4528))
	craft_room = is_in_rectangle(pos, (8810, 5054), (9138, 4556))
	sociology_room = is_in_rectangle(pos, (8804, 5572), (9141, 5085))
	martial_arts_club = is_in_rectangle(pos, (8126, 5829), (8618, 6086))
	light_music_club = is_in_rectangle(pos, (7588, 5769), (8089, 6095))
	art_club = is_in_rectangle(pos, (7566, 5857), (7056, 6117))
	library = is_in_rectangle(pos, (6858, 5077), (6530, 5583))
	student_council_room = is_in_rectangle(pos, (6858, 5045), (6530, 4556))
	calligraphy_room = is_in_rectangle(pos, (6861, 4522), (6530, 4019))
	gym = is_in_rectangle(pos, (5976, 4460), (4832, 5152))
	pool = is_in_rectangle(pos, (4332, 4468), (3248, 5148))
	running_track = is_in_rectangle(pos, (5916, 5564), (3300, 5292))
	gates = is_in_rectangle(pos, (5300, 2040), (3912, 1032))
	storage_west_1 = is_in_rectangle(pos, (6528, 3040), (6871, 2889))
	storage_east_1 = is_in_rectangle(pos, (8800, 2892), (9148, 3049))
	storage_east_2 = is_in_rectangle(pos, (8796, 6112), (9151, 5945))
	storage_west_2 = is_in_rectangle(pos, (6522, 6107), (6868, 5949))
	storage_west_3 = is_in_rectangle(pos, (56, 3057), (395, 2904))
	storage_east_3 = is_in_rectangle(pos, (2337, 2900), (2682, 3058))
	near_storage_west_1 = is_in_rectangle(pos, (6877, 3057), (7039, 2884))
	near_storage_east_1 = is_in_rectangle(pos, (8633, 2889), (8794, 3051))
	near_storage_west_2 = is_in_rectangle(pos, (6878, 6109), (7039, 5949))
	near_storage_east_2 = is_in_rectangle(pos, (8632, 6112), (8792, 5904))
	near_storage_west_3 = is_in_rectangle(pos, (416, 3068), (572, 2901))
	near_storage_east_3 = is_in_rectangle(pos, (2166, 3075), (2320, 2917))
	near_art_club = is_in_rectangle(pos, (6989, 5846), (7578, 5597))
	near_light_music_club = is_in_rectangle(pos, (7580, 5791), (8106, 5498))
	near_martial_arts_club = is_in_rectangle(pos, (8711, 5849), (8120, 5587))
	near_sociology_room = is_in_rectangle(pos, (8618, 5625), (8803, 5071))
	near_craft_room = is_in_rectangle(pos, (8613, 4548), (8793, 5069))
	near_science_lab = is_in_rectangle(pos, (8613, 4548), (8793, 4006))
	near_headmaster_room = is_in_rectangle(pos, (1105, 972), (1640, 786))
	near_library = is_in_rectangle(pos, (7062, 5583), (6895, 5062))
	near_student_council = is_in_rectangle(pos, (7059, 4539), (6895, 5062))
	near_calligraphy_room = is_in_rectangle(pos, (7059, 4539), (6878, 4013))
	near_guidance_councelor = is_in_rectangle(pos, (6886, 2008), (7054, 2530))
	near_teacher_room = is_in_rectangle(pos, (6886, 2008), (7060, 1488))
	near_infirmary = is_in_rectangle(pos, (6884, 952), (7060, 1488))
	near_homecare_room = is_in_rectangle(pos, (8800, 956), (8618, 1490))
	near_sewing_room = is_in_rectangle(pos, (8782, 2016), (8618, 1490))
	near_meeting_room = is_in_rectangle(pos, (8782, 2016), (8614, 2524))
	near_occult_club = is_in_rectangle(pos, (8708, 2536), (8108, 2780))
	near_drama_club = is_in_rectangle(pos, (7572, 2520), (8096, 2708))
	near_cooking_club = is_in_rectangle(pos, (7580, 2512), (6972, 2772))
	near_english_room = is_in_rectangle(pos, (2140, 1492), (2332, 964))
	near_biology_lab = is_in_rectangle(pos, (2140, 1492), (2328, 2020))
	near_art_room = is_in_rectangle(pos, (2146, 2528), (2328, 2020))
	near_science_club = is_in_rectangle(pos, (1638, 2538), (2248, 2790))
	near_newspaper_club = is_in_rectangle(pos, (1638, 2538), (1114, 2714))
	near_photography_club = is_in_rectangle(pos, (502, 2794), (1112, 2526))
	near_audiovisual_room = is_in_rectangle(pos, (404, 2020), (598, 2536))
	near_computer_class = is_in_rectangle(pos, (404, 2020), (594, 1500))
	near_announcement_room = is_in_rectangle(pos, (412, 964), (594, 1500))
	near_labyrinth = is_in_rectangle(pos, (5530, 2548), (5430, 2204))
	between_men_shower_and_pool = is_in_rectangle(pos, (3232, 4446), (4350, 4284))
	barrel = is_in_rectangle(pos, (3236, 4264), (3712, 4064))
	between_women_shower_and_gym = is_in_rectangle(pos, (5678, 4448), (4754, 4260))
	near_class_11 = is_in_rectangle(pos, (7529, 958), (7008, 664))
	near_class_12 = is_in_rectangle(pos, (8143, 970), (8691, 667))
	near_class_21 = is_in_rectangle(pos, (6887, 4013), (7656, 3730))
	near_class_22 = is_in_rectangle(pos, (8722, 4005), (8012, 3710))
	near_class_31 = is_in_rectangle(pos, (1105, 975), (500, 678))
	near_class_32 = is_in_rectangle(pos, (1646, 967), (2245, 681))
	near_toilets_west_1 = is_in_rectangle(pos, (8623, 596), (8802, 25))
	near_toilets_east_1 = is_in_rectangle(pos, (6878, 599), (7059, 0))
	near_toilets_west_2 = is_in_rectangle(pos, (6875, 3657), (7051, 3139))
	near_toilets_east_2 = is_in_rectangle(pos, (8793, 3648), (8623, 3142))
	near_toilets_west_3 = is_in_rectangle(pos, (588, 537), (412, 84))
	near_toilets_east_3 = is_in_rectangle(pos, (2158, 551), (2330, 82))
	men_toilet_west_1 = is_in_rectangle(pos, (6512, 342), (6875, 69))
	men_toilet_east_1 = is_in_rectangle(pos, (9161, 73), (8800, 345))
	men_toilet_west_2 = is_in_rectangle(pos, (6872, 3403), (6513, 3138))
	men_toilet_east_2 = is_in_rectangle(pos, (9161, 3132), (8797, 3401))
	men_toilet_west_3 = is_in_rectangle(pos, (50, 347), (404, 87))
	men_toilet_east_3 = is_in_rectangle(pos, (2332, 89), (2692, 353))
	women_toilet_west_1 = is_in_rectangle(pos, (6512, 342), (6874, 601))
	women_toilet_east_1 = is_in_rectangle(pos, (9159, 595), (8800, 345))
	women_toilet_west_2 = is_in_rectangle(pos, (6872, 3403), (6515, 3662))
	women_toilet_east_2 = is_in_rectangle(pos, (9164, 3655), (8797, 3401))
	women_toilet_west_3 = is_in_rectangle(pos, (50, 347), (407, 613))
	women_toilet_east_3 = is_in_rectangle(pos, (2336, 596), (2692, 353))
	women_shower = is_in_rectangle(pos, (5475, 4259), (4757, 4047))
	men_shower = is_in_rectangle(pos, (3753, 4248), (4457, 4047))
	cafeteria = is_in_rectangle(pos, (8004, 3334), (7668, 3942))
	near_gardening_club = is_in_rectangle(pos, (3806, 1994), (3602, 2762))


	if labyrinth: return "у лабиринта"
	elif confession_tree: return "под деревом признаний"
	elif east_fountain: return "у восточного фонтана"
	elif west_fountain: return "у западного фонтана"
	elif west_japanese_garden: return "около западного японского сада"
	elif west_japanese_garden_inside: return "в западном японском саду"
	elif east_japanese_garden: return "около восточного японского сада"
	elif east_japanese_garden_inside: return "в восточном японском саду"
	elif inner_garden: return "во внутреннем дворике"
	elif inner_garden_east: return "в восточном внутреннем дворике"
	elif inner_garden_west: return "в западном внутреннем дворике"
	elif south_roof: return "в южной части крыши"
	elif between_gym_and_pool: return "между спортзалом и бассейном"
	elif between_showers: return "между душевых"
	elif male_shower_south: return "южнее мужской душевой"
	elif female_shower_south: return "южнее женской душевой"
	elif gardening_club: return "в клубе садоводства"
	elif lockers: return "около шкафчиков"
	elif class_11: return "в классе 1-1"
	elif class_12: return "в классе 1-2"
	elif class_21: return "в классе 2-1"
	elif class_22: return "в классе 2-2"
	elif class_31: return "в классе 3-1"
	elif class_32: return "в классе 3-2"
	elif south_east_stairway_1: return "на юго-восточной лестнице 1 этажа"
	elif south_west_stairway_1: return "на юго-западной лестнице 1 этажа"
	elif north_east_stairway_1: return "на северо-восточной лестнице 1 этажа"
	elif north_west_stairway_1: return "на северо-западной лестнице 1 этажа"
	elif south_east_stairway_2: return "на юго-восточной лестнице 2 этажа"
	elif south_west_stairway_2: return "на юго-западной лестнице 2 этажа"
	elif north_west_stairway_2: return "на северо-западной лестнице 2 этажа"
	elif north_east_stairway_2: return "на северо-восточной лестнице 2 этажа"
	elif north_east_stairway_3: return "на северо-восточной лестнице 3 этажа"
	elif south_east_stairway_3: return "на юго-восточной лестнице 3 этажа"
	elif south_west_stairway_3: return "на юго-западной лестнице 3 этажа"
	elif north_west_stairway_3: return "на северо-западной лестнице 3 этажа"
	elif english_class: return "в кабинете английского"
	elif biology_lab: return "в биологической лаборатории"
	elif art_room: return "в кабинете искусств"
	elif science_club: return "в научном клубе"
	elif newspaper_club: return "в газетном клубе"
	elif photography_club: return "в клубе фотографии"
	elif audiovisual_room: return "в аудиовизуальной комнате"
	elif computer_class: return "в компьютерном классе"
	elif announcement_room: return "в кабинете объявлений"
	elif headmaster_room: return "в кабинете директора"
	elif cooking_club: return "в клубе кулинарии"
	elif drama_club: return "в клубе драмы"
	elif occult_club: return "в оккультном клубе"
	elif meeting_room: return "в кабинете совещаний"
	elif sewing_room: return "в кабинете шитья"
	elif homecare_room: return "в кабинете домоводства"
	elif infirmary: return "в медпункте"
	elif teacher_room: return "в учительской"
	elif guidance_councelor_room: return "в кабинете методистки"
	elif science_lab: return "в научной лаборатории"
	elif craft_room: return "в мастерской"
	elif sociology_room: return "в кабинете социологии"
	elif martial_arts_club: return "в клубе боевых искусств"
	elif light_music_club: return "в клубе лёгкой музыки"
	elif art_club: return "в арт клубе"
	elif library: return "в библиотеке"
	elif student_council_room: return "в кабинете студенческого совета"
	elif calligraphy_room: return "в кабинете каллиграфии"
	elif gym: return "в спортзале"
	elif pool: return "на бассейне"
	elif running_track: return "на беговой дорожке"
	elif gates: return "около ворот"
	elif storage_west_1: return "в западной кладовке на 1 этаже"
	elif storage_east_1: return "в восточной кладовке на 1 этаже"
	elif storage_east_2: return "в восточной кладовке на 2 этаже"
	elif storage_west_2: return "в западной кладовке на 2 этаже"
	elif storage_west_3: return "в западной кладовке на 3 этаже"
	elif storage_east_3: return "в восточной кладовке на 3 этаже"
	elif near_storage_west_1: return "около западной кладовки на 1 этаже"
	elif near_storage_east_1: return "около восточной кладовки на 1 этаже"
	elif near_storage_west_2: return "около западной кладовки на 2 этаже"
	elif near_storage_east_2: return "около восточной кладовки на 2 этаже"
	elif near_storage_west_3: return "около западной кладовки на 3 этаже"
	elif near_storage_east_3: return "около восточной кладовки на 3 этаже"
	elif near_art_club: return "около арт клуба"
	elif near_light_music_club: return "около клуба лёгкой музыки"
	elif near_martial_arts_club: return "около клуба боевых искусств"
	elif near_sociology_room: return "около кабинета социологии"
	elif near_craft_room: return "около мастерской"
	elif near_science_lab: return "около научной лаборатории"
	elif near_headmaster_room: return "около кабинета директора"
	elif near_library: return "около библиотеки"
	elif near_student_council: return "около кабинета студенческого совета"
	elif near_calligraphy_room: return "около кабинета каллиграфии"
	elif near_guidance_councelor: return "около кабинета методистки"
	elif near_teacher_room: return "около учительской"
	elif near_infirmary: return "около медпункта"
	elif near_homecare_room: return "около кабинета домоводства"
	elif near_sewing_room: return "около кабинета шитья"
	elif near_meeting_room: return "около кабинета совещаний"
	elif near_occult_club: return "около оккультного клуба"
	elif near_drama_club: return "около клуба драмы"
	elif near_cooking_club: return "около клуба кулинарии"
	elif near_english_room: return "около кабинета английского"
	elif near_biology_lab: return "около биологической лаборатории"
	elif near_art_room: return "около кабинета искусств"
	elif near_science_club: return "около клуба науки"
	elif near_newspaper_club: return "около газетного клуба"
	elif near_photography_club: return "около клуба фотографии"
	elif near_audiovisual_room: return "около аудиовизуальной комнаты"
	elif near_computer_class: return "около компьютерного класса"
	elif near_announcement_room: return "около кабинета объявлений"
	elif near_labyrinth: return "около лабиринта"
	elif between_men_shower_and_pool: return "между мужской душевой и бассейном"
	elif barrel: return "около горящей бочки"
	elif between_women_shower_and_gym: return "между женской душевой и спортзалом"
	elif near_gardening_club: return "около клуба садоводства"
	elif near_class_11: return "около класса 1-1"
	elif near_class_12: return "около класса 1-2"
	elif near_class_21: return "около класса 2-1"
	elif near_class_22: return "около класса 2-2"
	elif near_class_31: return "около класса 3-1"
	elif near_class_32: return "около класса 3-2"
	elif near_toilets_west_1: return "около западных туалетов на 1 этаже"
	elif near_toilets_east_1: return "около восточных туалетов на 1 этаже"
	elif near_toilets_west_2: return "около западных туалетов на 2 этаже"
	elif near_toilets_east_2: return "около восточных туалетов на 2 этаже"
	elif near_toilets_west_3: return "около западных туалетов на 3 этаже"
	elif near_toilets_east_3: return "около восточных туалетов на 3 этаже"
	elif men_toilet_west_1: return "в западном мужском туалете на 1 этаже"
	elif men_toilet_east_1: return "в восточном мужском туалете на 1 этаже"
	elif men_toilet_west_2: return "в западном мужском туалете на 2 этаже"
	elif men_toilet_east_2: return "в восточном мужском туалете на 2 этаже"
	elif men_toilet_west_3: return "в западном мужском туалете на 3 этаже"
	elif men_toilet_east_3: return "в восточном мужском туалете на 3 этаже"
	elif women_toilet_west_1: return "в западном женском туалете на 1 этаже"
	elif women_toilet_east_1: return "в восточном женском туалете на 1 этаже"
	elif women_toilet_west_2: return "в западном женском туалете на 2 этаже"
	elif women_toilet_east_2: return "в восточном женском туалете на 2 этаже"
	elif women_toilet_west_3: return "в западном женском туалете на 3 этаже"
	elif women_toilet_east_3: return "в восточном женском туалете на 3 этаже"
	elif women_shower: return "в женской душевой"
	elif men_shower: return "в мужской душевой"
	elif cafeteria: return "в внутреннем кафетерии"
	else: return f"({pos[0]}, {pos[1]})"

categories = {
	"1980": {
		"Учителя":{
    	    "Кёко Коясу",
			"Муцуко Нишимура",
			"Нориё Хирамацу",
			"Отомэ Нагасако",
			"Рёко Угаки",
			"Сузуко Нака",
			"Цуру Кария"
    	},
    	"Ученики":{
    	    "Кагуя Вакайзуми",
			"Моэко Ракуёна",
			"Хонами Ходошима",
			"Сумико Тачибана",
			"Рицуко Чиканари",
			"Ай Доруяши",
			"Тейко Набатасай",
			"Комако Фунакоши",
			"Чигуса Бусуджима",
			"Азума Такахоши",
			"Азуса Мицуиши",
			"Айка Исери",
			"Акари Комияку",
			"Акифуми Анно",
			"Банри Масаюки",
			"Бунзо Ота",
			"Вака Ямага",
			"Ватару Мурата",
			"Гакуто Имакаке",
			"Гота Кушида",
			"Дайзо Момосэ",
			"Дайчи Сузуки",
			"Джицуко Фурусава",
			"Дорэми Шимахара",
			"Зенджи Шинокура",
			"Ивао Сато",
			"Икуэ Яйтабаши",
			"Ицуми Юуки",
			"Ичиэй Накаяма",
			"Кагемори Такаги",
			"Кахо Мики",
			"Кохару Хината",
			"Маая Оши",
			"Махиро Хонда",
			"Меи Мио",
			"Мурасаки Нобумото",
			"Нагако Андо",
			"Нагахару Курудо",
			"Окимото Фурукава",
			"Оми Охара",
			"Джокичи Юдасей",
			"Райзо Мориока",
			"Райму Ичиджо",
			"Ран Учимара",
			"Риоба Аиши",
			"Рюсей Коки",
			"Сабуро Мешино",
			"Сачи Ёнеяма",
			"Сачихико Фукуока",
			"Сейширо Саданага",
			"Соноко Саканоуэ",
			"Сора Сосуке",
			"Сота Юки",
			"Тадааки Сунада",
			"Тайчи Хиранака",
			"Такако Уэда",
			"Тиру Суторику",
			"Того Атацума",
			"Уи Тунесу",
			"Уманосукэ Ёшинари",
			"Умеко Учияма",
			"Фуджио Кио",
			"Фуджиэ Хайджима",
			"Фуюкичи Като",
			"Фуюми Тачики",
			"Ханаэ Оно",
			"Харуто Юто",
			"Хачиро Исо",
			"Хаято Харуки",
			"Химеко Дерегучи",
			"Хозуми Такеда",
			"Хонока Киёкава",
			"Чидори Икегами",
			"Чизуру Ямагучи",
			"Чикао Цурумаки",
			"Чуджиро Китасуме",
			"Шинако Бунзай",
			"Шичиро Куросапу",
			"Эйичи Асари",
			"Эйко Ногучи",
			"Эцуджи Одака",
			"Эцуко Хаяшибара",
			"Юи Рио",
			"Юна Хина",
			"Яхико Онода",
			"Яэ Огата"
		},
		"Члены клуба кулинарии":{
    	    "Акифуми Анно",
    	    "Банри Масаюки",
    	    "Чикао Цурумаки",
    	    "Айка Исери",
    	    "Уи Тунесу"
		},
    	"Члены клуба драмы":{
    	    "Дайчи Сузуки",
    	    "Фуджио Кио",
    	    "Эйичи Асари",
    	    "Чидори Икегами",
    	    "Химеко Дерегучи"
		},
    	"Члены оккультного клуба":{
    	    "Гакуто Имакаке",
			"Хачиро Исо",
    	    "Ичиэй Накаяма",
    	    "Эйко Ногучи",
    	    "Фуджиэ Хайджима"
		},
    	"Члены арт клуба":{
    	    "Нагахару Курудо",
    	    "Окимото Фурукава",
    		"Райзо Мориока",
    	    "Джицуко Фурусава",
    	    "Кахо Мики"
		},
    	"Члены клуба лёгкой музыки":{
    	    "Оми Охара",
    	    "Ран Учимара",
    	    "Сачи Ёнеяма",
    	    "Такако Уэда",
    	    "Умеко Учияма"
		},
    	"Члены клуба боевых искусств":{
    	    "Сачихико Фукуока",
    	    "Тадааки Сунада",
    	    "Уманосукэ Ёшинари",
    	    "Маая Оши",
    	    "Нагако Андо"
		},
    	"Члены клуба фотографии":{
    	    "Ватару Мурата",
    	    "Яхико Онода",
    	    "Зенджи Шинокура",
    	    "Вака Ямага",
    	    "Яэ Огата"
		},
    	"Члены газетного клуба":{
    	    "Шинако Бунзай",
    	    "Кагемори Такаги",
    	    "Махиро Хонда",
    	    "Ханаэ Оно",
    	    "Икуэ Яйтабаши"
		},
    	"Члены клуба науки":{
    	    "Азума Такахоши",
    	    "Бунзо Ота",
    	    "Чуджиро Китасуме",
    	    "Азуса Мицуиши",
    	    "Чизуру Ямагучи"
		},
    	"Члены клуба спорта":{
    	    "Дайзо Момосэ",
    	    "Эцуджи Одака",
    	    "Фуюкичи Като",
    	    "Эцуко Хаяшибара",
    	    "Фуюми Тачики"
		},
    	"Члены клуба садоводства":{
    	    "Гота Кушида",
    	    "Хозуми Такеда",
    	    "Ивао Сато",
    	    "Хонока Киёкава",
    	    "Ицуми Юуки",
		},
    	"Члены клуба лёгкой музыки, кроме лидера":{
    	    "Ран Учимара",
    	    "Сачи Ёнеяма",
    	    "Такако Уэда",
    	    "Умеко Учияма"
		},
    	"Члены клуба фотографии, кроме лидера":{
    	    "Яхико Онода",
    	    "Зенджи Шинокура",
    	    "Вака Ямага",
    	    "Яэ Огата"
		},
    	"Члены газетного клуба, кроме лидера":{
    	    "Кагемори Такаги",
    	    "Махиро Хонда",
    	    "Ханаэ Оно",
    	    "Икуэ Яйтабаши"
		},
		"Правонарушители":{
    	    "Сейширо Саданага",
			"Тайчи Хиранака",
			"Шичиро Куросапу",
			"Того Атацума",
			"Сабуро Мешино"
		},
    	"Правонарушительницы":{
    	    "Тиру Суторику",
			"Дорэми Шимахара",
			"Мурасаки Нобумото",
			"Акари Комияку",
			"Райму Ичиджо"
		},
    	"Члены студенческого совета":{
    	    "Рейичи Танаами",
    	    "Дайсаку Арагаки",
    	    "Джозе Шиуба",
    	    "Кен Кёнашима"
		},
		"Радужные парни":{
			"Харуто Юто",
			"Сора Сосуке",
			"Рюсей Коки",
			"Сота Юки",
			"Хаято Харуки"
		},
		"Радужные девушки":{
			"Юи Рио",
			"Юна Хина",
			"Меи Мио",
			"Кохару Хината"
		},
		"Все ученики класса 1-1":{
			"Уи Тунесу",
			"Химеко Дерегучи",
			"Фуджиэ Хайджима",
			"Кахо Мики",
			"Умеко Учияма",
			"Нагако Андо",
			"Яэ Огата",
			"Чизуру Ямагучи",
			"Фуюми Тачики",
			"Ицуми Юуки",
			"Икуэ Яйтабаши",
			"Сота Юки",
			"Джозе Шиуба",
			"Райму Ичиджо",
			"Кохару Хината"
		},
		"Все ученики класса 1-2":{
			"Айка Исери",
			"Чидори Икегами",
			"Эйко Ногучи",
			"Джицуко Фурусава",
			"Такако Уэда",
			"Маая Оши",
			"Вака Ямага",
			"Азуса Мицуиши",
			"Эцуко Хаяшибара",
			"Хонока Киёкава",
			"Ханаэ Оно",
			"Хаято Харуки",
			"Чигуса Бусуджима",
			"Акари Комияку",
			"Меи Мио"
		},
		"Все ученики класса 2-1":{
			"Чикао Цурумаки",
			"Фуджио Кио",
			"Ичиэй Накаяма",
			"Райзо Мориока",
			"Сачи Ёнеяма",
			"Уманосукэ Ёшинари",
			"Зенджи Шинокура",
			"Чуджиро Китасуме",
			"Фуюкичи Като",
			"Ивао Сато",
			"Кагуя Вакайзуми",
			"Рюсей Коки",
			"Мурасаки Нобумото",
			"Шичиро Куросапу"
		},
		"Все ученики класса 2-2":{
			"Моэко Ракуёна",
			"Хонами Ходошима",
			"Сумико Тачибана",
			"Ай Доруяши",
			"Тейко Набатасай",
			"Юи Рио",
			"Юна Хина",
			"Того Атацума",
			"Рицуко Чиканари",
			"Сабуро Мешино",
			"Махиро Хонда",
			"Комако Фунакоши",
			"Дайсаку Арагаки",
			"Соноко Саканоуэ",
			"Тайчи Хиранака"
		},
		"Все ученики класса 3-1":{
			"Банри Масаюки",
			"Эйичи Асари",
			"Хачиро Исо",
			"Окимото Фурукава",
			"Ран Учимара",
			"Тадааки Сунада",
			"Яхико Онода",
			"Бунзо Ота",
			"Эцуджи Одака",
			"Хозуми Такеда",
			"Кагемори Такаги",
			"Харуто Юто",
			"Кен Кёнашима",
			"Дорэми Шимахара",
			"Сейширо Саданага"
		},
		"Все ученики класса 3-2":{
			"Акифуми Анно",
			"Дайчи Сузуки",
			"Гакуто Имакаке",
			"Нагахару Курудо",
			"Оми Охара",
			"Сачихико Фукуока",
			"Ватару Мурата",
			"Азума Такахоши",
			"Дайзо Момосэ",
			"Гота Кушида",
			"Шинако Бунзай",
			"Сора Сосуке",
			"Рейичи Танаами",
			"Тиру Суторику",
			"Джокичи Юдасей"
		},
		"Парни из клуба спорта":{
			"Дайзо Момосэ",
    	    "Эцуджи Одака",
    	    "Фуюкичи Като"
		},
		"Лидеры клубов":{
			"Азума Такахоши",
			"Акифуми Анно",
			"Гакуто Имакаке",
			"Гота Кушида",
			"Дайзо Момосэ",
			"Дайчи Сузуки",
			"Нагахару Курудо",
			"Оми Охара",
			"Сачихико Фукуока",
			"Шинако Бунзай"
		},
		"Соперницы":{
			"Кагуя Вакайзуми",
			"Моэко Ракуёна",
			"Хонами Ходошима",
			"Сумико Тачибана",
			"Рицуко Чиканари",
			"Ай Доруяши",
			"Тейко Набатасай",
			"Комако Фунакоши",
			"Чигуса Бусуджима",
			"Соноко Саканоуэ"
		},
		"Учителя, кроме Цуру Карии":{
			"Кёко Коясу",
			"Муцуко Нишимура",
			"Нориё Хирамацу",
			"Отомэ Нагасако",
			"Рёко Угаки",
			"Сузуко Нака"
		},
		"Одиночки":{
			"Джокичи Юдасей",
			"Харуто Юто",
			"Сора Сосуке",
			"Рюсей Коки",
			"Сота Юки",
			"Хаято Харуки",
			"Юи Рио",
			"Юна Хина",
			"Меи Мио",
			"Кохару Хината"
		}
	},	
	"202X": {
		"Учителя":{
			"Карин Ханабуса",
			"Кахо Канокоги",
			"Киоши Тачикава",
			"Нацуки Абурая",
			"Рейна Набатаме",
			"Рино Фукахори",
			"Шиори Рикитаке"
		},
    	"Ученики":{
			"Аджиа Ашитоми",
			"Аканэ Ториясу",
			"Амай Одаяка",
			"Аой Рюгоку",
			"Берума Динкури",
			"Беши Такамине",
			"Борупен Сайшики",
			"Будо Масута",
			"Гаку Хикицури",
			"Гейджу Цука",
			"Гема Таку",
			"Гита Ямахато",
			"Дайроку Сурикизу",
			"Даку Ацу",
			"Дафуни Бурейку",
			"Джуку Рен",
			"Дора Тамамото",
			"Инкью Басу",
			"Ирука Доруфино",
			"Итачи Заметора",
			"Кага Куша",
			"Кашико Мурасаки",
			"Кенко Сукояка",
			"Киба Каваито",
			"Кокона Харука",
			"Кокоро Момоиро",
			"Кокума Джуцу",
			"Куроко Каменага",
			"Куу Дере",
			"Кьюджи Конагава",
			"Май Вайфу",
			"Мака Тансей",
			"Мантаро Сашимасу",
			"Мека Никару",
			"Мидори Гурин",
			"Мина Раи",
			"Миюджи Шан",
			"Мусуме Роншаку",
			"Осана Наджими",
			"Отохико Меичи",
			"Пиппи Осу",
			"Райбару Фумецу",
			"Рику Сома",
			"Роджасу Норубиру",
			"Рюто Иппонго",
			"Саки Мию",
			"Сакура Хагивара",
			"Сакью Басу",
			"Сейо Аканиши",
			"Таро Ямада",
			"Сукуби Дубиду",
			"Сумире Сузуки",
			"Супана Чуру",
			"Тога Табара",
			"Токуко Китагава",
			"Умеджи Кизугучи",
			"Унаги Денкашиза",
			"Уэкия Энгейка",
			"Фуреддо Джонзу",
			"Хазу Кашибучи",
			"Хана Дайдайяма",
			"Хаянари Цумеато",
			"Химари Фуджита",
			"Ходжиро Замеширо",
			"Хокуто Фурукизу",
			"Хому Курусу",
			"Хоро Гураму",
			"Хоруда Пуресу",
			"Хошико Мизудори",
			"Цубаки Уэсуги",
			"Цурузо Ямазаки",
			"Чоджо Текина",
			"Шима Шия",
			"Шин Хигаку",
			"Широми Тораёши",
			"Шо Кунин",
			"Шозо Куросава",
			"Шоку Цубурая",
			"Энпицу Бьёга",
			"Эфуде Нуримоно",
			"Яку Заиши",
			"Аяно Аиши",
		},
		"Члены клуба кулинарии":{
			"Аджиа Ашитоми",
			"Кенко Сукояка",
			"Саки Мию",
			"Сейо Аканиши",
			"Шоку Цубурая",
		},
    	"Члены клуба драмы":{
			"Кокона Харука",
			"Рику Сома",
			"Токуко Китагава",
			"Цурузо Ямазаки",
			"Шозо Куросава",
		},
    	"Члены оккультного клуба":{
			"Даку Ацу",
			"Кокума Джуцу",
			"Супана Чуру",
			"Чоджо Текина",
			"Шин Хигаку",
		},
		"Парни из оккультного клуба":{
			"Даку Ацу",
			"Чоджо Текина",
			"Шин Хигаку",
		},
    	"Члены арт клуба":{
			"Борупен Сайшики",
			"Гейджу Цука",
			"Мака Тансей",
			"Энпицу Бьёга",
			"Эфуде Нуримоно",
		},
		"Парни из арт клуба":{
			"Борупен Сайшики",
			"Гейджу Цука",
			"Энпицу Бьёга",
		},
    	"Члены клуба лёгкой музыки":{
			"Беши Такамине",
			"Гита Ямахато",
			"Дора Тамамото",
			"Киба Каваито",
			"Миюджи Шан",
		},
    	"Члены клуба боевых искусств":{
			"Будо Масута",
			"Джуку Рен",
			"Мина Раи",
			"Шима Шия",
			"Шо Кунин",
		},
    	"Члены клуба фотографии":{
			"Берума Динкури",
			"Дафуни Бурейку",
			"Роджасу Норубиру",
			"Сукуби Дубиду",
			"Фуреддо Джонзу",
		},
    	"Члены клуба видеоигр":{
			"Гема Таку",
			"Май Вайфу",
			"Мидори Гурин",
			"Пиппи Осу",
			"Рюто Иппонго",
		},
    	"Члены клуба науки":{
			"Кага Куша",
			"Мека Никару",
			"Хому Курусу",
			"Хоро Гураму",
			"Яку Заиши",
		},
    	"Члены клуба спорта":{
			"Ирука Доруфино",
			"Итачи Заметора",
			"Мантаро Сашимасу",
			"Унаги Денкашиза",
			"Ходжиро Замеширо",
		},
    	"Члены клуба садоводства":{
			"Сакура Хагивара",
			"Сумире Сузуки",
			"Уэкия Энгейка",
			"Химари Фуджита",
			"Цубаки Уэсуги",
		},
    	"Члены клуба лёгкой музыки, кроме лидера":{
			"Беши Такамине",
			"Гита Ямахато",
			"Дора Тамамото",
			"Киба Каваито",
		},
    	"Члены клуба фотографии, кроме лидера":{
			"Берума Динкури",
			"Дафуни Бурейку",
			"Роджасу Норубиру",
			"Сукуби Дубиду",
		},
    	"Члены клуба видеоигр, кроме лидера":{
			"Май Вайфу",
			"Пиппи Осу",
			"Мидори Гурин",
			"Рюто Иппонго",
		},
		"Правонарушители":{
			"Гаку Хикицури",
			"Дайроку Сурикизу",
			"Умеджи Кизугучи",
			"Хаянари Цумеато",
			"Хокуто Фурукизу",
		},
    	"Члены студенческого совета":{
			"Аканэ Ториясу",
			"Аой Рюгоку",
			"Куроко Каменага",
			"Широми Тораёши",
		},
		"Задиры":{
			"Кашико Мурасаки",
			"Кокоро Момоиро",
			"Мусуме Роншаку",
			"Хана Дайдайяма",
			"Хошико Мизудори",
		},
		"Все ученики класса 1-1":{
			"Берума Динкури",
			"Киба Каваито",
			"Кокона Харука",
			"Кокума Джуцу",
			"Куу Дере",
			"Май Вайфу",
			"Мантаро Сашимасу",
			"Отохико Меичи",
			"Саки Мию",
			"Хому Курусу",
			"Хошико Мизудори",
			"Цубаки Уэсуги",
			"Шима Шия",
			"Широми Тораёши",
			"Эфуде Нуримоно",
		},
		"Все ученики класса 1-2":{
			"Аджиа Ашитоми",
			"Дафуни Бурейку",
			"Дора Тамамото",
			"Ирука Доруфино",
			"Кокоро Момоиро",
			"Мака Тансей",
			"Мека Никару",
			"Мидори Гурин",
			"Мина Раи",
			"Сумире Сузуки",
			"Супана Чуру",
			"Токуко Китагава",
			"Хазу Кашибучи",
		},
		"Все ученики класса 2-1":{
			"Беши Такамине",
			"Гаку Хикицури",
			"Даку Ацу",
			"Джуку Рен",
			"Райбару Фумецу",
			"Осана Наджими",
			"Рику Сома",
			"Сакура Хагивара",
			"Сейо Аканиши",
			"Сукуби Дубиду",
			"Унаги Денкашиза",
			"Хана Дайдайяма",
			"Хоруда Пуресу",
			"Энпицу Бьёга",
			"Яку Заиши",
			"Аяно Аиши",
		},
		"Все ученики класса 2-2":{
			"Амай Одаяка",
			"Аой Рюгоку",
			"Дайроку Сурикизу",
			"Инкью Басу",
			"Сакью Басу",
			"Хаянари Цумеато",
			"Хокуто Фурукизу",
		},
		"Все ученики класса 3-1":{
			"Аканэ Ториясу",
			"Борупен Сайшики",
			"Гита Ямахато",
			"Кашико Мурасаки",
			"Кенко Сукояка",
			"Кьюджи Конагава",
			"Роджасу Норубиру",
			"Рюто Иппонго",
			"Умеджи Кизугучи",
			"Химари Фуджита",
			"Ходжиро Замеширо",
			"Хоро Гураму",
			"Чоджо Текина",
			"Шо Кунин",
		},
		"Все ученики класса 3-2":{
			"Будо Масута",
			"Гейджу Цука",
			"Гема Таку",
			"Итачи Заметора",
			"Кага Куша",
			"Куроко Каменага",
			"Миюджи Шан",
			"Мусуме Роншаку",
			"Таро Ямада",
			"Тога Табара",
			"Уэкия Энгейка",
			"Фуреддо Джонзу",
			"Цурузо Ямазаки",
			"Шин Хигаку",
			"Шоку Цубурая",
		},
		"Лидеры клубов":{
			"Будо Масута",
			"Гейджу Цука",
			"Гема Таку",
			"Кага Куша",
			"Куроко Каменага",
			"Миюджи Шан",
			"Уэкия Энгейка",
			"Цурузо Ямазаки",
			"Шин Хигаку",
			"Шоку Цубурая",
		},
		"Соперницы":{
			"Амай Одаяка",
			"Осана Наджими",
		},
		"Учителя, кроме Киоши Тачикавы":{
			"Карин Ханабуса",
			"Кахо Канокоги",
			"Нацуки Абурая",
			"Рейна Набатаме",
			"Рино Фукахори",
			"Шиори Рикитаке"
		},
		"Одиночки":{
			"Инкью Басу",
			"Куу Дере",
			"Кьюджи Конагава",
			"Отохико Меичи",
			"Сакью Басу",
			"Таро Ямада",
			"Тога Табара",
			"Хазу Кашибучи",
			"Хоруда Пуресу",
		}
	}
}

with (open("schedule.csv", "w", encoding="utf-8") as schedule_file,
	  open("sample_map.json") as map_file):
	csv_writer = csv.writer(schedule_file, lineterminator="\n")
	map_json = json.load(map_file)
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
			if i[0] == "*":
				i = i[1:].strip()
				if i in categories["210928X0"[is_1980_mode::2]].keys():
					for member in categories["210928X0"[is_1980_mode::2]][i]: 
						places[location][timeframe].append(member)
				else:
					places[location][timeframe].append(i)
			else:
				timeframe = i
				places[location][timeframe] = []

	students = set(irt.chain(*[places[place][time] for place in places.keys() for time in places[place].keys()]))
	visits = {student:list() for student in students}
	for student in students:
		for place in places.keys():
			for time in places[place].keys():
				if student in places[place][time]:
					visits[student].append((time, place))

	maxsites = max(map(len, visits.values()))
	csv_writer.writerow(["Имя и фамилия", "Имя", "Местоимение", *list(map(lambda x: " ".join(x), zip(["Время", "Место", "Занятие"] * maxsites, map(str, sorted(list(range(1, maxsites+1)) * 3)))))])
	lines = []
	for name, sites in visits.items():
		line = [None] * (3 + 3*maxsites)
		line[0] = name.strip()
		line[1] = name.split()[0]
		for i, site in enumerate(sites):
			line[3 + 3*i] = site[0]
			line[4 + 3*i] = site[1]
		lines.append(line)
	csv_writer.writerows(lines)
	