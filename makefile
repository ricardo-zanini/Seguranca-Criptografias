PYFILES := $(wildcard *.py)

# Digite "make" no prompt de comandos para executar todos arquivos simultaneamente.
run:
	@for f in $(PYFILES); do \
		python $$f; \
		echo ""; \
	done