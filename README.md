ham
===

Fabric web interface and API

Setup
-----

Add your fabric scripts as a submodule. It must be formatted like [mine](https://github.com/koddsson/fabric-scripts).

    git submodule add <your_scripts_repo> scripts

Usage
-----

Endpoints are exposed in the following manner:

    http://localhost:5000/run/<host>/<task>

Query parameters map to task arguments. So if you have the following task:

```python
    from fabric.api import run, task

    @task
    def curl(url):
        return run('curl {url}'.format(url=url))
```

The request you'd like is something like:

    http://localhost:5000/run/<host>/curl?url=http://tldr.is

Clients that I know of
----------------------

- [ham-web-app](https://github.com/koddsson/ham-web-app)

TODO
----
- Run fabric scripts on demand.
- Run fabric scripts periodically
