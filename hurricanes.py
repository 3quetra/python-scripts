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


# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages():
  return [float(damage_record[:-1]) * conversion[damage_record[-1]] if not damage_record == 'Damages not recorded' else 'Damages not recorded' for damage_record in damages]

# Save updated damages in a variable to use later
updated_damages = update_damages()



# Create and organise hurricanes dictionary by name 
def hurricanes_byName():
  hurricanes_dict_byNames = {}
  for index in range(len(names)):
    hurricanes_dict_byNames[names[index]] = {
      'Name': names[index],
      'Month': months[index],
      'Year': years[index],
      'Max Sustained Wind': max_sustained_winds[index],
      'Areas Affected': areas_affected[index],
      'Damage': updated_damages[index],
      'Deaths': deaths[index]
    }
  return hurricanes_dict_byNames
print(hurricanes_byName())
# Save hurricanes dictionary by name in a variable to use later
hurricanes = hurricanes_byName()
# Output hurricanes dict
print(hurricanes)



# Create and organise hurricanes dictionary by year
def hurricanes_byYear():
  hurricanes_dict_byYear = {} 
  for hurricane in hurricanes.values():
    if not hurricane['Year'] in hurricanes_dict_byYear:
      hurricanes_dict_byYear[hurricane['Year']] = []

    hurricanes_dict_byYear[hurricane['Year']].append(hurricane)
  return hurricanes_dict_byYear
print(hurricanes_byYear())


# Counting Damaged Areas
def area_count():
  hurricanes_dict_areas = {}
  for hurricane in hurricanes.values():
    for area in hurricane['Areas Affected']:
      if not area in hurricanes_dict_areas:
        hurricanes_dict_areas[area] = 0
      hurricanes_dict_areas[area] += 1    
  return hurricanes_dict_areas
print(area_count())      

# Save Damaged Areas values in a variable to use later
hurricanes_dict_areas = area_count()

# Calculating Maximum Hurricane Count
def find_max_affected_area():
  max_affected_area = ('max affected area name', -1)
  for element in hurricanes_dict_areas.items():
    if element[1] > max_affected_area[1]:
      max_affected_area = element
  return max_affected_area
print(find_max_affected_area())

# Calculating the Deadliest Hurricane
def find_deadliest():
  deadliest = ('deadliest hurricane name', -1)
  for hurricane_value in hurricanes.values():
    if hurricane_value['Deaths'] > deadliest[1]:
      deadliest = hurricane_value['Name'], hurricane_value['Deaths']
  return deadliest
# output highest mortality hurricane and the number of deaths
print(find_deadliest())


def find_mortality_rate(hurricane_value):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                   5: float('inf')}
  for mortality_rate, mortality_threshold in mortality_scale.items():
    if hurricane_value['Deaths'] <= mortality_threshold:
      return mortality_rate

# Rating Hurricanes by Mortality
def hurricanes_by_mortality():
  dict_hurricanes_by_mortality = {}
  for hurricane_value in hurricanes.values():
    mortality_rate = find_mortality_rate(hurricane_value)
    if not mortality_rate in dict_hurricanes_by_mortality:
      dict_hurricanes_by_mortality[mortality_rate] = []
    dict_hurricanes_by_mortality[mortality_rate].append(hurricane_value)
  return dict_hurricanes_by_mortality
# output hurricanes in new dictionary with mortality severity as key
print(hurricanes_by_mortality())


# Calculating Hurricane Maximum Damage
def find_max_demage_hurricane():
  max_demage_hurricane = ('hurricane name', -1)
  for hurricane_value in hurricanes.values():
    if not hurricane_value['Damage'] == 'Damages not recorded' and hurricane_value['Damage'] > max_demage_hurricane[1]:
      max_demage_hurricane = hurricane_value['Name'], hurricane_value['Damage']
  return max_demage_hurricane
# find highest damage inducing hurricane and its total cost
print(find_max_demage_hurricane())

# Rating Hurricanes by Damage
def find_damage_rate(hurricane_value):
  if hurricane_value['Damage'] == 'Damages not recorded':
    return 'Damages not recorded'
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000,
                5: float('inf')}
  for damage_rate, damage_threshold in damage_scale.items():
    if hurricane_value['Damage'] <= damage_threshold:
      return damage_rate

# Rating Hurricanes by Damage
def hurricanes_by_damages():
  dict_hurricanes_by_damage = {}
  for hurricane_value in hurricanes.values():
    damage_rate = find_damage_rate(hurricane_value)
    if not damage_rate in dict_hurricanes_by_damage:
      dict_hurricanes_by_damage[damage_rate] = []
    dict_hurricanes_by_damage[damage_rate].append(hurricane_value['Name'])
  return dict_hurricanes_by_damage
  # Output categorized hurricanes in new dictionary with damage severity as key
print(hurricanes_by_damages())


  

