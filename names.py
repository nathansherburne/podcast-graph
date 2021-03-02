import sys
import spacy
from spacy.tokens import Span
import re
import csv

def main():
    nlp = spacy.load('en_core_web_sm')
    #nlp.add_pipe(expand_person_entities, after='ner')
    allnames = set()

    with open(sys.argv[1]) as myfile:
        if sys.argv[1].endswith('.csv'):
            names = csvstrat(myfile)
# post-process with NLP
#            csvnames = csvstrat(myfile)
#            names = []
#            for name in csvnames:
#                ns = extract_names(nlp, name)
#                for n in ns:
#                    names.append(n[0])
        else:
            names = nlpstrat(nlp, myfile)

        for name in names:
            ns = re.compile(' and | & |:').split(name)
            for n in ns:
                n = re.sub('dr. ', '', n, flags=re.I)
                n = n.strip()
                if n:
                    allnames.add(n)
    
    allnames = list(allnames)
    allnames.sort()
    [print(f'[[{name}]]') for name in allnames]

def extract_names(nlp, s):
    doc = nlp(s)
    names = [(ent.text, ent.label_) for ent in doc.ents if ent.label_=='PERSON']
    return names

def nlpstrat(nlp, txtfile):
    allnames = []
    for line in txtfile:
        names = extract_names(nlp, line)
        for name in names:
            allnames.append(name[0])
    return allnames

def csvstrat(csvfile):
    allnames = []
    r = csv.reader(csvfile)
    for row in r:
        if len(sys.argv) == 4:
            custom_filter = sys.argv[3]
            if custom_filter:
                if not eval(custom_filter):
                    continue
        names = list(filter(lambda item: item, row[int(sys.argv[2])].split(",")))
        for name in names:
            allnames.append(name)
    return allnames



#def expand_person_entities(doc):
#    new_ents = []
#    for ent in doc.ents:
#        if ent.label_ == "PERSON":
#            if ent.start != 0:
#                new_ents.append(ent)
#        else:
#            new_ents.append(ent)
#    doc.ents = new_ents
#    return doc
#

if __name__ == "__main__":
    main()
