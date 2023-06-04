

def subtract(args):
    return int(args[0]) - int(args[1])


def add(args):
    return int(args[0]) + int(args[1])


FN_LOOKUP = {
    'ADD': add,
    'SUBTRACT': subtract,
}

with open('commands.txt') as f:
    for line in f.readlines():
        # Remove whitespace/linebreaks
        line = line.strip()
        # Command is the first string before a whitespace
        cmd = line.split(' ')[0]
        # Arguments are everything after that, separated by whitespaces
        args = line.split(' ')[1:]
        if cmd in FN_LOOKUP:
            # If the command is in the dict, execute it with its args
            result = FN_LOOKUP[cmd](args)
            args_str = ', '.join(args)
            print(f'{cmd}({args_str}) = {result}')
        else:
            # If not, raise an error
            raise ValueError(f'{cmd} is not a valid command!')
