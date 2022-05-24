MDS := README.md $(shell grep -o '[a-z0-9/-]\+\.md' SUMMARY.md | grep -v index.md)

all: proselint wordcheck

proselint: 
	@proselint $(MDS)

wordcheck: 
	@./mgrep $(MDS)

wc:
	@wc $(MDS)

uni.md:
	./uni.py $(MDS)

epub: uni.md
	pandoc -o uncurled.epub --epub-cover-image=uncurled.jpg epub.txt uni.md
	rm uni.md

pdf: uni.md
	pandoc -o uncurled.pdf pdf.txt uni.md
	rm uni.md
