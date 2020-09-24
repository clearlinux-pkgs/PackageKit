#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x17ACBA8DFA970E17 (richard@hughsie.com)
#
Name     : PackageKit
Version  : 1.1.13
Release  : 8
URL      : https://www.freedesktop.org/software/PackageKit/releases/PackageKit-1.1.13.tar.xz
Source0  : https://www.freedesktop.org/software/PackageKit/releases/PackageKit-1.1.13.tar.xz
Source1  : https://www.freedesktop.org/software/PackageKit/releases/PackageKit-1.1.13.tar.xz.asc
Summary  : PackageKit is a system daemon for installing stuff.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: PackageKit-autostart = %{version}-%{release}
Requires: PackageKit-bin = %{version}-%{release}
Requires: PackageKit-data = %{version}-%{release}
Requires: PackageKit-lib = %{version}-%{release}
Requires: PackageKit-libexec = %{version}-%{release}
Requires: PackageKit-license = %{version}-%{release}
Requires: PackageKit-locales = %{version}-%{release}
Requires: PackageKit-man = %{version}-%{release}
Requires: PackageKit-services = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : autoconf-archive-dev
BuildRequires : automake
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : vala

%description
PackageKit
A DBUS packaging abstraction layer
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package autostart
Summary: autostart components for the PackageKit package.
Group: Default

%description autostart
autostart components for the PackageKit package.


%package bin
Summary: bin components for the PackageKit package.
Group: Binaries
Requires: PackageKit-data = %{version}-%{release}
Requires: PackageKit-libexec = %{version}-%{release}
Requires: PackageKit-license = %{version}-%{release}
Requires: PackageKit-services = %{version}-%{release}

%description bin
bin components for the PackageKit package.


%package data
Summary: data components for the PackageKit package.
Group: Data

%description data
data components for the PackageKit package.


%package dev
Summary: dev components for the PackageKit package.
Group: Development
Requires: PackageKit-lib = %{version}-%{release}
Requires: PackageKit-bin = %{version}-%{release}
Requires: PackageKit-data = %{version}-%{release}
Provides: PackageKit-devel = %{version}-%{release}
Requires: PackageKit = %{version}-%{release}

%description dev
dev components for the PackageKit package.


%package doc
Summary: doc components for the PackageKit package.
Group: Documentation
Requires: PackageKit-man = %{version}-%{release}

%description doc
doc components for the PackageKit package.


%package lib
Summary: lib components for the PackageKit package.
Group: Libraries
Requires: PackageKit-data = %{version}-%{release}
Requires: PackageKit-libexec = %{version}-%{release}
Requires: PackageKit-license = %{version}-%{release}

%description lib
lib components for the PackageKit package.


%package libexec
Summary: libexec components for the PackageKit package.
Group: Default
Requires: PackageKit-license = %{version}-%{release}

%description libexec
libexec components for the PackageKit package.


%package license
Summary: license components for the PackageKit package.
Group: Default

%description license
license components for the PackageKit package.


%package locales
Summary: locales components for the PackageKit package.
Group: Default

%description locales
locales components for the PackageKit package.


%package man
Summary: man components for the PackageKit package.
Group: Default

%description man
man components for the PackageKit package.


%package services
Summary: services components for the PackageKit package.
Group: Systemd services

%description services
services components for the PackageKit package.


%prep
%setup -q -n PackageKit-1.1.13
cd %{_builddir}/PackageKit-1.1.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581013155
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-dbus-sys=/usr/share/dbus-1/system.d --enable-swupd --with-dbus-services=/usr/share/dbus-1/system-services --sysconfdir=/usr/share/PackageKit/
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1581013155
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PackageKit
cp %{_builddir}/PackageKit-1.1.13/COPYING %{buildroot}/usr/share/package-licenses/PackageKit/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/PackageKit-1.1.13/lib/packagekit-glib2/COPYING %{buildroot}/usr/share/package-licenses/PackageKit/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang PackageKit
## Remove excluded files
rm -f %{buildroot}/var/lib/PackageKit/transactions.db

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/pk-gtk-module.desktop

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/system-update.target.wants/packagekit-offline-update.service

