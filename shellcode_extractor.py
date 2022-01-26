"""
SHELLCODE-EXTRACTOR
Tool used to extract shellcode and lenght from an object/binary file.

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

CONTACTS:
    - neetx@protonmail.com
"""

import sys, re

usage_message = "\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py \n" 

if not sys.stdin.isatty():
    try:
        # Read in object file and 
        shellcode = ""
        length = 0
        while True:
            item = sys.stdin.readline()
            if item:
                if re.match("^[ ]*[0-9a-f]*:.*$",item):
                    item =item.split(":")[1].lstrip()
                    x = item.split("\t")
                    opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                    for i in opcode:
                        shellcode += "\\x" + i
                        length += 1
            else: 
                break
        if shellcode == "":
            print("Nothing to extract")
        else:    
            print("\n" + shellcode)
            print("\nLength: " + str(length) + "\n")
            print("Dumping shellcode to shelltest.c ...")

            shelltest_text = """
            #include<stdio.h>
            #include<string.h>
            #include <sys/mman.h>
            #include <unistd.h>

            /*
            * This program originally appeared in Dr. Alexandros Kapravelos' CSC 405 class, at NC State
            * University.
            */

            unsigned char print_unity_shellcode[] = "%s";

            int main() 
            {
                int pagesize = getpagesize(); // Get the page size for this system
                void *addrOfThePage = print_unity_shellcode - ((unsigned int)print_unity_shellcode %% pagesize); // calculate the address of the page code is on (subtract the difference between the pagesize and the address to code to get the offset)
                mprotect(addrOfThePage, pagesize, PROT_EXEC | PROT_WRITE); // Set the premissions for the page to be EXECUABLE (PROT_EXEC flag)
                
                int (*ret)() = (int(*)())print_unity_shellcode;
                ret();
            }
            """ % shellcode

            with open("shelltest.c", "w+") as f:
                f.write(shelltest_text)
                f.close()
    except Exception as e:
        print(e)
        pass
else:
    print(usage_message)
