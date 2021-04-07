import sys
import random 

students = [
    "Samuel",
    "Ruan",
    "Roland",
    "Nur-Ayn",
    "Nicky",
    "Sergio",
    "William",
    "Rahul",
    "Sarah",
    "Georgi",
    "Grant",
    "Kabelo",
    "Gabriel",
    "Justin",
    "Sebastian"
]

random.shuffle(students) #randomise order of students

n = 2 # By default select 2 students

if len(sys.argv) == 2:
    n = int(sys.argv[1]) # In case one wants to mark more than 2

print("Students to mark:",students[:n]) 