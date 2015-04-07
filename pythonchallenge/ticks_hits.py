text = "recognize the characters. maybe they are in the book, but MAYBE they are in the page source."
output = ""
for char in text:
    l = text.count(char)
    if l < 20:
        print char, ":", l


