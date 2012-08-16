#!/bin/sh
# 
# Start / Shutdown script for RasPiLEDChaser
#

DIR=$(cd $(dirname "$0"); pwd)

case "$1" in
  start)

    # Start RasPiLEDChaser
    `which python` "${DIR}"/main.py &

    ;;
  stop)
    # Stop RasPiLEDChaser
    `which kill` `cat /var/run/raspiledchaser.pid`
    `which rm` /var/run/raspiledchaser.pid

    ;;

  *)
    echo "Usage: $0 {start|stop}" >&2
    exit 1

    ;;

esac

exit 0
