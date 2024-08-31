# Open the file in read mode
with open('results.txt', 'r') as file:
    # Read the words from the file
    # words = file.read().splitlines()
    words = [line.strip() for line in file.read().splitlines()]

counter = 0
entry = ''
entry_list = []
pre_index = 0
pre_word = ''
for word in words:
    counter += 1
    # print(word)
    entry += word + ' '
    if counter % 8 == 0:
        entry += '\n'
        print(entry)
        entry_list.append(entry)
        entry = ''

# Sort the words in alphabetical order
sorted_entries = sorted(entry_list)
# Print the sorted words
# print(sorted_entries)
with open('sorted_results.txt', 'w') as file:
    for entry in sorted_entries:
        file.write(entry)

