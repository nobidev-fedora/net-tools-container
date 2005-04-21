%define npversion	1.2.9

Summary: Basic networking tools.
Name: net-tools
Version: 1.60
Release: 51.test1
License: GPL
Group: System Environment/Base
Source0: http://www.tazenda.demon.co.uk/phil/net-tools/net-tools-%{version}.tar.bz2
Source1: netplug-%{npversion}.tar.bz2
Source2: net-tools-%{version}-config.h
Source3: net-tools-%{version}-config.make
Source4: ether-wake.c
Source5: etherwake.8
Source6: mii-diag.c
Source7: mii-diag.8
Patch1: net-tools-1.57-bug22040.patch
Patch2: net-tools-1.60-miiioctl.patch
Patch3: net-tools-1.60-manydevs.patch
Patch4: net-tools-1.60-virtualname.patch
Patch5: net-tools-1.60-cycle.patch
Patch6: net-tools-1.60-nameif.patch
Patch7: net-tools-1.60-ipx.patch
Patch8: net-tools-1.60-inet6-lookup.patch
Patch9: net-tools-1.60-man.patch
Patch10: net-tools-1.60-gcc33.patch
Patch11: net-tools-1.60-trailingblank.patch
Patch12: net-tools-1.60-interface.patch
Patch14: net-tools-1.60-gcc34.patch
Patch15: net-tools-1.60-overflow.patch
#included in netlpug-execshield.patch
#Patch16: net-tools-1.60-execshield.patch
Patch19: net-tools-1.60-siunits.patch
Patch20: net-tools-1.60-trunc.patch
Patch21: net-tools-1.60-return.patch
Patch22: net-tools-1.60-parse.patch
Patch23: net-tools-1.60-netmask.patch
Patch24: net-tools-1.60-ulong.patch
Patch25: net-tools-1.60-bcast.patch
Patch26: net-tools-1.60-mii-tool-obsolete.patch
Patch27: net-tools-1.60-netstat_ulong.patch
Patch28: net-tools-1.60-note.patch
Patch29: net-tools-1.60-num-ports.patch
Patch30: net-tools-1.60-duplicate-tcp.patch
Patch31: net-tools-1.60-statalias.patch
Patch32: net-tools-1.60-isofix.patch
Patch33: net-tools-1.60-bitkeeper.patch
Patch34: net-tools-1.60-ifconfig_ib.patch
Patch35: net-tools-1.60-de.patch
Patch36: netplug-1.2.9-execshield.patch
Patch37: net-tools-1.60-pie.patch
Patch38: net-tools-1.60-ifaceopt.patch
Patch39: net-tools-1.60-trim_iface.patch
Patch40: net-tools-1.60-stdo.patch

BuildRoot: %{_tmppath}/%{name}-root
Requires(post,preun): chkconfig
BuildRequires: gettext

%description
The net-tools package contains basic networking tools, including
ifconfig, netstat, route, and others.

%prep
%setup -q -a 1
%patch1 -p1 -b .bug22040
%patch2 -p1 -b .miiioctl
%patch3 -p0 -b .manydevs
%patch4 -p1 -b .virtualname
%patch5 -p1 -b .cycle
%patch6 -p1 -b .nameif
%patch7 -p1 -b .ipx
%patch8 -p1 -b .inet6-lookup
%patch9 -p1 -b .man
%patch10 -p1 -b .gcc33
%patch11 -p1 -b .trailingblank
%patch12 -p1 -b .interface
%patch14 -p1 -b .gcc34
%patch15 -p1 -b .overflow
#%patch16 -p1 -b .execshield
%patch19 -p1 -b .siunits
%patch20 -p1 -b .trunc
%patch21 -p1 -b .return
%patch22 -p1 -b .parse
%patch23 -p1 -b .netmask
%patch24 -p1 -b .ulong
%patch25 -p1 -b .bcast
%patch26 -p1 -b .obsolete
%patch27 -p1 -b .netstat_ulong
%patch28 -p1 -b .note
%patch29 -p1 -b .num-ports
%patch30 -p1 -b .dup-tcp
%patch31 -p1 -b .statalias
%patch32 -p1 -b .isofix
%patch33 -p1 -b .bitkeeper
%patch34 -p1 -b .ifconfig_ib
%patch35 -p1 
%patch36 -p1 -b .execshield
%patch37 -p1 -b .pie
%patch38 -p1 -b .ifaceopt
%patch39 -p1 -b .trim-iface
%patch40 -p1 -b .stdo

cp %SOURCE2 ./config.h
cp %SOURCE3 ./config.make
cp %SOURCE4 .
cp %SOURCE5 ./man/en_US
cp %SOURCE6 .
cp %SOURCE7 ./man/en_US

