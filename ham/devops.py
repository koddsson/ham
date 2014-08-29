from datetime import datetime
from db import hosts as db_hosts


def fetch_hosts_info(host_names):
    """
    Fetch the latest version info for each host

    :param host_names: List of hosts to update
    :return: The updated hosts
    """
    updated_hosts = []
    for host_name in host_names:
        uhost = next(
            (h for h in db_hosts if h['host_name'] == host_name),
            None
        )
        if uhost:
            uhost['cache_time'] = datetime.now()
            updated_hosts.append(uhost)
    return updated_hosts