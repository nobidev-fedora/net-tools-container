Summary: Basic networking tools.
Name: net-tools
Version: 1.60
Release: 7
Copyright: GPL
Group: System Environment/Base
Source0: http://www.tazenda.demon.co.uk/phil/net-tools/net-tools-%{version}.tar.bz2
Source1: net-tools-%{version}-config.h
Source2: net-tools-%{version}-config.make
Source3: ether-wake.c
Patch4: net-tools-1.57-bug22040.patch
Patch5: net-tools-1.60-miiioctl.patch
Patch6: net-tools-1.60-manydevs.patch
Patch7: net-tools-1.60-virtualname.patch
BuildRoot: %{_tmppath}/%{name}-root

%description
The net-tools package contains basic networking tools, including
ifconfig, netstat, route, and others.

%prep
%setup -q
%patch4 -p 1 -b .bug22040
%patch5 -p 1 -b .miiioctl
%patch6 -p 0 -b .manydevs
%patch7 -p 1 -b .virtualname

cp %SOURCE1 ./config.h
cp %SOURCE2 ./config.make
cp %SOURCE3 .

%build
make
gcc $RPM_OPT_FLAGS -o ether-wake ether-wake.c

%install
rm -rf $RPM_BUILD_ROOT

make BASEDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

install -m 755 ether-wake %{buildroot}/sbin

rm %{buildroot}/sbin/rarp
rm %{buildroot}%{_mandir}/man8/rarp.8*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
/sbin/*
%{_mandir}/man[158]/*
%lang(de_DE)	%{_mandir}/de_DE/man[158]/*
%lang(fr_FR)	%{_mandir}/fr_FR/man[158]/*
%lang(pt_BR)	%{_mandir}/pt_BR/man[158]/*

%changelog
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
