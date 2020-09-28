from puid import get_puid

def test_puid():
    assert get_puid('test-data/test.jpg') == 'fmt/42'

def test_no_puid():
    assert get_puid('test-data/no-file') == None



