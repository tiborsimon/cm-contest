.PHONY: all f1 f2 f3 t1 t2 t3 test

run: f1 f2 f3

test: t1 t2 t3

f1:
	@echo '==============================='
	@echo ' F E L A D A T   1'
	@echo '==============================='
	@echo ' I N P U T'
	@echo '-------------------------------'
	@cat input-1.txt
	@echo ''
	@python feladat-1/main.py input-1.txt output-1.txt
	@echo ' O U T P U T'
	@echo '-------------------------------'
	@cat output-1.txt
	@printf "\n\n"

f2:
	@echo '==============================='
	@echo ' F E L A D A T   2'
	@echo '==============================='
	@echo ' I N P U T'
	@echo '-------------------------------'
	@cat input-2.txt
	@echo ''
	@python feladat-2/main.py input-2.txt output-2.txt
	@echo ' O U T P U T'
	@echo '-------------------------------'
	@cat output-2.txt
	@printf "\n\n"

f3:
	@echo '==============================='
	@echo ' F E L A D A T   3'
	@echo '==============================='
	@echo ' I N P U T'
	@echo '-------------------------------'
	@cat input-3.txt
	@echo ''
	@python feladat-3/main.py input-3.txt output-3.txt
	@echo ' O U T P U T'
	@echo '-------------------------------'
	@cat output-3.txt
	@printf "\n\n"

t1:
	@echo 'TESTING FELADAT 1'
	@cd feladat-1 && python -m unittest discover
	@printf "\n\n"

t2:
	@echo 'TESTING FELADAT 2'
	@cd feladat-2 && python -m unittest discover
	@printf "\n\n"

t3:
	@echo 'TESTING FELADAT 3'
	@cd feladat-3 && python -m unittest discover
	@printf "\n\n"

