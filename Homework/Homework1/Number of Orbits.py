""" 
    File : Favorite Things
    Author : Jayden Mautsa 
    Date : 9/12/2025
    Section : Homework 1
    E-mail : jmautsa1@umbc.edu
    Description : This is about orbites 
    """

# Constants for our cosmic voyage
mu = 6.6743 * 5.97219 * (10 ** 13)
pi = 3.1415927
radius = 6371000  

# Ask the user for altitude and orbit time
altitude_km = float(input("What is yer altitude in km, ye landlubber? "))
time_min = float(input("How long in minutes do ye spend in that orbit? "))

r = radius + (altitude_km * 1000)

v0 = (mu / r) ** 0.5

circumference = 2 * pi * r

time_per_orbit = (circumference / v0) / 60

num_orbits = (time_min * 60) * v0 / circumference

print(f"The orbital speed be {v0} m/s and the circumference of the orbit be {circumference} m.")
print(f"Each orbit takes {time_per_orbit} minutes and the number of orbits be {num_orbits}.")

