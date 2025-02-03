# Explain why the code below prints different values on lines 3 and 4.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The substring on line 4 is smaller as we are slicing it, while substring on line 5 is the full string.

# Line 3 first extracts a slice from text ranging from index 21 through index 35. That returns the string 'for the fjords'. rfind then returns 8, the index of the rightmost instance of an 'f'.

# On the other hand, line 4 does a search for the rightmost f between indexes 21 and 35. Since the f occurs at index 29, that's what the method returns.
