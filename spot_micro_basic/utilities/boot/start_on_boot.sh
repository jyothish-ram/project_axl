#!/bin/bash

yes | sudo cp -f ~/spotmicroai/utilities/boot/spotmicroai.service /etc/systemd/system/spotmicroai.service

echo "Enabling SpotMicroAI to run on boot"
sudo systemctl enable spotmicroai.service;
sudo systemctl daemon-reload;
echo "Done"

if ! systemctl is-active --quiet service; then
  echo "Service spotmicroai is not running, run 'sudo systemctl start spotmicroai.service' to start it"
fi

