import sieve


def test2():
    s = sieve.sieve()
    i = iter(s)
    i.next()
    i.next()
    i.next()
    i.next()
    assert i.next() == 13

test2()