%ifarch alpha
perl -pi -e "s|-O2||" Makefile
%endif

#man pages conversion
#french 
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/fr_FR/arp.8 && mv arp.tmp man/fr_FR/arp.8
iconv -f iso-8859-1 -t utf-8 -o ethers.tmp man/fr_FR/ethers.5 && mv ethers.tmp man/fr_FR/ethers.5
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/fr_FR/hostname.1 && mv hostname.tmp man/fr_FR/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/fr_FR/ifconfig.8 && mv ifconfig.tmp man/fr_FR/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/fr_FR/netstat.8 && mv netstat.tmp man/fr_FR/netstat.8
iconv -f iso-8859-1 -t utf-8 -o plipconfig.tmp man/fr_FR/plipconfig.8 && mv plipconfig.tmp man/fr_FR/plipconfig.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/fr_FR/rarp.8 && mv rarp.tmp man/fr_FR/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/fr_FR/route.8 && mv route.tmp man/fr_FR/route.8
iconv -f iso-8859-1 -t utf-8 -o slattach.tmp man/fr_FR/slattach.8 && mv slattach.tmp man/fr_FR/slattach.8
#portugal
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/pt_BR/arp.8 && mv arp.tmp man/pt_BR/arp.8
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/pt_BR/hostname.1 && mv hostname.tmp man/pt_BR/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/pt_BR/ifconfig.8 && mv ifconfig.tmp man/pt_BR/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/pt_BR/netstat.8 && mv netstat.tmp man/pt_BR/netstat.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/pt_BR/rarp.8 && mv rarp.tmp man/pt_BR/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/pt_BR/route.8 && mv route.tmp man/pt_BR/route.8
#german
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/de_DE/arp.8 && mv arp.tmp man/fr_FR/arp.8
iconv -f iso-8859-1 -t utf-8 -o ethers.tmp man/de_DE/ethers.5 && mv ethers.tmp man/fr_FR/ethers.5
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/de_DE/hostname.1 && mv hostname.tmp man/fr_FR/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/de_DE/ifconfig.8 && mv ifconfig.tmp man/fr_FR/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/de_DE/netstat.8 && mv netstat.tmp man/fr_FR/netstat.8
iconv -f iso-8859-1 -t utf-8 -o plipconfig.tmp man/de_DE/plipconfig.8 && mv plipconfig.tmp man/fr_FR/plipconfig.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/de_DE/rarp.8 && mv rarp.tmp man/fr_FR/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/de_DE/route.8 && mv route.tmp man/fr_FR/route.8
iconv -f iso-8859-1 -t utf-8 -o slattach.tmp man/de_DE/slattach.8 && mv slattach.tmp man/fr_FR/slattach.8

%build
export CFLAGS="$RPM_OPT_FLAGS $CFLAGS"

make
gcc $RPM_OPT_FLAGS -o ether-wake ether-wake.c
gcc $RPM_OPT_FLAGS -o mii-diag mii-diag.c
pushd netplug-%{npversion}
make
popd

%install
rm -rf $RPM_BUILD_ROOT
mv man/de_DE man/de
mv man/fr_FR man/fr
mv man/pt_BR man/pt

make BASEDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

install -m 755 ether-wake %{buildroot}/sbin
install -m 755 mii-diag %{buildroot}/sbin

pushd netplug-%{npversion}
make install prefix=$RPM_BUILD_ROOT \
        initdir=$RPM_BUILD_ROOT/%{_initrddir} \
        mandir=$RPM_BUILD_ROOT/%{_mandir}
mv README README.netplugd
mv TODO TODO.netplugd
popd

rm %{buildroot}/sbin/rarp
rm %{buildroot}%{_mandir}/man8/rarp.8*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
  /sbin/chkconfig --add netplugd
  exit 0

%preun
if [ "$1" = "0" ]; then
  /sbin/chkconfig --del netplugd || :
  /sbin/service netplugd stop &> /dev/null || :
fi
exit 0

%postun
  /sbin/service netplugd condrestart >/dev/null 2>&1 || :
  exit 0

