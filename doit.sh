python dic.py -u $1 -v -e -f10 -sinput > tmp.tex ; latex tmp.tex ; dvipdf tmp.dvi ; evince tmp.pdf
