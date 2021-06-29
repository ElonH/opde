---
title: "compile.42"
date: 2021-06-29 09:28:26.565572
hidden: false
draft: false
weight: -42
---

build number: `42`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/packages/perl-mail-spamassassin/compile -j$(nproc) || make package/feeds/packages/perl-mail-spamassassin/compile V=s
```

#### Compile.txt

``` bash
not installing man pages in man1; no man1 dir found at - line 275.
What email address or URL should be used in the suspected-spam report
text for users who want more information on your filter installation?
(In particular, ISPs should change this to a local Postmaster contact)
default text: [the administrator of that system] the administrator of that system
ERROR: the required Net::DNS module is not installed,
minimum required version is 0.34.

NOTE: settings for "make test" are now controlled using "t/config.dist". 
See that file if you wish to customize what tests are run, and how.

checking module dependencies and their versions...

***************************************************************************

  Used for all DNS-based tests (SBL, XBL, SpamCop, DSBL, etc.),
  perform MX checks, and is also used when manually reporting spam to
  SpamCop.

  You need to make sure the Net::DNS version is sufficiently up-to-date:

  - version 0.34 or higher on Unix systems
  - version 0.46 or higher on Windows systems


***************************************************************************
NOTE: the optional Digest::SHA1 module is not installed.

  The Digest::SHA1 module is still required by the Razor2 plugin.
  Other modules prefer Digest::SHA, which is a Perl base module.


***************************************************************************
NOTE: the optional DB_File module is not installed.

  Used to store data on-disk, for the Bayes-style logic and
  auto-whitelist.  *Much* more efficient than the other standard Perl
  database packages.  Strongly recommended.


***************************************************************************
NOTE: the optional Mail::SPF module is not installed.

  Used to check DNS Sender Policy Framework (SPF) records to fight email
  address forgery and make it easier to identify spams.


***************************************************************************
NOTE: the optional GeoIP2::Database::Reader module is not installed.

  Used by the RelayCountry plugin (not enabled by default) to
  determine the domain country codes of each relay in the path of an email. 
  Also used by the URILocalBL plugin (not enabled by default) to provide ISP
  and Country code based filtering.


***************************************************************************
NOTE: the optional Geo::IP module is not installed.

  Used by the RelayCountry plugin (not enabled by default) to determine
  the domain country codes of each relay in the path of an email.  Also used by 
  the URILocalBL plugin to provide ISP and Country code based filtering.


***************************************************************************
NOTE: the optional IP::Country::DB_File module is not installed.

  Used by the RelayCountry plugin (not enabled by default) to
  determine the domain country codes of each relay in the path of an email. 
  Also used by the URILocalBL plugin (not enabled by default) to provide
  Country code based filtering.


***************************************************************************
NOTE: the optional Net::CIDR::Lite module is not installed.

  Used by the URILocalBL plugin to process IP address ranges.


***************************************************************************
NOTE: the optional Razor2 module is not installed,
minimum required version is 2.61.

  Used to check message signatures against Vipul's Razor collaborative
  filtering network. Razor has a large number of dependencies on CPAN
  modules. Feel free to skip installing it, if this makes you nervous;
  SpamAssassin will still work well without it.

  More info on installing and using Razor can be found
  at http://wiki.apache.org/spamassassin/InstallingRazor .


***************************************************************************
NOTE: the optional IO::Socket::INET6 module is not installed.

  This module is an older alternative to IO::Socket::IP.
  Spamd, as well some underlying modules, will fall back to using
  IO::Socket::INET6 if IO::Socket::IP is unavailable. One or the other
  module is required to support IPv6 (e.g. in spamd/spamc protocol,
  for DNS lookups or in plugins like DCC). Some plugins or underlying
  modules may still require IO::Socket::INET6 for IPv6 support even
  if IO::Socket::IP is available.


***************************************************************************
NOTE: the optional IO::Socket::SSL module is not installed,
minimum required version is 1.76.

  If you wish to use SSL encryption to communicate between spamc and
  spamd (the --ssl option to spamd), you need to install this
  module. (You will need the OpenSSL libraries and use the
  ENABLE_SSL="yes" argument to Makefile.PL to build and run an SSL
  compatible spamc.)


***************************************************************************
NOTE: the optional Mail::DKIM module is not installed,
minimum required version is 0.31, recommended version is 0.37 or higher.

  If this module is installed and the DKIM plugin is enabled,
  SpamAssassin will perform DKIM signature verification when DKIM-Signature
  header fields are present in the message headers, and check ADSP rules
  (e.g. anti-phishing) when a mail message does not contain a valid author
  domain signature. Version 0.37 or later is needed to fully support ADSP.


***************************************************************************
NOTE: the optional LWP::UserAgent module is not installed.

  The "sa-update" program requires this module to make HTTP requests.


