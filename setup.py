from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="meddata-package",  # Distribution name
    version="0.1",           # Version of your package
    packages=find_packages(),  # Automatically find packages
    install_requires=install_requires,  # Dependencies from requirements.txt
    python_requires=">=3.10"  # Python version
)