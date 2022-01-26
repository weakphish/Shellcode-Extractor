
            #include<stdio.h>
            #include<string.h>
            #include <sys/mman.h>
            #include <unistd.h>

            /*
            * This program originally appeared in Dr. Alexandros Kapravelos' CSC 405 class, at NC State
            * University.
            */

            unsigned char print_unity_shellcode[] = "\xeb\x28\x5e\x48\xc7\xc0\x01\x00\x00\x00\x48\xc7\xc7\x01\x00\x00\x00\x48\xc7\xc2\x0e\x00\x00\x00\x0f\x05\x48\xc7\xc0\x3c\x00\x00\x00\x48\xc7\xc7\x00\x00\x00\x00\x0f\x05\xe8\xd3\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\x0a";

            int main() 
            {
                int pagesize = getpagesize(); // Get the page size for this system
                void *addrOfThePage = print_unity_shellcode - ((unsigned int)print_unity_shellcode % pagesize); // calculate the address of the page code is on (subtract the difference between the pagesize and the address to code to get the offset)
                mprotect(addrOfThePage, pagesize, PROT_EXEC | PROT_WRITE); // Set the premissions for the page to be EXECUABLE (PROT_EXEC flag)
                
                int (*ret)() = (int(*)())print_unity_shellcode;
                ret();
            }
            