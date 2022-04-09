MDS := $(shell grep -o '[a-z0-9/-]\+\.md' SUMMARY.md | grep -v index.md) README.md

all: proselint wordcheck

proselint: 
	@proselint $(MDS)

wordcheck: 
	@./mgrep $(MDS)

wc:
	@wc $(MDS)
