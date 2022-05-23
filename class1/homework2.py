from turtle import right
import os

with open('words.txt', 'r', encoding='UTF-8')as f:
    dictionary = [word.strip() for word in f if word != '\n']
    f.close()
new_dictionary = []
new_dictionary_path = 'sort_dictionary.txt'
if os.path.exists(new_dictionary_path):
    with open(new_dictionary_path, 'r', encoding='UTF-8')as f:
        for word in f:
            new_dictionary.append(tuple(word.strip().split(",")))
        f.close()
    for word in new_dictionary:
        word = "".join(word)
# print(new_dictionary)


def better_solution(random_word, dictionary):
    sorted_random_word = "".join(sorted(list(random_word)))
    # print(sorted_random_word)

    if len(new_dictionary) == 0:
        for word in dictionary:
            # print(word)
            sorted_word = "".join(sorted(list(word)))
            new_dictionary.append((sorted_word, word))

        new_dictionary.sort()
        f = open(new_dictionary_path, 'w')
        for words in new_dictionary:
            f.write(words[0]+","+words[1]+'\n')
        f.close()
        # print(new_dictionary)

    # print(dictionary[0][0] > sorted_random_word)
    # print(new_dictionary)
    # left, right = 0, len(dictionary)-1
    # mid = (left+right)//2
    # print(dictionary[mid][0] == word)
    anagram = binary_search(sorted_random_word, new_dictionary)
    print(anagram)


def binary_search(word, dictionary):
    result = []
    # print(word)
    # print(dictionary)

    left, right = 0, len(dictionary)-1
    while left <= right:
        mid = (left+right)//2
        # print(dictionary[mid][0])
        if dictionary[mid][0] == word:
            # print("一致")
            # print(dictionary[mid][1])
            result.append(dictionary[mid][1])
            tmp = mid
            while dictionary[mid+1][0] == word:
                result.append(dictionary[mid+1][1])
                mid += 1
            mid = tmp
            while dictionary[mid-1][0] == word:
                result.append(dictionary[mid-1][1])
                mid -= 1

            break
        elif dictionary[mid][0] < word:
            left = mid+1
        else:
            right = mid-1
    return result


better_solution("acdr", dictionary)
