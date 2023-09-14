```shell
docker build -t loki-python .
```


```shell
docker run --network=datawiz loki-python
```

```shell
docker run -d --name ploki --network=datawiz --log-driver=loki --log-opt loki-url="http://host.docker.internal:3100/loki/api/v1/push" --log-opt loki-retries=5 --log-opt loki-batch-size=3 python-loki
```