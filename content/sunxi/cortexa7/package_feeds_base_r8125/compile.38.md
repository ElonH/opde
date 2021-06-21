---
title: "compile.38"
date: 2021-06-21 06:12:30.164629
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
make package/feeds/base/r8125/compile -j$(nproc) || make package/feeds/base/r8125/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06'
/openwrt/staging_dir/host/bin/find: '/lib/modules/5.8.0-1033-azure/kernel/drivers/net/ethernet': No such file or directory
/openwrt/staging_dir/host/bin/find: '/lib/modules/5.8.0-1033-azure/kernel/drivers/net': No such file or directory
make -C /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124 M=/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06 modules
make[5]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.o
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_release_board':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:10211:9: error: implicit declaration of function 'pci_clear_mwi'; did you mean 'pmd_clear_bad'? [-Werror=implicit-function-declaration]
         pci_clear_mwi(pdev);
         ^~~~~~~~~~~~~
         pmd_clear_bad
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_init_board':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11123:17: error: implicit declaration of function 'pci_disable_link_state'; did you mean 'pci_disable_ats'? [-Werror=implicit-function-declaration]
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                 ^~~~~~~~~~~~~~~~~~~~~~
                 pci_disable_ats
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11123:46: error: 'PCIE_LINK_STATE_L0S' undeclared (first use in this function); did you mean 'PCIE_LNK_WIDTH_RESRV'?
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                                              ^~~~~~~~~~~~~~~~~~~
                                              PCIE_LNK_WIDTH_RESRV
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11123:46: note: each undeclared identifier is reported only once for each function it appears in
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11123:68: error: 'PCIE_LINK_STATE_L1' undeclared (first use in this function); did you mean 'PCIE_LNK_X1'?
                 pci_disable_link_state(pdev, PCIE_LINK_STATE_L0S | PCIE_LINK_STATE_L1 |
                                                                    ^~~~~~~~~~~~~~~~~~
                                                                    PCIE_LNK_X1
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11124:40: error: 'PCIE_LINK_STATE_CLKPM' undeclared (first use in this function); did you mean 'PCI_EXP_LNKCAP_CLKPM'?
                                        PCIE_LINK_STATE_CLKPM);
                                        ^~~~~~~~~~~~~~~~~~~~~
                                        PCI_EXP_LNKCAP_CLKPM
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11137:13: error: implicit declaration of function 'pci_set_mwi'; did you mean 'dev_set_mtu'? [-Werror=implicit-function-declaration]
         if (pci_set_mwi(pdev) < 0) {
             ^~~~~~~~~~~
             dev_set_mtu
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_enable_msix':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11454:27: error: array type has incomplete element type 'struct msix_entry'
         struct msix_entry msix_ent[R8125_MAX_MSIX_VEC];
                           ^~~~~~~~
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11463:17: error: implicit declaration of function 'pci_enable_msix_range'; did you mean 'pci_enable_sriov'? [-Werror=implicit-function-declaration]
         nvecs = pci_enable_msix_range(tp->pci_dev, msix_ent,
                 ^~~~~~~~~~~~~~~~~~~~~
                 pci_enable_sriov
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11454:27: warning: unused variable 'msix_ent' [-Wunused-variable]
         struct msix_entry msix_ent[R8125_MAX_MSIX_VEC];
                           ^~~~~~~~
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_try_msi':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11527:19: error: implicit declaration of function 'pci_enable_msi'; did you mean 'pci_enable_ats'? [-Werror=implicit-function-declaration]
         else if (!pci_enable_msi(pdev))
                   ^~~~~~~~~~~~~~
                   pci_enable_ats
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_disable_msi':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11550:17: error: implicit declaration of function 'pci_disable_msix'; did you mean 'pci_disable_sriov'? [-Werror=implicit-function-declaration]
                 pci_disable_msix(pdev);
                 ^~~~~~~~~~~~~~~~
                 pci_disable_sriov
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:11552:17: error: implicit declaration of function 'pci_disable_msi'; did you mean 'pci_disable_ats'? [-Werror=implicit-function-declaration]
                 pci_disable_msi(pdev);
                 ^~~~~~~~~~~~~~~
                 pci_disable_ats
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_close':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:14604:17: error: implicit declaration of function 'pci_clear_master'; did you mean 'pci_set_master'? [-Werror=implicit-function-declaration]
                 pci_clear_master(tp->pci_dev);
                 ^~~~~~~~~~~~~~~~
                 pci_set_master
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c: In function 'rtl8125_suspend':
/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.c:14749:9: error: implicit declaration of function 'pci_prepare_to_sleep'; did you mean 'pci_resource_to_user'? [-Werror=implicit-function-declaration]
         pci_prepare_to_sleep(pdev);
         ^~~~~~~~~~~~~~~~~~~~
         pci_resource_to_user
cc1: some warnings being treated as errors
make[6]: *** [scripts/Makefile.build:262: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/r8125_n.o] Error 1
make[5]: *** [Makefile:1734: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06] Error 2
make[5]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/linux-5.4.124'
make[4]: *** [Makefile:168: modules] Error 2
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06'
make[3]: *** [Makefile:48: /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-sunxi_cortexa7/r8125-9.005.06/.built] Error 2
```
