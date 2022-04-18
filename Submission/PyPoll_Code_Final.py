# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 2: Track the largest county and county voter turnout. Need to initialize largest_county variable as an empty string. The other two variables can be set to zero

largest_county = ""
largest_county_count = 0
largest_county_percentage = 0

# Opening election results CSV and converting data to dictionaries 

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header so that the for loop will read everything past header

    header = next(reader)

    # For each row in the CSV file (skips header)
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.

        candidate_name = row[2]

        # 3: Extracting county name from each row, county_name is second column in Election_results csv

        county_name = row[1]

        # Checking to see if candidate name is in the list, add candidate name to the list if it not already found in list.
        
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count by setting the candidate vote count for each candidate to zero. candidate name is column 3 in csv
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count

        candidate_votes[candidate_name] += 1

        # 4a: Checking to see if each county already existis in the county list
        
        if county_name not in county_list:


            # 4b: if the county isn't in county_list, then add it to county list

            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count by setting vote count to zero
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count

        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: For loop that gets each county name in county dictionary

    for county_name in county_votes:

        # 6b: Get the vote count for each county (Already calc'd in previous for loop)
        
        votes_county = county_votes[county_name]

        # 6c: Calculate the percentage of votes for each county.

        county_percentage = float(votes_county) / float(total_votes) * 100
        
        # 6d: Print the county results to the terminal, county percentage is formatted to one decimal 

        county_results = (
            f"{county_name}: {county_percentage: .1f}% ({votes_county:,})\n")
        
        print(county_results)

         # 6e: Save the county votes to a text file.

        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count. Checking if each county's votes are greater than the previous largest county. If so, it then becomes the largest county

        if (votes_county > largest_county_count) and (county_percentage > largest_county_percentage):
            largest_county_count = votes_county
            largest_county = county_name
            largest_county_percentage = county_percentage
    
    # 7: Print the county with the largest turnout to the terminal.

    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    
    # 8: Save the county with the largest turnout to a text file.

    txt_file.write(largest_county_summary)
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
