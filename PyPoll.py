#The data we need to retreive
file = 'election_results.csv'
data = open(file, 'r')
file = csv.reader(data)
headers = next(file)
print(headers)
for row in file:
    print(row)
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
