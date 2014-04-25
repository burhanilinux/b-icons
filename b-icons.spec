# Spec file for package b-icons
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:		b-icons
Version:	2.0
Release:	0

Summary:	B-icons theme
Group:		System/GUI/Other
License:    LGPL-3.0+ or CC-BY-SA-3.0

Group:      System/GUI/GNOME

Source0:	%{name}-%{version}.tar.gz

Requires:	hicolor-icon-theme, gnome-icon-theme
BuildArch:	noarch


%description
These are the B-icons you're looking for

%prep
%setup -q

# Delete dead icon symlinks
find -L . -type l -delete

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a B-icons/ $RPM_BUILD_ROOT%{_datadir}/icons/

%files
%doc {AUTHORS,COPYING,LICENSE}
%{_datadir}/icons/B-icons/
