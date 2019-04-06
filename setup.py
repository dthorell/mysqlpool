import re
import os
import setuptools
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_mysqlpool",
    version=find_version("flask_mysqlpool", "__init__.py"),
    author="Daniel Thorell",
    author_email="dthorell@outlook.com",
    description="Wrapper for mysql.connector.python to get a pool of mysql connections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dthorell/mysqlpool",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        'flask >= 1.0.0',
        'mysql-connector-python >= 8.0.0'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        "Operating System :: OS Independent",
    ],
)
