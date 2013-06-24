def ispalindrome(word):
    return word == word[::-1]
    
palindrome_word = raw_input("Fill in the following sentence: Is _______ a palindrome?\n")
print ispalindrome(palindrome_word)