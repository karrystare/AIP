import re
import os

fileresult = open("result.txt", mode = "a", encoding = "utf-8")
filestop = open("stopwords.txt", 'r', encoding='utf-8').read()
stoplist = filestop.split("\n")
filestop.close()

def process(string_list)
    result = []
    sentence = ""
    for line in string_list:
        line = re.sub('[^\w \n\.]+', '', line)
        line = re.sub('[0-9\.\_]+', '', line)
        line = re.sub('((\w)\2{2,})', '', line).strip().lower()
        words = line.split(' ')
        for character in word:
            if character not in stoplist and len(character) > 2:
                sentence += (character + ' ').strip()            
        if sentence != '' and len(sentence) > 3:
            if sentence.find(' ') != -1:
                sentence += '\n'
                result.append(sentence)        
    return result

def clean(filename):
    file = open(filename, mode = "r", encoding = "utf-8")
    lines = file.read().split("\n")
    file.close()
    lines = process(lines)
    lines = set(filter(None, lines))
    lines.pop() 
    string = "\n".join(lines)
    fileresult.write(string + "\n")
    
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    path = os.path.basename(f)
    if path.find("convert") == -1 and path.find("result") == -1 and f.find('stopwords') == -1 and f.endswith('.txt') == 1:
        print(f)
        clean(f)
        
fileresult.close()
