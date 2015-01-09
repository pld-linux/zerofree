Summary:	Utility to force unused ext2 inodes and blocks to zero
Name:		zerofree
Version:	1.0.3
Release:	1
License:	GPL+
Group:		Applications/System
Source0:	http://intgat.tigress.co.uk/rmy/uml/%{name}-%{version}.tgz
# Source0-md5:	7fffca9639a2acc9c889c49b3f94a0c6
Source1:	http://intgat.tigress.co.uk/rmy/uml/sparsify.c
# Source1-md5:	919ad782c7120d1e4a9c0ccc9f45b8ef
Source2:	http://intgat.tigress.co.uk/rmy/uml/index.html
# Source2-md5:	b30d82b3980d2cbfe7f299cd646e7018
Source3:	%{name}.sgml
# Source3-md5:	694621b0e046c34a674da25f8328585b
URL:		http://intgat.tigress.co.uk/rmy/uml/
BuildRequires:	e2fsprogs-devel
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

%prep
%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"
%{__cc} %{rpmcflags} sparsify.c -o sparsify -lext2fs

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
%doc COPYING index.html
%attr(755,root,root) %{_sbindir}/zerofree
%attr(755,root,root) %{_sbindir}/sparsify
%{_mandir}/man8/zerofree.8*
