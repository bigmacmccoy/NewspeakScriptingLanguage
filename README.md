# Newspeak Scripting Language
## Scripting Language for Newspeak, as seen in George Orwell's 1984.

Newspeak and the Newspeak comiler was written by Braedon McCoy. Newspeak has much of the same syntax as Javascript, but many of the keywords have been changed to be more *goodthinkful*.

## Newspeak Syntax
Newspeak is a scripting language defined by these terms:
	#### Variables
	- Variables are loosely typed. Strings, Integers, Floats and everything else can be defined as oldspeak
		oldspeak string_variable equal "Hello World"
		soldspeakec integer_variable equal 4
		oldspeak float_variable equal 2.5
		oldspeak boolean_variable equal True

	#### Logic
	- A Negation can be performed by un()
		un(variable)
	- If statements are defined by verify()
		verify(var1 equal var2){}
	- Variable aritmetic still uses + - / *
		var3 equal var1 + var2

	#### Control Flow
	- Comments can be defined as goodthink. Comments can be multi-line as long as they are between brackets.
		goodthink { Comments go here! }
	- Classes can be defined as bb
		bb(var1, var2){}
	- Functions can be defined as dayorder
		dayorder FunctionName(var1, var2) {}
	- Return Statements are defined as upsub
		upsub(var1)

	#### Input/Output
	- A script can output to the command line through report
		report("Hello, World!")

## Example Program

`dayorder HelloWorldFunc(){
	oldspeak greeting equal "Hello, World!"
	report(greeting)
	report()
	}`

## Newspeak Compiler
The Newspeak Compiler is written in JavaScript.