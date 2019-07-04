import csv
import sys
import os

def transcribe(i, o):

	if !os.path.isdir(o):
		os.mkdir(o)

	with open(i, mode='r') as csv_file:
		reader = csv.DictReader(csv_file)
		count = 0
		for row in reader:
			if count == 0:
				headers = row
			else:
				with open(f'{o}/{row[rows[0]]}.txt', mode="w+") as file:
					for key in rows:
						file.write(f'{key}: {row[key]}\n')
		return
	# Open CSV File
	# If dir doesnt exist, create.
	# Loop through rows
	# Create text file in that directory with name as first row
	# Loop through properties of row
	# Write to text file with format: 'Name of Row: Value'
	# Return directory