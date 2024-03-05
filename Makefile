.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: hundreds_chart.pdf

hundreds_chart.pdf: hundreds_chart_default.pdf

hundreds_chart_default.pdf: hundreds_chart.py space_filling_curve.py
	python3 hundreds_chart.py

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
