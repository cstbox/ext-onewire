# CSTBox framework
#
# Makefile for building the Debian distribution package containing the
# 1-Wire support extension.
#
# author = Eric PASCUAL - CSTB (eric.pascual@cstb.fr)

# name of the CSTBox module
MODULE_NAME=onewire

include $(CSTBOX_DEVEL_HOME)/lib/makefile-dist.mk

copy_files: \
	check_metadata_files \
	copy_bin_files \
	copy_python_files \
	copy_init_scripts 
	@echo '----- copying customized owfs configuration...'
	$(RSYNC) \
	    $(ETC_FROM)/owfs.conf $(BUILD_DIR)/etc/
