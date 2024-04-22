#Check if input strings are anagram


def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")

are_anagrams("listen","silent")