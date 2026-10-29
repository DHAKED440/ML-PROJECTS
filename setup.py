from setuptools import find_packages, setup  # pyright: ignore[reportMissingImports]
from typing import List

def get_requirements(file_path :str)->List[str]:

    '''
    this fuction returns the list of requiremnets

    '''
    HYPHEN_E_DOT="-e ."

    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Rahul',
    author_email='rdhaked440@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)