from setuptools import find_packages, setup
from typing import List




<<<<<<< HEAD
def get_requirements()->List[str]:
    
    requirements_list : List[str] = []
=======
# def get_requirements()->list[str]:
    
#     requirements_list = list[str] = []
>>>>>>> adb88597ccbf9b1aa6947973685191b4dc3fcdb5

#     return requirements_list

    




setup(
name = "sensor",
version = "0.0.1",
author = "Anuj",
author_email = "anujjhariya02@gmail.com",
packages = find_packages(),
<<<<<<< HEAD
install_requires = get_requirements(),    #["pymongo"]
# install_requires =["pymongo"]
=======
# install_requires = get_requirements(),    #["pymongo"]
install_requires =["pymongo"]
>>>>>>> adb88597ccbf9b1aa6947973685191b4dc3fcdb5
)