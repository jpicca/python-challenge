import csv

# Path to the input data
fname = './employee_data.csv'

# A dictionary to use for converting state names to abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create empty lists to hold our data
empID, firstName, lastName, dob, ssn, state = [],[],[],[],[],[]

# Open an input stream
with open(fname, 'r') as csvfile:
    
    # Create the reader object
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Grab the header information to use later
    header = next(csvreader)
    
    # Loop through rows of the reader object
    for row in csvreader:
        
        # Employee ID
        empID.append(row[0])
        
        # Grab the first name by splitting the name on the space and taking the first element
        firstName.append(row[1].split(" ")[0])
        
        # Take the second element of the split for the last name
        lastName.append(row[1].split(" ")[1])
        
        # Split on the hyphens to grab year/month/day for the formatted date
        dob.append(f'{row[2].split("-")[1]}/{row[2].split("-")[2]}/{row[2].split("-")[0]}')
                   
        # Split on the hyphens to format the SSN and hide first two parts
        ssn.append(f'***-**-{row[3].split("-")[2]}')
                   
        # Use the state dictionary to append the state abbreviation
        state.append(us_state_abbrev[row[4]])
                   
    # After loopign is complete, zip up our lists
    zipper = zip(empID,firstName,lastName,dob,ssn,state)
        
    # Have to update the header since we split the name
header.insert(1, 'First Name')
header[2] = 'Last Name'

# Open a stream to write our output
with open('./output.csv','w') as outputfile:
    
    # Create our writer object
    csvwriter = csv.writer(outputfile)
    
    # Write the header first
    csvwriter.writerow(header)
    
    # Write the zipped object to the file next
    csvwriter.writerows(zipper)