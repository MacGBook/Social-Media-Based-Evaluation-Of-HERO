# IMPORTS

import pandas as pd
import ollama

##############################################################################################################################################################################################################################################################################################################################################################

df = pd.read_csv("test.csv")

# DO NOT REMOVE ROWS WITH MISSING VALUES
# Missing metadata values such as in_reply_to_user_id are allowed to remain as NaN.

column_lists = {
    column: df[column].tolist()
    for column in df.columns
}

##############################################################################################################################################################################################################################################################################################################################################################

tweet_id_list = column_lists["tweet_id"]

created_at_list = column_lists["created_at"]

search_window_list = column_lists["search_window"]

search_query_list = column_lists["search_query"]

author_id_list = column_lists["author_id"]

conversation_id_list = column_lists["conversation_id"]

in_reply_to_user_id_list = column_lists["in_reply_to_user_id"]

language_list = column_lists["language"]

text_list = column_lists["text"]

retweet_count_list = column_lists["retweet_count"]

reply_count_list = column_lists["reply_count"]

like_count_list = column_lists["like_count"]

quote_count_list = column_lists["quote_count"]

##############################################################################################################################################################################################################################################################################################################################################################

# LLM SET UP

# Ollama: function for basic text generation

def generate_text(model_name, prompt):

    response = ollama.generate(model=model_name, prompt=prompt)

    return(f"Generated text ({model_name}):\n{response['response']}\n")

##############################################################################################################################################################################################################################################################################################################################################################

# COLLECT FOR AGENT 5 TYPE

langague_tweet_id_list = []

langague_created_at_list = []

langague_search_window_list = []

langague_search_query_list = []

langague_author_id_list = []

langague_conversation_id_list = []

langague_in_reply_to_user_id_list = []

langague_language_list = []

langague_text_list = []

langague_retweet_count_list = []

langague_reply_count_list = []

langague_like_count_list = []

langague_quote_count_list = []


# Go through the indices in reverse order

for language_index in range(len(language_list) - 1, -1, -1):

    if language_list[language_index] != "en":

        langague_tweet_id_list.append(tweet_id_list[language_index])

        langague_created_at_list.append(created_at_list[language_index])

        langague_search_window_list.append(search_window_list[language_index])

        langague_search_query_list.append(search_query_list[language_index])

        langague_author_id_list.append(author_id_list[language_index])

        langague_conversation_id_list.append(conversation_id_list[language_index])

        langague_in_reply_to_user_id_list.append(in_reply_to_user_id_list[language_index])

        langague_language_list.append(language_list[language_index])

        langague_text_list.append(text_list[language_index])

        langague_retweet_count_list.append(retweet_count_list[language_index])

        langague_reply_count_list.append(reply_count_list[language_index])

        langague_like_count_list.append(like_count_list[language_index])

        langague_quote_count_list.append(quote_count_list[language_index])


# Delete the same index from every original list

        del tweet_id_list[language_index]

        del created_at_list[language_index]

        del search_window_list[language_index]

        del search_query_list[language_index]

        del author_id_list[language_index]

        del conversation_id_list[language_index]

        del in_reply_to_user_id_list[language_index]

        del language_list[language_index]

        del text_list[language_index]

        del retweet_count_list[language_index]

        del reply_count_list[language_index]

        del like_count_list[language_index]

        del quote_count_list[language_index]

##############################################################################################################################################################################################################################################################################################################################################################

# AI SORT INTO AGENT TYPES

ai_agent_response_list = []

for tweet_text_string in text_list:

    prompt_intro = 'You receive the following tweet: '

    # tweet_test_string

    prompt_desc = 'I need you to determine which categories the text of this tweet falls into. '

    agent_1_prompt = 'If the tweet mentions a human struggling with mobility or transportation, return the label STUCK in your answer.'

    agent_2_prompt = 'If the tweet discusses human age in their message, return the label ELDERLY in your answer.'

    agent_3_prompt = 'If the tweet discusses the hospital or injuries or anything related to medicine or medical treatment, return the label HOSPITAL in your answer.'

    final_clarifications = 'It is ok if your answer does not mention any of these labels. It is ok if your answer provides multiple lables. Just make sure all labels applied are mentioned in all capital letters.'

    full_prompt = prompt_intro + tweet_text_string + prompt_desc + agent_1_prompt + agent_2_prompt + agent_3_prompt + final_clarifications

    ai_response = generate_text('gemma3:1b', full_prompt)

    ai_agent_response_list.append(ai_response)

##############################################################################################################################################################################################################################################################################################################################################################


agent_1_tweet_id_list = []

agent_1_created_at_list = []

agent_1_search_window_list = []

agent_1_search_query_list = []

agent_1_author_id_list = []

