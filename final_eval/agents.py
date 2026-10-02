
# SOCIAL SIMULATION AGENTS
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

#General
import json
import ollama

#SET CURRENT MODEL
from curr_mod import current_model

#SET EVAC MESSAGE
from evac_mess import evacuation_message

##############################################################################################################################################################################################################################################################################################################################################################
#LLM SET UP
# Ollama: function for basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

# Initialized list we will add generated agent responses to
agent_response_list = []

##############################################################################################################################################################################################################################################################################################################################################################
#AGENT FRAMEWORK AND INDIVIDUAL LLM FRAMEWORK

# AGENT 1
agent_1_description = "You are a resident of Manteo, North Carolina. You are elderly, and have a disability with high medical needs that makes you wheelchair bound. Mobility is difficult for you physically and with regards to transportation. "
agent1_prompt = agent_1_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent1_response = generate_text(current_model, agent1_prompt)
agent_response_list.append(agent1_response)

# AGENT 2
agent_2_description = "You are a resident of Manteo, North Carolina. You are elderly. "
agent2_prompt =  agent_2_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent2_response = generate_text(current_model, agent2_prompt)
agent_response_list.append(agent2_response)

# AGENT 4
agent_4_description = "You are a resident of Manteo, North Carolina. You currently have a family member who is on life support at the local hospital that you care about deeply. "
agent4_prompt =  agent_4_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent4_response = generate_text(current_model, agent4_prompt)
agent_response_list.append(agent4_response)

# AGENT 6
agent_6_description = "You are a resident of Manteo, North Carolina. You have a medical disability that makes mobility difficult. You rely on a walker to get around and also need weekly physical therapy at the local hospital. "
agent6_prompt =  agent_6_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent6_response = generate_text(current_model, agent6_prompt)
agent_response_list.append(agent6_response)

# AGENT 10
agent_10_description = "You are a resident of Manteo, North Carolina. You first language is Spanish, and you have a limited understanding of English. All responses you write should be either in Spanish or in very simple English. "
agent10_prompt =  agent_10_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent10_response = generate_text(current_model, agent10_prompt)
agent_response_list.append(agent10_response)

# AGENT 13
agent_13_description = "You are a resident of Manteo, North Carolina. You have lived here for many years and seen many hurricanes here before. You have a car, money, support, and a family here in Manteo. "
agent13_prompt =  agent_13_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not. "
agent13_response = generate_text(current_model, agent13_prompt)
agent_response_list.append(agent13_response)


##############################################################################################################################################################################################################################################################################################################################################################
# PREP AGENT RESPONSES 

cleaned_agent_response_list = []
for string in agent_response_list:
    new_string = string.replace('Generated text (gemma3:1b):', '')
    no_line_new_string = new_string.strip('\n')
    cleaned_agent_response_list.append(no_line_new_string)

agent_name_list = ['agent1', 'agent2', 'agent4', 'agent6', 'agent10','agent13']

agent_response_dict = dict(zip(agent_name_list, cleaned_agent_response_list))

#cleaned_agent_response_list = string list of all agent responses
#agent_name_list = the list of the agent
#agent_response_dict = dictionary with agent name as key and their generated response as the value