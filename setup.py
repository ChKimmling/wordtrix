from setuptools import setup, find_packages

setup(
    name="wordtrix",
    version="0.1.0",
    author="Christian Kimmling",
    author_email="ckimmling@gmail.com",
    description="WordTrix is a command-line tool and library for managing and checking anagrams.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChKimmling/wordtrix",
    packages=find_packages(),
    install_requires=[],  # add dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)