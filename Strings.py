# concatinating strings
x = 40
Name = "Nate"
result = str(x) + Name
print("Concatenated String:", result)

# Removing spaces at the beginning, middle and end of a string
txt = "  Hello,  Uganda!    "
cleaned = txt.strip().replace(" ", "").replace("  ", "")
print("Cleaned String:", cleaned)

# 3. Converting the value of ‘txt’ to uppercase
uppercase_txt = txt.upper()
print("Uppercase:", uppercase_txt)

# 4. Replacing character ‘U’ with ‘V’ in the string
replaced_txt = txt.replace("U", "V")
print("Replaced string:", replaced_txt)

# 5. Return characters in 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
print("2nd to 4th characters:", y[1:4])

# 6. Correct the string with quotation marks
x = 'All "Data Scientists" are cool!'  # Use single quotes outside
print(x)