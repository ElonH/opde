# OPDE
Yet another way to build OpenWrt firmware

## Purpose
There are many way to build openwrt, such as github actions.

## Feature

- no environment population, install apt packages.
- intergated with github actions, more easy to reimplement compile error in local machine
- compiled packages what you need with SDK
- burned firmware what you need with ImageBuilder (in agenda)

## User Manual

1. fetch opde sdk image: `docker pull elonh/opde:sdk`
2. run docker

		docker run -it --rm \
			-e http_proxy=http://192.168.123.94:10801 \
			-e https_proxy=http://192.168.123.94:10801 \
			elonh/opde:sdk bash

3. update and install feeds: `opde feeds`
4. `make menuconfig`

## Devlop Environment for opde

1. Install apt packages `sudo apt install python3-pip python3-venv cmake build-essential`
2. Install [poetry](https://python-poetry.org/docs/#installation)
3. `git clone https://github.com/ElonH/opde.git && code opde`
4. Setup python virtual env `python3 -m venv .venv && poetry install`

## Build Log

<https://elonh.github.io/opde>
