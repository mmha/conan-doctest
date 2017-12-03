# The fastest feature-rich C++98/C++11 single-header testing framework for unit tests and TDD

[Conan.io](https://conan.io) package for [doctest](https://github.com/onqtam/doctest) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/mmha/conan/doctest).

## For Users: Use this package

### Basic setup

    $ conan install doctest/1.2.6@mmha/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    doctest/1.2.6@mmha/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## License
[MIT](LICENSE)
