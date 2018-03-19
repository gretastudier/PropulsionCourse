#This program calculates the delta velocity needed to go from a circular orbit around the sun
#to an elliptical orbit to your desired planet(Mars)
#Created By: Greta Studier
#Date Created: 3/7/18

import numpy as np
import pandas as pd
data = pd.DataFrame(columns = ['Planet', 'Propellant', 'VelCirc', 'VelEllipt', 'DeltaV', 'PropMass', 'Length' ,'CaseRadius', 'BoreRadius'])
#---USER INPUTS----------------------------------------------------------------------------------------------------

planet = 'Mars'

ISP = 300

fIntert = 0.09

# [1] for Star 48/Star 37
# [2] for Star 63D
# [3] for Orbus 21/Orbus 6
Propellant = 1

#Please choose one to Optimize by setting it equal to the variable optimize: "= optimize"
Length = 2.0
#CaseRadius = optimize
BoreRadius = 0.2344

def Planet(Planet):
    loop = True
    while loop:
        if Planet == 'Mars' or Planet == 'mars':
            aphelion = 228000000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Mercury' or Planet == 'mercury':
            aphelion = 57909050.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Venus' or Planet == 'venus':
            aphelion = 108900000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Jupiter' or Planet == 'jupiter':
            aphelion = 817000000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Saturn' or Planet == 'saturn':
            aphelion = 1500000000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Uranus' or Planet == 'uranus':
            aphelion = 3006900000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        elif Planet == 'Neptune' or Planet == 'neptune':
            aphelion = 4547800000.0
            data.loc[0, 'Planet'] = Planet
            loop = False
        else:
            print 'Sorry that\'s not a planet! '

        return aphelion

def Propellant():
    loop = True
    while loop:
        if Propellant == '1':
            rho = 1800  # kg/m^3
            # print '\nPropellant: ', 'Star 48/Star 37'
            data.loc[0, 'Propellant'] = 'Star 48/Star 37'
            loop = False
        elif Propellant == '2':
            rho = 1800  # kg/m^3
            data.loc[0, 'Propellant'] = 'Star 63D'
            loop = False
        elif Propellant == '3':
            rho = 108900000.0
            data.loc[0, 'Propellant'] = 'Orbus 21/Orbus 6'
            loop = False
        else:
            print 'Sorry please choose 1, 2, or 3 for Propellant! '




Planet(planet)
print data
perihelion = 149599650.0 #km for Sun to Earth
