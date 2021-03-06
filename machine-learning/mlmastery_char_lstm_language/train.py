# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


if __name__ == '__main__':
    from numpy import array
    from pickle import dump
    from keras.utils import to_categorical
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM
    # load
    in_filename = 'char_sequences.txt'
    raw_text = load_doc(in_filename)
    lines = raw_text.split('\n')

    chars = sorted(list(set(raw_text)))
    mapping = dict((c, i) for i, c in enumerate(chars))

    sequences = list()
    for line in lines:
        encoded_seq = [mapping[c] for c in line]
        sequences.append(encoded_seq)

    vocab_size = len(mapping)

    print('Vocabulary size %d: ' % vocab_size)

    # Split input and output

    sequences = array(sequences)
    X, y = sequences[:, :-1], sequences[:, -1]
    sequences = [to_categorical(x, num_classes = vocab_size) for x in X]
    X = array(sequences)
    y = to_categorical(y, num_classes = vocab_size)

    # Fit model

    # define model

    model = Sequential()
    # LSTM with 75 memory calls
    print((X.shape[1], X.shape[2]))
    model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dense(vocab_size, activation='softmax'))
    print(model.summary())

    model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=100, verbose=2)

    # save model
    model.save('model.h5')
    dump(mapping, open('mapping.pkl', 'wb'))

