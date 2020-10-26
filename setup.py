from setuptools import setup

setup(
    name="pytest-coverage",
    description="pytest plugin for providing test coverage reports",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="v0.0.1",
    url="https://github.com/steinbergs-python-packages/pytest-coverage",
    author="Stephan Steinberg",
    author_email="st.steinberg@t-online.de",
    license="MIT",
    py_modules=["pytest_coverage"],
    entry_points={"pytest11": ["coverage = pytest_coverage"]},
    platforms="any",
    python_requires=">=3.6",
    install_requires=["coverage", "pytest>=3.4.1"],
    keywords="python pytest coverage test report",
    classifiers=[
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
