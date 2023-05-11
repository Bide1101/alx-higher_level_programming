#!/usr/bin/python3
import dis
import marshal

if __name__ == "__main__":

    with open('hidden_4.pyc', 'rb') as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code = marshal.load(f)

    instructions = dis.get_instructions(code)
    for i in instructions:
        if i.opname == 'LOAD_GLOBAL':
            name = instr.argval
            if not name.startswith('__'):
                print(name)

