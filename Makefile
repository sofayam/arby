vocab.pdf : vocab.tex
	latex vocab.tex
	dvipdf vocab.dvi
clean:
	rm -f *.pyc tmp.* *.dvi *.aux *~ *.pdf *.log \#*\#
