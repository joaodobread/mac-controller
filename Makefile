# Makefile

.PHONY: all clean

all: build

build:
	python setup.py py2app

run:
	python setup.py py2app -A
	open dist/MacControllerApi.app

build_dev:
	python setup.py py2app -A


clean:
	rm -rf build dist

