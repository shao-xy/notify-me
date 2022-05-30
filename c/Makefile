CC = gcc

all: launcher

launcher: launcher.c
	${CC} -o $@ $< -g

.PHONY: clean
clean:
	-rm -f launcher *.o

