import os
import csv

i = 0 
results = {}
num_votes = 0 
winner = ""
highest = -1

votesfile = os.path.join("Resources","election_data.csv")
writefile = os.path.join("Resources","results.csv")

with open(votesfile, mode = "r") as csv_file:
    csvreader = csv.reader(csv_file)    
    next(csvreader)
    
    for row in csvreader: 
        num_votes = num_votes + 1
        cand = row[2]
        if cand in results:
            results[cand] = results[cand] + 1
        else:
            results[cand] = 1
    
with open(writefile, mode = "w") as write_file:
    write_file.write("\nElection Results\n")   
    write_file.write("-------------------------\n")
    write_file.write("Total Votes: " + str(num_votes) + "\n")
    write_file.write("-------------------------\n")    
 
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(num_votes))
    print("-------------------------")

    for c in results:
        if results[c] > highest:
            winner = c
            highest = results[c]
        
        print (c + ": " + str( "%.3f" % (results[c] * 100 / num_votes)  ) + "%" + " (" + str(results[c]) + ")" )
        write_file.write(c + ": " + str( "%.3f" % (results[c] * 100 / num_votes)  ) + "%" + " (" + str(results[c]) + ")\n" )

    write_file.write("-------------------------\n")
    write_file.write("Winner: " + winner + "\n")    
    write_file.write("-------------------------\n")

    print("-------------------------")
    print("Winner: " + winner)    
    print("-------------------------")
        
            
    
