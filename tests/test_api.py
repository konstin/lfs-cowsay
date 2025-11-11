import pytest

import lfs_cowsay


def test_char_names():

    characters = ['beavis', 'cheese', 'daemon', 'cow', 'dragon',
                  'ghostbusters', 'kitty', 'meow', 'milk', 'stegosaurus',
                  'stimpy', 'turkey', 'turtle', 'tux',
                  'pig', 'trex', 'miki', 'fox', 'octopus']

    assert len(lfs_cowsay.char_names) == len(characters)
    assert lfs_cowsay.char_names == sorted(characters)


def test_draw_error():
    with pytest.raises(lfs_cowsay.CowsayError) as e:
        lfs_cowsay.draw('', '')
    assert e.value.args[0] == 'Pass something meaningful to lfs_cowsay'


def test_get_output_string():
    assert isinstance(lfs_cowsay.get_output_string(char='cow', text='Hello'), str)


def test_get_output_string_error():
    with pytest.raises(lfs_cowsay.CowsayError) as e:
        lfs_cowsay.get_output_string('random', 'random text')
    assert e.value.args[0] == f'Available Characters: {lfs_cowsay.char_names}'
