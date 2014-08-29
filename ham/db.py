from datetime import datetime

hosts = [
    {
        "id": 1,
        "host_name": "laika0.coredata.is",
        "backend": "laika",
        "version": "2.2.2",
        "tenants": ["azazo", "koddsson", "kodasonur"],
        "cache_time": datetime(2014, 8, 29, 12, 05, 06)
    },
    {
        "id": 2,
        "host_name": "drkoddson.coredata.is",
        "backend": "nuxeo",
        "version": "1.3.3.7",
        "tenants": None,
        "cache_time": datetime(2014, 8, 29, 12, 05, 06)
    }
]


def get_hosts():
    """

    :return:
    """
    return hosts


def update_hosts(updated_hosts):
    for uhost in updated_hosts:
        for host in hosts:
            if host['id'] == uhost['id']:
                host['cache_time'] = uhost['cache_time']
                break