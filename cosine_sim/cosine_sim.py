# COSINE SIMILARITY COMBINATION CALCULATIONS

##############################################################################################################
# IMPORTS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

##############################################################################################################
# CSV READ-IN
import pandas as pd

df = pd.read_csv("cosine_strings.csv", encoding="latin1")

for column in df.columns:
    globals()[column] = df[column].dropna().tolist()

##############################################################################################################
# # DATA LOADING
# agent_1_tweet = ['hello', 'goodbye']
# agent_1_sim = ['hello', 'goodbye']

# agent_2_tweet = ['hello', 'goodbye']
# agent_2_sim = ['hello', 'goodbye']

# agent_3_tweet = ['hello', 'goodbye']
# agent_3_sim = ['hello', 'goodbye']

# agent_4_tweet = ['hello', 'goodbye']
# agent_4_sim = ['hello', 'goodbye']

# # language
# agent_5_tweet = ['hello', 'goodbye']
# agent_5_sim = ['hello', 'goodbye']

# # baseline
# agent_6_tweet = ['hello', 'goodbye']
# agent_6_sim = ['hello', 'goodbye']



print('agent_1_tweet')
print(len(agent_1_tweet))

print('agent_1_sim')
print(len(agent_1_sim))

print('agent_2_tweet')
print(len(agent_2_tweet))

print('agent_2_sim')
print(len(agent_2_sim))

print('agent_3_tweet')
print(len(agent_3_tweet))

print('agent_3_sim')
print(len(agent_3_sim))

print('agent_4_tweet')
print(len(agent_4_tweet))

print('agent_4_sim')
print(len(agent_4_sim))

print('agent_5_tweet')
print(len(agent_5_tweet))

print('agent_5_sim')
print(len(agent_5_sim))

print('agent_6_tweet')
print(len(agent_6_tweet))

print('agent_6_sim')
print(len(agent_6_sim))

##############################################################################################################
# CREATE THE COSINE SIMILARITY FUNCTION
def cosine_calc(string1, string2):
    pair = [string1, string2]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(pair)
    vector1 = tfidf_matrix[0]
    vector2 = tfidf_matrix[1]
    similarity_score = cosine_similarity(vector1, vector2)
    return float(similarity_score[0][0])

##############################################################################################################
# PERFORM THE AGENT LOOPS 

# AGENT 1
agent_1_results = []
for string_1 in agent_1_tweet:
    for string_2 in agent_1_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_1_results.append(cosine_value)


# AGENT 2
agent_2_results = []
for string_1 in agent_2_tweet:
    for string_2 in agent_2_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_2_results.append(cosine_value)


# AGENT 3
agent_3_results = []
for string_1 in agent_3_tweet:
    for string_2 in agent_3_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_3_results.append(cosine_value)


# AGENT 4
agent_4_results = []
for string_1 in agent_4_tweet:
    for string_2 in agent_4_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_4_results.append(cosine_value)


# AGENT 5
agent_5_results = []
for string_1 in agent_5_tweet:
    for string_2 in agent_5_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_5_results.append(cosine_value)


# AGENT 6
agent_6_results = []
for string_1 in agent_6_tweet:
    for string_2 in agent_6_sim:
        cosine_value = cosine_calc(string_1, string_2)
        print(cosine_value)
        agent_6_results.append(cosine_value)

##############################################################################################################
#PRINT STATEMENTS
print("RESULT LENGTHS")
print("agent 1:", len(agent_1_results))
print("agent 2:", len(agent_2_results))
print("agent 3:", len(agent_3_results))
print("agent 4:", len(agent_4_results))
print("agent 5:", len(agent_5_results))
print("agent 6:", len(agent_6_results))

##############################################################################################################
#CSV SAVES
df = pd.DataFrame({
    "agent 1": pd.Series(agent_1_results),
    "agent 2": pd.Series(agent_2_results),
    "agent 3": pd.Series(agent_3_results),
    "agent 4": pd.Series(agent_4_results),
    "agent 5": pd.Series(agent_5_results),
    "agent 6": pd.Series(agent_6_results)
})

df.to_csv("cosine_similarity_results.csv", index=False)