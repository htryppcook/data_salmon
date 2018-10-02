# DataSalmon

Python3 library used to generate sample datasets from configuration files. Users can specify a dataset they wish to build using the DSL, and then generate files by calling DataSalmon:

```
# Generate 100 records using the dataset definition in dataset.dsl
data_salmon dataset.dsl 100
```

## DSL Examples

With fishes.dsl
```
fishes {
  string index = ordered_choice(1, 2, "red", "blue")
  string fish = value("fish")
}
```
Call:
```
> data_salmon -i fishes.dsl -o txt 4
1fish2fishredfishbluefish
> data_salmon -i fishes.dsl -o csv 4
index,fish
1,fish
2,fish
red,fish
blue,fish
```

With 4-tuple netflow.dsl
```
netflow {
  uint16 from_port = incremental_range(0, 65536, 1)
  ipv4 from_addr = random_range('192.168.0.0', '192.168.255.255')
  uint16 to_port = random_range(443, 8080)
  ipv4 to_addr = incremental_range('10.0.0.0', '10.255.255.255', 1)
}
```
Call:
```
> data_salmon -i netflow.dsl -o csv 4
from_port,from_addr,to_port,to_addr
0,192.168.245.216,784,10.0.0.0
1,192.168.169.178,3835,10.0.0.1
2,192.168.83.14,5284,10.0.0.2
3,192.168.218.10,2060,10.0.0.3
```
Binary output example:
```
> data_salmon -i netflow.dsl -o bin 4 > netflow.bin
> hexdump -C netflow.bin
00000000  00 00 c0 a8 f6 6a 09 28  0a 00 00 00 00 01 c0 a8  |.....j.(........|
00000010  4f 54 18 a1 0a 00 00 01  00 02 c0 a8 41 60 0e 9c  |OT..........A`..|
00000020  0a 00 00 02 00 03 c0 a8  2b dc 04 4a 0a 00 00 03  |........+..J....|
00000030
```

Running from docker instance:
```
> cat netflow.dsl | docker run -i data_salmon -o csv 4
from_port,from_addr,to_port,to_addr
0,192.168.245.216,784,10.0.0.0
1,192.168.169.178,3835,10.0.0.1
2,192.168.83.14,5284,10.0.0.2
3,192.168.218.10,2060,10.0.0.3
```

## DSL Definitions

Dataset
```
dataset_name {
  type field_name = strategy(arguments, arguments)
}
```

Currently supported types:
string
int16, int32, int64, uint16, uint32, uint64
ipv4, ipv6

Currently supported strategies:
value(argument)
Can only generate the argument specified in the strategy constructor for each record.

incremental_range(min, max, increment)
Supports integer and IP address types.
Returns min for the first record generated, then increases by the specified increment for each additional record generated until it reaches the max value, then starts over at min.

random_range(min, max)
Supports integer and IP address types.
Generates a random value between min and max for each record.

ordered_choice(choice0, choice1, ...)
Supports all types.
Returns values from the list of options specified in the strategy constructor in order.

random_choice(choice0, choice1, ...)
Supports all types.
Returns a random value from the list of options specified in the strategy constructor.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to transceptor-technology for [pyleri](https://github.com/transceptor-technology/pyleri) which is used to parse out the custom dsl.
