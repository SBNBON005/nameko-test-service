# nameko-test-service

## Prerequisites

Install `Docker`

Install `Docker Compose`

Clone `https://github.com/SBNBON005/nameko-test-service`

## Running

Once you clone repository simply run docker-compose up . This will pull pre-built RabbitMQ image from public Docker Hub repository and build the test service.

```
$ cd /path/to/nameko-test-service/directory
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
[1, 2, 9, 4, 25, 81]
```

2) Dictionary from string

```
>>> response = n.rpc.invictus_service.get_compressed_strings(['bongani', 'sibanda', 'hired'])
>>> response

```
It should print output as 

```
{
 'bongani': 'x\x9cKÊÏKOÌË\x04\x00\x0by\x02ß', 
 'sibanda': 'x\x9c+ÎLJÌKI\x04\x00\x0b\x83\x02Ó', 
 'hired': 'x\x9cËÈ,JM\x01\x00\x065\x02\r'
}


```

3) zlib decoder

```
>>> for _, value in response.items():
...     print(f"Uncompressed: {n.rpc.invictus_service.get_decompressed_string(value)} and Compressed: {value}")

```

It should print output as 

```
Uncompressed: bongani and Compressed: x KÊÏKOÌË
                                               yß
Uncompressed: sibanda and Compressed: x +ÎLJÌKI

Uncompressed: hired and Compressed: x ËÈ,JM5

```

# Running Tests
Install test requirements
```
$ cd /path/to/nameko-test-service/directory
$ pip install -r test_requirements.txt
```

```
$ python -m pytest tests
```

# My thoughts on nameko 
1) It is simple enough to get it going for http plugin like flask
2) I don't like that it require you install rabbitmq to do rpc