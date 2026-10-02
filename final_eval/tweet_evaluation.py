# EVALUATE TWITTER RESPONSES PER AGENT TYPE

# IMPORTS
import pandas as pd
import ollama
import json
import re 
from evac_mess import mess_1
from evac_mess import mess_2
from evac_mess import mess_3
from curr_mod import current_model

# AGENT 1
df = pd.read_csv("agent_1.csv")
# Read the Ith column as a list of strings, excluding the header
agent_1_list = df.iloc[:, 8].astype(str).tolist()

# AGENT 2
df2 = pd.read_csv("agent_2.csv")
# Read the Ith column as a list of strings, excluding the header
agent_2_list = df2.iloc[:, 8].astype(str).tolist()

# AGENT 3
df3 = pd.read_csv("agent_3.csv")
# Read the Ith column as a list of strings, excluding the header
agent_3_list = df3.iloc[:, 7].astype(str).tolist()

# AGENT 4
df4 = pd.read_csv("agent_4.csv")
# Read the Ith column as a list of strings, excluding the header
agent_4_list = df4.iloc[:, 8].astype(str).tolist()

# AGENT Baseline
df_baseline = pd.read_csv("agent_baseline.csv")
# Read the Ith column as a list of strings, excluding the header
agent_baseline_list = df_baseline.iloc[:, 8].astype(str).tolist()

# AGENT Language
df_language = pd.read_csv("agent_language.csv")
# Read the Ith column as a list of strings, excluding the header
agent_language_list = df_language.iloc[:, 8].astype(str).tolist()



##############################################################################################################################################################################################################################################################################################################################################################
#LLM SET UP & READABILITY 

# Ollama: function for basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

# LISTS
complete_sum_list = []
agent_responses_list = []

# FUNCTION FOR EXTRACTING RESULTS
def obtain_ranking_function(eval_agent_response):

    # Find the first value inside square brackets
    obtain_ranking = re.search(r'\[([^\]]*)\]', eval_agent_response)

    if not obtain_ranking:
        return 404

    content = obtain_ranking.group(1).strip()

    # Remove quotes, spaces, and backslashes
    content = content.strip().strip('"').strip("'").strip("\\").strip()

    # Make sure the remaining content is a number
    if content.isdigit():
        return int(content)

    return 404

##############################################################################################################################################################################################################################################################################################################################################################
# EVALUATION 

final_evaluations_list = []

#print(agent_1_list)
#print(agent_2_list)
#print(agent_3_list)
#print(agent_4_list)
#print(agent_baseline_list)
#print(agent_language_list)


repeated_list = ['agent_1'] * len(agent_1_list)

for message in agent_1_list:

    eval_agent_intro = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "

    eval_rankings_list = []

    eval_agent_prompt_who =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands who will be effected by the storm in the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    who_total = eval_agent_intro + eval_agent_prompt_who
    eval_agent_response_who = generate_text(current_model, who_total)
    get_int_who = obtain_ranking_function(eval_agent_response_who)
    eval_rankings_list.append(get_int_who)

    eval_agent_prompt_what =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands what the threat is in the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    what_total = eval_agent_intro + eval_agent_prompt_what
    eval_agent_response_what = generate_text(current_model, what_total)
    get_int_what = obtain_ranking_function(eval_agent_response_what)
    eval_rankings_list.append(get_int_what)

    eval_agent_prompt_where =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands where the threat is in the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    where_total = eval_agent_intro + eval_agent_prompt_where
    eval_agent_response_where = generate_text(current_model, where_total)
    get_int_where = obtain_ranking_function(eval_agent_response_where)
    eval_rankings_list.append(get_int_where)

    eval_agent_prompt_when =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands when the threat will occure based on the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    when_total = eval_agent_intro + eval_agent_prompt_when
    eval_agent_response_when = generate_text(current_model, when_total)
    get_int_when = obtain_ranking_function(eval_agent_response_when)
    eval_rankings_list.append(get_int_when)

    eval_agent_prompt_why =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands why to take emergency action based on the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    why_total = eval_agent_intro + eval_agent_prompt_why
    eval_agent_response_why = generate_text(current_model, why_total)
    get_int_why = obtain_ranking_function(eval_agent_response_why)
    eval_rankings_list.append(get_int_why)

    eval_agent_prompt_how =  "The person you are grading receives the following messages: " + mess_1 + mess_2 + mess_3 + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands how to take emergency action based on the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    how_total = eval_agent_intro + eval_agent_prompt_how
    eval_agent_response_how = generate_text(current_model, how_total)
    get_int_how = obtain_ranking_function(eval_agent_response_how)
    eval_rankings_list.append(get_int_how)

    total_agent_message_sum_list = []

    for value in eval_rankings_list:
        if value == int(404):
            pass # We don't count 404 errors to the overall score. Notably, 404 codes could be used to count model or prompting efficiency going forward
        else:
            total_agent_message_sum_list.append(value)

    total_agent_message_sum = int(sum(total_agent_message_sum_list))
    final_evaluations_list.append(total_agent_message_sum)




import os

# Create a DataFrame from the two lists
df_new = pd.DataFrame({
    "column_1": repeated_list,
    "column_2": final_evaluations_list
})

# Check whether the CSV already exists and contains data
if os.path.exists("tweet_evaluations.csv") and os.path.getsize("tweet_evaluations.csv") > 0:

    # Append the new results to the existing CSV
    df_new.to_csv(
        "tweet_evaluations.csv",
        mode="a",
        index=False,
        header=False,
        encoding="utf-8-sig"
    )

else:

    # Create a new CSV
    df_new.to_csv(
        "tweet_evaluations.csv",
        mode="w",
        index=False,
        header=True,
        encoding="utf-8-sig"
    )