def adv_print(*args, **kwargs):
    if 'in_file' in kwargs.keys():
        if kwargs['in_file'] is True:
            with open('adv_file.txt', 'w', encoding='UTF-8') as f:
                for arg in args:
                    f.write(arg)
    if 'max_line' in kwargs.keys():
        max_line = kwargs['max_line']
    else:
        max_line = 120
    if 'start' in kwargs.keys():
        start = kwargs['start']
    else:
        start = ''
    if 'sep' in kwargs.keys():
        sep = kwargs['sep']
    else:
        sep = ' '
    if 'end' in kwargs.keys():
        end = kwargs['end']
    else:
        end = '\n'
    if 'file' in kwargs.keys():
        file = kwargs['file']
    else:
        file = None
    if 'flush' in kwargs.keys():
        flush = kwargs['flush']
    else:
        flush = False
    line = sep.join([str(arg) for arg in args])
    i = 0
    step = max_line
    while i < len(line):
        print(f'{start}{line[i:max_line]}', end=end, file=file, flush=flush)
        i += step
        max_line += step
