.text
.global main
main:
	jmp saveme
shellcode:
	pop %rsi
	mov $1, %rax   # opcode for write syscall
	mov $1, %rdi   # 1st arg, fd = 1 (stdout)
	mov $14, %rdx   # 3rd arg, len
	syscall        # syscall interrupt
	mov $60, %rax  # opcode for exit system call
	mov $0, %rdi   # 1st arg, exit(0)
	syscall 
saveme:
	call shellcode
	.string "Hello, world!\n"
