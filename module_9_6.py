def all_variants(text):
    for a in range(len(text)):
        for x in range(len(text)-a):
            yield text[x:x + a + 1]

a = all_variants("abc")
for i in a:
     print(i)
