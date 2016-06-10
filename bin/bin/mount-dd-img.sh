#!/usr/bin/bash

set -e

usage() {
	cat << USAGE
Mount first vfat volume on raw dd image

Usage: $(basename $0) [-m|--mount] | [-u|--umount] /path/to/file.img
USAGE
}

ARGUMENT=$1
PATH=$2

case "$ARGUMENT" in
	-h|--help)
		usage
		exit 0
		;;
	-u|--umount)
		sudo umount /mnt && echo "Unmounted" || echo "Error"
		;;
	-m|--mount)
		VFAT=$(fdisk -l $PATH | grep FAT32 | head -1 | awk '{print $3}')
		VFAT_OFFSET=$(( $VFAT *512 ))
		sudo mount -o loop,offset=$VFAT_OFFSET -t vfat $PATH /mnt && echo "$PATH mounted to /mnt" || echo "Error while mounting $PATH"
		;;
	*)
		usage
		exit 1
		;;
esac
