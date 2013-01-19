import sieve


def test3():
    s = sieve.next()
    i = iter(s)
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    assert i.next() == 29

test3()