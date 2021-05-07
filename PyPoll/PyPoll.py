import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis','election_results.txt')

total_votes = 0
candidate_list = []
candidate_votes = {}
winner_votes = 0


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # print(csvheader)
    
    for row in csvreader:
        # Total votes cast
        total_votes += 1 
      
        # Candidate list who recieved votes      
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            
            candidate_votes[row[2]] = 0
            
        candidate_votes[row[2]] += 1
        
        
with open(output_path, 'w') as text:
    
    election_part1 = f'''
    Election Results
    -----------------------------
    Total Votes: {total_votes}
    -----------------------------
    '''
    
    print(election_part1)
    text.write(election_part1)

     
    for candidate in candidate_votes:
        
        # Retrieving vote count and percentage for each candidate
        votes = candidate_votes.get(candidate)
        vote_percent  = float(votes) / float(total_votes) * 100
        
        # Determining election's winner
        if (votes > winner_votes):
            winner_votes = votes
            winner_candidate = candidate
        election_part2 = f'{candidate}: {vote_percent:.3f}% ({votes})'
        print(election_part2, end='')

        text.write(election_part2)
        
    election_part3 = f'''
    ----------------------------
    Winner: {winner_candidate}
    ----------------------------
    '''
    
    print(election_part3)
    
    text.write(election_part3)

        
        
        