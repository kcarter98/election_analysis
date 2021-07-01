# Election_Analysis

## Resources
- Data Source: election_results.csv
- Software: Python, Visual Studio Code

## Candidate Analysis Overview 
A Colorado Board of Elections emplyee has given the following tasks to complete the election audit of a recent local election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winner of the election based on popular vote.

## Candidate Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
	- Diana DeGette received 73.8% of the vote and 272,892 votes.	
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
-The winner of the election was:
	- Diana DeGette, who received 73.8% of the votes and 272,892 votes.

## County Analysis Overview
The election commission had additional tasks needed to complete the election audit regarding the county data.

1. Get a complete list of counties where votes were cast.
2. Calculate the voter turnout for each county.
3. Calculate the percentage of votes from each county out of the total count.
4. Determine the county with the highest vote count.

## County Results
The additional analysis of the county election data shows that:
- The counties were:
	- Denver
	- Jefferson
	- Arapahoe
- The county results were:
	- Denver county received 82.8% of the total votes and 306,055 votes.
	- Jefferson county received 10.5% of the total votes and 38,855 votes.
	- Arapahoe county received 6.7% of the total votes and 24,801 votes.
- The county with the highest vote count was:
	- Denver, which received 82.8% of the total votes and 306,055 votes.

## Summary
The program within this project is able to take a CSV taking three lines coulmns of election data, ID, county, and candidate chosen, and tell you about various election data. The output can tell you a breakdown of votes cast for each candidate to determine a winner, as well as voter turnout by county. This program is able to be re-used for many elections, and one revision necessary would be the file path used to access the election results csv if a new file is being used. Another revision to be considered would be the path to the text file which stores the output data and detailed results of the election. You can see an example of what would need to be changed below.

![Image1](/resources/FilePath.PNG)