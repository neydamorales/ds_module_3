# Modules
import csv

# Set path for file
csvpath = r"C:\Users\polit\Desktop\Data Analytics Bootcamp\homework\ds_module_3\Starter_Code\PyPoll\Resources\election_data.csv"

# variables
vote_count = 0
candidate_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # count votes
        vote_count = vote_count + 1
  
        # calculating votes per candidate by adding to dictionary
        row_candidate = row[2]
        
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

print(vote_count)
print(candidate_dict)    

# creating output
output = f"""Election Results 
-------------------------
Total Votes: {vote_count}
-------------------------\n"""
max_candidate = ""
max_votes = 0

for candidate in candidate_dict.keys():
    # gathering votes and percentage of votes per candidate
    votes = candidate_dict[candidate]
    percent = 100 * (votes / vote_count)

    line = f"{candidate}: {round(percent, 3)}% ({votes})\n"
    output += line

    # getting winner 
    if votes > max_votes:
        max_candidate = candidate
        max_votes = votes 

last_line = f"""-------------------------
Winner: {max_candidate}
-------------------------"""
output += last_line

print(output)

with(open("output_pypoll_neyda.txt", 'w') as f):
        f.write(output) 
