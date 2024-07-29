# Program for the measurement of temperture
# as a function of time using PT1000 and ExpEYES

# Establish Connection
import eyes17.eyes
p = eyes17.eyes.open()

# Import python libreary 
import time, math
import numpy as np

t0=time.time()                  # Time initialization
# Measure the temperature
while True:                     # For Contineous measurement
   R0 = 1000                    # PT1000 (RTD Name)
   Alpha = 3.85/1000            # Temperature coefficient
   n = 10                       # NO of measurements for averaging
   Rsum = 0
   for x in range (0,n):        # Loop for averaging
      r = p.get_resistance()    # Measure the resistance in ohm
      Rsum = Rsum+r             # Sum of resistance
   R = Rsum/n                   # Average resistance
   T = (1/Alpha)*((R/R0)-1)     # Calculate Temperature from Resistance
   ts=time.time()               # current time
   t=ts-t0                      # Difference time
   print("%4.2f" % t, "S", "  ","%4.1f" % T,"°C") # Print on screen
   file = open ("Temperature.dat", "a") # Appending file
   file.write("{0:4.2f} {1:4.1f}\n".format(t,T)) #write on file  
   time.sleep(1)                # Wait for 1 sec
file.close()                    
