import json
import lzma

from nameko.rpc import rpc


class TestService(object):
    name = 'invictus_service'

    @rpc
    def get_odd_number_squared(self, list_of_integers):
        return json.dumps([pow(num, 2) if num & 1 else num for num in list_of_integers])

    @rpc
    def get_compressed_strings(self, list_of_strings):
        return {string: lzma.compress(string.encode(encoding='utf-8')).decode(encoding='ISO-8859-1')
                for string in list_of_strings}

    @rpc
    def get_decompressed_string(self, lzma_compressed_string):
        return lzma.decompress(lzma_compressed_string.encode(encoding='ISO-8859-1')).decode(encoding='utf-8')

