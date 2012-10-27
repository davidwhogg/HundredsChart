.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: against_school.pdf hundreds_chart.pdf rubiks_cube.pdf

hundreds_chart.pdf: hundreds_chart_default.pdf

hundreds_chart_default.pdf: hundreds_chart.py
	python hundreds_chart.py

%.pdf: %.tex hogg_book.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
