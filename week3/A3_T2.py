
print("Program starting.")
print("String comparisons")
wordfirst = input("Insert first word: ")
character = input("Insert a character: ")
if character in wordfirst:
    print(f'Word "{wordfirst}" contains character "{character}"')
else:
    print(f'Word "{wordfirst}" doesn\'t contain character "{character}"')
wordsecond = input("Insert second word: ")
if wordfirst == wordsecond:
    print(f'Both inserted words are the same alphabetically, "{wordfirst}"')
elif wordfirst < wordsecond:
    print(f'The first word "{wordfirst}" is before the second word "{wordsecond}" alphabetically.')
else:
    print(f'The second word "{wordsecond}" is before the first word "{wordfirst}" alphabetically.')
print("Program ending.")
