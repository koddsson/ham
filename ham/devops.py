from datetime import datetime
from db import hosts as db_hosts
from subprocess import Popen, PIPE


def fetch_hosts_info(host_names):
    """
    Fetch the latest version info for each host

    :param host_names: List of hosts to update
    :return: The updated hosts
    """

    # p = Popen(["sh", "update_hosts.sh"],
    # p = Popen(["/home/axel/work/CoreStatus/ham/update_hosts.sh"],
    #             stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate()

    output = "'[azazo.coredata.is] Executing task \\'coredata.version\\'
[32m[azazo on azazo.coredata.is] 2.2.2[0m

Done.
Disconnecting from azazo.coredata.is... done.
'"
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