%files -f %{name}.lang
%defattr(-,root,root)
%doc netplug-%{npversion}/TODO.netplugd netplug-%{npversion}/README.netplugd COPYING
/bin/*
/sbin/*
%{_mandir}/man[158]/*
%lang(de)	%{_mandir}/de/man[158]/*
%lang(fr)	%{_mandir}/fr/man[158]/*
%lang(pt)	%{_mandir}/pt/man[158]/*
%dir	%{_sysconfdir}/netplug
%config %{_sysconfdir}/netplug/netplugd.conf
%{_sysconfdir}/netplug.d
%{_sysconfdir}/rc.d/init.d/netplugd

%changelog
- /etc/neplug is owned by net-tools (#130621)

* Tue Apr 05 2005 Radek Vokal <rvokal@redhat.com> 1.60-51
- flush output in mii-tool (#152568)

* Wed Mar 30 2005 Radek Vokal <rvokal@redhat.com> 1.60-50
- added mii-diag tool
- added newer ether-wake
- remove useless -i option from ifconfig
- stop trimming interface names (#152457)

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 01 2005 Radek Vokal <rvokal@redhat.com> 1.60-48
- behaviour of netstat -i option changed (#115987)
- netstat -i shows all interface, -I<Iface> only one

* Mon Feb 28 2005 Radek Vokal <rvokal@redhat.com> 1.60-47
- added RPM_OPT_FLAGS
- execshield patch for netplug <t8m@redhat.com>

* Wed Feb 16 2005 Radek Vokal <rvokal@redhat.com> 1.60-46
- small typo in german translation (#148775)

* Wed Feb 09 2005 Radek Vokal <rvokal@redhat.com> 1.60-45
- included infiniband support (#147396) <tduffy@sun.com>
- added etherwake man page

* Mon Feb 07 2005 Radek Vokal <rvokal@redhat.com> 1.60-44
- net-plug-1.2.9 - no changes, upstream included Red Hat patches
- ether-wake-1.08 - few changes in implementation (#145718)

* Mon Jan 10 2005 Radek Vokal <rvokal@redhat.com> 1.60-43
- don't report statistics for virtual devices (#143981) <kzak@redhat.com>
- fixing translation headers - content type format
- kill bitkeeper warning messages

* Fri Dec 03 2004 Radek Vokal <rvokal@redhat.com> 1.60-42
- filter out duplicate tcp entries (#139407)

* Thu Nov 25 2004 Radek Vokal <rvokal@redhat.com> 1.60-41
- added note to hostname(1) (#140239)
- fixed --num-ports option for netstat (#115100)

* Thu Nov 11 2004 Radek Vokal <rvokal@redhat.com> 1.60-40
- mii-tool(8) fixed, labeled as obsolete, added info (#138687)
- netstat crashing on i64 fixed (#138804) Patch by <Andreas.Hirstius@cern.ch>

* Thu Nov 04 2004 Radek Vokal <rvokal@redhat.com> 1.60-39
- IBM patch for netstat -s returning negative values on 64bit arch (#144064)
- broadcast calulated if only netmask provided (#60509)

* Tue Nov 02 2004 Radek Vokal <rvokal@redhat.com> 1.60-38
- fixed fail to assign the specified netmask before adress is assigned
- patch by Malita, Florin <florin.malita@glenayre.com>

* Wed Sep 29 2004 Radek Vokal <rvokal@redhat.com> 1.60-37
- spec file updated, added conversion for french and portugal man pages to UTF-8

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 1.60-36
- parse error fixed (#131539)

* Fri Sep 03 2004 Radek Vokal <rvokal@redhat.com> 1.60-35
- The return value of nameif was wrong (#129032) - patch from Fujitsu QA 

* Tue Aug 30 2004 Radek Vokal <rvokal@redhat.com> 1.60-34
- Trunc patch added (#128359)

* Mon Aug 30 2004 Radek Vokal <rvokal@redhat.com> 1.60-33
- Added patch for SI units by Tom "spot" Callaway <tcallawa@redhat.com> #118006

* Tue Aug 17 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-32
- Fix installopts for netplug.

* Sun Aug 08 2004 Alan Cox <alan@redhat.com> 1.60-31
- Build requires gettext.

* Mon Aug 02 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-30
- Update to latest netplugd version.

* Mon Jul 12 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-29
- Fixed initscript patch for netplug (#127351)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 14 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-27
- Fixed compiler warning/error in netplug.
- Updated to netplug-1.2.6 for security update and fixes.

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-26
- Updated netplugd to latest upstream version.
- Fixed execshield problem in main.c of netplugd.

* Thu Apr 15 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-25
- Fixed several possible buffer overflows (#120343)

* Tue Mar 30 2004 Harald Hoyer <harald@redhat.com> - 1.60-24
- fixed compilation with gcc34

* Tue Mar 23 2004 Karsten Hopp <karsten@redhat.de> 1.60-23 
- add chkconfig call in post and preun, fix init script (#116555)

* Thu Feb 19 2004 Phil Knirsch <pknirsch@redhat.com>
- Added netplug-1.2.1 to net-tools (FR #103419).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Aug 25 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-20.1
-rebuilt

* Mon Aug 25 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-20
- interface option now works as described in the man page (#61113).

* Tue Aug 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-19.1
- rebuilt

* Tue Aug 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-19
- Fixed trailing blank bug in hostname output (#101263).
- Remove -O2 fir alpha (#78955).
- Updated netstat statistic output, was still broken.

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-18.1
- rebuilt

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-18
- fix ether-wake.c build with gcc 3.3
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-16.1
- Bumped release and rebuilt

* Fri May 23 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-16
- Fixed ether-wake usage output (#55801).

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.60-15
- fix build with gcc 3.3

* Thu May 22 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-14
- Fixed wrong manpage (#55473).

* Wed May 21 2003 Phil Knirsch <pknirsch@redhat.com>
- Added inet6-lookup patch from John van Krieken (#84108).
- Fixed outdated link in ifconfig manpage (#91287).

* Tue May 20 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed incorrect address display for ipx (#46434).
- Fixed wrongly installed manpage dirs (#50664).

* Wed Mar 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-13
- Fixed nameif problem (#85748).

* Fri Feb 07 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-12
- Fixed -s parameter.
- Fix /proc statistics for -nic operation.
- Fixed -i operation in general.

* Mon Jan 27 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-11
- Disable smp build.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.60-10
- rebuilt

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 1.60-9
- Rebuild
- Copyright -> License.

* Thu Dec 05 2002 Elliot Lee <sopwith@redhat.com> 1.60-8
- Rebuild

* Tue Aug 06 2002 Phil Knirsch <pknirsch@redhat.com> 
- Added patch from Norm for a corrected output.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12 2002 Jeremy Katz <katzj@redhat.com>
- fix nstrcmp() to be correct in the case where there are many devices 
  of the same type, eg, "eth10" > "eth1"  (#61436)

* Tue Jul 31 2001 Bill Nottingham <notting@redhat.com>
- do *not* use SIOCDEVPRIVATE for MII ioctls

* Fri Jun  1 2001 Preston Brown <pbrown@redhat.com>
- include wake-on-lan wakeup utility, ether-wake by Donald Becker

* Wed Apr 18 2001 Crutcher Dunnavant <crutcher@redhat.com>
- itterate to 1.60

* Sun Apr  8 2001 Preston Brown <pbrown@redhat.com>
- use find_lang macro
- less specific locale dirs for man pages

* Mon Apr  2 2001 Preston Brown <pbrown@redhat.com>
- don't use this version of rarp, doesn't work with our 2.4.

* Tue Feb  6 2001 Crutcher Dunnavant <crutcher@redhat.com>
- fixed man page typo, closing bug #25921

* Fri Feb  1 2001 Crutcher Dunnavant <crutcher@redhat.com>
- applied twaugh's patch to close bug #25474
- which was a buffer length bug.

* Wed Dec 27 2000 Jeff Johnson <jbj@redhat.com>
- locales not initialized correctly (#20570).
- arp: document -e option (#22040).

* Sat Oct  7 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.57.
- MTU (and other) option(s) not parsed correctly (#9215).
- allow more granularity iwth --numeric (#9129).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.56.
- FHS packaging.

* Sat Apr 15 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.55.

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- fix "netstat -ci" (#6904).
- document more netstat options (#7429).

* Thu Jan 13 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.54.
- enable "everything but DECnet" including IPv6.

* Sun Aug 29 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.53.

* Wed Jul 28 1999 Jeff Johnson <jbj@redhat.com>
- plug "netstat -c" fd leak (#3620).

* Thu Jun 17 1999 Jeff Johnson <jbj@redhat.com>
- plug potential buffer overruns.

* Sat Jun 12 1999 John Hardin <jhardin@wolfenet.com>
- patch to recognize ESP and GRE protocols for VPN masquerade

* Fri Apr 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.52.

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- update interface statistics continuously (#1323)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.51.
- strip binaries.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.50.
- added slattach/plipconfig/ipmaddr/iptunnel commands.
- enabled translated man pages.

* Tue Dec 15 1998 Jakub Jelinek <jj@ultra.linux.cz>
- update to 1.49.

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.48.

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.47.

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.46

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include ethers.5

* Thu Jun 11 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 1.45
- patched hostname.c to initialize buffer
- patched ax25.c to use kernel headers

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- added config patch

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- changed to net-tools 1.432
- removed old glibc 2.1 patch
 
* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added extra patches for glibc 2.1

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- included complete set of network protocols (some were removed for
  initial glibc work)

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated glibc patch for glibc 2.0.5

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- updated to 1.33
