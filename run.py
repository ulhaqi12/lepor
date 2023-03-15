from lepor.sentence_level import lepor


def main():
    reference = 'a bird is on a stone.'
    output = 'a stone on a bird.'

    print('Lepor: ', lepor(reference, output))

    reference = 'a bird is on a stone.'
    output = 'a bird is on a stone.'

    print('Lepor: ', lepor(reference, output))

    reference = 'a bird is on a stone.'
    output = 'scary cow was not bad'

    print('Lepor: ', lepor(reference, output))


if __name__ == '__main__':
    main()
