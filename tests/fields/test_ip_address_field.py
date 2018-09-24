
from nose.tools import assert_equals
from nose.tools import assert_true
import ipaddress

from data_salmon.fields.ip_address_field import IPAddressField

class TestIPAddressField:
    def test_integer_field(self):
        test_cases = [
            {
                'input': {
                    'kwargs': {
                        'typ': 'ipv6',
                        'arguments': ['2001:db8::1000']
                    }
                },
                'expected': {
                    'version': 6,
                    'strategy': 'value',
                    'arguments': ['2001:db8::1000'],
                    'construct_ip': ipaddress.IPv6Address
                }
            },
            {
                'input': {
                    'kwargs': {
                        'typ': 'ipv4',
                        'arguments': ['1.2.3.4']
                    }
                },
                'expected': {
                    'version': 4,
                    'strategy': 'value',
                    'arguments': ['1.2.3.4'],
                    'construct_ip': ipaddress.IPv4Address
                }
            },
            {
                'input': {
                    'kwargs': {
                        'typ': 'ipv4',
                        'strategy': 'random_range',
                        'arguments': ['1.2.3.4', '2.3.4.5']
                    }
                },
                'expected': {
                    'version': 4,
                    'strategy': 'random_range',
                    'arguments': ['1.2.3.4', '2.3.4.5'],
                    'construct_ip': ipaddress.IPv4Address
                }
            }
        ]

        for test_case in test_cases:
            field = IPAddressField(name='field',
                                   **test_case['input']['kwargs'])
            for key in test_case['expected'].keys():
                assert_equals(getattr(field, key), test_case['expected'][key])

    def test_cast(self):
        test_cases = [
            { 'input': 0, 'expected': 0 },
            { 'input': '1.2.3.4', 'expected': 16909060 },
        ]

        for test_case in test_cases:
            field = IPAddressField('f0', 'ipv4')
            assert_equals(
                field.cast(test_case['input']), test_case['expected'])

    def test_format(self):
        test_cases = [
            {
                'input': {
                    'arguments': ['1.2.3.4'],
                    'type': 'ipv4',
                    'output_format': 'txt'
                },
                'expected': '1.2.3.4'
            },
            {
                'input': {
                    'arguments': ['1.2.3.4'],
                    'type': 'ipv4',
                    'output_format': 'hex'
                },
                'expected': '01020304'
            },
            {
                'input': {
                    'arguments': ['1.2.3.4'],
                    'type': 'ipv4',
                    'output_format': 'bin'
                },
                'expected': bytes([0x01, 0x02, 0x03, 0x04])
            },
            {
                'input': {
                    'arguments': [65535],
                    'type': 'ipv4',
                    'output_format': 'bin'
                },
                'expected': bytes([0x00, 0x00, 0xff, 0xff])
            }
        ]

        for test_case in test_cases:
            try:
                field = IPAddressField(
                    name='field',
                    typ=test_case['input']['type'],
                    arguments=test_case['input']['arguments'])
                assert_equals(
                    field.format(field.arguments[0],
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except OverflowError as oe:
                assert_equals(type(oe), type(test_case['expected']))
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
