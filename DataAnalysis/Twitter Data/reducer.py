import sys

curr_word = None
curr_count = 0
word = None

# how to run the code
# cat .\use_for_mapper.txt | sort | python .\reducer.py
# use_for_mapper.txt: result from cleanTwitterText.py

# OR: don't have to write to a text file
# python .\cleanTwitterText.py | sort | python .\reducer.py

#sys.stdout = open("map_reduce_result.txt", "a", encoding='utf-8')

keyLists = ['covid', 'death', 'unemployment', 'health', 'income']

result_dict = dict(zip(keyLists, [0]*len(keyLists)))

#covid_list = ["covid", "coronavirus"]
#death_list = ["death", "die", "dead"]
#unemployment_list = ["unemployment", "unemployed"]
#health_list = ["welfare", "health", "pensioners"]
#income_list = ["income"]

covid_counter = 0
death_counter = 0
unemployment_counter = 0
health_counter = 0
income_counter = 0

for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)
    
    count = int(count)

    covid_matched = False
    death_matched = False
    unemployment_matched = False
    health_matched = False
    income_matched = False

    if curr_word:
        if ("covid" in curr_word) or ("coronavirus" in curr_word):
            covid_matched = True
            covid_counter += count
        
        if ("death" in curr_word) or ("die" in curr_word) or ("dead" in curr_word):
            death_matched = True
            death_counter += count

        if ("unemployment" in curr_word) or ("unemployed" in curr_word):
            unemployment_matched = True
            unemployment_counter += count
        
        if ("welfare" in curr_word) or ("health" in curr_word) or ("pensioners" in curr_word):
            health_matched = True
            health_counter += count

        if "income" in curr_word:
            income_matched = True
            income_counter += count
    
    if covid_matched == False or death_matched == False or health_matched == False or income_matched == False:
        curr_word = word

result_dict['covid'] = covid_counter
result_dict['death'] = death_counter
result_dict['unemployment'] = unemployment_counter
result_dict['health'] = health_counter
result_dict['income'] = income_counter

print(result_dict)

