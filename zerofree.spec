Summary:	Utility to force unused ext2 inodes and blocks to zero
Summary(pl.UTF-8):	Narzędzie wymuszające wyzerowanie nie używanych i-węzłów i bloków ext2
Name:		zerofree
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://frippery.org/uml/%{name}-%{version}.tgz
# Source0-md5:	4f2d6bdba4212e54eb7dd22a8fbb6d29
Source1:	https://frippery.org/uml/sparsify.c
# Source1-md5:	919ad782c7120d1e4a9c0ccc9f45b8ef
Source2:	https://frippery.org/uml/index.html
# Source2-md5:	b7ab83b45706013757af28d9bba641cc
Source3:	%{name}.sgml
# Source3-md5:	694621b0e046c34a674da25f8328585b
URL:		https://frippery.org/uml/
BuildRequires:	docbook-to-man
BuildRequires:	e2fsprogs-devel >= 1.41
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zerofree is a utility to set unused filesystem inodes and blocks of an
ext2 filesystem to zero. This can improve the compressibility and
privacy of an ext2 filesystem.

This tool was inspired by the ext2fs privacy (i.e. secure deletion)
patch described in a Linux kernel mailing list thread.

WARNING: The filesystem to be processed should be unmounted or mounted
read-only. The tool tries to check this before running, but you should
be careful.

%description -l pl.UTF-8
zerofree to narzędzie zerujące nie używane i-węzły i bloki systemu
plików ext2. To może poprawić kompresowalność i prywatność systemu
plików.

Narzędzie było inspirowane łatką prywatności (bezpiecznego usuwania)
dla ext2fs, opisaną w wątku listy dyskusyjnej jądra Linuksa.

UWAGA: system plików do przetwarzania powinien być odmontowany lub
zamontowany tylko do odczytu. Narzędzie próbuje sprawdzić to przed
działaniem, ale trzeba być ostrożnym.

%prep
%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmldflags} %{rpmcflags} %{rpmcppflags}"

%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} sparsify.c -o sparsify -lext2fs

docbook-to-man zerofree.sgml > zerofree.8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -p zerofree $RPM_BUILD_ROOT%{_sbindir}
install -p sparsify $RPM_BUILD_ROOT%{_sbindir}
cp -p zerofree.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html
%attr(755,root,root) %{_sbindir}/zerofree
%attr(755,root,root) %{_sbindir}/sparsify
%{_mandir}/man8/zerofree.8*
