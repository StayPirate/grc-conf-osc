#
# spec file for package grc-osc
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define archive_prefix grc-osc
%define grcoscdir /opt/grc-osc

Name:           grc-osc
Version:        1.2
Release:        0
Summary:        OSC conf files for GRC
License:        MIT
Group:          Development/Tools/Other
Url:            https://github.com/StayPirate/grc-conf-osc
Source:         %{archive_prefix}-%{version}.tar.xz
BuildArch:      noarch
Requires:       osc >= 0.162.1
Requires:       grc

%description
OSC conf files for GRC

%prep
%setup -q -n %{archive_prefix}-%{version}

%build

%install
mkdir -p %{buildroot}%{grcoscdir}
cp -r * %{buildroot}%{grcoscdir}
test -f %{buildroot}/etc/grc.conf || touch %{buildroot}/etc/grc.conf
cat %{grcoscdir}/osc-grc.conf >> %{buildroot}/etc/grc.conf

%files
%defattr(644,root,root)
/etc/grc.conf
%defattr(755,root,root)
%{grcoscdir}

%changelog
