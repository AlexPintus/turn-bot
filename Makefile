.PHONY: init run push

init:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && python main.py

push:
	pip freeze > requirements.txt
	. .venv/bin/activate && pip-licenses --format=markdown > licences/LIBRARY_LICENCE
	git add * && git commit -m "$(message)" && git push
