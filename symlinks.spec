Summary:	Symbolic link sanity checker
Summary(de):	Symbolic-Link-Sanity-Checker 
Summary(es):	Verificador de validez para links simb�licos
Summary(fr):	V�rificateur de la coh�rence des liens symboliques
Summary(pl):	Sprawdzanie poprawno�ci symlink�w
Summary(pt_BR):	Verificador de validade para links simb�licos
Summary(tr):	Simgesel ba�lant� denetleyici
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
Dieses Programm pr�ft das System auf eine Reihe von Problemen im
Zusammenhang mit Symlinks, einschlie�lich Symlinks, die auf nicht
vorhandene Dateien zeigen (baumelnde Symlinks). Au�erdem kann es
absolute Symlinks automatisch in relative verwandeln.

%description -l es
Este programa chequea varios problemas con symlinks en un sistema,
incluido symlinks que apuntan para archivo inexistente. Puede tambi�n,
autom�ticamente, convertir symlinks absolutos a symlinks relativos.

%description -l fr
Ce programme v�rifie un certain nombre de probl�mes avec les liens
symboliques sur un syst�me, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l pl
Program wyszukuje r�ne problemy zwi�zane z dowi�zaniami
symbolicznymi, w tym dowi�zania pokazuj�ce na nieistniej�ce pliki.
Mo�e te� automatycznie konwertowa� bezwzgl�dne dowi�zania symboliczne
na wzgl�dne.

%description -l pt_BR
Este programa checa v�rios problemas com symlinks em um sistema,
incluindo symlinks que apontam para arquivo inexistentes. Ele pode
tamb�m automaticamente converter symlinks absolutos para symlinks
relativos.

%description -l tr
Bu program sistemdeki simgesel ba�lant�larla ilgili sorunlar�
(varolmayan bir dosyay� g�steren simgesel ba�lant�lar gibi) kontrol
eder. Ayr�ca, mutlak simgesel ba�lant�lar� ba��l simgesel ba�lant�lara
d�n��t�r�r.

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
