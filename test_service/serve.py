import zlib

from nameko.rpc import rpc


class TestService(object):
    name = 'invictus_service'

    @rpc
    def get_odd_number_squared(self, list_of_integers):
        """This function squares each odd number in a given list of integers."""
        return [pow(num, 2) if num & 1 else num for num in list_of_integers]

    @rpc
    def get_compressed_strings(self, list_of_strings):
        """This function accepts a list of strings, and returns a dictionary of the strings - the key being the original
         string, and the value being a compressed version of that string."""
        return {string: zlib.compress(string.encode(encoding='utf-8')).decode(encoding='ISO-8859-1')
                for string in list_of_strings}

    @rpc
    def get_decompressed_string(self, zlib_compressed_string):
        """This function decodes a given zlib encoded string."""
        return zlib.decompress(zlib_compressed_string.encode(encoding='ISO-8859-1')).decode(encoding='utf-8')
