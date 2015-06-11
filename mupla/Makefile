CC=gcc
LDFLAGS=-lcrypto
INC= -I../mupdf-1.6-source/include
OBJ_PATH = ../mupdf-1.6-source/build/debug/
OBJ= $(OBJ_PATH)*.a $(OBJ_PATH)freetype/*.o $(OBJ_PATH)jpeg/*.o $(OBJ_PATH)jbig2dec/*.o $(OBJ_PATH)**/*.o $(OBJ_PATH)pdf/js/*.o

all: clean mupla.o libmupla.a test runtest

mupla.o: mupla.c
	$(CC) -c mupla.c -shared -fPIC $(INC) -lcrypto

libmupla.a: mupla.o $(OBJ)
	ar rcs libmupla.a mupla.o $(OBJ)

test: test.c
	$(CC) -o test test.c -L. $(INC) libmupla.a -lm -lcrypto

clean:
	rm -f mupla.o libmupla.a test

runtest:
	./test

