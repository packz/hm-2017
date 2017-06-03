
OUTPUT_DIR=staging_dir

build: $(OUTPUT_DIR)
	#hash markdown-to-slides
	while true; do \
		rsync --verbose --recursive js images video $(OUTPUT_DIR); \
		markdown-to-slides --watch talk.md -o $(OUTPUT_DIR)/index.html --script $(OUTPUT_DIR)/js/configure.js --template template.html; \
	done

$(OUTPUT_DIR):
	mkdir $@

clean:
	rm -vfr $(OUTPUT_DIR)
