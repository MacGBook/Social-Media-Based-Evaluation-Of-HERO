# IMPORTS
import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
import statistics

##############################################################################################################################
# READ IN DATA
df = pd.read_csv("read_in.csv")

##############################################################################################################################
# CLEAN DATA
A1_sim_pre = df["A1_sim"].tolist()
arr_a1_sim = np.array(A1_sim_pre)
A1_sim = arr_a1_sim[~np.isnan(arr_a1_sim)].tolist()

A1_tweets_pre = df["A1_tweets"].tolist()
arr_a1_tweets = np.array(A1_tweets_pre)
A1_tweets = arr_a1_tweets[~np.isnan(arr_a1_tweets)].tolist()

A2_sim_pre = df["A2_sim"].tolist()
arr_a2_sim = np.array(A2_sim_pre)
A2_sim = arr_a2_sim[~np.isnan(arr_a2_sim)].tolist()

A2_tweets_pre = df["A2_tweets"].tolist()
arr_a2_tweets = np.array(A2_tweets_pre)
A2_tweets = arr_a2_tweets[~np.isnan(arr_a2_tweets)].tolist()

A3_sim_pre = df["A3_sim"].tolist()
arr_a3_sim = np.array(A3_sim_pre)
A3_sim = arr_a3_sim[~np.isnan(arr_a3_sim)].tolist()

A3_tweets_pre = df["A3_tweets"].tolist()
arr_a3_tweets = np.array(A3_tweets_pre)
A3_tweets = arr_a3_tweets[~np.isnan(arr_a3_tweets)].tolist()

A4_sim_pre = df["A4_sim"].tolist()
arr_a4_sim = np.array(A4_sim_pre)
A4_sim = arr_a4_sim[~np.isnan(arr_a4_sim)].tolist()

A4_tweets_pre = df["A4_tweets"].tolist()
arr_a4_tweets = np.array(A4_tweets_pre)
A4_tweets = arr_a4_tweets[~np.isnan(arr_a4_tweets)].tolist()

A5_sim_pre = df["A5_sim"].tolist()
arr_a5_sim = np.array(A5_sim_pre)
A5_sim = arr_a5_sim[~np.isnan(arr_a5_sim)].tolist()

A5_tweets_pre = df["A5_tweets"].tolist()
arr_a5_tweets = np.array(A5_tweets_pre)
A5_tweets = arr_a5_tweets[~np.isnan(arr_a5_tweets)].tolist()

A6_sim_pre = df["A6_sim"].tolist()
arr_a6_sim = np.array(A6_sim_pre)
A6_sim = arr_a6_sim[~np.isnan(arr_a6_sim)].tolist()

A6_tweets_pre = df["A6_tweets"].tolist()
arr_a6_tweets = np.array(A6_tweets_pre)
A6_tweets = arr_a6_sim[~np.isnan(arr_a6_tweets)].tolist()

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
# MANN-WHITNEY TESTS

##############################################################################################################################
# AGENT 1
#print(A1_sim)
#print(A1_tweets)

u_statistic, p_value = mannwhitneyu(A1_sim, A1_tweets, alternative="two-sided")

print("AGENT 1")
print("U statistic:", u_statistic)

print("p-value:", p_value)

if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
# AGENT 2
#print(A2_sim)
#print(A2_tweets)

u_statistic, p_value = mannwhitneyu(A2_sim, A2_tweets, alternative="two-sided")

print("AGENT 2")
print("U statistic:", u_statistic)
# ANSWER:
print("p-value:", p_value)
# ANSWER: 
# RESULT:
if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
# AGENT 3
#print(A3_sim)
#print(A3_tweets)

u_statistic, p_value = mannwhitneyu(A3_sim, A3_tweets, alternative="two-sided")

print("AGENT 3")
print("U statistic:", u_statistic)
# ANSWER:
print("p-value:", p_value)
# ANSWER: 
# RESULT:
if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
# AGENT 4
#print(A4_sim)
#print(A4_tweets)

u_statistic, p_value = mannwhitneyu(A4_sim, A4_tweets, alternative="two-sided")

print("AGENT 4")
print("U statistic:", u_statistic)
# ANSWER:
print("p-value:", p_value)
# ANSWER: 
# RESULT:
if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
# AGENT 5- Language
#print(A5_sim)
#print(A5_tweets)

u_statistic, p_value = mannwhitneyu(A5_sim, A5_tweets, alternative="two-sided")

print("AGENT 5")
print("U statistic:", u_statistic)
# ANSWER:
print("p-value:", p_value)
# ANSWER: 
# RESULT:
if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
# AGENT 6- Baseline
#print(A6_sim)
#print(A6_tweets)

u_statistic, p_value = mannwhitneyu(A6_sim, A6_tweets, alternative="two-sided")

print("AGENT 6")
print("U statistic:", u_statistic)
# ANSWER:
print("p-value:", p_value)
# ANSWER: 
# RESULT:
if p_value <= 0.05:
    print("STAT SIG")
else:
    print("NOT STAT SIG")
print("#################################################")

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
# STATISTICAL ANALYSIS

print("###########################################################################################################")
print("MEAN")


