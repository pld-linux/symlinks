Summary:	Symbolic link sanity checker
Summary(de):	Symbolic-Link-Sanity-Checker 
Summary(es):	Verificador de validez para links simbólicos
Summary(fr):	Vérificateur de la cohérence des liens symboliques
Summary(pl):	Sprawdzanie poprawno¶ci symlinków
Summary(pt_BR):	Verificador de validade para links simbólicos
Summary(tr):	Simgesel baðlantý denetleyici
Name:		symlinks
Version:	1.2
Release:	15
License:	distributable
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/file/%{name}-%{version}.tar.gz
Patch0:		%{name}-fixman.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The symlinks utility performs maintenance on symbolic links. Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files. Symlinks can also automatically convert absolute
symlinks to relative symlinks.

%description -l de
Dieses Programm prüft das System auf eine Reihe von Problemen im
Zusammenhang mit Symlinks, einschließlich Symlinks, die auf nicht
vorhandene Dateien zeigen (baumelnde Symlinks). Außerdem kann es
absolute Symlinks automatisch in relative verwandeln.

%description -l es
Este programa chequea varios problemas con symlinks en un sistema,
incluido symlinks que apuntan para archivo inexistente. Puede también,
automáticamente, convertir symlinks absolutos a symlinks relativos.

%description -l fr
Ce programme vérifie un certain nombre de problèmes avec les liens
symboliques sur un système, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l pl
Program wyszukuje ró¿ne problemy zwi±zane z dowi±zaniami
symbolicznymi, w tym dowi±zania pokazuj±ce na nieistniej±ce pliki.
Mo¿e te¿ automatycznie konwertowaæ bezwzglêdne dowi±zania symboliczne
na wzglêdne.

%description -l pt_BR
Este programa checa vários problemas com symlinks em um sistema,
incluindo symlinks que apontam para arquivo inexistentes. Ele pode
também automaticamente converter symlinks absolutos para symlinks
relativos.

%description -l tr
Bu program sistemdeki simgesel baðlantýlarla ilgili sorunlarý
(varolmayan bir dosyayý gösteren simgesel baðlantýlar gibi) kontrol
eder. Ayrýca, mutlak simgesel baðlantýlarý baðýl simgesel baðlantýlara
dönüþtürür.

%prep
%setup -q
%patch -p1

%build
%{__cc} %{rpmcflags} -o symlinks symlinks.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install symlinks $RPM_BUILD_ROOT%{_bindir}
install symlinks.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/symlinks
%{_mandir}/man8/symlinks.8*
