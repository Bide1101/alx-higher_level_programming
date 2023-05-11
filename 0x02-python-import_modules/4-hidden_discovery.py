#!/usr/bin/python3
import dis
if __name__ == "__main__":
    filename = 'hidden_4.pyc'

    with open(filename, 'rb') as f:
        code = f.read()

    instructions = dis.get_instructions(code)

    names = set()
    for i in instructions:
        if i.opname == 'STORE_NAME':
            name = instr.argval
            if not name.startswith('__'):
                names.add(name)
    for name in names:
        print(name)
