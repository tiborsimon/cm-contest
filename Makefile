YELLOW := $(shell tput setaf 3)
RESET:= $(shell tput sgr0)

.PHONY: run f1 f2 f3 t1 t2 t3 test

run: f1 f2 f3

test: t1 t2 t3

f1:
	@echo "$(YELLOW)FELADAT 1$(RESET)"
	@echo '-------------------------------'
	@cat input-1.txt
	@python feladat-1/f1.py input-1.txt output-1.txt
	@echo '-------------------------------'
	@cat output-1.txt
	@printf "\n\n"

f2:
	@echo "$(YELLOW)FELADAT 2$(RESET)"
	@echo '-------------------------------'
	@cat input-2.txt
	@python feladat-2/f2.py input-2.txt output-2.txt
	@echo '-------------------------------'
	@cat output-2.txt
	@printf "\n\n"

f3:
	@echo "$(YELLOW)FELADAT 3$(RESET)"
	@echo '-------------------------------'
	@cat input-3.txt
	@python feladat-3/f3.py input-3.txt output-3.txt
	@echo '-------------------------------'
	@cat output-3.txt
	@printf "\n\n"

t1:
	@echo "$(YELLOW)FELADAT 1$(RESET)"
	@cd feladat-1 && python -m unittest discover
	@printf "\n\n"

t2:
	@echo "$(YELLOW)FELADAT 2$(RESET)"
	@cd feladat-2 && python -m unittest discover
	@printf "\n\n"

t3:
	@echo "$(YELLOW)FELADAT 3$(RESET)"
	@cd feladat-3 && python -m unittest discover
	@printf "\n\n"

