Summary: The basic tools for setting up networking.
Name: net-tools
Version: 1.57
Release: 1
Copyright: GPL
Group: System Environment/Base
Source0: http://www.tazenda.demon.co.uk/phil/net-tools/net-tools-%{version}.tar.bz2
Source1: net-tools-%{version}-config.h
Source2: net-tools-%{version}-config.make
Patch0: net-tools-1.56-fhs.patch
Patch1: net-tools-1.57-bug9215.patch
Patch2: net-tools-1.57-bug9129.patch
BuildRoot: %{_tmppath}/%{name}-root

%description
The net-tools package contains the basic tools needed for setting up
networking:  ethers, route and others.

%prep
%setup -q
%patch0 -p 1 -b .fhs
%patch1 -p 1 -b .bug9215
%patch2 -p 1 -b .bug9129

cp %SOURCE1 ./config.h
cp %SOURCE2 ./config.make

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make BASEDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/bin/*
/sbin/*
%{_mandir}/man[158]/*
%lang(cs)	%{_datadir}/locale/cs/LC_MESSAGES/net-tools.mo
%lang(de)	%{_mandir}/de_DE/man[158]/*
%lang(de)	%{_datadir}/locale/de/LC_MESSAGES/net-tools.mo
%lang(et)	%{_datadir}/locale/et_EE/LC_MESSAGES/net-tools.mo
%lang(fr)	%{_mandir}/fr_FR/man[158]/*
%lang(fr)	%{_datadir}/locale/fr/LC_MESSAGES/net-tools.mo
%lang(pt_BR)	%{_mandir}/pt_BR/man[158]/*
%lang(pt_BR)	%{_datadir}/locale/pt_BR/LC_MESSAGES/net-tools.mo

%changelog
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
