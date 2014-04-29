#!/bin/bash

DST_DIR="$HOME/Backup/minimal-profile/"
ARC_FILE="$HOME/Backup/minimal-profile.tar.bz2"
ARC_FILE_P="$HOME/Backup/minimal-profile.7z"
INCLUDE=" \
	$(find $HOME/ -maxdepth 1 -type f -iname '.*') \
	$HOME/.config \
	$HOME/.ecryptfs \
	$HOME/.fonts \
	$HOME/.gconf \
	$HOME/.gnome2 \
	$HOME/.icons \
	$HOME/.local \
	$HOME/.mozilla \
	$HOME/.purple \
	$HOME/.remmina \
	$HOME/.ssh \
	$HOME/.vim \
	$HOME/.themes/Numix-old \
	$HOME/.themes/Sky \
	$HOME/.themes/Radiance-Blue \
	$HOME/.themes/Radiance-LightGreen \
	$HOME/Docs/Wiki \
	$HOME/Programs \
	$(ls -1 -d $HOME/Work/* | grep -v "VMs") \
	$HOME/Install/Misc/xkb \
	$HOME/Backup/installed-packages.txt \
"
INFO_COLOR='\e[1;34m'
NO_COLOR='\e[0m'

dpkg --get-selections > $HOME/Backup/installed-packages.txt

function info() {
	echo -e "$INFO_COLOR*$NO_COLOR $1"
}

function make_archive {
	info "Create archive $ARC_FILE"
	tar -cjf $ARC_FILE $INCLUDE && info "$ARC_FILE $(du -sh $ARC_FILE | awk '{print $1}')"
}

case "$1" in
	--password|-p)
		info "Enable password protection archive"
		read -s -p "Enter password: " password
		echo ""
		make_archive
		info "Create password protection archive $ARC_FILE_P $(du -sh $ARC_FILE | awk '{print $1}')"
		7z a -p$password -mhe=on -mx=0 $ARC_FILE_P $ARC_FILE
		info "Delete archive"
		rm $ARC_FILE
		;;
	--help|-h)
		echo "Usage: minimal-profile.sh [-p|--password]"
		echo "Files:"
		for FILE in $INCLUDE; do echo $FILE; done
		;;
	*)
		make_archive
		;;
esac