agent_1_conversation_id_list = []

agent_1_in_reply_to_user_id_list = []

agent_1_language_list = []

agent_1_text_list = []

agent_1_retweet_count_list = []

agent_1_reply_count_list = []

agent_1_like_count_list = []

agent_1_quote_count_list = []

agent_1_response = []


agent_2_tweet_id_list = []

agent_2_created_at_list = []

agent_2_search_window_list = []

agent_2_search_query_list = []

agent_2_author_id_list = []

agent_2_conversation_id_list = []

agent_2_in_reply_to_user_id_list = []

agent_2_language_list = []

agent_2_text_list = []

agent_2_retweet_count_list = []

agent_2_reply_count_list = []

agent_2_like_count_list = []

agent_2_quote_count_list = []

agent_2_response = []


agent_3_tweet_id_list = []

agent_3_created_at_list = []

agent_3_search_window_list = []

agent_3_search_query_list = []

agent_3_author_id_list = []

agent_3_conversation_id_list = []

agent_3_in_reply_to_user_id_list = []

agent_3_language_list = []

agent_3_text_list = []

agent_3_retweet_count_list = []

agent_3_reply_count_list = []

agent_3_like_count_list = []

agent_3_quote_count_list = []

agent_3_response = []


agent_4_tweet_id_list = []

agent_4_created_at_list = []

agent_4_search_window_list = []

agent_4_search_query_list = []

agent_4_author_id_list = []

agent_4_conversation_id_list = []

agent_4_in_reply_to_user_id_list = []

agent_4_language_list = []

agent_4_text_list = []

agent_4_retweet_count_list = []

agent_4_reply_count_list = []

agent_4_like_count_list = []

agent_4_quote_count_list = []

agent_4_response = []


normal_tweet_id_list = []

normal_created_at_list = []

normal_search_window_list = []

normal_search_query_list = []

normal_author_id_list = []

normal_conversation_id_list = []

normal_in_reply_to_user_id_list = []

normal_language_list = []

normal_text_list = []

normal_retweet_count_list = []

normal_reply_count_list = []

normal_like_count_list = []

normal_quote_count_list = []

normal_response = []


##############################################################################################################################################################################################################################################################################################################################################################

