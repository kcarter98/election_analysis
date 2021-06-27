# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of total votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to load the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter
total_votes = 0

# Initialize Candidates list
candidate_options = []

# Initialize Candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
     
     # Read and print the header row.
     headers = next(file_reader)
     
     # Print each row in the CSV file.
     for row in file_reader:
        # Add total vote count
          total_votes += 1
        
          candidate_name = row[2]
        # Add candidate to list if not there already
          if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             
             # Begin tracking candidates vote count
             candidate_votes[candidate_name] = 0

          # Add Vote Count
          candidate_votes[candidate_name] += 1
          
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
  election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
  )
  print(election_results, end = "")
  # Save the final vote to the text file
  txt_file.write(election_results)
            

  # Determine the percentage of votes for each candidate by looping through the counts.
  # Iterate through the candidate list.
  for candidate_name in candidate_votes:
      # Retrieve vote count of a candidate.
      votes = candidate_votes[candidate_name]
      # Calculate the percentage of votes.
      vote_percentage = float(votes) / float(total_votes) * 100
      
      # Create candidates results variable
      candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      # Print each candidate, their voter count, and percentage to the terminal.
      print(candidate_results)
      #  Save the candidate results to our text file.
      txt_file.write(candidate_results)
      
      # Determine winning vote count and candidate
      if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        
  winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")
  print(winning_candidate_summary)

  txt_file.write(winning_candidate_summary)