from tangelo_challenge.functions import get_languages, create_dataframe
import pandas as pd

def test_get_languages():
    assert get_languages({'spa':'Spanish','eng':'English'})=='[Spanish,English]'
def test_get_languages_one():
    assert get_languages({'spa':'Spanish'})=='[Spanish]'
def test_get_languages_empty():
    assert get_languages({})=='[]'
