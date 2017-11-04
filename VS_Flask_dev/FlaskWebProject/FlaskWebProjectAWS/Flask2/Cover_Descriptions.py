
def cover_discription():
	cover_discription_dict = {
			'open_poor' : ['Open Space, Poor Condition (Grass cover <50%)',68,79,86,89],
			'open_fair' : ['Open Space, Fair Condition (Grass cover 50% to 75%)',49,69,79,84],
			'open_good' : ['Open Space, Good Condition (Grass cover >75%)',39,61,74,80],
			'roadway_paved' : ['Roadway Impervious Area, Paved',98,98,98,98],
			'curb_paved' : ['Paved; Curbs and storm sewers',98,98,98,98],
			'ditches_paved' : ['Paved; Open Ditches',83,89,92,93],
			'gravel' : ['Gravel',76,85,89,91],
			'dirt' : ['Dirt',72,82,87,89],
			'natur_desert_landscape' : ['Natural Desrt Lanscaping',63,77,85,88],
			'artif_desert_landscape' : ['Artificial Desrt Lanscaping',96,96,96,96],
			'urban_commercial' : ['Urban Districts: Commercial and Business',89,92,94,95],
			'urban_industrial' : ['Urban Districts: Industrial',81,88,91,93],
			'residential_65' : ['Residential: 65% Impervious (1/8 Acre)',77,85,90,92],
			'residential_38' : ['Residential: 38% Impervious (1/4 Acre)',61,75,83,87],
			'residential_30' : ['Residential: 30% Impervious (1/3 Acre)',57,72,81,86],
			'residential_25' : ['Residential: 25% Impervious (1/2 Acre)',54,70,80,85],
			'residential_20' : ['Residential: 20% Impervious (1 Acre)',51,68,79,84],
			'residential_12' : ['Residential: 12% Impervious (2 Acre)',46,65,77,82],
			'graded_new' : ['Newly graded areas',77,86,91,94],
			'pasture_poor' : ['Pasture, Grassland, or Range, Poor Condition',68,79,86,89],
			'pasture_fair' : ['Pasture, Grassland, or Range, Fair Condition',49,69,79,84],
			'pasture_good' : ['Pasture, Grassland, or Range, Good Condition',39,61,74,80],
			'protected_meadow' : ['Meadow, protected from grazing',30,58,71,78],
			'brush_poor' : ['Brush - Brush, weed grass combination, Poor Condition',48,67,77,83],
			'brush_fair' : ['Brush - Brush, weed grass combination, Fair Condition',35,56,70,77],
			'brush_good' : ['Brush - Brush, weed grass combination, Good Condition',30,48,65,73],
			'wood_grass_poor' : ['Wood - Grass combination, Poor Condition',57,73,82,86],
			'wood_grass_fair' : ['Wood - Grass combination, Fair Condition',43,65,76,82],
			'wood_grass_good' : ['Wood - Grass combination, Good Condition',32,58,72,79],
			'wood_orchard_poor' : ['Woods (Orchard or Tree Farm), Poor Condition',45,66,77,83],
			'wood_orchard_fair' : ['Woods (Orchard or Tree Farm), Fair Condition',36,60,73,79],
			'wood_orchard_good' : ['Woods (Orchard or Tree Farm), Good Condition',30,55,70,77],
			'farmsteads_and_construction' : ['Farmsteads, buildings, lanes, driveways, and surrounding lots',59,74,82,86],
			'open_water' : ['Open water: lakes, wetlands, ponds, etc.',100,100,100,100]
	}
	titles = {'cover_id' : ['cover Description', 'A', 'B', 'C', 'D']}
	return cover_discription_dict, titles

#print(list(cover_discription().keys()))