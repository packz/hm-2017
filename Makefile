
OUTPUT_DIR=staging_dir

build: $(OUTPUT_DIR)
	#hash markdown-to-slides
	while true; \
		do markdown-to-slides --watch talk.md -o $(OUTPUT_DIR)/index.html --script js/configure.js --template template.html; \
		rsync --recursive js images $(OUTPUT_DIR); \
	done

$(OUTPUT_DIR):
	mkdir $@

clean:
	rm -vfr $(OUTPUT_DIR)
