from setuptools import setup


with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

setup(
    name="cn_bing_translator",
    version="0.0.2",
    author="minibear",
    description="microsoft cn.bing translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="microsoft bing translator",
    url="https://github.com/minibear2021/cn_bing_translator",
    packages=["cn_bing_translator"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["requests>=2.21.0"],
)
