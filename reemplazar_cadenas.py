def replace(stri, repl):
	new_String = stri + repl[1:]
	return new_String

if __name__ == '__main__':
    var = replace('Leoncio','VALERIA')
    print (var)