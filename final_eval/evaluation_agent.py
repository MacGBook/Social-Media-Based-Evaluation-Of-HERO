# SOCIAL SIMULATION EVALUATION AGENT
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

#General
import json
import ollama
import re 

#SET CURRENT MODEL
from curr_mod import current_model

#SET EVAC MESSAGE
from evac_mess import evacuation_message

#From agents.py
from agents import agent_response_dict

##############################################################################################################################################################################################################################################################################################################################################################
#LLM SET UP
# Ollama: function for basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

complete_sum_list = []
agent_responses_list = []
##############################################################################################################################################################################################################################################################################################################################################################
#EVALUATION AGENT PROMPTING


def obtain_ranking_function(eval_agent_response):

    # Isolate that LLM ranking as an integer and add it to a list
    obtain_ranking = re.search(r'\[(.*?)\]', eval_agent_response)
    if obtain_ranking: 
        content = obtain_ranking.group(1)
        #this_is_a_number = int(content)
    else:
        content = str(404) #If 404 appears as the ranking, it's a sign that the LLM as provided an invalid response
        #this_is_a_number = int(404)

    does_content_have_non_numbers = any(char.isalpha() for char in content)

    # Now, we clear out any generated values that still have letters
    if does_content_have_non_numbers == True:
        final_add = int(404) #if the answer has letters, we assign it a 404 error code
    if does_content_have_non_numbers == False:
        final_add = int(content) # else, we convert it directly into an integer 

    return final_add



#print(agent_response_dict)

for message in agent_response_dict.values():

    eval_rankings_list = [] # We initialize a list to hold the rankings for each agent response


    #Obtain an LLM ranking of who
    eval_agent_description_who = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_who =  eval_agent_description_who + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands who will be effected by the storm in the original message, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    #print(eval_agent_prompt_who)
    eval_agent_response_who = generate_text(current_model, eval_agent_prompt_who)
    #print(eval_agent_response_who)
    get_int_who = obtain_ranking_function(eval_agent_response_who)
    eval_rankings_list.append(get_int_who)

    #Obtain an LLM ranking of what
    eval_agent_description_what = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_what =  eval_agent_description_what + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands what the threat of the original message is, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    eval_agent_response_what = generate_text(current_model, eval_agent_prompt_what)
    #print(eval_agent_response_what)
    get_int_what = obtain_ranking_function(eval_agent_response_what)    
    eval_rankings_list.append(get_int_what)

    #Obtain an LLM ranking of when
    eval_agent_description_when = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_when =  eval_agent_description_when + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if this person understands when this storm will impact them, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    eval_agent_response_when = generate_text(current_model, eval_agent_prompt_when)
    #print(eval_agent_response_when)
    get_int_when = obtain_ranking_function(eval_agent_response_when)
    eval_rankings_list.append(get_int_when)

    #Obtain an LLM ranking of where
    eval_agent_description_where = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_where =  eval_agent_description_where + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands where this storm will hit, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    eval_agent_response_where = generate_text(current_model, eval_agent_prompt_where)
    #print(eval_agent_response_where)
    get_int_where = obtain_ranking_function(eval_agent_response_where)
    eval_rankings_list.append(get_int_where)
    
    #Obtain an LLM ranking of why
    eval_agent_description_why = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_why =  eval_agent_description_why + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands why it is important for them to take action or why the storm is dangerous, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    eval_agent_response_why = generate_text(current_model, eval_agent_prompt_why)
    #print(eval_agent_response_why)
    get_int_why = obtain_ranking_function(eval_agent_response_why)
    eval_rankings_list.append(get_int_why)

    #Obtain an LLM ranking of how
    eval_agent_description_how = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt_how =  eval_agent_description_how + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands how to take proper action from this threat, return [1] as your answer. If they do not, return [0] as your answer. Your answer must include one of the following: [1] or [0]. Your ranking must be in square brackets!"
    eval_agent_response_how = generate_text(current_model, eval_agent_prompt_how)
    #print(eval_agent_response_how)
    get_int_how = obtain_ranking_function(eval_agent_response_how)
    eval_rankings_list.append(get_int_how)


    #print(eval_rankings_list)

    # We initialize a counter to sum up the overall score of all agent responses
    total_agent_message_sum_list = []

    for value in eval_rankings_list:
        if value == int(404):
            pass # We don't count 404 errors to the overall score. Notably, 404 codes could be used to count model or prompting efficiency going forward
        else:
            total_agent_message_sum_list.append(value)

    total_agent_message_sum = sum(total_agent_message_sum_list)
    agent_responses_list.append(total_agent_message_sum_list)
    complete_sum_list.append(total_agent_message_sum)

#print(agent_responses_list)
#print(complete_sum_list)
total_message_sum = sum(complete_sum_list) # This is the overall score of all agent responses across all categories, which we can use for an overall evaluation of the model's performance in this task.

# This provides us with a final dictionary llinking rankings as values to keys as agent names
eval_response_dict = dict(zip(agent_response_dict.keys(), complete_sum_list))

#printing for testing
#print(eval_response_dict)
#print('Total Message Score: ')
#print(total_message_sum)