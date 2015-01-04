import os
import codecs


def get_fixture(name):
    filename = os.path.join(os.path.dirname(__file__), 'fixtures', name)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()
