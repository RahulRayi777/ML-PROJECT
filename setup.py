from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str, include_editable: bool = False) -> List[str]:
    """
    Reads requirements.txt and returns a list of package names.
    Removes '-e .' unless `include_editable=True`.
    """
    with open(file_path, "r") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    # Remove '-e .' unless explicitly allowed
    if not include_editable and HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Rahul',
    author_email='rayirahul67@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt',include_editable=False)
)