for evaluation_index, evaluation in enumerate(ai_agent_response_list):

    evaluation = evaluation.upper()

    # ---------------------------------------------------------
    # AGENT 4: HOSPITAL + STUCK
    # ---------------------------------------------------------

    if "HOSPITAL" in evaluation and "STUCK" in evaluation:

        agent_4_tweet_id_list.append(tweet_id_list[evaluation_index])

        agent_4_created_at_list.append(created_at_list[evaluation_index])

        agent_4_search_window_list.append(search_window_list[evaluation_index])

        agent_4_search_query_list.append(search_query_list[evaluation_index])

        agent_4_author_id_list.append(author_id_list[evaluation_index])

        agent_4_conversation_id_list.append(conversation_id_list[evaluation_index])

        agent_4_in_reply_to_user_id_list.append(in_reply_to_user_id_list[evaluation_index])

        agent_4_language_list.append(language_list[evaluation_index])

        agent_4_text_list.append(text_list[evaluation_index])

        agent_4_retweet_count_list.append(retweet_count_list[evaluation_index])

        agent_4_reply_count_list.append(reply_count_list[evaluation_index])

        agent_4_like_count_list.append(like_count_list[evaluation_index])

        agent_4_quote_count_list.append(quote_count_list[evaluation_index])

        agent_4_response.append(evaluation)


    # ---------------------------------------------------------
    # AGENT 1: STUCK
    # ---------------------------------------------------------

    elif "STUCK" in evaluation:

        agent_1_tweet_id_list.append(tweet_id_list[evaluation_index])

        agent_1_created_at_list.append(created_at_list[evaluation_index])

        agent_1_search_window_list.append(search_window_list[evaluation_index])

        agent_1_search_query_list.append(search_query_list[evaluation_index])

        agent_1_author_id_list.append(author_id_list[evaluation_index])

        agent_1_conversation_id_list.append(conversation_id_list[evaluation_index])

        agent_1_in_reply_to_user_id_list.append(in_reply_to_user_id_list[evaluation_index])

        agent_1_language_list.append(language_list[evaluation_index])

        agent_1_text_list.append(text_list[evaluation_index])

        agent_1_retweet_count_list.append(retweet_count_list[evaluation_index])

        agent_1_reply_count_list.append(reply_count_list[evaluation_index])

        agent_1_like_count_list.append(like_count_list[evaluation_index])

        agent_1_quote_count_list.append(quote_count_list[evaluation_index])

        agent_1_response.append(evaluation)


    # ---------------------------------------------------------
    # AGENT 2: ELDERLY
    # ---------------------------------------------------------

    elif "ELDERLY" in evaluation:

        agent_2_tweet_id_list.append(tweet_id_list[evaluation_index])

        agent_2_created_at_list.append(created_at_list[evaluation_index])

        agent_2_search_window_list.append(search_window_list[evaluation_index])

        agent_2_search_query_list.append(search_query_list[evaluation_index])

        agent_2_author_id_list.append(author_id_list[evaluation_index])

        agent_2_conversation_id_list.append(conversation_id_list[evaluation_index])

        agent_2_in_reply_to_user_id_list.append(in_reply_to_user_id_list[evaluation_index])

        agent_2_language_list.append(language_list[evaluation_index])

        agent_2_text_list.append(text_list[evaluation_index])

        agent_2_retweet_count_list.append(retweet_count_list[evaluation_index])

        agent_2_reply_count_list.append(reply_count_list[evaluation_index])

        agent_2_like_count_list.append(like_count_list[evaluation_index])

        agent_2_quote_count_list.append(quote_count_list[evaluation_index])

        agent_2_response.append(evaluation)


    # ---------------------------------------------------------
    # AGENT 3: HOSPITAL
    # ---------------------------------------------------------

    elif "HOSPITAL" in evaluation:

        agent_3_tweet_id_list.append(tweet_id_list[evaluation_index])

        agent_3_created_at_list.append(created_at_list[evaluation_index])

        agent_3_search_window_list.append(search_window_list[evaluation_index])

        agent_3_search_query_list.append(search_query_list[evaluation_index])

        agent_3_author_id_list.append(author_id_list[evaluation_index])

        agent_3_conversation_id_list.append(conversation_id_list[evaluation_index])

        agent_3_in_reply_to_user_id_list.append(in_reply_to_user_id_list[evaluation_index])

        agent_3_language_list.append(language_list[evaluation_index])

        agent_3_text_list.append(text_list[evaluation_index])

        agent_3_retweet_count_list.append(retweet_count_list[evaluation_index])

        agent_3_reply_count_list.append(reply_count_list[evaluation_index])

        agent_3_like_count_list.append(like_count_list[evaluation_index])

        agent_3_quote_count_list.append(quote_count_list[evaluation_index])

        agent_3_response.append(evaluation)


    # ---------------------------------------------------------
    # NORMAL: NO LABELS
    # ---------------------------------------------------------

    else:

        normal_tweet_id_list.append(tweet_id_list[evaluation_index])

        normal_created_at_list.append(created_at_list[evaluation_index])

        normal_search_window_list.append(search_window_list[evaluation_index])

        normal_search_query_list.append(search_query_list[evaluation_index])

        normal_author_id_list.append(author_id_list[evaluation_index])

        normal_conversation_id_list.append(conversation_id_list[evaluation_index])

        normal_in_reply_to_user_id_list.append(in_reply_to_user_id_list[evaluation_index])

        normal_language_list.append(language_list[evaluation_index])

        normal_text_list.append(text_list[evaluation_index])

        normal_retweet_count_list.append(retweet_count_list[evaluation_index])

        normal_reply_count_list.append(reply_count_list[evaluation_index])

        normal_like_count_list.append(like_count_list[evaluation_index])

        normal_quote_count_list.append(quote_count_list[evaluation_index])

        normal_response.append(evaluation)


##################################################################################################

# CHECK THAT EVERY ENGLISH EVALUATION WAS SORTED

total_sorted = (

    len(agent_1_response)

    + len(agent_2_response)

    + len(agent_3_response)

    + len(agent_4_response)

    + len(normal_response)

)

print("Total evaluations:", len(ai_agent_response_list))

print("Total sorted:", total_sorted)

print("English tweets classified:", len(text_list))

print("Non-English tweets saved for later:", len(langague_text_list))

print("Total tweets accounted for:", len(text_list) + len(langague_text_list))


##################################################################################################

# SAVE TO CSVs


df = pd.DataFrame({

    "agent_1_tweet_id": agent_1_tweet_id_list,

    "agent_1_created_at": agent_1_created_at_list,

    "agent_1_search_window": agent_1_search_window_list,

    "agent_1_search_query": agent_1_search_query_list,

    "agent_1_author_id": agent_1_author_id_list,

    "agent_1_conversation_id": agent_1_conversation_id_list,

    "agent_1_in_reply_to_user_id": agent_1_in_reply_to_user_id_list,

    "agent_1_language": agent_1_language_list,

    "agent_1_text": agent_1_text_list,

    "agent_1_retweet_count": agent_1_retweet_count_list,

    "agent_1_reply_count": agent_1_reply_count_list,

    "agent_1_like_count": agent_1_like_count_list,

    "agent_1_quote_count": agent_1_quote_count_list,

    "agent_1_response": agent_1_response

})

