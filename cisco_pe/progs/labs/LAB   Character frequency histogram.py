with open("BaseExceptionTree.py", "r") as stream:
    character = stream.read(1)
    res = {}
    while character:
        if character not in res.keys():
            res[character] = 1
        else:
            res[character] += 1
        character = stream.read(1)
    for key, value in res.items():
        print (f"{key} -> {value}")