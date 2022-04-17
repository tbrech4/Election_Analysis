# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initializing counter

total_votes = 0

# Initialize canidate list

candidate_options = []

# Initialize dictionary where votes will go

candidate_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here. Everything must be indented until we close election_data csv
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        # Add to total vote count

        total_votes += 1

        #Print candidate name from each row

        candidate_name = row[2]

        # Add the candidate name to the candidate list if candidate name not previously in list 

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        # Add vote for each candidate, outside of if statement

        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
      #  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.

            winning_count = votes
            winning_percentage = vote_percentage

        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
        
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    
    txt_file.write(election_results)

    candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    print(candidate_results)

    txt_file.write(candidate_results)

    #  winning_candidate_summary = (
    #     f"-------------------------\n"
        #    f"Winner: {winning_candidate}\n"
        #    f"Winning Vote Count: {winning_count:,}\n"
        #    f"Winning Percentage: {winning_percentage:.1f}%\n"
        #   f"-------------------------\n")

    #print(winning_candidate_summary)
    



