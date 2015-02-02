#!/usr/bin/env bash

# Load options from config file
# ARC_FILE="archive_file.tar.bz2
# ARC_FILE_P="archive_file_with_password.7z"
# INCLUDE="include_file"
# EXCLUDE="exclude_file"

. $HOME/.config/backup-profile.cfg

INFO_COLOR='\e[1;34m'
NO_COLOR='\e[0m'

dpkg --get-selections > $HOME/Backup/installed-packages.txt

function info() {
	echo -e "$INFO_COLOR*$NO_COLOR $1"
}

function make_archive {
	info "Create archive $ARC_FILE"
	tar -cj $(for i in $EXCLUDE; do echo "--exclude $i "; done) -f $ARC_FILE $INCLUDE && \
		info "$ARC_FILE $(du -sh $ARC_FILE | awk '{print $1}')"
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
		echo "Usage: $0 [-p|--password]"
		echo "Files:"
		for FILE in $INCLUDE; do echo $FILE; done
		;;
	*)
		make_archive
		;;
esac
