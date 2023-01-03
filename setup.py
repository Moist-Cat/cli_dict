import setuptools
from pathlib import Path

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
     name="cli_dict",
     version="1.0.0",
     author="Moist-Cat",
     author_email="moistanonpy@gmail.com",
     description="offline CLI-based dictionary",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Moist-Cat/cli_dict",
     include_package_data=True,
#     package_dir={"":"src"},
#     packages=setuptools.find_packages(where="src"),
     python_requires=">=3.8",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Linux",
     ],
 )
