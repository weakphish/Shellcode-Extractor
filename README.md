ShellcodeExtractor
========

SHELLCODE-EXTRACTOR
Tool used to extract shellcode and length from an object/binary file.

Copyright (C) 2017  Neetx

This file is part of Shellcode-Extractor.

Shellcode-Extractor is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Shellcode-Extractor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

### CONTACTS:
[Neetx](mailto:neetx@protonmail.com)

[Weakphish](mailto:john123allison@gmail.com)

---
# About 
This is a fork of Neetx's `shellcode-extractor`, written to be updated to Python 3 and include a feature to dump to a test C program written by St4rl3ss (thanks!).

The latter works by taking the generated shellcode and dumping it into a C file that will check if it works. The Makefile has a rule to compile the test file once generated.

# Usage

Write assembly code, product an object file and the use this script in pipeline to objdump.

Provided is a Hello World assembly file for testing. 

Example:
```
$ make hello_world.o
$ objdump -z -d hello_world.o | python3 shellcode_extractor.py 
$ make shelltest 
$ ./shelltest
Hello, world!
```
