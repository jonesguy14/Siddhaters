#!/usr/bin/python3
from urllib.request import urlopen
import json
import urllib.request, urllib.parse

class Siddhater(object):  
    def __init__(self):
        book = None

    def replace_all(self, text):
        #gets rid of bad html stuff
        for i, j in self.rdict.items():
            text = text.replace(i, j)
        return text
    
    def showsome(self, searchfor):
      #google search
      link = 'null'
      query = urllib.parse.urlencode({'q': 'sparknotes '+searchfor})
      url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
      search_response = urllib.request.urlopen(url)
      search_results = search_response.read().decode("utf8")
      results = json.loads(search_results)
      data = results['responseData']
      #print('Total results: %s' % data['cursor']['estimatedResultCount'])
      hits = data['results']
      #print('Top %d hits:' % len(hits))
      for h in hits: 
        if link=='null': link = h['url']#print(' '+h['url'])
      #print('For more results, see %s' % data['cursor']['moreResultsUrl'])
      return link

    def search(self, title):
        self.rdict = { "&rsquo;" : "'",
                  "<i>" : "",
                  "</i>" : "",
                  "&ldquo;" : "\"",
                  "&rdquo;" : "\"",
                  "Sparknotes: " : "",
                  "Mr." : "Mr",
                  "Mrs." : "Mrs",
                  "Dr." : "Dr" }
    
        book = title
        main_url = self.showsome(book)
        print(main_url)
        self.get_title(main_url)
        self.get_facts(main_url)
        self.get_characters(main_url)
        self.get_themes(main_url)

    def get_title(self, main_url):
        #title
        webpage = urlopen(main_url+'/summary.html').read().decode('utf-8')
        index = webpage.index("<title>")
        index2 = webpage.index("</title>")
        print(self.replace_all(webpage[index+7:index2])+"\n")

    def get_facts(self, main_url):
        #facts (author)
        factspage = urlopen(main_url+'/facts.html').read().decode()
        for line in factspage.splitlines():
            #if all(s not in line for s in [";&nbsp;", "</p>", "author"]):
            if line.find(";&nbsp;")!=-1 and line.find("</p>")!=-1 and line.find("author")!=-1:
                start = line.index(";&nbsp;")
                end = line.index("</p>")
                print("Author: "+self.replace_all(line[start+7:end])+"\n")

    def get_characters(self, main_url):
        #characters
        print("CHARACTERS")
        print_next = 0
        characterpage = urlopen(main_url+'/characters.html').read().decode()
        for line in characterpage.splitlines():
            if print_next == 1:
                if "." in self.replace_all(line):
                    print_next = 0
                    upto = line.find(".")
                    print(self.replace_all(charstr), self.replace_all(begstr), self.replace_all(line[0:upto+1]))
                else:
                    begstr = line.strip()
            if line.find("<b>")!=-1:
                start = line.index("<b>")
                end = line.index("</b")
                charstr = "-"+line[start+3:end]+": "
                print_next = 1

    def get_themes(self, main_url):
        #themes
        themespage = urlopen(main_url+'/themes.html').read().decode('utf-8')
        theme_tit_s = themespage.index("<title>")
        theme_tit_e = themespage.index("</title>")
        print("\n"+themespage[theme_tit_s+7:theme_tit_e].replace("SparkNotes: ",""))
        for line in themespage.splitlines():
            if (line.find("<h5")!=-1 and line.find("</h5>")!=-1 and line.find("href")==-1):
                start = line.index("<h5")
                end = line.index("</h5")
                if "id=" in line:
                    print("-"+self.replace_all(line[start+4:end]).split(">")[1])
                else: print("-"+self.replace_all(line[start+4:end]))
                
Nirvana = Siddhater()