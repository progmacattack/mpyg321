import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mpg321-4br3mm0rd",
    version="0.0.1",
    author="4br3mm0rd",
    author_email="4br3mm0rd@example.com",
    description="mpg321 wrapper for python - music player for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4br3mm0rd/mpyg321",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)