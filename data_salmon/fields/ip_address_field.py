
import ipaddress

from .field import Field

class IPAddressField(Field):
    supported_strategies = (
        'value', 'incremental_range', 'random_range', 'ordered_choice',
        'random_choice'
    )

    supported_types = ('ipv4', 'ipv6')

    def __init__(self, name, typ, strategy='value', arguments=[]):
        super(IPAddressField, self).__init__(name, typ, strategy, arguments)

        if typ not in self.supported_types:
            raise TypeError('Invalid IPAddress type: {}'.format(typ))

        self.version = int(self.typ[3:])

        if self.version == 6:
            self.construct_ip = ipaddress.IPv6Address
        else:
            self.construct_ip = ipaddress.IPv4Address

    def __str__(self):
        return ('IntegerField(strategy={}, arguments={}, version={})').format(
                    self.strategy, self.arguments, self.version)

    def cast(self, item):
        return int(self.construct_ip(item))

    def format(self, item, output_format='txt'):
        ip_addr = self.construct_ip(item)

        if output_format == 'csv' or output_format == 'txt':
            return str(ip_addr)
        elif output_format == 'hex':
            return ip_addr.packed.hex()
        elif output_format == 'bin':
            return ip_addr.packed
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))
