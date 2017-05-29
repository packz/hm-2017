build:
	while true;do markdown-to-slides --watch talk.md -o index.html --script js/configure.js --template template.html; done
