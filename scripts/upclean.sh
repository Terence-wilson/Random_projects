#!/bin/bash

#Updates, then upgrades, then cleans everything afterwards:)

apt --fix-broken install
apt update
apt upgrade -y
apt dist-upgrade -y
apt autoremove -y
apt autoclean
