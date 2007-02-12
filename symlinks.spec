Summary:	Symbolic link sanity checker
Summary(de.UTF-8):   Symbolic-Link-Sanity-Checker
Summary(es.UTF-8):   Verificador de validez para links simbólicos
Summary(fr.UTF-8):   Vérificateur de la cohérence des liens symboliques
Summary(pl.UTF-8):   Sprawdzanie poprawności symlinków
Summary(pt_BR.UTF-8):   Verificador de validade para links simbólicos
Summary(tr.UTF-8):   Simgesel bağlantı denetleyici
Name:		symlinks
Version:	1.2
Release:	16
License:	distributable
Group:		Applications/File
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/file/%{name}-%{version}.tar.gz
# Source0-md5:	b4bab0a5140e977c020d96e7811cec61
Patch0:		%{name}-fixman.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The symlinks utility performs maintenance on symbolic links. Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files. Symlinks can also automatically convert absolute
symlinks to relative symlinks.

%description -l de.UTF-8
Dieses Programm prüft das System auf eine Reihe von Problemen im
Zusammenhang mit Symlinks, einschließlich Symlinks, die auf nicht
vorhandene Dateien zeigen (baumelnde Symlinks). Außerdem kann es
absolute Symlinks automatisch in relative verwandeln.

%description -l es.UTF-8
Este programa chequea varios problemas con symlinks en un sistema,
incluido symlinks que apuntan para archivo inexistente. Puede también,
automáticamente, convertir symlinks absolutos a symlinks relativos.

%description -l fr.UTF-8
Ce programme vérifie un certain nombre de problèmes avec les liens
symboliques sur un système, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l pl.UTF-8
Program wyszukuje różne problemy związane z dowiązaniami
symbolicznymi, w tym dowiązania pokazujące na nieistniejące pliki.
Może też automatycznie konwertować bezwzględne dowiązania symboliczne
na względne.

%description -l pt_BR.UTF-8
Este programa checa vários problemas com symlinks em um sistema,
incluindo symlinks que apontam para arquivo inexistentes. Ele pode
também automaticamente converter symlinks absolutos para symlinks
relativos.

%description -l tr.UTF-8
Bu program sistemdeki simgesel bağlantılarla ilgili sorunları
(varolmayan bir dosyayı gösteren simgesel bağlantılar gibi) kontrol
eder. Ayrıca, mutlak simgesel bağlantıları bağıl simgesel bağlantılara
dönüştürür.

%prep
%setup -q
%patch0 -p1

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o symlinks symlinks.c

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
