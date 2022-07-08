def thesaurus(*args):
    answer = {}
    for name in args:
        key = name[0].capitalize()
        if key not in answer:
            answer[key] = []
        answer[key].append(name)
    print(answer)
