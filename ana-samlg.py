#def is_anagram(first_word, second_word):
#    result = []
#    for character1 in first_word:
#        for character2 in second_word:
#            if character1 == character2:
#                result.append(character1)
#                break
#    return result
def is_anagram(first_word, second_word):
    result = []
    for character in first_word:
        if character in second_word:
            result.append(character)
    return result

first_word="scare"
second_word="races"
result = is_anagram(first_word, second_word)
print (result)

x=(len(result))
y=(len(first_word))
if x == y:
    print('yes it is a anagram')
else:
    print('no is not a anagram')
if(len(result)) == (len(first_word)):
    print('ja, ein Anagramm')
else:
    print('nein, kein Anagramm')
#def is_anagram(first_word, second_word):
#    result = []
#    for character1 in first_word:
#        for character2 in second_word:
#            if character1 == character2:
#                result.append(character1)
#                break
#    return result

#def is_anagram(first_word, second_word):
#    result = []
#    for character in first_word:
#        if character in second_word:
#            result.append(character)
#    return result


def is_anagram(first_word, second_word):
    return [(character) for character in first_word if character in second_word]
    #return [True for character in first_word if character in second_word]

first_word="scare"
second_word="races"
result = is_anagram(first_word, second_word)
print (result)

x=(len(result))
y=(len(first_word))
if x == y:
    print('yes it is a anagram')
else:
    print('no is not a anagram')
if(len(result)) == (len(first_word)):
    print('ja, ein Anagramm')
else:
    print('nein, kein Anagramm')
#def is_anagram(first_word, second_word):
#    result = []
#    for character1 in first_word:
#        for character2 in second_word:
#            if character1 == character2:
#                result.append(character1)
#                break
#    return result

#def is_anagram(first_word, second_word):
#    result = []
#    for character in first_word:
#        if character in second_word:
#            result.append(character)
#    return result


#def is_anagram(first_word, second_word):
#    return [(character) for character in first_word if character in second_word]
#    #return [True for character in first_word if character in second_word]

def is_anagram(first_word, second_word):
   return sum(character in second_word for character in first_word)

print(is_anagram('Lagerregal', 'Garllarege'))


first_word="scare"
second_word="races"
result = is_anagram(first_word, second_word)
print (result)
z=str(result)
x=(len(z))
y=(len(first_word))
if x == y:
    print('yes it is a anagram')
else:
    print('no is not a anagram')
if(len(str(result))) == (len(first_word)):
    print('ja, ein Anagramm')
else:
    print('nein, kein Anagramm')
#def is_anagram(first_word, second_word):
#    result = []
#    for character1 in first_word:
#        for character2 in second_word:
#            if character1 == character2:
#                result.append(character1)
#                break
#    return result

#def is_anagram(first_word, second_word):
#    result = []
#    for character in first_word:
#        if character in second_word:
#            result.append(character)
#    return result


#def is_anagram(first_word, second_word):
#    return [(character) for character in first_word if character in second_word]
#    #return [True for character in first_word if character in second_word]

#def is_anagram(first_word, second_word):
#   return sum(character in second_word for character in first_word)

def is_anagram(a, b):
    return len(a) == len(b) and sorted(a.lower()) == sorted(b.lower())

result=(is_anagram('Lagerregal', 'Garllarege'))
print (result)

if True:
    print('yes it is a anagram')
else:
    print('no is not a anagram')
def is_anagram(first_word, second_word):
    result = []
    for character1 in first_word:
        for character2 in second_word:
            if character1 == character2:
                result.append(character1)
                break
    return result
first_word="scare"
second_word="races"
result = is_anagram(first_word, second_word)
print (result)

x=(len(result))
y=(len(first_word))
if x == y:
    print('yes it is a anagram')
else:
    print('no is not a anagram')
if(len(result)) == (len(first_word)):
    print('ja, ein Anagramm')
else:
    print('nein, kein Anagramm')
#!/usr/bin/python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def get_sword(word):
    return "".join(sorted(word.replace("'", "").lower()))


def get_words(words="words"):
    words = open(words)

    for word in words:
        word = word.strip()

        sword = get_sword(word)

        if not sword in wordmap:
            wordmap[sword] = []

        wordmap[sword].append(word)


def main():
    word = input("Anagram letters: ")
    while word:
        sword = get_sword(word)

        if sword in wordmap:
            print("Anagrams:", ", ".join(wordmap[sword]))
        else:
            print("No anagrams.")

        word = input("Anagram letters: ")


wordmap = {}

get_words()

if __name__ == '__main__':
    main()
