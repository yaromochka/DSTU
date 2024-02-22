    for string, function in commands.items():
        if re.fullmatch(string, mas): return function(mas)
    return False