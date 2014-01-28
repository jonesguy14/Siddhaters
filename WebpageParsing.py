from urllib.request import urlopen

book = input("Enter the book/essay/etc you need (make it work plz): ")
#title
webpage = urlopen('http://www.sparknotes.com/lit/'+book+'/summary.html').read().decode('utf-8')
index = webpage.index("<title>")
index2 = webpage.index("</title>")
print(webpage[index+7:index2].replace("SparkNotes: ","")+"\n")

#characters
print("CHARACTERS")
characterpage = urlopen('http://www.sparknotes.com/lit/'+book+'/characters.html').read().decode()
for line in characterpage.splitlines():
    if line.find("<b>")!=-1:
        start = line.index("<b>")
        end = line.index("</b")
        print("-"+line[start+3:end].replace("&rsquo;","'"))

#themes
themespage = urlopen('http://www.sparknotes.com/lit/'+book+'/themes.html').read().decode('utf-8')
theme_tit_s = themespage.index("<title>")
theme_tit_e = themespage.index("</title>")
print("\n"+themespage[theme_tit_s+7:theme_tit_e].replace("SparkNotes: ",""))
for line in themespage.splitlines():
    if (line.find("<h5")!=-1 and line.find("</h5>")!=-1 and line.find("href")==-1):
        start = line.index("<h5")
        end = line.index("</h5")
        if "id=" in line:
            print("-"+line[start+4:end].replace("&rsquo;","'").split(">")[1])
        else: print("-"+line[start+4:end].replace("&rsquo;","'"))