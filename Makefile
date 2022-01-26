shelltest: shelltest.c hello_world.o
	gcc shelltest.c -o shelltest -fno-stack-protector -z execstack -no-pie

hello_world.o: hello_world.s
	gcc -no-pie -c hello_world.s -o hello_world.o
