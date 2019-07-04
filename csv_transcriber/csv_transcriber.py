import csv
import sys
import os

def transcribe(i, o):

	if not os.path.isdir(o):
		os.mkdir(o)

	with open(i, mode='r') as csv_file:
		re = list(csv.reader(csv_file))
		headers = re[0]
		for row in re[1:]:
			with open(f'{o}/{row[0]}.txt', mode="w+") as file:
				for key in range(len(headers)):
					file.write(f'{headers[key]}: {row[key]}\n')
		return
	# Open CSV File
	# If dir doesnt exist, create.
	# Loop through rows
	# Create text file in that directory with name as first row
	# Loop through properties of row
	# Write to text file with format: 'Name of Row: Value'
	# Return directory
