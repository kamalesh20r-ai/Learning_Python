def reverse_string(text):
    if len(text) == 1:
        return text
    return text[-1] + reverse_string(text[:-1])
text = reverse_string("Python")
print("Reversed String :", text)