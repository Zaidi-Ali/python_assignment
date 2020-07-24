
sent = input("Enter a sentence of your choice: \n").lower()

letter_search = input("\nEnter a Search Letter: ").lower()

length = len(sent)
index = 0

if length > 0:
    if letter_search in sent:
        count = sent.count(letter_search)
        index = sent.index(letter_search)
        print(f"\nSubstring count: {count} \n")
        print(f"Length = {length} \n")
        print(f"Index of the Sub_String : {index} \n")

    else:
        print("\n please enter a valid string to search ")
