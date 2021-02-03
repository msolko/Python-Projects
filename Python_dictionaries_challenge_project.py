# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def new_damages(damages_list):
    new_damages_list = []
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for i in damages_list:
        if i[-1] in conversion.keys():
            new_damage = float(i[:-1])*conversion[i[-1]]
            new_damages_list.append(new_damage)
        elif i == "Damages not recorded":
            new_damages_list.append(i)
    return new_damages_list
new_damage = new_damages(damages)
##print(new_damage)

# write your construct hurricane dictionary function here:

def new_hurricane_dictionary(name, month, year, wind, area, damage, death):
    new_dict = {}
    for i in range(len(name)):
        new_dict[name[i]] = {"Name":name[i], "Month":month[i],
                             "Year":year[i], "Max Sustained Wind": wind[i],
                             "Areas Affected": area[i], "Damage": damage[i],
                             "Death": death[i]}
    return new_dict
hurricane_data = new_hurricane_dictionary(names,months,years,max_sustained_winds,areas_affected,
                               new_damage,deaths)
##print(hirricane_data)

# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(hurricane_dictionary):
    new_dictionary = {}
    for entry in hurricane_dictionary:
        year = hurricane_dictionary[entry]['Year']
        hurricane_data = hurricane_dictionary[entry]
        if year in new_dictionary:
            new_dictionary[year].append(hurricane_data)
        else:
            new_dictionary[year] = [hurricane_data]
    return new_dictionary
##temp = hurricanes_by_year(hurricane_data)
##for i in temp:
##    print(i,temp[i])
##print(hurricanes_by_year(hurricane_data))

# write your count affected areas function here:
def area_affected_count(hurricane_dictionary):
    new_dictionary = {}
    for entry in hurricane_dictionary:
        areas_affected = hurricane_dictionary[entry]['Areas Affected']
        for area in areas_affected:
            if area in new_dictionary:
                new_dictionary[area] += 1
            else:
                new_dictionary[area] = 1
    return new_dictionary
a_a_d = area_affected_count(hurricane_data)
##print(a_a_d)

# write your find most affected area function here:
def most_hit_area(area_dictionary):
    temp = max(area_dictionary, key = area_dictionary.get)
    return temp, area_dictionary[temp]
##print(most_hit_area(a_a_d))

# write your greatest number of deaths function here:
def most_tragic(hurricane_dictionary):
    temp = max(hurricane_dictionary, key=lambda x: hurricane_dictionary[x]['Death'])
    return temp, hurricane_dictionary[temp]['Death']
##print(most_tragic(hurricane_data))

# write your catgeorize by mortality function here:
def mortality_scale(hurricane_dictionary):
    mortality_scale = {0:0,
                       1:100,
                       2:500,
                       3:1000,
                       4:10000}
    new_dictionary = {1:[],
                      2:[],
                      3:[],
                      4:[],
                      5:[]}
    for entry in hurricane_dictionary:
        death = hurricane_dictionary[entry]['Death']
        hurricane_data = hurricane_dictionary[entry]
        for i in range(5):
            if death > mortality_scale[4-i]:
                new_dictionary[5-i].append(hurricane_data)
                break
    return new_dictionary
##print(mortality_scale(hurricane_data))

# write your greatest damage function here:
def most_damage(hurricane_dictionary):
    temp_dict = {}
    for entry in hurricane_dictionary:
        damage = hurricane_dictionary[entry]['Damage']
        if damage != "Damages not recorded":
            temp_dict[entry] = hurricane_dictionary[entry]
    temp = max(temp_dict, key=lambda x: temp_dict[x]['Damage'])
    return temp, hurricane_dictionary[temp]['Damage']
##print(most_damage(hurricane_data))

# write your catgeorize by damage function here:
def damage_scale(hurricane_dictionary):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    new_dictionary = {1:[],
                      2:[],
                      3:[],
                      4:[],
                      5:[]}
    for entry in hurricane_dictionary:
        damage = hurricane_dictionary[entry]['Damage']
        hurricane_data = hurricane_dictionary[entry]
        if damage != "Damages not recorded":
            for i in range(5):
                if damage > damage_scale[4-i]:
                    new_dictionary[5-i].append(hurricane_data)
                    break
    return new_dictionary
##for i in range(5):
##    print(damage_scale(hurricane_data)[i+1])

