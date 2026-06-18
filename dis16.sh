printf "\ec\e[47;31m\ngive me asm file?\n"
read a
rasm2 -D -a x86 -b 16 -B -f $a 


