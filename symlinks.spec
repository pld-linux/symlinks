Summary:     	Symbolic link sanity checker
Summary(de): 	Symbolic-Link-Sanity-Checker 
Summary(fr): 	Vérificateur de la cohérence des liens symboliques
Summary(pl): 	Sprawdzanie poprawno¶ci symlinków
Summary(tr): 	Simgesel baðlantý denetleyici
Name:        	symlinks
Version:     	1.2
Release:     	4
Group:       	Utilities/File
Group(pl):	Narzêdzia/Pliki
Copyright:  	distributable
Source:      	ftp://sunsite.unc.edu/pub/Linux/utils/file/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This program check for a number of problems with symlinks on a system,
including symlinks which point to nonexistant files (dangling symlinks).
It can also automatically convert absolute symlinks to relative symlinks.

%description -l de
Dieses Programm prüft das System auf eine Reihe von Problemen im 
Zusammenhang mit Symlinks, einschließlich Symlinks, die auf nicht 
vorhandene Dateien zeigen (baumelnde Symlinks). Außerdem kann es 
absolute Symlinks automatisch in relative verwandeln. 

%description -l fr
Ce programme vérifie un certain nombre de problèmes avec les liens
symboliques sur un système, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l pl
Program wyszukuje ró¿ne problemy zzi±zane z dowi±zaniami symbolicznymi, w
tym dowizania pokazuj±ce na nieistniej±ce pliki. Mo¿e te¿ automatycznie
konwertowaæ bezwzglêdne dowi±zania symboliczne na wzglêdne.

%description -l tr
Bu program sistemdeki simgesel baðlantýlarla ilgili sorunlarý (varolmayan
bir dosyayý gösteren simgesel baðlantýlar gibi) kontrol eder. Ayrýca,
mutlak simgesel baðlantýlarý baðýl simgesel baðlantýlara dönüþtürür.

%prep
%setup -q

%build
gcc $RPM_OPT_FLAGS -o symlinks symlinks.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man8}

install -s symlinks $RPM_BUILD_ROOT%{_bindir}
install symlinks.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/symlinks
%{_mandir}/man8/symlinks.8*

%changelog
* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.2-4]
- removed man group from man pages
- added Group(pl)
- compiled on rpm 3

* Fri Sep 25 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [1.2-3]
- added full %attr description in %files,
- removed `-u root -o root' in %install, allowing building from non-root
  account,
- added pl translation,
- use %{name} and %{version} macros,
- added using $RPM_OPT_FLAGS on compile time,
- added `rm -rf $ROM_BUILD_ROOT' on top %install.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- changed build root to /var/tmp, not /var/lib
- updated to version 1.2

* Wed Jul 09 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- build-rooted
