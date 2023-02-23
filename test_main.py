from main import UFO, Cow, Abductable

def test_ufo_initialises_correctly():
    u = UFO()
    assert u.capacity == 5
    assert isinstance(u.storage, list)

def test_cow_is_abductable():
    c = Cow("Bessie")

    assert isinstance(c, Cow)
    assert isinstance(c, Abductable)
    assert c.fear_level == 3

def test_abduction_adds_to_storage():
    c = Cow("Testarina")
    u = UFO()

    assert len(u.storage) == 0

    u.abduct(c)

    assert len(u.storage) == 1


def test_cow_reacts_emotionally(capsys):
    c = Cow("Testarina")
    u = UFO()

    assert c.fear_level == 3

    u.abduct(c)

    output = capsys.readouterr() # Take a snapshot of out/err
    print_output = output.out # Just look at standard output
    assert "Moo!" in print_output

    assert c.fear_level == 9