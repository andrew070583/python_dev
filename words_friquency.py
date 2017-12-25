with open('test.txt') as f:
    arr = []
    words = {}

    for line in f:
        s = line.lower().strip()

        for i in s.split():

            arr.append(i.strip('.,?!'))

    print(' '.join([i for i in arr]))

    for i in arr:
        words[i] = words.get(i, 0) + 1
    for w in sorted(words, key=words.get, reverse=True):
        print(w, words[w])