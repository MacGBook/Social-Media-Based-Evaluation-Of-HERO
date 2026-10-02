# Evacuation-Social-Simulation-Component

# RUN INSTRUCTIONS

(1) Ensure Ollama is downloaded and working on your computer. Once downloaded, open Ollama in the desktop app. There should be a dropdown menue with a number of LLM models you can use. Click on one to download that model. I reccomend starting with gemma3:1b as that is currently what the program is confirgured to. 

(2) Once that model version is downloaded, feild Ollama a general question like "what color is the sky" to get it running and make sure it is working. Keep the desktop app open while you run the following code for best and fastest results. 

(4) Open your terminal and CD into the file that the code is stored in (i.e. Evacuation-Social-Simulation-Component-[your_branch_name] wherever it is located on your device or tied to Github).

(5) On this branch of the code, you should have a document called "your_list_of_prompts.md". This document will have 10 prompts saved as strings under variable names. 

(6) Copy the prompt string (only the string, not the variable name) and past it over the existing prompt in the evac_mess.py file. This should mean evacuation_message = the prompt string you're starting with. Save all files. 

(7) You will be asked to do 100 social simulation runs on this prompt. To do this, run the following loop command in your terminal: for i in {1..100}; do python main.py; done 

(8) This will take a while to load! If this is too many runs all at once (i.e. if the program crashes when you run this) feel free to break up this loop to how many number of runs works at once i.e. run "for i in {1..5}; do python main.py; done" 20 times, "for i in {1..10}; do python main.py; done" 10 times...etc to get to 100 runs. 

(9) These runs with automatically save and append themselves to the respective CSV files. Once you're done with the runs, save all your code and push it to your branch on the repo. This will share your CSV run file results with me for our statistical analyses. And you're done! 
