# Constants for planet surface gravity factors
nMERCURY_GRAVITY = 0.38
nVENUS_GRAVITY = 0.91
nMOON_GRAVITY = 0.165
nMARS_GRAVITY = 0.38
nJUPITER_GRAVITY = 2.34
nSATURN_GRAVITY = 0.93
nURANUS_GRAVITY = 0.92
nNEPTUNE_GRAVITY = 1.12
nPLUTO_GRAVITY = 0.066

# Prompt user for their name
sUSER_NAME_INPUT = input("What is your name: ")

# Prompt user for their weight
sUSER_WEIGHT_INPUT = input("What is your weight: ")
nWEIGHT = float(sUSER_WEIGHT_INPUT)

# Output introduction message
print(f"{sUSER_NAME_INPUT} here are your weights on our Solar System’s planets:")

# named list of planets and gravity
for sPLANET, nGRAVITY in {
    "MERCURY": nMERCURY_GRAVITY,
    "VENUS": nVENUS_GRAVITY,
    "MOON": nMOON_GRAVITY,
    "MARS": nMARS_GRAVITY,
    "JUPITER": nJUPITER_GRAVITY,
    "SATURN": nSATURN_GRAVITY,
    "URANUS": nURANUS_GRAVITY,
    "NEPTUNE": nNEPTUNE_GRAVITY,
    "PLUTO": nPLUTO_GRAVITY,
}.items():
    nWEIGHT_ON_PLANETS = nWEIGHT * nGRAVITY
    # Print formatted weight that take up 10 postions
    print(f" Weight on {sPLANET:<10}: {nWEIGHT_ON_PLANETS:>10.2f}")

# Wait for user input before closing
input("Press 'Enter' to close the script.")  

