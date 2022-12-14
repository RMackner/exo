%global libliftoff_minver 0.2.0
%global _default_patch_fuzz 2

%define version_string 3.11.47

%define commit 2f95c0fa5d7d9a266a0d266f45e6c12be8ad4273
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global build_timestamp %(date +"%Y%m%d")
%global rel_build git.%{build_timestamp}.%{shortcommit}%{?dist}


Name:           gamescope
Version:        %{version_string}
Release:        %{rel_build}
Summary:        Micro-compositor for video games on Wayland

License:        BSD
URL:            https://github.com/Plagman/gamescope
Source0:        %{url}/archive/%{version}/master.tar.gz#/%{name}-master.tar.gz
# Create stb.pc to satisfy dependency('stb')
Source1:        stb.pc

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  (wlroots-devel >= 0.15.0 with wlroots-devel < 0.16)
BuildRequires:  libliftoff-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
BuildRequires:  /usr/bin/glslangValidator

# libliftoff hasn't bumped soname, but API/ABI has changed for 0.2.0 release
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

%description
%{name} is the micro-compositor optimized for running video games on Wayland.

%prep
%autosetup -n %{name}-%{version} -p1
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc


%build
export PKG_CONFIG_PATH=pkgconfig
%meson -Dpipewire=enabled -Dforce_fallback_for=[]
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/gamescope


%changelog
* Thu Feb 10 2022 Neal Gompa <ngompa@fedoraproject.org> - 3.11.9-1
- Rebase to 3.11.9

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.8.4-2
- Pin wlroots dependency to 0.13

* Sun Jul 04 2021 Neal Gompa <ngompa13@gmail.com> - 3.8.4-1
- Rebase to version 3.8.4
- Drop merged wlroots patch
- Backport patch for libliftoff 0.1.0 support
- Add explicit dependency on libliftoff >= 0.1.0

* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Add patch for wlroots 0.13.0 API changes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.7-2
- Rebuild for wlroots 0.12

* Sun Oct  4 15:56:25 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 3.7-1
- Initial packaging
