import sys

curr_word = None
curr_count = 0
word = None

for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)
    # Convert the count to an int
    count = int(count)
    # If the current word is the same as the previous word,
    # increment its count, otherwise print the words count
    # to stdout
    if curr_word == word:
        #print("current word:")
        #print(curr_word, curr_count)
        curr_count += count
    else:
        # Write word and its number of occurrences as a key-value
        # pair to stdout
        if curr_word:
            #print("word:")
            #print(curr_word)
            print ('{0}\t{1}'.format(curr_word, curr_count))
        curr_word = word
        curr_count = count

# Output the count for the last word
if curr_word == word:
    
    print ('{0}\t{1}'.format(curr_word, curr_count))
    print("end")


