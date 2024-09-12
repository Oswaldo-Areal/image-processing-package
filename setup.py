from setuptools import setup, find_packages

with open("README.md") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name="image_processing",
  version="0.0.1",
  author="Oswaldo Areal",
  description="Image Processing Package using Skimage",
  long_description=page_description,
  url="https://github.com/Oswaldo-Areal/image-processing-package",
  packages=find_packages(),
  install_requires=requirements,
  python_requires=">=3.5",
)
