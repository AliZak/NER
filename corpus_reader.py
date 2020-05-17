def read_txt(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset = []
    sentence = []
    for i in range(len(lines)):
        if(lines[i] == ""):
            dataset.append(sentence);
            sentence = []
            continue
        if(lines[i][0] == '#'):
            continue
        label = lines[i].split(' ')
        try:
            word = (label[0], label[1])
        except:
            print(label)
        sentence.append(word)

    return dataset
        

if __name__ == "__main__":
    pass
