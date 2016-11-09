YELLOW := $(shell tput setaf 3)
RESET:= $(shell tput sgr0)

.PHONY: run p1 p2 p3 t1 t2 t3 test

run: p1 p2 p3

test: t1 t2 t3

p1:
	@echo "$(YELLOW)PROBLEM 1$(RESET)"
	@echo '-------------------------------'
	@cat input-1.txt
	@python problem-1/p1.py input-1.txt output-1.txt
	@echo '-------------------------------'
	@cat output-1.txt
	@printf "\n\n"

p2:
	@echo "$(YELLOW)PROBLEM 2$(RESET)"
	@echo '-------------------------------'
	@cat input-2.txt
	@python problem-2/p2.py input-2.txt output-2.txt
	@echo '-------------------------------'
	@cat output-2.txt
	@printf "\n\n"

p3:
	@echo "$(YELLOW)PROBLEM 3$(RESET)"
	@echo '-------------------------------'
	@cat input-3.txt
	@python problem-3/p3.py input-3.txt output-3.txt
	@echo '-------------------------------'
	@cat output-3.txt
	@printf "\n\n"

t1:
	@echo "$(YELLOW)PROBLEM 1$(RESET)"
	@cd problem-1 && python -m unittest discover
	@printf "\n\n"

t2:
	@echo "$(YELLOW)PROBLEM 2$(RESET)"
	@cd problem-2 && python -m unittest discover
	@printf "\n\n"

t3:
	@echo "$(YELLOW)PROBLEM 3$(RESET)"
	@cd problem-3 && python -m unittest discover
	@printf "\n\n"

