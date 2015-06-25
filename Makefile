STOW = /usr/bin/stow
BASH_DIR = $(HOME)/.config/bash

.PHONY: all prepare restow_bin

all: prepare

prepare: $(STOW) $(BASH_DIR)

$(STOW):
	sudo apt-get install stow

$(BASH_DIR):
	mkdir -p $(BASH_DIR)

restow_bin:
	stow -R bin
