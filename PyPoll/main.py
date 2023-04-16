import csv

path = 'Resources/election_data.csv'

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)

    total_votes = 0
    vote_counts = {}
    for row in csv_reader:
    
        total_votes += 1


        candidate = row[2]
        if candidate not in vote_counts:
            vote_counts[candidate] = 0
        vote_counts[candidate] += 1

    vote_percentages = {}
    for candidate, count in vote_counts.items():
        vote_percentages[candidate] = count / total_votes * 100


    winner = max(vote_counts, key=vote_counts.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, count in vote_counts.items():
        percentage = vote_percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({count})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
