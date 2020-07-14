from typing import List

# define BuildTargets/DumpCurrent
#   .PHONY: dumpinfo
#   dumpinfo : export DESCRIPTION=$$(Target/Description)
#   dumpinfo:
# 	@echo 'Target: $(TARGETID)'; \
# 	 echo 'Target-Board: $(BOARD)'; \
# 	 echo 'Target-Name: $(BOARDNAME)$(if $(SUBTARGETS),$(if $(SUBTARGET),))'; \
# 	 echo 'Target-Arch: $(ARCH)'; \
# 	 echo 'Target-Arch-Packages: $(if $(ARCH_PACKAGES),$(ARCH_PACKAGES),$(ARCH)$(if $(CPU_TYPE),_$(CPU_TYPE))$(if $(CPU_SUBTYPE),_$(CPU_SUBTYPE)))'; \
# 	 echo 'Target-Features: $(FEATURES)'; \
# 	 echo 'Target-Depends: $(DEPENDS)'; \
# 	 echo 'Target-Optimization: $(if $(CFLAGS),$(CFLAGS),$(DEFAULT_CFLAGS))'; \
# 	 echo 'CPU-Type: $(CPU_TYPE)$(if $(CPU_SUBTYPE),+$(CPU_SUBTYPE))'; \
# 	 echo 'Linux-Version: $(LINUX_VERSION)'; \
# 	$(if $(LINUX_TESTING_VERSION),echo 'Linux-Testing-Version: $(LINUX_TESTING_VERSION)';) \
# 	 echo 'Linux-Release: $(LINUX_RELEASE)'; \
# 	 echo 'Linux-Kernel-Arch: $(LINUX_KARCH)'; \
# 	$(if $(SUBTARGET),,$(if $(DEFAULT_SUBTARGET), echo 'Default-Subtarget: $(DEFAULT_SUBTARGET)'; )) \
# 	 echo 'Target-Description:'; \
# 	 echo "$$$$DESCRIPTION"; \
# 	 echo '@@'; \
# 	 echo 'Default-Packages: $(DEFAULT_PACKAGES) $(call extra_packages,$(DEFAULT_PACKAGES))'; \
# 	 $(DUMPINFO)
# 	$(if $(CUR_SUBTARGET),$(SUBMAKE) -r --no-print-directory -C image -s DUMP=1 SUBTARGET=$(CUR_SUBTARGET))
# 	$(if $(SUBTARGET),,@$(foreach SUBTARGET,$(SUBTARGETS),$(SUBMAKE) -s DUMP=1 SUBTARGET=$(SUBTARGET); ))
# endef


# ifndef Profile
# define Profile
#   $(eval $(call ProfileDefault))
#   $(eval $(call Profile/$(1)))
#   dumpinfo : $(call shexport,Profile/$(1)/Description)
#   PACKAGES := $(filter-out -%,$(PACKAGES))
#   DUMPINFO += \
# 	echo "Target-Profile: $(1)"; \
# 	$(if $(PRIORITY), echo "Target-Profile-Priority: $(PRIORITY)"; ) \
# 	echo "Target-Profile-Name: $(NAME)"; \
# 	echo "Target-Profile-Packages: $(PACKAGES) $(call extra_packages,$(DEFAULT_PACKAGES) $(PACKAGES))"; \
# 	echo "Target-Profile-Description:"; \
# 	echo "$$$$$$$$$(call shvar,Profile/$(1)/Description)"; \
# 	echo "@@"; \
# 	echo;
# endef
# endif

class Profile:
    '''
    Target Profile
    '''
    profile: str
    name: str
    priority: str
    packs: List[str]
    hasImageMetadata: str
    supportedDevices: str
    description: str


class Subtarget:
    '''
    Subtarget
    '''

    subtarget: str
    board: str
    name: str
    arch: str
    arch_packs: str
    features: List[str]
    deps: None
    optimization: str
    cpu_type: str
    linux_version: str
    linux_release: str
    linux_kernel_arch: str
    description: str
    default_packs: List[str]
    profile: List[Profile]


class TargetSystem:
    '''
    Target System
    '''
    source_makefile: str
    target: str
    board: str
    name: str
    arch: str
    arch_packs: str
    features: List[str]
    deps: None
    optimization: str
    cpu_type: str
    linux_version: str
    linux_release: str
    linux_kernel_arch: str
    description: str
    default_packs: List['str']
    subtargets: List[Subtarget]


TargetInfoAst = List[TargetSystem]
