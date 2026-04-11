%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksQuickUI
%define devname %mklibname SonicFrameworksQuickUI -d
#define git 20240217

Name: sonic-frameworks-quick-ui
Version: 6.25.0
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-frameworks-quick-ui
# %if 0%{?git:1}
# Source0: https://invent.kde.org/frameworks/kirigami/-/archive/master/kirigami-master.tar.bz2#/kirigami-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: QtQuick plugins to build user interfaces following the SonicDE Human Interface Guidelines
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6ShaderTools)
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Conflicts:   kf6-kirigami

%patchlist

%description
%summary

%package -n %{libname}
Summary: QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines
Group: System/Libraries
Requires: %{name} = %{EVRD}
# %{_qtdir}/qml/org/kde/kirigami/AbstractApplicationWindow.qml
Requires: qml(org.kde.desktop)
Conflicts: %{_lib}KirigamiPlatform

%description -n %{libname}
%summary

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KirigamiPlatform-devel

%description -n %{devname}
%summary

%files -f %{name}.lang
%{_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_datadir}/qlogging-categories6/kirigami.categories

%files -n %{devname}
%{_includedir}/KF6/Kirigami
%{_libdir}/cmake/KF6Kirigami*

%files -n %{libname}
%{_libdir}/libKirigami.so*
%{_libdir}/libKirigamiControls.so*
%{_libdir}/libKirigamiDelegates.so*
%{_libdir}/libKirigamiDialogs.so*
%{_libdir}/libKirigamiLayouts.so*
%{_libdir}/libKirigamiLayoutsPrivate.so*
%{_libdir}/libKirigamiPlatform.so*
%{_libdir}/libKirigamiPolyfill.so*
%{_libdir}/libKirigamiPrimitives.so*
%{_libdir}/libKirigamiPrivate.so*
%{_libdir}/libKirigamiTemplates.so*
%{_qtdir}/qml/org/kde/kirigami
