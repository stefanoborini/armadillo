env:
	python -m venv .envs/py37
	. .envs/py37/bin/activate && \
		pip install -r ci/requirements.txt && \
		pip install -r ci/dev-requirements.txt

clean:
	rm -rf .envs/py37


flake8:
	flake8 armadillo tests
