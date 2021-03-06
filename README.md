# nameko-test-service

## Prerequisites

Install `Docker`

Install `Docker Compose`

Clone `git@github.com:SBNBON005/nameko-test-service.git`

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

# My thoughts on nameko [spent about 4 hrs]
1) It is simple enough to get it going for http plugin like flask
2) I don't like that it require you install rabbitmq to do rpc
3) Because it was design with testability in mind, it was easy to write unittests for handlers
4) I haven't seen what sets it apart from other frameworks like flask and pyramid (maybe I missed the point)
5) Most of my time was spent trying to understand what the framework is trying to solve.

# Suitable compression algorithm [spent about 1 hour]
After going through the following articles I settled on using deflate algorithm. That's because the user might not even notice or care much about the 1 or 5 second saved from using lzma as opposed to deflate. And again zlib is the most used.
- https://cran.r-project.org/web/packages/brotli/vignettes/brotli-2015-09-22.pdf
- https://gregoryszorc.com/blog/2017/03/07/better-compression-with-zstandard/
- https://news.ycombinator.com/item?id=10721244