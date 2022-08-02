import sys
from game_components.ship import Ship
from game_components.world import Environment


ship = Ship()



print( ship.description() )

e = Environment()

e.oxygen = 20
e.carbon_dioxide = 5

print( e.threat_assessment() )

e.nitrogen = 0
e.oxygen = 0
e.carbon_dioxide = 0

print( e.threat_assessment() )







