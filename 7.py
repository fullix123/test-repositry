text2 = """
    Python is a powerful programming language.

    It is used in data science, web devolepment,
   automation, and many other fields!

   PYTHON is easy to learn, yet very versatile
"""
text2 = text2.lower()
text2 = text2.strip()
text2 = text2.replace("!", ".")
text2 = text2.split(".")
print(text2)
text1 = f"{text2[0]}"
text1 = text1.strip()
text1 = text1.lower()
print(text1)
print(text1.count("python"))
print(text1.startswith("python"), text1.endswith("language"))
print(len(f"{text2}"), (f'{text2}').count("a"), (f'{text2}').find("data"))

text = """
    Python is a powerful programming language.

    It is used in data science, web devolepment,
   automation, and many other fields!

   PYTHON is easy to learn, yet very versatile
"""
slova = {

}
text = text.replace("\n", "")
text = text.replace(".", "")
words = text.split(" ")
for i in (words):
    if i != "\n" and i != "":
        slova[i] = words.count(i)
a = ''
words1 = []
for i in words:
    if i != "\n" and i != "":
        words1.append(i)

for i in words1:
    a = a + i + "-"
