from setuptools import setup, find_packages

setup(
    name="Test-project",
    version="0.1.0",
    description="A short description of my project",
    author="Yiping",
    author_email="yiping.liu@rwth-aachen.de",
    packages=find_packages(),
    install_requires=[
        "requests==2.26.0",
    ],
    tests_require=[
        "pytest==6.2.4",
    ],
)
