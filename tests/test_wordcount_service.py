from services import WordCountService as wcs
from werkzeug.exceptions import BadRequest
import pytest


def test_getAndProcess_success():
    url = "http://www.virtusize.com"
    word = "fit"
    assert wcs.getAndProcess(url, word) == 10

def test_getAndProcess_failure():
    url = "http://www.virtusize"
    word = "fit"
    with pytest.raises(BadRequest):
        wcs.getAndProcess(url, word)
