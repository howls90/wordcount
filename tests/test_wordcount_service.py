from services import WordCountService as wcs
from werkzeug.exceptions import NotFound
import pytest


def test_getAndProcess_success():
    '''Test process payload '''
    data = {
        'url': "http://www.virtusize.com",
        'word': "fit"
    }
    assert wcs.getAndProcess(**data) == 10

def test_getAndProcess_failure():
    ''' Domain do not exist '''
    data = {
        'url': "http://www.virtusize",
        'word': "fit"
    }
    with pytest.raises(NotFound):
        wcs.getAndProcess(**data)
