.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: against_school.pdf hundreds_chart.pdf

against_school.pdf: *.tex

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
