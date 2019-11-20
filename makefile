.PHONY: clean build publish

build: clean
	python -m pip install --upgrade --quiet setuptools wheel twine
	python setup.py --quiet sdist bdist_wheel

publish: build
	python -m twine check dist/*
	python -m twine upload dist/*
	python -m twine upload --skip-existing dist/*

clean:
	rm -r build dist *.egg-info || true