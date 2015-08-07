# Newspeak Scripting Language

## As seen in George Orwell's 1984

Newspeak has much of the same syntax as Javascript, but many of the keywords have been changed to be more *goodthinkful*.
Newspeak is written in Python using PLY.

## Newspeak Syntax

Newspeak is a scripting language defined by the following terms.

#### Variables

- Variables are loosely typed. Strings, Integers, Floats and everything else can be defined as <oldspeak>

	```
	oldspeak string_variable equal "Hello World"
	oldspeak integer_variable equal 4
	```

#### Logic

- A Negation can be performed by un()

	```
	un(variable)
	```

- If statements are defined by <think()>

	```
	think expression then statement
	```

- Variable aritmetic still uses <+ - / *>

	```
	var3 equals var1 + var2
	```

#### Control Flow

- Comments can be defined as <goodthink<. Comments can be multi-line as long as they are between brackets.

	```
	goodthink { Comments go here! }
	```

- Classes can be defined as <bb>

	```
	bb(var1, var2){}
	```

- Functions can be defined as dayorder

	```
	dayorder FunctionName(var1, var2) {}
	```

- Return Statements are defined as upsub()

	```
	upsub(var1)
	```

#### Input/Output

- A script can output to the command line through telescreen

	```
	telescreen("Hello, World!")
	```

- A script can input from the command line through speakwrite

	```
	oldspeak var1 = speakwrite()
	```

## Example Program

	```
	oldspeak string_variable greeting equals "Hello"
	greeting equals greeting + " World!"
	telescreen(greeting)
	```

## Newspeak Compiler

The Newspeak Compiler is written in Python.

## July 13th Status Update

* See Above

* Language is based on JavaScript, the compiler may be written in JavaScript or C++

* We have created the README and started cloning the repo. It's Monday.

* By next week we want:
    1. The README to be completed with the full language fleshed out.
    2. The parser should be completed as well.
    3. Everyone who hasn't read 1984 has 3 days to do so.

* Momentum. But really, we just need to start coding. Also, we need to figure out exactly who does what.