from optparse import OptionParser
import string
import sys
import glob

import arabsort

parser = OptionParser()


parser.add_option("-u", "--unit", dest="unit", default="")
parser.add_option("-o", "--output", dest="output", default="")
parser.add_option("-f", "--font", dest="font", default="40")
parser.add_option("-e", "--english", action="store_true", dest="english", default=False)
parser.add_option("-v", "--vocalize", action="store_true", dest="vocalize", default=False)
parser.add_option("-s", "--sort", type="choice", action="store", dest="sort", default="input", choices=["input", "english", "arabic"])
parser.add_option("-a", "--attributes", type="choice", action="store", dest="attr", default="x",
                  choices=["a", "v", "p", "n", "o", "x"])

(options, args) = parser.parse_args()
texhead = """
\\documentclass[40pt]{article}
\\usepackage{arabtex}
\\begin{document}
\\setarab
\\novocalize
% \\transtrue
\\arabtrue
\\huge

\\begin{RLtext}


"""

textail = """
\end{RLtext}
\end{document}
"""

englishinsert = "\\end{RLtext} %s \\begin{RLtext}"


def splitline(line):
    return string.split(line,";")

def addenglish(e):
    return englishinsert % e

def buildtable():
    pass

atoe = {}
etoa = {}
arabkeys = []


if options.unit:
    files = ["unit%s.inc" % options.unit]
else:
    files = glob.glob("*.inc")
    files.sort()

        
# process the input files

for f in files:
    lines = open(f).readlines()
    for line in lines:
        if string.find(line,";") == -1: continue
        arabic, english, attrs = splitline(line)
        attrs += (", f:%s" % f)
        if options.attr != "x":
            if options.attr != attrs.strip()[0]:
                continue
        # duplicate english where needed
        if string.find(english,",") == -1:
            ewords = [english]
        else:
            ewords = string.split(english)
        atoe[arabic] = english
        arabkeys.append(arabic)
        for eword in ewords:
            etoa[eword.strip()] = arabic

#   
# establish sorting order



if options.sort == "input":
    index = arabkeys
elif options.sort == "english":
    index = []
    englishkeys = etoa.keys()
    englishkeys.sort()
    for key in englishkeys:
        index.append(etoa[key])
elif options.sort == "arabic":
    index = sorted(arabkeys, arabsort.arabic_compare)
    #print arabkeys
    #print index
    #sys.exit()
elif options.sort == "random":
    pass
else:
    raise "Sorting error"


# process output options

if options.vocalize:
    texhead = texhead.replace("novocalize", "vocalize")

texhead = texhead.replace("40pt",("%spt" % options.font))

if options.output == "":
    outfile = sys.stdout
else:
    outfile = open(options.output)



# generate the output files

def writeln(l=""):
    outfile.write("%s\n" % l)
writeln(texhead)


    
for arabic in index:
    writeln(arabic)
    if options.english:
        writeln(addenglish(atoe[arabic]))
    writeln()
writeln(textail)
