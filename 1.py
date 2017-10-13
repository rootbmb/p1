from sys import argv

filename = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']

with open(filename, 'r') as f:
    for line in f:
        if not line.startswith('!'):
            print(line.rstrip())
