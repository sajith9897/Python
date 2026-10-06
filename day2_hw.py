paragraph = """Python is an incredible programming language used for web development, 
data science, machine learning, and automation. This Python course will guide you 
through fundamental programming concepts step-by-step."""


print("Length of paragraph:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("First 50 characters preview:",paragraph[0:50])

replaced_paragraph = paragraph.replace("Python", "PYTHON")
print("\nReplaced Paragraph:\n", replaced_paragraph)

lowercase_paragraph = paragraph.lower()
print("\nLowercase Paragraph:\n", lowercase_paragraph)

trimmed_paragraph = paragraph.strip()
print("\nTrimmed Paragraph:\n", trimmed_paragraph)

words_list = trimmed_paragraph.split()
print("\nWords List:\n", words_list)

if "course" in paragraph: 
    print("\nMessage: The word 'course' was found in the paragraph!")


final_message = "The course description is {} characters long and has {} words.".format(len(trimmed_paragraph), len(words_list))

print("\n" + final_message)