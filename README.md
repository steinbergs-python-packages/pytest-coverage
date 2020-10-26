# pytest-coverage

This [pytest](http://pytest.org) plugin generates test coverage reports.

## Requirements

1. pytest-coverage searches a ```.coveragerc``` file in the root path of test project in order to enable test coverage:
   ```
    # .coveragerc to control coverage.py
    [run]
    omit =  *usr/local/lib*
            */ve/*
            */__init__.py
            */conftest.py
            */testcoverage.py
            tests/*

    # leave this field empty to include imported modules only
    source =

    # leave this field empty if only reports are needed
    # specify this to store coverage data for later processing (e.g. combining with others)
    data_file =

    [report]
    exclude_lines =
        pragma: no cover
        sys.exit
        NotImplementedError
        if platform.system() == "Windows":
        if "Windows" in platform.system():

    [html]
    # leave this field empty to disable html report
    directory = results/coverage/html

    [xml]
    # leave this field empty to disable xml report
    output = results/coverage/coverage.xml
   ```
   If no such file is found, test coverage is disabled.

## Installation

To install pytest-coverage, you can use (one of) the following command(s):
```
$ pip install git+https://github.com/steinbergs-python-packages/pytest-coverage
$ pip install git+https://github.com/steinbergs-python-packages/pytest-coverage@v0.0.1
$ pip install https://github.com/steinbergs-python-packages/pytest-coverage/archive/v0.0.1/pytest-coverage.zip
```

To uninstall pytest-coverage, you can use the following command:
```
$ pip uninstall pytest-coverage
```
