import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="NgiaNgia"
    version="0.0.1",
    author="T Justice Lee",
    author_email="txawjcojlee@gmail.com",
    url="https://github.com/tjusticelee/NgiaNgia",
    description="This is a calculator that manages income and expenses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

