.phony: clean
clean:
	find . -type f -name *.pyc | xargs rm -rf
	find . -type d -name *.py*cache* | xargs rm -rf
	find . -type d -name __pycache__ | xargs rm -rf
