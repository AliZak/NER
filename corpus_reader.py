def read_txt(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset = []
    sentence = []
    for i in range(len(lines)):
        if(lines[i] == ""):
            dataset.append(sentence);
            sentence = []
            continue
        label = lines[i].split(' ')
        word = (label[0], label[1])
        sentence.append(word)

    return dataset
        

if __name__ == "__main__":
    pass