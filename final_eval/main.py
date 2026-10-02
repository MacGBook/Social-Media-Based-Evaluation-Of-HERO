# SOCIAL SIMULATION MAIN
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

import csv
import pandas as pd

# From evaluation_agent:
from evaluation_agent import eval_response_dict
from evaluation_agent import total_message_sum
from evaluation_agent import agent_responses_list
from agents import agent_response_dict

header = ["who_ranking", "what_ranking", "when_ranking", "where_ranking", "why_ranking", "how_ranking"]

##############################################################################################################################################################################################################################################################################################################################################################
# COMPLETING THE RUN AND SAVING IT TO A CSV

#Save individual rankings to their csv
with open("ind_ag_output.csv", mode='a', newline="") as f:
    writer = csv.DictWriter(f, eval_response_dict.keys())
    writer.writeheader()
    writer.writerow(eval_response_dict)


try:
    with open("agent_response_output.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the integer as a single row
        writer.writerow(agent_responses_list)
except IOError as e:
    print(f"Error writing to file: {e}")

try:
    with open("total_output.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the integer as a single row
        writer.writerow([total_message_sum])
except IOError as e:
    print(f"Error writing to file: {e}")

df = pd.DataFrame([list(agent_response_dict.values())])
df.to_csv(
    "written_agent_responses.csv",
    mode="a",
    index=False,
    header=False
)

# for i in {1..5}; do python3 script.py; done