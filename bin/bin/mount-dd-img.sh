#!/usr/bin/env bash

case "$1" in
	-h|--help)
		echo "$0: mount first vfat volume on raw dd image"
		echo "Usage: $0 [-u|--umount] ]/path/to/file.img"
		;;
	-u|--umount)
		sudo umount /mnt && echo "Unmounted" || echo "Error"
		;;
	*)
		FILENAME=$(basename $1)
		VFAT=$(fdisk -l $1 | grep FAT32 | head -1 | awk '{print $3}')
		VFAT_OFFSET=$(( $VFAT *512 ))
		sudo mount -o loop,offset=$VFAT_OFFSET -t vfat $1 /mnt && echo "$1 mounted to /mnt" || echo "Error $1"
		;;
esac
