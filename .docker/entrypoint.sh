#!/bin/sh

set -e

python manage.py migrate
python manage.py createdataframe
python manage.py createdataframeincra

shutdown() 
{
    echo "shutting down container"

    # first shutdown any service started by runit
    for service in $(ls -1 /etc/service);
    do
        sv force-stop $service
    done

    # shutdown runsvdir command
    kill -HUP $RUNSVDIR
    wait $RUNSVDIR

    # give processes time to stop
    sleep 0.5

    # kill any other processes still running in the container
    for process_id in $(ps -eo pid | grep -v PID  | tr -d ' ' | grep -v '^1$' | head -n -6); 
    do
        timeout -t 5 /bin/sh -c "kill $process_id && wait $process_id || kill -9 $process_id"
    done
    exit
}

exec runsvdir -P /etc/service &
RUNSVDIR="$!"

echo "Started runsvdir, PID is $RUNSVDIR"
echo "wait for processes to start...."

sleep 5
for service in $(ls -1 /etc/service); do
    sv status $service
done

trap shutdown SIGTERM SIGHUP SIGQUIT SIGINT
wait $RUNSVDIR

shutdown
