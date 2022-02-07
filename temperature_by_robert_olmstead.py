import csv

with open('temperature_readings.csv', newline='') as temperature_readings:
    temperature_reader = csv.DictReader(temperature_readings)

print('''INSERT INTO Person (Taken, Temp)
VALUES)