A1_sim_mean = statistics.mean(A1_sim)
print("A1_sim_mean")
print(A1_sim_mean)
A1_tweets_mean = statistics.mean(A1_tweets)
print("A1_tweets_mean")
print(A1_tweets_mean)
A2_sim_mean = statistics.mean(A2_sim)
print("A2_sim_mean")
print(A2_sim_mean)
A2_tweets_mean = statistics.mean(A2_tweets)
print("A2_tweets_mean")
print(A2_tweets_mean)
A3_sim_mean = statistics.mean(A3_sim)
print("A3_sim_mean")
print(A3_sim_mean)
A3_tweets_mean = statistics.mean(A3_tweets)
print("A3_tweets_mean")
print(A3_tweets_mean)
A4_sim_mean = statistics.mean(A4_sim)
print("A4_sim_mean")
print(A4_sim_mean)
A4_tweets_mean = statistics.mean(A4_tweets)
print("A4_tweets_mean")
print(A4_tweets_mean)
A5_sim_mean = statistics.mean(A5_sim)
print("A5_sim_mean")
print(A5_sim_mean)
A5_tweets_mean = statistics.mean(A5_tweets)
print("A5_tweets_mean")
print(A5_tweets_mean)
A6_sim_mean = statistics.mean(A6_sim)
print("A6_sim_mean")
print(A6_sim_mean)
A6_tweets_mean = statistics.mean(A6_tweets)
print("A6_tweets_mean")
print(A6_tweets_mean)


print("###########################################################################################################")
print("STDEV")


A1_sim_sd = statistics.stdev(A1_sim)
print("A1_sim_sd")
print(A1_sim_sd)
A1_tweets_sd = statistics.stdev(A1_tweets)
print("A1_tweets_sd")
print(A1_tweets_sd)
A2_sim_sd = statistics.stdev(A2_sim)
print("A2_sim_sd")
print(A2_sim_sd)
A2_tweets_sd = statistics.stdev(A2_tweets)
print("A2_tweets_sd")
print(A2_tweets_sd)
A3_sim_sd = statistics.stdev(A3_sim)
print("A3_sim_sd")
print(A3_sim_sd)
A3_tweets_sd = statistics.stdev(A3_tweets)
print("A3_tweets_sd")
print(A3_tweets_sd)
A4_sim_sd = statistics.stdev(A4_sim)
print("A4_sim_sd")
print(A4_sim_sd)
A4_tweets_sd = statistics.stdev(A4_tweets)
print("A4_tweets_sd")
print(A4_tweets_sd)
A5_sim_sd = statistics.stdev(A5_sim)
print("A5_sim_sd")
print(A5_sim_sd)
A5_tweets_sd = statistics.stdev(A5_tweets)
print("A5_tweets_sd")
print(A5_tweets_sd)
A6_sim_sd = statistics.stdev(A6_sim)
print("A6_sim_sd")
print(A6_sim_sd)
A6_tweets_sd = statistics.stdev(A6_tweets)
print("A6_tweets_sd")
print(A6_tweets_sd)

# RESULT PRINT OUTS

# AGENT 1
# U statistic: 650987.5
# p-value: 2.219313305813892e-10
# STAT SIG
# #################################################
# AGENT 2
# U statistic: 456142.5
# p-value: 3.4210360058276325e-06
# STAT SIG
# #################################################
# AGENT 3
# U statistic: 34203.0
# p-value: 0.030822816597994216
# STAT SIG
# #################################################
# AGENT 4
# U statistic: 5792.5
# p-value: 0.7219717218578496
# NOT STAT SIG
# #################################################
# AGENT 5
# U statistic: 43318.0
# p-value: 0.04622524205460272
# STAT SIG
# #################################################
# AGENT 6
# U statistic: 181318.0
# p-value: 0.7575651847722036
# NOT STAT SIG
# #################################################
# ###########################################################################################################
# MEAN
# A1_sim_mean
# 5.631911532385466
# A1_tweets_mean
# 5.007692307692308
# A2_sim_mean
# 5.606635071090047
# A2_tweets_mean
# 5.096036585365853
# A3_sim_mean
# 5.661927330173776
# A3_tweets_mean
# 5.915254237288136
# A4_sim_mean
# 5.442338072669826
# A4_tweets_mean
# 5.315789473684211
# A5_sim_mean
# 5.311216429699842
# A5_tweets_mean
# 5.651006711409396
# A6_sim_mean
# 5.551342812006319
# A6_tweets_mean
# 5.590987868284229
# ###########################################################################################################
# STDEV
# A1_sim_sd
# 1.1118147064723447
# A1_tweets_sd
# 1.9925496618305607
# A2_sim_sd
# 1.139795210273762
# A2_tweets_sd
# 1.8881580041262631
# A3_sim_sd
# 0.9949655301080261
# A3_tweets_sd
# 0.27969064676509087
# A4_sim_sd
# 1.3384204153818173
# A4_tweets_sd
# 2.083070158815998
# A5_sim_sd
# 1.4472203624366113
# A5_tweets_sd
# 0.8998961989438402
# A6_sim_sd
# 1.216046040445777
# A6_tweets_sd
# 1.1422087649373858
# (base) madeleine@Air-1957 Mann-Whitney % 