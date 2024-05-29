#!/bin/bash

service_exists() {
    local n=$1
    if [[ $(systemctl list-units --all -t service --full --no-legend "$n.service" | cut -f1 -d' ') == $n.service ]]; then
        return 0
    else
        return 1
    fi
}

if ! service_exists spotmicroai; then
  echo "Service spotmicroai is not installed as service"
  exit
fi

echo "Disabling SpotMicroAI to run on boot"
sudo systemctl disable spotmicroai.service;
sudo systemctl daemon-reload;
echo "Done"

if systemctl is-active --quiet spotmicroai; then
  echo "Service spotmicroai is still running, run 'sudo systemctl stop spotmicroai.service' to stop it"
fi

