%global __os_install_post %{nil}

Name: harbour-openlara
Version: 1.0.0
Release: 1
Summary: OpenLara
License: BSD-2-Clause
Url: http://xproger.info/projects/OpenLara/
Source: %{name}-%{version}.tar.bz2
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(audioresource)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(keepalive-glib)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(wayland-client)

%description
OpenLara is an open-source re-implementation of Classic Tomb Raider game engine
NOTE: This requires the original game data i.e. the whole DATA and FMV folders to
be copied to $HOME/.local/share/harbour-openlara.

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if 0%{?_chum}
Title: OpenLara
Type: desktop-application
DeveloperName: Timur Gagiev
PackagedBy: Matti Lehtimäki
Categories:
 - Game
Custom:
  PackagingRepo: https://github.com/mlehtima/harbour-openlara
  Repo: https://github.com/XProger/OpenLara
PackageIcon: https://github.com/mlehtima/harbour-openlara/raw/master/rpm/harbour-openlara.svg
Screenshots:
 - https://github.com/mlehtima/harbour-openlara/raw/master/screenshots/screenshot1.png
 - https://github.com/mlehtima/harbour-openlara/raw/master/screenshots/screenshot2.png
Links:
  Bugtracker: https://github.com/mlehtima/harbour-openlara/issues
%endif

%prep
%autosetup %{name}-%{version}

%build
pushd src/platform/sdl2
%make_build -f Makefile.sailfish
popd

%install
pushd src/platform/sdl2
make install DESTDIR=%{?buildroot} -f Makefile.sailfish
popd

desktop-file-install --delete-original \
    --dir=%{buildroot}/%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root)%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*
