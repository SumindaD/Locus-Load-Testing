# Locus Load Testing

> This repo contains locus load testing files for the project HAnalytics.

### Setup

> Install required Python packages

```shell
$ pip install locustio
```

> Run the desired load test file

```shell
$ locust -f <Python file name> -H <Host URL>
```

Or

```shell
$ locust -f <Python file name> -H <Host URL> -c <Number of Users> -r <Hatch Rate> --no-web -t 60s
```