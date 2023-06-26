from lepor import sentence_lepor


def test_one():
    reference = 'a bird is on a stone.'
    output = 'a stone on a bird.'

    assert round(sentence_lepor(reference, output), 3) == 0.736


def test_two():
    reference = 'a bird is on a stone.'
    output = 'a bird is on a stone.'

    assert sentence_lepor(reference, output) == 1


def test_three():
    reference = 'a bird is on a stone.'
    output = 'scary cow was not bad'

    assert round(sentence_lepor(reference, output), 3) == 0.00