df.to_csv("agent_1.csv", index=False, encoding="utf-8-sig")


df2 = pd.DataFrame({

    "agent_2_tweet_id": agent_2_tweet_id_list,

    "agent_2_created_at": agent_2_created_at_list,

    "agent_2_search_window": agent_2_search_window_list,

    "agent_2_search_query": agent_2_search_query_list,

    "agent_2_author_id": agent_2_author_id_list,

    "agent_2_conversation_id": agent_2_conversation_id_list,

    "agent_2_in_reply_to_user_id": agent_2_in_reply_to_user_id_list,

    "agent_2_language": agent_2_language_list,

    "agent_2_text": agent_2_text_list,

    "agent_2_retweet_count": agent_2_retweet_count_list,

    "agent_2_reply_count": agent_2_reply_count_list,

    "agent_2_like_count": agent_2_like_count_list,

    "agent_2_quote_count": agent_2_quote_count_list,

    "agent_2_response": agent_2_response

})

df2.to_csv("agent_2.csv", index=False, encoding="utf-8-sig")


df3 = pd.DataFrame({

    "agent_3_tweet_id": agent_3_tweet_id_list,

    "agent_3_created_at": agent_3_created_at_list,

    "agent_3_search_window": agent_3_search_window_list,

    "agent_3_search_query": agent_3_search_query_list,

    "agent_3_author_id": agent_3_author_id_list,

    "agent_3_conversation_id": agent_3_conversation_id_list,

    "agent_3_in_reply_to_user_id": agent_3_in_reply_to_user_id_list,

    "agent_3_language": agent_3_language_list,

    "agent_3_text": agent_3_text_list,

    "agent_3_retweet_count": agent_3_retweet_count_list,

    "agent_3_reply_count": agent_3_reply_count_list,

    "agent_3_like_count": agent_3_like_count_list,

    "agent_3_quote_count": agent_3_quote_count_list,

    "agent_3_response": agent_3_response

})

df3.to_csv("agent_3.csv", index=False, encoding="utf-8-sig")


df4 = pd.DataFrame({

    "agent_4_tweet_id": agent_4_tweet_id_list,

    "agent_4_created_at": agent_4_created_at_list,

    "agent_4_search_window": agent_4_search_window_list,

    "agent_4_search_query": agent_4_search_query_list,

    "agent_4_author_id": agent_4_author_id_list,

    "agent_4_conversation_id": agent_4_conversation_id_list,

    "agent_4_in_reply_to_user_id": agent_4_in_reply_to_user_id_list,

    "agent_4_language": agent_4_language_list,

    "agent_4_text": agent_4_text_list,

    "agent_4_retweet_count": agent_4_retweet_count_list,

    "agent_4_reply_count": agent_4_reply_count_list,

    "agent_4_like_count": agent_4_like_count_list,

    "agent_4_quote_count": agent_4_quote_count_list,

    "agent_4_response": agent_4_response

})

df4.to_csv("agent_4.csv", index=False, encoding="utf-8-sig")


dfnormal = pd.DataFrame({

    "normal_tweet_id": normal_tweet_id_list,

    "normal_created_at": normal_created_at_list,

    "normal_search_window": normal_search_window_list,

    "normal_search_query": normal_search_query_list,

    "normal_author_id": normal_author_id_list,

    "normal_conversation_id": normal_conversation_id_list,

    "normal_in_reply_to_user_id": normal_in_reply_to_user_id_list,

    "normal_language": normal_language_list,

    "normal_text": normal_text_list,

    "normal_retweet_count": normal_retweet_count_list,

    "normal_reply_count": normal_reply_count_list,

    "normal_like_count": normal_like_count_list,

    "normal_quote_count": normal_quote_count_list,

    "normal_response": normal_response

})

dfnormal.to_csv("agent_normal.csv", index=False, encoding="utf-8-sig")


dflanguage = pd.DataFrame({

    "langague_tweet_id": langague_tweet_id_list,

    "langague_created_at": langague_created_at_list,

    "langague_search_window": langague_search_window_list,

    "langague_search_query": langague_search_query_list,

    "langague_author_id": langague_author_id_list,

    "langague_conversation_id": langague_conversation_id_list,

    "langague_in_reply_to_user_id": langague_in_reply_to_user_id_list,

    "langague_language": langague_language_list,

    "langague_text": langague_text_list,

    "langague_retweet_count": langague_retweet_count_list,

    "langague_reply_count": langague_reply_count_list,

    "langague_like_count": langague_like_count_list,

    "langague_quote_count": langague_quote_count_list

})

dflanguage.to_csv("agent_language.csv", index=False, encoding="utf-8-sig")