

class Environment:
    oxygen = 20.0
    nitrogen = 80.0
    carbon_dioxide = 0.05
    toxic_gases = 0.0
    hydrogen = 0.0
    temperature = 19

    def pressure(self):
        total_gases = self.oxygen + self.nitrogen + self.carbon_dioxide + self.toxic_gases
        pressure = total_gases / 100 * 14.7
        return pressure

    def threat_assessment(self):
        threats = []

        if ( self.oxygen < 6.0 ):
            threats.append( ["Lethal", "Oxygen level below 6%"] )
        elif ( self.oxygen < 12 ):
            threats.append( ["Danger", "Oxygen level below 12%"] )

        if ( self.carbon_dioxide > 8):
            threats.append( ["Lethal", "CO2 level above 8%"] )
        elif ( self.carbon_dioxide > 4):
            threats.append( ["Danger", "CO2 level above 4%"] )
        elif ( self.carbon_dioxide > 1.5 ):
            threats.append( ["Caution", "CO2 level above 1.5%" ] )

        if ( self.pressure() < 6 ):
            threats.append( ["Lethal", "Loss of pressure"] )
        
        
        if ( len(threats) == 0 ):
            return ( ["No threats"] )
        return threats

    