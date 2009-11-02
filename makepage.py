page = u"""
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ar" lang="ar">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      
      
</head>      
   
<body>
    <<here>>
</body>
</html>


"""


def makepage(text, filename):
    import codecs
    outfile = codecs.open(filename, "w", encoding="utf-8")
    res = page.replace("<<here>>", text)
    outfile.write(res)
    outfile.close()

def test():
    import arabise
    text = makepage(arabise.arabise("qlAm"),"test.html")
    
    

if __name__ == "__main__":
    test()

