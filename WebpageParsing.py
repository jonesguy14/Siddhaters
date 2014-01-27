from urllib.request import urlopen

webpage = urlopen('http://www.sparknotes.com/lit/siddhartha/summary.html').read().decode('utf-8')
#title
index = webpage.index("<title>")
index2 = webpage.index("</title>")
print(webpage[index+7:index2])
#characters
characterpage = urlopen('http://www.sparknotes.com/lit/siddhartha/characters.html')#.read().decode('utf-8')
print(characterpage.read().decode('utf-8'))
for line in characterpage.splitlines():
    if line.find("<b>")!=-1:
        start = line.index("<b>")
        end = line.index("</b")
        print(webpage[start+3:end])
        print("\n")