#This program calculates the delta velocity needed to go from a circular orbit around the sun
#to an elliptical orbit to your desired planet(Mars)
#
#Created By: Greta Studier
#Date Created: 3/7/18

import numpy as np
import pandas as pd
data = pd.DataFrame(columns = ['Planet', 'Propellant', 'VelCirc', 'VelEllipt', 'DeltaV', 'PropMass', 'Length' ,'CaseRadius', 'BoreRadius'])
#----------------------------------------------------------------------------------
#INPUT(perahelion = earth to sun distance | apahelion = sun to planet distance)

perihelion = 149599650.0 #km for Sun to Earth

#Get Planet and aphelion distance for calculating velocity
aps = {'mars': 228000000.0,
       'mercury': 57909050.0,
       'venus': 108900000.0,
       'jupiter': 817000000.0,
       'saturn': 1500000000.0,
       'uranus': 3006900000.0,
       'neptune': 4547800000.0}

while True:
    choice = raw_input("Please enter planet you wish to travel to: ")
    #choice = 'mars'
    if choice.lower() in aps:
        aphelion = aps[choice.lower()]
        data.loc[0,'Planet'] = choice
        break
    else:
        print 'Sorry that\'s not a planet! '

#Get type of propellant for calculating propulsion mass
loop = True
while loop:
    choice = raw_input("\n[1] for Star 48/Star 37\n[2] for Star 63D\n[3] for Orbus 21/Orbus 6\nPlease choose propellant you wish to use: ")
    #choice = '1'
    if choice == '1':
        rho = 1800 #kg/m^3
        #print '\nPropellant: ', 'Star 48/Star 37'
        data.loc[0, 'Propellant'] = 'Star 48/Star 37'
        loop=False
    elif choice == '2':
        rho = 1800  # kg/m^3
        data.loc[0, 'Propellant'] = 'Star 63D'
        loop = False
    elif choice == '3' :
        rho = 108900000.0
        data.loc[0, 'Propellant'] = 'Orbus 21/Orbus 6'
        loop = False
    else:
        print 'Sorry please choose 1, 2, or 3! '

def Velocity():
    mu_sun = 132715440000.0  # km^3/s^2                                   #gravitational parameter
    r_ES = 149599650.0  # km                                              #Earth-Sun radius
    epsilon = -1 * (mu_sun / (perihelion + aphelion))

    v_circular = np.sqrt(mu_sun / r_ES)  # velocity needed to get into circular orbit around sun from Earth
    v_transfer_elliptical = np.sqrt(2 * ((mu_sun / perihelion) + (epsilon)))  # circular orbit to elliptical orbit
    delta_v = v_transfer_elliptical - v_circular


    data.loc[0, 'VelCirc'] =  "%.2f" %v_circular
    data.loc[0, 'VelEllipt'] = "%.2f" % v_transfer_elliptical
    data.loc[0, 'DeltaV'] = "%.2f" %delta_v
    return delta_v

    # print "\nVelocity Circular: ", ("%.2f" % v_circular), '(km/s)'
    # print "Velocity Elliptical: ", ("%.2f" % v_transfer_elliptical), '(km/s)'
    # print "Velocity Transfer: ", ("%.2f" % delta_v), '(km/s)'

def PropMass():
    # finert = raw_input("Please enter desired finert: ")
    # ISP = raw_input("Please enter desired ISP: ")
    # pay = raw_input("Please enter Payload Mass(kg): ")

    finert = 0.09 #from 0.05-0.15
    ISP = 300.00 #from 260-300
    m_pay = 1063.00 #kg
    g0 = 9.8067/1000 #km/s^2

    m_prop = abs((m_pay*(np.exp(Velocity()/(ISP*g0))-1)*(1-finert))/(1-finert*(np.exp(Velocity()/(ISP*g0)))))

    loop = True
    while loop:
        choice = raw_input(
            "\n[1] optimize length (input case radius and bore radius)\n[2] optimize bore radius (input length and case radius)\n[3] optimize case radius (input bore radius and length)\nPlease choose what you wish to optimize: ")
        if choice == '1':
            in1 = raw_input("Please enter Case Radius of rocket motor in meters: ")
            r_case = float(in1)  # m
            in2 = raw_input("Please enter Bore Radius of rocket motor in meters: ")
            r_bore = float(in2)
            length = m_prop / (np.pi * rho * (r_case ** 2 - r_bore ** 2))
            loop = False
        elif choice == '2':
            in1 = raw_input("Please enter Length of rocket motor in meters: ")
            length = float(in1)  # m
            in2 = raw_input("Please enter Case Radius of rocket motor in meters: ")
            r_case = float(in2)  # m
            r_bore = np.sqrt((np.pi * length * r_case ** 2 * rho - m_prop) / (np.pi * length * rho))
            loop = False
        elif choice == '3':
            in1 = raw_input("Please enter Length of rocket motor: ")
            length = float(in1)  # m
            in2 = raw_input("Please enter Bore Radius of rocket motor: ")
            r_bore = float(in2)  # m
            r_case = np.sqrt((np.pi * length * r_bore ** 2 * rho + m_prop) / (np.pi * length * rho))
            loop = False
        else:
            print 'Sorry please choose 1, 2, or 3! '

    data.loc[0, 'PropMass'] = "%.2f" % m_prop
    data.loc[0, 'Length'] = "%.2f" % length
    data.loc[0, 'CaseRadius'] = "%.2f" % r_case
    data.loc[0, 'BoreRadius'] = "%.2f" % r_bore
    # return "%.2f"%m_prop, "%.2f"%length, "%.2f"%r_case, "%.2f"%r_bore #  mass_prop]

def Outputs():
    Velocity()
    PropMass()
    print data
Outputs()
