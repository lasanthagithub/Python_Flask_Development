class Cover_Descriptions:
    def __ini__(self):
        self.cover_discription_dict = {
            'open_poor' : 'Open Space, Poor Condition (Grass cover <50%)',
            'open_fair' : 'Open Space, Fair Condition (Grass cover 50% to 75%)',
            'open_good' :'Open Space, Good Condition (Grass cover >75%)',
            'roadway_paved' : 'Roadway Impervious Area, Paved',
            'curb_paved' : 'Paved; Curbs and storm sewers',
            'ditches_paved' : 'Paved; Open Ditches',
            'gravel' : 'Gravel',
            'dirt' : 'Dirt',
            'natur_desert_landscape' : 'Natural Desrt Lanscaping',
            'artif_desert_landscape' : 'Artificial Desrt Lanscaping',
            'urban_commercial' : 'Urban Districts: Commercial and Business',
            'urban_industrial' : 'Urban Districts: Industrial',
            'residential_65' : 'Residential: 65% Impervious (1/8 Acre)',
            'residential_38' : 'Residential: 38% Impervious (1/4 Acre)',
            'residential_30' : 'Residential: 30% Impervious (1/3 Acre)',
            'residential_25' : 'Residential: 25% Impervious (1/2 Acre)',
            'residential_20' : 'Residential: 20% Impervious (1 Acre)',
            'residential_12' : 'Residential: 12% Impervious (2 Acre)',
            'graded_new' : 'Newly graded areas',
            'pasture_poor' : 'Pasture, Grassland, or Range, Poor Condition',
            'pasture_fair' : 'Pasture, Grassland, or Range, Fair Condition',
            'pasture_good' : 'Pasture, Grassland, or Range, Good Condition',
            'protected_meadow' : 'Meadow, protected from grazing',
            'brush_poor' : 'Brush - Brush, weed grass combination, Poor Condition',
            'brush_fair' : 'Brush - Brush, weed grass combination, Fair Condition',
            'brush_good' : 'Brush - Brush, weed grass combination, Good Condition',
            'wood_grass_poor' : 'Wood - Grass combination, Poor Condition',
            'wood_grass_fair' : 'Wood - Grass combination, Fair Condition',
            'wood_grass_good' : 'Wood - Grass combination, Good Condition',
            'wood_orchard_poor' : 'Woods (Orchard or Tree Farm), Poor Condition',
            'wood_orchard_fair' : 'Woods (Orchard or Tree Farm), Fair Condition',
            'wood_orchard_good' : 'Woods (Orchard or Tree Farm), Good Condition',
            'farmsteads_and_construction' : 'Farmsteads, buildings, lanes, driveways, and surrounding lots',
            'open_water' : 'Open water: lakes, wetlands, ponds, etc.'
            }

a = Cover_Descriptions()
print(a.cover_discription_dict)



