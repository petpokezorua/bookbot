# Opening file: -- GLOBAL 
with open("books/frankenstein.txt") as f:
    print("Reading the book of 'Frankenstein'...")
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    print("Success! Here are the numbers :)")

# Counting the letters:
def countLetters(bookContentString):
    dict = {}
    bookContentString = bookContentString.lower()
    for char in bookContentString:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict


# Dict to list of dicts function:
def dictToList(dict):
    outputList = []
    for letter in dict:
        if (letter.isalpha()): 
            smallDict = {'name': letter, 'letterCount': dict[letter]}
            outputList.append(smallDict)
        else:
            continue
    
    return outputList                           # Hồi nãy ghi return list xong ăn l trong khi append hết vô outputDict, dui.

# Taking from Boot.dev hints - grabbing the key to sort.
def sort_on(dict):
    return dict['letterCount']

# Sorting function
def sortList(outputList):
    outputList.sort(reverse = True, key = sort_on)
    return outputList

# Outputting function     
def output(num_words, outputList):
    print(f"{num_words} words found in the document.")
    for dict in outputList:
        print(f"The '{dict['name']}' word was found {dict['letterCount']} times")

    
if __name__ == "__main__":
    dict = countLetters(file_contents)
    outputList = dictToList(dict)
    outputList = sortList(outputList)
    output(num_words, outputList)