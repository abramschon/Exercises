import sys
import random 

students = [
    "Samuel",
    "Ruan",
    "Roland",
    "Nicky",
    "Sergio",
    "William",
    "Georgi",
    "Kabelo",
    "Gabriel",
    "Justin",
    "Sebastian"
]

random.shuffle(students) #randomise order of students

n = 2 # By default select 2 students
if len(sys.argv) == 2:
    n = int(sys.argv[1]) # In case one wants to mark more than 2

with open("who_to_mark.txt", "a") as f:
    for tut in range(int(len(students)/n)):
        f.write(f"Tut {tut+1}\n {students[tut*n:tut*n+n]}\n") 
        
