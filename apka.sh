#!/bin/sh
__EOF__
sudo cat <<__EOF__>/etc/systemd/system/Discord.service
[Unit]
Description=Python python service
#Documentation=
After=network.target
[Service]
RestartSec=10
Restart=always
# Main process
ExecStart=/usr/bin/python3 /DiscordKacper/app.py
[Install]
WantedBy=multi-user.target
__EOF__
systemctl enable --now Discord
