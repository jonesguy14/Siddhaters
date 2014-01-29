#!/usr/bin/python3
from urllib.request import urlopen
import json
import urllib.request, urllib.parse

class Siddhater(object):
    def end_of_sent(line):
        if line.find(".")!=-1:
            ind = line.find(".")
            if line[ind-2]=="M" or line[ind-3]=="M":
                #not end of sentence
                if end_of_sent(line[ind+1:line.__len__()])==False:
                    return False
                else: return True
            else: return False
        else: return False
        
    def showsome(searchfor):
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

    def get_title(main_url):
        #title
        webpage = urlopen(main_url+'/summary.html').read().decode('utf-8')
        index = webpage.index("<title>")
        index2 = webpage.index("</title>")
        print(webpage[index+7:index2].replace("SparkNotes: ","")+"\n")

    def get_facts(main_url):
        #facts (author)
        factspage = urlopen(main_url+'/facts.html').read().decode()
        for line in factspage.splitlines():
            #if all(s not in line for s in [";&nbsp;", "</p>", "author"]):
            if line.find(";&nbsp;")!=-1 and line.find("</p>")!=-1 and line.find("author")!=-1:
                start = line.index(";&nbsp;")
                end = line.index("</p>")
                print("Author: "+line[start+7:end].replace("&rsquo;","'")+"\n")

    def get_characters(main_url):
        #characters
        print("CHARACTERS")
        print_next = 0
        characterpage = urlopen(main_url+'/characters.html').read().decode()
        for line in characterpage.splitlines():
            if print_next == 1:
                if __self__.end_of_sent(line)==True:
                    print_next = 0
                    upto = line.find(".")
                    print(charstr, begstr, line[0:upto+1].replace("&rsquo;","'").replace("<i>","").replace("</i>",""))
                else:
                    begstr = line.replace("&rsquo;","'").strip()
            if line.find("<b>")!=-1:
                start = line.index("<b>")
                end = line.index("</b")
                charstr = "-"+line[start+3:end].replace("&rsquo;","'")+": "
                print_next = 1

    def get_themes(main_url):
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
                    print("-"+line[start+4:end].replace("&rsquo;","'").split(">")[1])
                else: print("-"+line[start+4:end].replace("&rsquo;","'"))
    
    book = input("Enter the book/essay/etc you need: ")
    main_url = showsome(book)
    print(main_url)
    get_title(main_url)
    get_facts(main_url)
    get_characters(main_url)
    get_themes(main_url)