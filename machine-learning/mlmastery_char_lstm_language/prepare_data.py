def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def preprocess_text(text):
    """
        Other methods:
            normalise to lower case,
            remove punctuations to reduce vocabulary size
            develop a  smaller and leaner model.
    """
    tokens = text.split()
    raw_text = ' '.join(tokens)
    return raw_text

def prepare_sequences(text, length):
    sequences = list()
    for i in range(length, len(text)):
        seq = text[i-length:i+1]
        sequences.append(seq)
    return sequences

def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


if __name__ == '__main__':
    raw_text = load_doc('rhyme.txt')
    print(raw_text)

    raw_text = preprocess_text(raw_text)

    length = 10
    sequences = prepare_sequences(raw_text, length)

    print('Total sequences %d' % len(sequences))

    save_doc(sequences, 'char_sequences.txt')