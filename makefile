PYFILES := $(wildcard *.py)
ZIPFILE = arquivos.zip
MAKEFILE = makefile

# Digite "make" no prompt de comandos para executar todos arquivos simultaneamente.
run:
	@for f in $(PYFILES); do \
		python $$f; \
		echo ""; \
	done

zip: $(ZIPFILE)

$(ZIPFILE): $(PYFILES)
	zip -r $(ZIPFILE) $(PYFILES) makefile