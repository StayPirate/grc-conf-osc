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
Version:        0.1
Release:        0
Summary:        OSC conf files for GRC
License:        MIT
Group:          Development/Tools/Other
Url:            https://github.com/StayPirate/grc-conf-osc
Source:         %{archive_prefix}-%{version}.tar.xz
BuildArch:      noarch
Requires:       osc
Requires:       grc
#BuildRequires:  grc

%description
OSC conf files for GRC

%prep
%setup -q -n %{archive_prefix}-%{version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/grc.conf.d/
install -Dm 0755 grc.conf.d/00-osc.conf %{buildroot}%{_sysconfdir}/grc.conf.d/00-osc.conf
mkdir -p %{buildroot}%{_datadir}/grc/
install -m 0644 conf.* %{buildroot}%{_datadir}/grc/

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/grc.conf.d/00-osc.conf
%{_datadir}/grc/

%changelog
