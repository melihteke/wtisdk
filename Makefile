delete: 
	rm -rf build/
	rm -rf dist/*
	rm -rf wtisdk.egg-info
	
build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

