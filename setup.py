import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyxml",
    version="0.0.1",
    author="Genadij Razdorov",
    author_email="genadijrazdorov@gmail.com",
    description="python xml declerativly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genadijrazdorov/pyxml",
    packages=setuptools.find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
