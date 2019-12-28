from .. import Stats

stats = Stats()

def test_alpha():
    result = stats.get_alpha_ratio('string')
    assert result == 100.0
    result = stats.get_alpha_ratio('Acta Non Verba.')
    assert result == 80.0
    result = stats.get_alpha_ratio('12345')
    assert result == 0.0
    
def test_digit():
    result = stats.get_digit_ratio('string')
    assert result == 0.0
    result = stats.get_digit_ratio('1. Acta Non Verba.')
    assert result == 5.555555555555555
    result = stats.get_digit_ratio('12345')
    assert result == 100.0
    
def test_ascii():
    result = stats.get_ascii_ratio('string')
    assert result == 100.0
    result = stats.get_ascii_ratio('Câ\x82\x81â\x82\x85Hâ\x82\x82â\x82\x84O')
    assert result == 20.0
    result = stats.get_ascii_ratio('https://www.oglaf.com/brimstone-vinegar/')
    assert result == 100.0
    
def test_empty():
    result = stats.get_empty_ratio('string')
    assert result == 0.0
    result = stats.get_empty_ratio(' ')
    assert result == 100.0
    result = stats.get_empty_ratio('word ')
    assert result == 20.0