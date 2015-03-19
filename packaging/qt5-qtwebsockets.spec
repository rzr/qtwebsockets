#
# Copyright (c) 2015 Philippe Coval <philippe.coval@eurogiciel.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name:           qt5-qtwebsockets
Version:        5.4.1
Release:        0
License:        LGPL-2.1+ or GPL-3.0
Summary:        Pure Qt implementation of WebSockets - both client and server
Url:            http://code.qt.io/cgit/qt/qtwebsockets.git
Group:          System/Libraries
# X-Vc-Url:     http://code.qt.io/git/qt/qtwebsockets.git
Group:          Contrib
Source:         %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest

BuildRequires:  make
BuildRequires:  fdupes
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  qt5-qmake
BuildRequires:  qt5-qtdeclarative-qtquick-devel
%description

Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt module to manage websockets.

%package devel
Summary:    Pure Qt implementation of WebSockets - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel

Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains development files for Qt module to manage websockets.

%prep
%setup -q -n %{name}-%{version}

%build
touch .git
cp %{SOURCE1001} .
export QTDIR=/usr/share/qt5
qmake -qt=5

%__make %{?_smp_mflags}


%install
%qmake_install
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%manifest %{name}.manifest
%{_libdir}/*.so.*
%{_libdir}/*/*/*
%{_libdir}/*.la
%{_libdir}/*.prl
%{_datadir}/*


%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
