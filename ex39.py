import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

print '-' * 10
hashmap.list(states)

print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# states = {
# 	'Oregon': 'OR',
# 	'Florida': 'FL',
# 	'California': 'CA',
# 	'New York': 'NY',
# 	'Michigan': 'MI'
# }
# 
# cities = {
# 	'CA': 'San Francisco',
# 	'MI': 'Detroit',
# 	'FL': 'Jacksonville'
# }
# 
# cities['NY'] = 'New York'
# cities['OR'] = 'Porland'
# 
# print '-' * 10
# print "NY State has: ", cities['NY']
# print "OR State has: ", cities['OR']
# 
# print '-' * 10
# print "Michigan has: ", cities[states["Michigan"]]
# print "Florida has: ", cities[states['Florida']]
# 
# print '-' * 10
# for state, abbrev in states.items():
# 	print "%s is abbreviated %s" % (state, abbrev)
# 	
# print '-' * 10
# for abbrev, city in cities.items():
# 	print "%s has the city %s" % (abbrev, city)
# 	
# print '-' * 10
# for state, abbrev in states.items():
# 	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
# 	
# print '-' * 10
# state = states.get("Texas")
# 
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city