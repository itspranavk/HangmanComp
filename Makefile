JAVA_SETUP: SETUP
	mv java_handler handler
	rm -f c_handler py_handler user_pgm.c user_pgm.py

C_SETUP:
	mv c_handler handler
	rm -f java_handler py_handler user_pgm.java user_pgm.py

PYTHON_SETUP:
	mv py_handler handler
	rm -f java_handler c_handler user_pgm.java user_pgm.c

SETUP:
	touch .output.txt

java: user_pgm.java
	javac user_pgm.java

c: user_pgm.c
	gcc user_pgm.c -o user_pgm

python: user_pgm.py

clean:
	rm -f *.o handler user_pgm
