import json
import lzma
from nameko.web.handlers import http


class TestService(object):
    name = 'invictus_service'

    @http('GET', '/odd-number-squared')
    def get_odd_number_squared(self, request):
        list_of_integers = [1, 2, 3, 4, 5, 9]
        return json.dumps([pow(num, 2) if num & 1 else num for num in list_of_integers])

    @http('GET', '/compressed-strings')
    def get_compressed_strings(self, request):
        list_of_strings = ['Bongani', 'Bernard', 'Sibanda']
        return {string: lzma.compress(string.encode(encoding='utf-8')) for string in list_of_strings}



