.PHONY: push

push:
	pip freeze > requirements.txt
	pip-licenses --format=markdown > licences/LIBRARY_LICENCE
    git add . && git commit -m "$(message)" && git push
