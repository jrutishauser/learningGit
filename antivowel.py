def anti_vowel(text):
    text = str(text)
    vowels = "aeiouAEIOU"
    for i in range(0, len(vowels)):
        text = text.replace(vowels[i], "")
    print text
    
anti_vowel('Hey look words!')