%files bin
%defattr(-,root,root,-)
/usr/bin/pkcon
/usr/bin/pkmon

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
/usr/share/PackageKit/PackageKit/CommandNotFound.conf
/usr/share/PackageKit/PackageKit/PackageKit.conf
/usr/share/PackageKit/PackageKit/Vendor.conf
/usr/share/PackageKit/cron.daily/packagekit-background.cron
/usr/share/PackageKit/helpers/test_spawn/search-name.sh
/usr/share/PackageKit/pk-upgrade-distro.sh
/usr/share/PackageKit/profile.d/PackageKit.sh
/usr/share/PackageKit/sysconfig/packagekit-background
/usr/share/bash-completion/completions/pkcon
/usr/share/dbus-1/interfaces/org.freedesktop.PackageKit.Transaction.xml
/usr/share/dbus-1/interfaces/org.freedesktop.PackageKit.xml
/usr/share/dbus-1/system-services/org.freedesktop.PackageKit.service
/usr/share/dbus-1/system.d/org.freedesktop.PackageKit.conf
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.packagekit.policy
/usr/share/polkit-1/rules.d/org.freedesktop.packagekit.rules

%files dev
%defattr(-,root,root,-)
/usr/include/PackageKit/packagekit-glib2/packagekit.h
/usr/include/PackageKit/packagekit-glib2/pk-bitfield.h
/usr/include/PackageKit/packagekit-glib2/pk-category.h
/usr/include/PackageKit/packagekit-glib2/pk-client-helper.h
/usr/include/PackageKit/packagekit-glib2/pk-client-sync.h
/usr/include/PackageKit/packagekit-glib2/pk-client.h
/usr/include/PackageKit/packagekit-glib2/pk-common.h
/usr/include/PackageKit/packagekit-glib2/pk-control-sync.h
/usr/include/PackageKit/packagekit-glib2/pk-control.h
/usr/include/PackageKit/packagekit-glib2/pk-desktop.h
/usr/include/PackageKit/packagekit-glib2/pk-details.h
/usr/include/PackageKit/packagekit-glib2/pk-distro-upgrade.h
/usr/include/PackageKit/packagekit-glib2/pk-enum-types.h
/usr/include/PackageKit/packagekit-glib2/pk-enum.h
/usr/include/PackageKit/packagekit-glib2/pk-error.h
/usr/include/PackageKit/packagekit-glib2/pk-eula-required.h
/usr/include/PackageKit/packagekit-glib2/pk-files.h
/usr/include/PackageKit/packagekit-glib2/pk-item-progress.h
/usr/include/PackageKit/packagekit-glib2/pk-media-change-required.h
/usr/include/PackageKit/packagekit-glib2/pk-offline.h
/usr/include/PackageKit/packagekit-glib2/pk-package-id.h
/usr/include/PackageKit/packagekit-glib2/pk-package-ids.h
/usr/include/PackageKit/packagekit-glib2/pk-package-sack-sync.h
/usr/include/PackageKit/packagekit-glib2/pk-package-sack.h
/usr/include/PackageKit/packagekit-glib2/pk-package.h
/usr/include/PackageKit/packagekit-glib2/pk-progress.h
/usr/include/PackageKit/packagekit-glib2/pk-repo-detail.h
/usr/include/PackageKit/packagekit-glib2/pk-repo-signature-required.h
/usr/include/PackageKit/packagekit-glib2/pk-require-restart.h
/usr/include/PackageKit/packagekit-glib2/pk-results.h
/usr/include/PackageKit/packagekit-glib2/pk-source.h
/usr/include/PackageKit/packagekit-glib2/pk-task-sync.h
/usr/include/PackageKit/packagekit-glib2/pk-task.h
/usr/include/PackageKit/packagekit-glib2/pk-transaction-list.h
/usr/include/PackageKit/packagekit-glib2/pk-transaction-past.h
/usr/include/PackageKit/packagekit-glib2/pk-update-detail.h
/usr/include/PackageKit/packagekit-glib2/pk-version.h
/usr/lib64/libpackagekit-glib2.so
/usr/lib64/pkgconfig/packagekit-glib2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/PackageKit/PackageKit-Common-functions.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-Enumerations.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-Offline-Updates.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PackageIDs.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkBitfield.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkCategory.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkClient.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkClientHelper.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkControl.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkDesktop.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkDetails.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkDistroUpgrade.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkError.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkEulaRequired.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkFiles.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkItemProgress.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkMediaChangeRequired.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkPackage.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkPackageSack.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkProgress.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkRepoDetail.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkRepoSignatureRequired.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkRequireRestart.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkResults.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkSource.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkTask.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkTransactionList.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkTransactionPast.html
/usr/share/gtk-doc/html/PackageKit/PackageKit-PkUpdateDetail.html
/usr/share/gtk-doc/html/PackageKit/PackageKit.devhelp2
/usr/share/gtk-doc/html/PackageKit/PackageKit.html
/usr/share/gtk-doc/html/PackageKit/Transaction.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-5-0.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-5-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-5-3.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-5-4.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-5-5.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-0.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-1.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-10.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-11.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-13.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-3.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-4.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-6-5.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-7-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-7-5.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-0.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-1.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-11.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-12.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-14.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-16.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-17.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-6.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-8-8.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-9-1.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-9-5.html
/usr/share/gtk-doc/html/PackageKit/api-index-0-9-6.html
/usr/share/gtk-doc/html/PackageKit/api-index-1-0-10.html
/usr/share/gtk-doc/html/PackageKit/api-index-1-0-12.html
/usr/share/gtk-doc/html/PackageKit/api-index-1-0-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-1-1-2.html
/usr/share/gtk-doc/html/PackageKit/api-index-1-1-8.html
/usr/share/gtk-doc/html/PackageKit/api-reference.html
/usr/share/gtk-doc/html/PackageKit/backend-compiled.html
/usr/share/gtk-doc/html/PackageKit/backend-spawn.html
/usr/share/gtk-doc/html/PackageKit/concepts.html
/usr/share/gtk-doc/html/PackageKit/home.png
/usr/share/gtk-doc/html/PackageKit/index.html
/usr/share/gtk-doc/html/PackageKit/introduction-backends.html
/usr/share/gtk-doc/html/PackageKit/introduction-cancellation.html
/usr/share/gtk-doc/html/PackageKit/introduction-errors.html
/usr/share/gtk-doc/html/PackageKit/introduction-group-type.html
/usr/share/gtk-doc/html/PackageKit/introduction-ideas-filters.html
/usr/share/gtk-doc/html/PackageKit/introduction-ideas-status.html
/usr/share/gtk-doc/html/PackageKit/introduction-ideas-transactionid.html
/usr/share/gtk-doc/html/PackageKit/introduction-ideas-transactions.html
/usr/share/gtk-doc/html/PackageKit/introduction.html
/usr/share/gtk-doc/html/PackageKit/left-insensitive.png
/usr/share/gtk-doc/html/PackageKit/left.png
/usr/share/gtk-doc/html/PackageKit/lpackagekit-glib2.html
/usr/share/gtk-doc/html/PackageKit/pk-structure.png
/usr/share/gtk-doc/html/PackageKit/pk-structure.svg
/usr/share/gtk-doc/html/PackageKit/pk-transactions-auto-untrusted.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-download.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-failure.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-repair-required.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-set-locale.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-sig-install.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-success.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions-trusted.png
/usr/share/gtk-doc/html/PackageKit/pk-transactions.svg
/usr/share/gtk-doc/html/PackageKit/right-insensitive.png
/usr/share/gtk-doc/html/PackageKit/right.png
/usr/share/gtk-doc/html/PackageKit/specification.html
/usr/share/gtk-doc/html/PackageKit/style.css
/usr/share/gtk-doc/html/PackageKit/up-insensitive.png
/usr/share/gtk-doc/html/PackageKit/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/modules/libpk-gtk-module.so
/usr/lib64/gtk-3.0/modules/libpk-gtk-module.so
/usr/lib64/libpackagekit-glib2.so.18
/usr/lib64/libpackagekit-glib2.so.18.1.3
/usr/lib64/packagekit-backend/libpk_backend_dummy.so
/usr/lib64/packagekit-backend/libpk_backend_test_fail.so
/usr/lib64/packagekit-backend/libpk_backend_test_nop.so
/usr/lib64/packagekit-backend/libpk_backend_test_spawn.so
/usr/lib64/packagekit-backend/libpk_backend_test_succeed.so
/usr/lib64/packagekit-backend/libpk_backend_test_thread.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/packagekit-direct
/usr/libexec/packagekitd
/usr/libexec/pk-command-not-found
/usr/libexec/pk-gstreamer-install
/usr/libexec/pk-offline-update

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PackageKit/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/PackageKit/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pkcon.1
/usr/share/man/man1/pkmon.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/system-update.target.wants/packagekit-offline-update.service
/usr/lib/systemd/system/packagekit-offline-update.service
/usr/lib/systemd/system/packagekit.service

%files locales -f PackageKit.lang
%defattr(-,root,root,-)

