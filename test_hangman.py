from hangman import reveal_letters, all_letters_found

def test_reveal_letter():
    assert reveal_letters("Vancouver", ["V",'a']) == ('V a _ _ _ _ _ _ _')
    assert reveal_letters("Vancouver", ['V','a','B','z']) == ('V a _ _ _ _ _ _ _')
    assert reveal_letters("Jovica", ['J']) == ('J _ _ _ _ _')
    assert reveal_letters("Pizza", ['P','i','B','z']) == ('P i z z _')

def test_all_letters_found():
    assert all_letters_found("Jovica", ['a','c','i','v','o','J'])  is True
    assert all_letters_found("Vancouver", ['V','a','n', 'o'])  is False
    assert all_letters_found("Pizza", ['P','i','z'])  is False
    assert all_letters_found("Subaru", ["S", "u", 'r'])  is False