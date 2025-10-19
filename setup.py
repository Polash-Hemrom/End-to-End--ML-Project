import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "End-to-End--ML-Project"
AUTHOR_USER_NAME = "Polash Hemrom"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "code.hemrom@gmail.com"

setuptools.setup (
    name = SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small Python Pacakge for ml app",
    long_description= "text/markdown",

    package_dir = {"": "src"},
    pacakges = setuptools.find_packages(where = "src")
)