---
title: "compile.38"
date: 2021-06-21 06:12:30.163989
hidden: false
draft: false
weight: -38
---

build number: `38`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/r8168/compile -j$(nproc) || make package/feeds/base/r8168/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-r8168-add-LED-configuration-from-OF.patch using plaintext: 
patching file src/r8168_n.c
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src'
/openwrt/staging_dir/host/bin/find: '/lib/modules/5.8.0-1033-azure/kernel/drivers/net/ethernet': No such file or directory
/openwrt/staging_dir/host/bin/find: '/lib/modules/5.8.0-1033-azure/kernel/drivers/net': No such file or directory
make -C /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124 M=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src modules
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.o
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c: In function 'rtl8168_init_board':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25550:17: error: implicit declaration of function 'pci_disable_link_state'; did you mean 'pci_disable_ats'? [-Werror=implicit-function-declaration]
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                 ^~~~~~~~~~~~~~~~~~~~~~
                 pci_disable_ats
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25550:46: error: 'PCIE_LINK_STATE_L0S' undeclared (first use in this function); did you mean 'PCIE_LNK_WIDTH_RESRV'?
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                                              ^~~~~~~~~~~~~~~~~~~
                                              PCIE_LNK_WIDTH_RESRV
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25550:46: note: each undeclared identifier is reported only once for each function it appears in
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25550:68: error: 'PCIE_LINK_STATE_L1' undeclared (first use in this function); did you mean 'PCIE_LNK_X1'?
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                                                                    ^~~~~~~~~~~~~~~~~~
                                                                    PCIE_LNK_X1
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25551:40: error: 'PCIE_LINK_STATE_CLKPM' undeclared (first use in this function); did you mean 'PCI_EXP_LNKCAP_CLKPM'?
                                        PCIE_LINK_STATE_CLKPM);
                                        ^~~~~~~~~~~~~~~~~~~~~
                                        PCI_EXP_LNKCAP_CLKPM
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25564:14: error: implicit declaration of function 'pci_set_mwi'; did you mean 'dev_set_mtu'? [-Werror=implicit-function-declaration]
         rc = pci_set_mwi(pdev);
              ^~~~~~~~~~~
              dev_set_mtu
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25676:9: error: implicit declaration of function 'pci_clear_mwi'; did you mean 'pmd_clear_bad'? [-Werror=implicit-function-declaration]
         pci_clear_mwi(pdev);
         ^~~~~~~~~~~~~
         pmd_clear_bad
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c: In function 'rtl8168_try_msi':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25899:21: error: implicit declaration of function 'pci_enable_msi'; did you mean 'pci_enable_ats'? [-Werror=implicit-function-declaration]
                 if (pci_enable_msi(pdev))
                     ^~~~~~~~~~~~~~
                     pci_enable_ats
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c: In function 'rtl8168_disable_msi':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.c:25914:17: error: implicit declaration of function 'pci_disable_msi'; did you mean 'pci_disable_ats'? [-Werror=implicit-function-declaration]
                 pci_disable_msi(pdev);
                 ^~~~~~~~~~~~~~~
                 pci_disable_ats
cc1: some warnings being treated as errors
make[6]: *** [scripts/Makefile.build:262: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src/r8168_n.o] Error 1
make[5]: *** [Makefile:1734: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
make[4]: *** [Makefile:140: modules] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/src'
make[3]: *** [Makefile:57: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8168-8.048.03/.built] Error 2
```
