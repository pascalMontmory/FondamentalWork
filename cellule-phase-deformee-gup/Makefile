TEX=main.tex
PDF=main.pdf

.PHONY: pdf figures clean

pdf:
	pdflatex $(TEX)
	pdflatex $(TEX)

figures:
	python3 scripts/generate_density_saturation.py

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz $(PDF)
