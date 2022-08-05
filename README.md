# AirBnB_clone
ALX Portfolio Project of making a clone of AirBnB website
Console
## Description

This team project is part of the ALX Full-Stack Software Engineer program.
It's the first step towards building a first full web application: an AirBnB clone.
This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.
## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.
## Execution
Your shell should work like this in the interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
![hbnb-screenshot]
(https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220805%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220805T062038Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=932aaf622c86c2c00df7a3b8ae756f048694be35d41502c7d4d020c598213779)
