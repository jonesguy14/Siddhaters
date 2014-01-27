from urllib.request import urlopen

#title
webpage = urlopen('http://www.sparknotes.com/lit/siddhartha/summary.html').read().decode('utf-8')
index = webpage.index("<title>")
index2 = webpage.index("</title>")
print(webpage[index+7:index2].replace("SparkNotes: ","")+"\n")

#characters
print("Characters: ")
characterpage = urlopen('http://www.sparknotes.com/lit/siddhartha/characters.html').read().decode()
for line in characterpage.splitlines():
    if line.find("<b>")!=-1:
        start = line.index("<b>")
        end = line.index("</b")
        print(line[start+3:end].replace("&rsquo;","'")+", ")

#themes
themespage = urlopen('http://www.sparknotes.com/lit/siddhartha/themes.html').read().decode('utf-8')
theme_tit_s = themespage.index("<title>")
theme_tit_e = themespage.index("</title>")
print(themespage[theme_tit_s+7:theme_tit_e].replace("SparkNotes: ","")+"\n")