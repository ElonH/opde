# Opde Derivate Index

- x86 - X86
  - x86_64 ([ElonH](https://github.com/ElonH/opde))
- ramips - MediaTek Ralink MIPS
  - mt7621 - MT7621 based board ([Derren-Bryan](https://github.com/Derren-Bryan/opde-ramips-mt7621))
- ipq40xx - Qualcomm Atheros IPQ40XX
  - generic - Generic ([Derren-Bryan](https://github.com/Derren-Bryan/opde-ipq40xx-generic))
- bcm27xx - Broadcom BCM27xx
  - bcm2709 - BCM2709/BCM2710/BCM2711 boards (32 bit) (TODO: waiting)

## Join in opde

Many target aren't in here, anyone can host opde for other target, subtarget.

1. fork [opde](https://github.com/ElonH/opde)

2. rename forked repository name to `opde-[target]-[subtarget]` (not necessary, but recommanded)

3. activate workflow in action page (if exist)

4. register [personal access token](https://github.com/settings/tokens), selects `public_repo, repo:status, workflow`, and copy the token into clipboard

5. go to your forked opde repository `Settings->Secrets` and add a new secret.  
  Name is `RELEASE_TOKEN`  
  Value is the token in your clipboard

6. clone your opde repo to local, and switch configuration to your target  
  Default target in [opde](https://github.com/ElonH/opde) is `x86_64`, of course, this isn't target you want.  
  There are some place need to be hacked:

    1. function `TARGET_X86_64` in `./scripts/common-vars.sh`.  
      This function is defined for `x86_64`.  
      You need to define other function for your target in `./scripts/common-vars.sh`.

    2. call your function in `./build_*.sh`  
      Replace function `TARGET_X86_64` as your function defined above in `./build_*.sh` => `base_pack_conf`.

    3. disable some of kernel packages that not compatiable with your target in `./build_*.sh` => `base_pack_conf`.

7. commit and push your change

8. tweak information for your repo.  
  `README.md` need to be modified, also this document.  
  If love to share your opde to anyone, you can ceate an [Issue in opde](https://github.com/ElonH/opde/issues) for joining your opde in Opde Derivate Index.
