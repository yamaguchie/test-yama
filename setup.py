from setuptools import find_packages, setup
from test_yama import __version__

setup(
    name="test_yama",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
