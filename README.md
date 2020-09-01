# pyRSA

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://mit-license.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Pure-Python RSA public-key cryptosystem implementation. Algorithm generates public and private keys using feeded 1,024 bit prime integers, and can encrypt and decrypt given messages. Currently half of the public and the complete private key are generated partially from enviromental noise using [os-specific functions](https://github.com/python/cpython/blob/master/Lib/os.py#L48-L89), while p, q, λ(n) parameters are under development.

<p align="center">
  <img width="460" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/CarmichaelLambda.svg/660px-CarmichaelLambda.svg.png">
  <p>Image: Carmichael function. A Carmichael prime-variation is used to generate λ(n).</p>
</p>

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [KAC](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2020-09-01

### Added

- README.md Changelog & Getting Started

## [1.0.0] - 2020-08-31

### Added

- Encryption and decryption function
- p, q, λ(n) deterministic implementation


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Running

The published script comes with a user-friendly example by running main.py.

```
>> py main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. pyRSA is under development.
