
OUTPUT_DIR=staging_dir
RFCOMM_DEV=rfcomm0

build: $(OUTPUT_DIR)
	#hash markdown-to-slides
	while true; do \
		rsync --verbose --recursive js images video extras $(OUTPUT_DIR); \
		markdown-to-slides --watch talk.md -o $(OUTPUT_DIR)/index.html --script $(OUTPUT_DIR)/js/configure.js --template template.html; \
	done

$(OUTPUT_DIR):
	mkdir $@

clean:
	rm -vfr $(OUTPUT_DIR)

### BLUETOOTH

rfcomm:
	#sudo rfcomm connect rfcomm0 `hcitool scan | grep 00:06:66 | awk '{print $1}'`
	sudo rfcomm connect $(RFCOMM_DEV) 00:06:66:7B:8B:4A
