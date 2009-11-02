python dic.py -v -e  -sinput > tmp.tex ; latex tmp.tex ; dvips tmp.dvi > tmp.ps ; psnup -n2 tmp.ps > tmp2.ps ; evince tmp2.ps
