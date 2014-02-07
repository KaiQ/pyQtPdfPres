all:
	pyuic4 -o ui.py ./GUI/pyQtPdfPres.ui

clean:
	${RM} *.pyc
