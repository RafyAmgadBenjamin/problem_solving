# How to traverse an array with two pointers

def reverse_single_word(sentence, r, l):
    temp_str = ""
    while (r >= l):
        temp_str += sentence[r]
        r -= 1
    return temp_str


def two_pointers(sentence):
    left = 0
    right = left + 1
    corr_str = ""
    while left <= len(sentence) - 1:
        if sentence[right] != " ":
            right += 1 
        else: 
           temp_word =  reverse_single_word(sentence, right, left)
           corr_str += temp_word
        #    corr_str += " "
           left = right + 1
           right += 1
    return corr_str

        


def reverse_words(sentence):
   # write you code
    sentence = sentence.strip()
    index = len(sentence) - 1
    rev_sent = ""
    while (index >= 0):
        if sentence[index] == " " and sentence[index-1] == " ":
            index = index -1
        else: 
            rev_sent += sentence[index]
        index -= 1 
    
    corr_str = two_pointers(rev_sent+ " ")

    return corr_str.strip()



if __name__ == "__main__":
    print(reverse_words("We love Python"))



