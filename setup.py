import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_mysqlpool",
    version="1.0.2",
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
