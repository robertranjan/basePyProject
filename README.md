# pybase

Here are the tools we need to have in a py-project

- [x] [tests][0]
- [x] [pre-commit][1]
- [x] flake8 - linter
- [x] [black][5] - code formatter
- [x] [tox][2] - test with multiple environments
- [x] [poetry][3] - packaging and dependency manager
- [ ] [pyenv][4] - py version manager
- [ ] makefile
- [ ] [github actions](https://github.com/pre-commit/action)

## poetry

    poetry new --name pybase pybase

## pre-commit

    pre-commit install
    pre-commit sample-config > .pre-commit-config.yaml
    pre-commit run --all-files

## flake8

    cat > .flake8 << EOL
    [flake8]
      max-line-length = 88
      extend-ignore =
        # See https://github.com/PyCQA/pycodestyle/issues/373
        E203,
    EOL

## tox

create `tox.ini`

    cat > tox.ini <<EOF

    [tox]
    envlist = py310,pre-commit
    isolated_build = True

    skipdist = True
    skip_missing_interpreters = True

    [testenv]
    setenv =
        key1 = value1
        key2 = value2

    deps =
        -rrequirements.txt

    commands =
        python --version
        python -m pip install --upgrade pip
        pytest -v tests/

    passenv = PYTHONPATH

    allowlist_externals = pre-commit

    [testenv:pre-commit]
    deps =
        ; black
        ; flake8
        ; flake8-black
        pre-commit
    commands =
        ; black  # you want black before flake8
        ; flake8
        ; pre-commit run --all-files --show-diff-on-failure
        ; pre-commit run --all-files
        pre-commit run
    EOF

[1]: https://github.com/pre-commit/pre-commit
[2]: https://tox.wiki/en/latest/index.html
[3]: https://python-poetry.org
[4]: https://github.com/pyenv/pyenv
[5]: https://black.readthedocs.io/en/stable/index.html
[0]: https://docs.pytest.org/en/7.1.x/contents.html
