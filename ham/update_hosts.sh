#!/bin/sh

cd /home/axel/work/devops
. bin/activate
fab -H azazo.coredata.is coredata.version
