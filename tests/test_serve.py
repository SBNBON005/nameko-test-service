from nameko.testing.services import worker_factory

from test_service.serve import TestService


def test_get_odd_number_squared():
    expected_results = [1, 2, 9, 4, 25, 81]
    list_of_integers = [1, 2, 3, 4, 5, -9]

    response = worker_factory(TestService).get_odd_number_squared(list_of_integers)

    assert expected_results == response


def test_get_compressed_strings():
    expected_results = {'Bongani': 'x\x9csÊÏKOÌË\x04\x00\n\x99\x02¿'}
    list_of_strings = ['Bongani']

    response = worker_factory(TestService).get_compressed_strings(list_of_strings)

    assert expected_results == response


def test_get_decompressed_string():
    expected_results = 'sibanda'
    compressed_string = 'x\x9c+ÎLJÌKI\x04\x00\x0b\x83\x02Ó'

    response = worker_factory(TestService).get_decompressed_string(compressed_string)

    assert expected_results == response
