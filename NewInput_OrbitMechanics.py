#This program calculates the delta velocity needed to go from a circular orbit around the sun
#to an elliptical orbit to your desired planet(Mars)
#Created By: Greta Studier
#Date Created: 3/7/18

import numpy as np
import pandas as pd
data = pd.DataFrame(columns = ['Planet', 'Propellant', 'VelCirc', 'VelEllipt', 'DeltaV', 'PropMass', 'Length' ,'CaseRadius', 'BoreRadius'])
#---USER INPUTS----------------------------------------------------------------------------------------------------

planet = 'Mars'
payloadMass = 1063.00 #kg
ISP = 300
fIntert = 0.09

# [1] for Star 48/Star 37
# [2] for Star 63D
# [3] for Orbus 21/Orbus 6
propellant = 1

#Please choose one to Optimize by setting it equal 'optimize'
length = 2.0
caseradius = 'optimize'
boreradius = 0.2344


#---FUNCTIONS----------------------------------------------------------------------------------------------------
def Planet(Planet):
    aps = {'mars': 228000000.0,
       'mercury': 57909050.0,
       'venus': 108900000.0,
       'jupiter': 817000000.0,
       'saturn': 1500000000.0,
       'uranus': 3006900000.0,
       'neptune': 4547800000.0}

    while True:
        if Planet.lower() in aps:
            aphelion = aps[Planet.lower()]
            data.loc[0, 'Planet'] = Planet
            break
        else:
            print 'Sorry that\'s not a planet! '
    return aphelion

def Propellant(Propellant):
    loop = True
    while loop:
        if Propellant == 1:
            rho = 1800  # kg/m^3
            # print '\nPropellant: ', 'Star 48/Star 37'
            data.loc[0, 'Propellant'] = 'Star 48/Star 37'
            loop = False
        elif Propellant == 2:
            rho = 1800  # kg/m^3
            data.loc[0, 'Propellant'] = 'Star 63D'
            loop = False
        elif Propellant == 2:
            rho = 108900000.0
            data.loc[0, 'Propellant'] = 'Orbus 21/Orbus 6'
            loop = False
        else:
            print 'Sorry please choose 1, 2, or 3 for Propellant! '
    return rho

def Velocity():
    mu_sun = 132715440000.0  # km^3/s^2                                   #gravitational parameter
    r_ES = 149599650.0  # km                                              #Earth-Sun radius
    perihelion = 149599650.0  # km for Sun to Earth
    epsilon = -1 * (mu_sun / (perihelion + Planet(planet)))

    v_circular = np.sqrt(mu_sun / r_ES)  # velocity needed to get into circular orbit around sun from Earth
    v_transfer_elliptical = np.sqrt(2 * ((mu_sun / perihelion) + (epsilon)))  # circular orbit to elliptical orbit
    delta_v = v_transfer_elliptical - v_circular

    data.loc[0, 'VelCirc'] =  "%.2f" %v_circular
    data.loc[0, 'VelEllipt'] = "%.2f" % v_transfer_elliptical
    data.loc[0, 'DeltaV'] = "%.2f" %delta_v
    return delta_v

rho = 18000
def PropMass(rho,m_pay,finert,l,c,b):
    g0 = 9.8067/1000 #km/s^2
    m_prop = abs((m_pay*(np.exp(Velocity()/(ISP*g0))-1)*(1-finert))/(1-finert*(np.exp(Velocity()/(ISP*g0)))))

    loop = True
    while loop:
        if l == 'optimize':
            B = b
            C = c
            L = m_prop / (np.pi * rho * (C ** 2 - B ** 2))
            loop = False
        elif b == 'optimize':
            L = l
            C = c
            B = np.sqrt((np.pi * L * C ** 2 * rho - m_prop) / (np.pi * L * rho))
            loop = False
        elif c == 'optimize':
            L = l
            B = b
            C = np.sqrt((np.pi * length * B ** 2 * rho + m_prop) / (np.pi * L * rho))
            loop = False
        else:
            print 'Sorry please try again! '
    data.loc[0, 'PropMass'] = "%.2f" % m_prop
    data.loc[0, 'Length'] = "%.2f" % L
    data.loc[0, 'CaseRadius'] = "%.2f" % C
    data.loc[0, 'BoreRadius'] = "%.2f" % B

def Pressure(rho):
    press = ((a*rho*Ab*c_star)/(At))**(1/(1-n))
    burnrate = a*press**n


def Outputs():
    Planet(planet)
    Propellant(propellant)
    Velocity()
    PropMass(rho,payloadMass,fIntert,length,caseradius,boreradius)
    print data
Outputs()

