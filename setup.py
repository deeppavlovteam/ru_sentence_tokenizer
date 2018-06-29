import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ru_sent_tokenize",
    version="0.0.1",
    author="Marat Zaynutdinov",
    author_email="tsundokum@gmail.com",
    description="Rule-based sentence tokenizer for Russian language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepmipt/ru_sentence_tokenizer",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)