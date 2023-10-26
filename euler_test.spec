Name:   euler_test
Version:  0.3.9.2
Release:  3
Summary:  A simple tool for pasting info onto sticky notes instances
BuildArch:  noarch
License:  GPLv3+
URL:    https://pagure.io/fpaste
Source0:  https://github.com/runshine/euler_test/raw/main/euler_test-0.3.9.2.tar.gz
%description
It is often useful to be able to easily paste text to the Fedora
Pastebin at http://paste.fedoraproject.org and this simple script
will do that and return the resulting URL so that people may
examine the output. This can hopefully help folks who are for
some reason stuck without X, working remotely, or any other
reason they may be unable to paste something into the pastebin

%prep
%autosetup

%build
#nothing required

./make.sh

%install
mkdir -p %{buildroot}%{_bindir}
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}


%files
%{_bindir}/%{name}
%doc README.rst TODO
%{_mandir}/man1/%{name}.1.gz
%license COPYING