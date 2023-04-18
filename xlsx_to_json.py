import sys
import pandas as pd
import json

# Get the input filename from the command line argument
input_file = sys.argv[1]

# Read the Excel file using pandas
df = pd.read_excel(input_file)

# Convert the data to a list of dictionaries
data = df.to_dict(orient='records')

# Use a default filename for the output file
output_file = 'output.json'

# Write the JSON data to a file
with open(output_file, 'w') as f:
    json.dump(data, f)
