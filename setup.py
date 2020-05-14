import setuptools

setuptools.setup(
    name="gounlimited",
    version="0.0.1",
    author="Nik96",
    author_email="nik96i@outlook.com",
    description="Unofficial Python API for GoUnlimited.to",
    keywords="api gounlimited video streaming hosting unlimited gounlimited.to",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nik96i/GoUnlimited",
    packages=['gounlimited'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
