from setuptools import find_packages, setup

setup(
    name="excel_method_editor",
    version="1.0",
    packages=find_packages(),
    license="MIT",
    description="Write automated methods using excel.",
    install_requires=[
        "loguru",
        "xlwings",
    ],
    url="https://github.com/Pfizer-BradleyBare/ExcelMethodEditor.git",
    author="Bradley Bare",
    author_email="Bradley.Bare@pfizer.com",
)
