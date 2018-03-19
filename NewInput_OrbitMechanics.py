#This program calculates the delta velocity needed to go from a circular orbit around the sun
#to an elliptical orbit to your desired planet(Mars)
#Created By: Greta Studier
#Date Created: 3/7/18

import numpy as np
import pandas as pd

#USER INPUTS:

Planet =

# [1] for Star 48/Star 37
# [2] for Star 63D
# [3] for Orbus 21/Orbus 6
Propellant =

# [1] optimize length (input case radius and bore radius)
# [2] optimize bore radius (input length and case radius)
# [3] optimize case radius (input bore radius and length)
Optimize =

#Please choose one to Optimize by setting it equal to the variable optimize: "= optimize"
Length =
CaseRadius =
BoreRadius =




data = pd.DataFrame(columns = ['Planet', 'Propellant', 'VelCirc', 'VelEllipt', 'DeltaV', 'PropMass', 'Length' ,'CaseRadius', 'BoreRadius'])
#----------------------------------------------------------------------------------
#INPUTS










perihelion = 149599650.0 #km for Sun to Earth