***************************************************************************
NOTE: the optional HTTP::Date module is not installed.

  The "sa-update" program requires this module to make HTTP
  If-Modified-Since GET requests.


***************************************************************************
NOTE: the optional Encode::Detect::Detector module is not installed.

  If you plan to use the normalize_charset config setting to
  decode message parts from their declared character set into Unicode, and
  such decoding fails, the Encode::Detect::Detector module (when available)
  may be consulted to provide an alternative guess on a character set of a
  problematic message part.


***************************************************************************
NOTE: the optional Net::Patricia module is not installed,
minimum required version is 1.16.

  If this module is available, it will be used for IP address lookups
  in tables internal_networks, trusted_networks, and msa_networks. Recommended
  when a number of entries in these tables is large, i.e. in hundreds
  or thousands. However, in case of overlapping (or conflicting) networks
  in these tables, lookup results may differ as Net::Patricia finds a
  tightest-matching entry, while a sequential NetAddr::IP search finds
  a first-matching entry. So when overlapping network ranges are given,
  specifying more specific subnets (longest netmask) first, followed by
  wider subnets ensures predictable results.


***************************************************************************
NOTE: the optional Net::DNS::Nameserver module is not installed.

  Net::DNS:Nameserver is typically part of Net::DNS.  However, RHEL/
  CentOS systems may install it using separate packages.  Because of this, we
  check for both Net::DNS and Net::DNS::Nameserver.  However, 
  Net::DNS::Nameserver is only used in make test as of June 2014.


***************************************************************************
NOTE: the optional BSD::Resource module is not installed.

  BSD::Resource provides BSD process resource limit and priority 
  functions.  It is used by the optional ResourceLimits Plugin.


***************************************************************************
NOTE: the optional Archive::Zip module is not installed.

  Archive::Zip provides an interface to ZIP archive files.
  It is used by the optional OLEVBMacro Plugin.


***************************************************************************
NOTE: the optional IO::String module is not installed.

  IO::String emulates file interface for in-core strings.
  It is used by the optional OLEVBMacro Plugin.

checking binary dependencies and their versions...

***************************************************************************
NOTE: the optional gpg binary is not installed,
recommended version is 1.0.6 or higher.

  The "sa-update" program requires this executable to verify  
  encryption signatures.  It is not recommended, but you can use 
  "sa-update" with the --no-gpg to skip the verification. 


***************************************************************************
NOTE: the optional wget binary is not installed,
recommended version is 1.8.2 or higher.

   Sa-update will use curl, wget or fetch to download updates.  
   Because perl module LWP does not support IPv6, sa-update as of
   3.4.0 will use these standard programs to download rule updates
   leaving LWP as a fallback if none of the programs are found.

   *IMPORTANT NOTE*: You only need one of these programs 
       It's only a concern if you are warned about all 3 
       i.e. (curl, wget & fetch) missing


***************************************************************************
NOTE: the optional fetch binary is not installed.

   Sa-update will use curl, wget or fetch to download updates.  
   Because perl module LWP does not support IPv6, sa-update as of
   3.4.0 will use these standard programs to download rule updates
   leaving LWP as a fallback if none of the programs are found.

   *IMPORTANT NOTE*: You only need one of these programs 
       It's only a concern if you are warned about all 3 
       i.e. (curl, wget & fetch) missing


***************************************************************************
NOTE: the optional re2c binary is not installed.

  The "re2c" program is used by sa-compile to compile rules 
  for regular expressions to speed up scanning.

dependency check complete...

REQUIRED module missing: Net::DNS
optional module missing: Digest::SHA1
optional module missing: DB_File
optional module missing: Mail::SPF
optional module missing: GeoIP2::Database::Reader
optional module missing: Geo::IP
optional module missing: IP::Country::DB_File
optional module missing: Net::CIDR::Lite
optional module missing: Razor2
optional module missing: IO::Socket::INET6
optional module missing: IO::Socket::SSL
optional module missing: Mail::DKIM
optional module missing: LWP::UserAgent
optional module missing: HTTP::Date
optional module missing: Encode::Detect::Detector
optional module missing: Net::Patricia
optional module missing: Net::DNS::Nameserver
optional module missing: BSD::Resource
optional module missing: Archive::Zip
optional module missing: IO::String
optional binary missing or nonfunctional: gpg
optional binary missing or nonfunctional: wget
optional binary missing or nonfunctional: fetch
optional binary missing or nonfunctional: re2c

warning: some functionality may not be available,
please read the above report before continuing!

/openwrt/staging_dir/host/bin/sed: can't read /openwrt/build_dir/target-aarch64_cortex-a72_musl/perl-mail-spamassassin-ssl/Mail-SpamAssassin-3.4.6/Makefile: No such file or directory
make[3]: *** [Makefile:104: /openwrt/build_dir/target-aarch64_cortex-a72_musl/perl-mail-spamassassin-ssl/Mail-SpamAssassin-3.4.6/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 2
```
