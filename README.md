# nameko-test-service

## Prerequisites

Docker

Docker Compose

## Running

Once you clone repository simply run docker-compose up . This will pull pre-built RabbitMQ image from public Docker Hub repository and build the test service.

```
$ docker-compose up
```

When you see `Connected to amqp:...` it means services are up and running.


## Testing it

```
$ docker exec -it nameko-test-service bash
```

```
$ nameko shell --config conf.yml
```
1) Odd number squared

```
>>> n.rpc.invictus_service.get_odd_number_squared([1, 2, 3, 4, 5, -9])

```
It should print output as

```
'[1, 2, 9, 4, 25, 81]'
```

2) Dictionary from string

```
>>> response = n.rpc.invictus_service.get_compressed_strings(['bongani', 'sibanda', 'hired'])
>>> response

```
It should print output as 

```
{
 'bongani': 'ý7zXZ\x00\x00\x04æÖ´F\x02\x00!\x01\x16\x00\x00\x00t/å£\x01\x00\x06bongani\x00\x00NdÑê¬t@\x8d\x00\x01\x1f\x07\x16.¸s\x1f¶ó}\x01\x00\x00\x00\x00\x04YZ', 
 'sibanda': 'ý7zXZ\x00\x00\x04æÖ´F\x02\x00!\x01\x16\x00\x00\x00t/å£\x01\x00\x06sibanda\x00\x00\x81Ýi£©B\x19\x80\x00\x01\x1f\x07\x16.¸s\x1f¶ó}\x01\x00\x00\x00\x00\x04YZ', 
 'hired': 'ý7zXZ\x00\x00\x04æÖ´F\x02\x00!\x01\x16\x00\x00\x00t/å£\x01\x00\x04hired\x00\x00\x00\x00DZHVÎ°\xa0Ê\x00\x01\x1d\x05¸-\x80¯\x1f¶ó}\x01\x00\x00\x00\x00\x04YZ'
}

```

3) LZMA decoder

```
>>> for _, value in response.items():
...     print("Compressed: %s, Uncompressed: %s" % (value, n.rpc.invictus_service.get_decompressed_string(value)))

```

It should print output as 

```
Compressed: ý7zXZæÖ´F!t/å£bonganiNdÑê¬t@ .¸s¶ó}YZ, Uncompressed: bongani
Compressed: ý7zXZæÖ´F!t/å£sibanda Ýi£©B .¸s¶ó}YZ, Uncompressed: sibanda
Compressed: ý7zXZæÖ´F!t/å£hiredDZHVÎ° Ê¸- ¯¶ó}YZ, Uncompressed: hired

```

