# Summary Creation Tool

[![DOI](https://zenodo.org/badge/532655669.svg)](https://zenodo.org/badge/latestdoi/532655669)
[![GitHub Release](https://img.shields.io/github/release/akshat22/SE_HW2345.svg)](https://github.com/akshat22/SE_HW2345/releases)
<a href="https://github.com/akshat22/SE_HW2345/blob/main/LICENSE.md"><img 
alt="License" src="https://img.shields.io/github/license/akshat22/SE_HW2345"></a>
[![GitHub contributors](https://img.shields.io/github/contributors/akshat22/SE_HW2345)](https://github.com/akshat22/SE_HW2345/graphs/contributors)
[![Open Issues](https://img.shields.io/github/issues/akshat22/SE_HW2345)](https://github.com/akshat22/SE_HW2345)
[![Pull Requests](https://img.shields.io/github/issues-pr/akshat22/SE_HW2345)](https://github.com/akshat22/SE_HW2345)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/akshat22/SE_HW2345.svg)](https://img.shields.io/github/repo-size/akshat22/SE_HW2345.svg)
[![codecov](https://codecov.io/gh/akshat22/SE_HW2345/branch/main/graph/badge.svg?token=HZ23J69UEJ)](https://codecov.io/gh/akshat22/SE_HW2345)
<!-- ![Intro page](./Images/Lua-vs-Python.jpg) -->

Python code for creating summaries of input CSV file by translating a lua code to python.

## Table of Contents

1. [LUA](#LUA)
2. [Goal](#Goal)
3. [Getting started](#Getting-started)
4. [File and function mapping](#file-and-function-mapping)
5. [License](#license)
6. [Contributors](#contributors)

## LUA

Lua is a lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications. The features of the lua programming language include:

- simple 
- efficient
- portable
- Suitable for use as an embedded language within a host application

## Goal

The goal is to write some code to read a CSV file and generate summaries of columns (medians and standard deviation for numerics; mode and entropy for symbolic columns).

## Getting Started

### Pre-requisites

Ensure python is installed. You can check the version of python in the system using:

``` bash
python --version
```

Check if pip is installed. This can be done with the command:

``` bash
pip --version
```

The csv file can be accessed in the [Data folder](./data/data.csv)

### Installation

Clone this repository using

``` bash
git clone https://github.com/akshat22/SE_HW2345.git
```

You can download all the dependencies required to run the file using:

``` bash
pip install -r requirements.txt
```


## File and function mapping

The implementations for only `Sym` and `Num` classes are done so far in this repo.
The implementation of different util functions are also done like - `coerce`, `per`, `probability`

The scripts for test cases `sym`, `num` are also prepared [here](./test). 

The Lua classes and corresponding python implementation scripts are listed below:

| Class | Corresponding python script  |
|-------|------------------------------|
| Num   | [Num](./code/columns/Num.py) |
| Sym   | [Sym](./code/columns/Sym.py) |

## License

This project is licensed under [MIT license](LICENSE).

## Contributors

<a href="https://github.com/akshat22/SE_HW2345/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=akshat22/SE_HW2345" />
</a>
