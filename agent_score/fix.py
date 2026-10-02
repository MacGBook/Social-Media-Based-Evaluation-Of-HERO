with open("check.csv", "r") as infile:
    lines = infile.readlines()

with open("fixed.csv", "w") as outfile:
    for line in lines:
        if line.strip() != "agent1,agent2,agent4,agent6,agent10,agent13":
            outfile.write(line)