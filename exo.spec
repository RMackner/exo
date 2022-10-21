%global xfceversion 4.17

Name:           exo
Version:        4.17.2
Release:        1%{?dist}
Summary:        Application library for the Xfce desktop environment

# libexo-hal exo-helper mount-notify and exo-mount are all GPLv2+
# everything else is LGPLv2+
License:        LGPLv2+ and GPLv2+
URL:            http://xfce.org/
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  perl-URI
BuildRequires:  glib2-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  libnotify-devel
BuildRequires:  intltool
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  make

%description
Extension library for Xfce, targeted at application development.

%package        devel
Summary:        Development tools for exo library

%description devel
Development tools and static libraries and header files for the exo library.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
 /usr/bin/exo-desktop-item-edit
   /usr/bin/exo-open
   /usr/include/exo-2/exo/exo-binding.h
   /usr/include/exo-2/exo/exo-cell-renderer-icon.h
   /usr/include/exo-2/exo/exo-config.h
   /usr/include/exo-2/exo/exo-enum-types.h
   /usr/include/exo-2/exo/exo-execute.h
   /usr/include/exo-2/exo/exo-gdk-pixbuf-extensions.h
   /usr/include/exo-2/exo/exo-gobject-extensions.h
   /usr/include/exo-2/exo/exo-gtk-extensions.h
   /usr/include/exo-2/exo/exo-icon-chooser-dialog.h
   /usr/include/exo-2/exo/exo-icon-chooser-model.h
   /usr/include/exo-2/exo/exo-icon-view.h
   /usr/include/exo-2/exo/exo-job.h
   /usr/include/exo-2/exo/exo-simple-job.h
   /usr/include/exo-2/exo/exo-string.h
   /usr/include/exo-2/exo/exo-thumbnail-preview.h
   /usr/include/exo-2/exo/exo-thumbnail.h
   /usr/include/exo-2/exo/exo-tree-view.h
   /usr/include/exo-2/exo/exo-utils.h
   /usr/include/exo-2/exo/exo.h
   /usr/lib/debug/usr/bin/exo-desktop-item-edit-4.17.2-1.fc3*
   /usr/lib/debug/usr/bin/exo-open-4.17.2-1.fc3*
   /usr/lib/debug/usr/lib64/libexo-2.so.0.1.0-4.17.2-1.fc3*
   /usr/lib64/libexo-2.so
   /usr/lib64/libexo-2.so.0
   /usr/lib64/libexo-2.so.0.1.0
   /usr/lib64/pkgconfig/exo-2.pc
   /usr/share/gtk-doc/html/exo-2/ExoCellRendererIcon.html
   /usr/share/gtk-doc/html/exo-2/ExoIconChooserDialog.html
   /usr/share/gtk-doc/html/exo-2/ExoIconView.html
   /usr/share/gtk-doc/html/exo-2/ExoJob.html
   /usr/share/gtk-doc/html/exo-2/ExoSimpleJob.html
   /usr/share/gtk-doc/html/exo-2/ExoTreeView.html
   /usr/share/gtk-doc/html/exo-2/ch01.html
   /usr/share/gtk-doc/html/exo-2/exo-2.devhelp2
   /usr/share/gtk-doc/html/exo-2/exo-Binding-Properties-Functions.html
   /usr/share/gtk-doc/html/exo-2/exo-Executing-Applications.html
   /usr/share/gtk-doc/html/exo-2/exo-Extensions-to-GObject.html
   /usr/share/gtk-doc/html/exo-2/exo-Extensions-to-Gtk.html
   /usr/share/gtk-doc/html/exo-2/exo-Extensions-to-gdk-pixbuf.html
   /usr/share/gtk-doc/html/exo-2/exo-Miscellaneous-Utility-Functions.html
   /usr/share/gtk-doc/html/exo-2/exo-String-Utility-Functions.html
   /usr/share/gtk-doc/html/exo-2/exo-Version-Information.html
   /usr/share/gtk-doc/html/exo-2/exo-cell-renderers.html
   /usr/share/gtk-doc/html/exo-2/exo-extensions.html
   /usr/share/gtk-doc/html/exo-2/exo-jobs.html
   /usr/share/gtk-doc/html/exo-2/exo-miscelleanous.html
   /usr/share/gtk-doc/html/exo-2/exo-overview.html
   /usr/share/gtk-doc/html/exo-2/exo-widgets.html
   /usr/share/gtk-doc/html/exo-2/home.png
   /usr/share/gtk-doc/html/exo-2/index.html
   /usr/share/gtk-doc/html/exo-2/ix15.html
   /usr/share/gtk-doc/html/exo-2/left-insensitive.png
   /usr/share/gtk-doc/html/exo-2/left.png
   /usr/share/gtk-doc/html/exo-2/right-insensitive.png
   /usr/share/gtk-doc/html/exo-2/right.png
   /usr/share/gtk-doc/html/exo-2/style.css
   /usr/share/gtk-doc/html/exo-2/up-insensitive.png
   /usr/share/gtk-doc/html/exo-2/up.png
   /usr/share/locale/am/LC_MESSAGES/exo.mo
   /usr/share/locale/ar/LC_MESSAGES/exo.mo
   /usr/share/locale/ast/LC_MESSAGES/exo.mo
   /usr/share/locale/az/LC_MESSAGES/exo.mo
   /usr/share/locale/az_AZ/LC_MESSAGES/exo.mo
   /usr/share/locale/be/LC_MESSAGES/exo.mo
   /usr/share/locale/bg/LC_MESSAGES/exo.mo
   /usr/share/locale/bn/LC_MESSAGES/exo.mo
   /usr/share/locale/ca/LC_MESSAGES/exo.mo
   /usr/share/locale/cs/LC_MESSAGES/exo.mo
   /usr/share/locale/da/LC_MESSAGES/exo.mo
   /usr/share/locale/de/LC_MESSAGES/exo.mo
   /usr/share/locale/el/LC_MESSAGES/exo.mo
   /usr/share/locale/en_AU/LC_MESSAGES/exo.mo
   /usr/share/locale/en_GB/LC_MESSAGES/exo.mo
   /usr/share/locale/es/LC_MESSAGES/exo.mo
   /usr/share/locale/et/LC_MESSAGES/exo.mo
   /usr/share/locale/eu/LC_MESSAGES/exo.mo
   /usr/share/locale/fa_IR/LC_MESSAGES/exo.mo
   /usr/share/locale/fi/LC_MESSAGES/exo.mo
   /usr/share/locale/fr/LC_MESSAGES/exo.mo
   /usr/share/locale/gl/LC_MESSAGES/exo.mo
   /usr/share/locale/he/LC_MESSAGES/exo.mo
   /usr/share/locale/hr/LC_MESSAGES/exo.mo
   /usr/share/locale/hu/LC_MESSAGES/exo.mo
   /usr/share/locale/hy/LC_MESSAGES/exo.mo
   /usr/share/locale/hy_AM/LC_MESSAGES/exo.mo
   /usr/share/locale/hye/LC_MESSAGES/exo.mo
   /usr/share/locale/id/LC_MESSAGES/exo.mo
   /usr/share/locale/ie/LC_MESSAGES/exo.mo
   /usr/share/locale/is/LC_MESSAGES/exo.mo
   /usr/share/locale/it/LC_MESSAGES/exo.mo
   /usr/share/locale/ja/LC_MESSAGES/exo.mo
   /usr/share/locale/kab/LC_MESSAGES/exo.mo
   /usr/share/locale/kk/LC_MESSAGES/exo.mo
   /usr/share/locale/kn/LC_MESSAGES/exo.mo
   /usr/share/locale/ko/LC_MESSAGES/exo.mo
   /usr/share/locale/lt/LC_MESSAGES/exo.mo
   /usr/share/locale/lv/LC_MESSAGES/exo.mo
   /usr/share/locale/ms/LC_MESSAGES/exo.mo
   /usr/share/locale/nb/LC_MESSAGES/exo.mo
   /usr/share/locale/nl/LC_MESSAGES/exo.mo
   /usr/share/locale/nn/LC_MESSAGES/exo.mo
   /usr/share/locale/oc/LC_MESSAGES/exo.mo
   /usr/share/locale/pa/LC_MESSAGES/exo.mo
   /usr/share/locale/pl/LC_MESSAGES/exo.mo
   /usr/share/locale/pt/LC_MESSAGES/exo.mo
   /usr/share/locale/pt_BR/LC_MESSAGES/exo.mo
   /usr/share/locale/ro/LC_MESSAGES/exo.mo
   /usr/share/locale/ru/LC_MESSAGES/exo.mo
   /usr/share/locale/si/LC_MESSAGES/exo.mo
   /usr/share/locale/sk/LC_MESSAGES/exo.mo
   /usr/share/locale/sl/LC_MESSAGES/exo.mo
   /usr/share/locale/sq/LC_MESSAGES/exo.mo
   /usr/share/locale/sr/LC_MESSAGES/exo.mo
   /usr/share/locale/sv/LC_MESSAGES/exo.mo
   /usr/share/locale/te/LC_MESSAGES/exo.mo
   /usr/share/locale/th/LC_MESSAGES/exo.mo
   /usr/share/locale/tr/LC_MESSAGES/exo.mo
   /usr/share/locale/ug/LC_MESSAGES/exo.mo
   /usr/share/locale/uk/LC_MESSAGES/exo.mo
   /usr/share/locale/ur/LC_MESSAGES/exo.mo
   /usr/share/locale/ur_PK/LC_MESSAGES/exo.mo
   /usr/share/locale/vi/LC_MESSAGES/exo.mo
   /usr/share/locale/zh_CN/LC_MESSAGES/exo.mo
   /usr/share/locale/zh_HK/LC_MESSAGES/exo.mo
   /usr/share/locale/zh_TW/LC_MESSAGES/exo.mo
   /usr/share/man/man1/exo-open.1.gz
   /usr/share/pixmaps/exo/exo-thumbnail-frame.png
   
%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/exo*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc



%changelog
* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.11-1
- Update to 0.2.11

* Tue Nov 26 2019 Kevin Fenzi <kevin@scrye.com> - 0.12.10-1
- Update to 0.12.10. Fixes bug #1775330

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.8-1
- Update to 0.12.8

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.12.7-2
- rebuild for xfce 4.14pre3

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.7-1
- Update to 0.12.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.6-2
- Rebuild for libxfce4util and libxfce4ui
- Add gobject-introspection-devel as BR

* Thu Jun 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.6-1
- Update to 0.12.6

* Wed May 01 2019 Kevin Fenzi <kevin@scrye.com> - 0.12.5-1
- Update to 0.12.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.4-1
- Update to 0.12.4

* Tue Oct 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.3-1
- Update to 0.12.3

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.2-20
- rebuild for xfce version 4.13

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Mon Jun 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon May 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.0-4
- Add BR:gcc-c++

* Sat Mar 03 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.0-3
- Explicitly list shared libraries

* Sun Feb 25 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.0-2
- Drop everything python-exo
- use ldconfig_scriptlets

* Fri Feb 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0
- Spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro HronÄok <mhroncok@redhat.com> - 0.10.7-4
- Rebuild for Python 3.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Miro HronÄok <mhroncok@redhat.com> - 0.10.7-2
- Port mailtoparse to Python 3 (#1282165)

* Mon Sep 14 2015 Mukundan Ragavan <nonamedotc@gmail.com> - 0.10.7-1
- Updated to 0.10.7
- Removed upstreamed missing URI patch

* Fri Jul 31 2015 Kevin Fenzi <kevin@scrye.com> 0.10.6-4
- Add patch to fix %%20's in uris. Fixes bug #1246383

* Thu Jun 25 2015 Kevin Fenzi <kevin@scrye.com> 0.10.6-3
- Fix mailtoparse for thunderbird and other cases. Fixes bug #1227021

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Kevin Fenzi <kevin@scrye.com> 0.10.6-1
- Update to 0.10.6
- Fixes bug #1217807

* Tue Mar 17 2015 Kevin Fenzi <kevin@scrye.com> 0.10.4-1
- Update to 0.10.4 with various bugfixes

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.3-1
- Update to 0.10.3
- Remove upstreamed patches

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.10.2-9
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Kevin Fenzi <kevin@scrye.com> 0.10.2-5
- Add patch to fix magnet links. Fixes bug #887457

* Sat May 18 2013 Kevin Fenzi <kevin@scrye.com> 0.10.2-4
- Set default browser to midori and default mail app to claws-mail to match our groups

* Fri May 10 2013 Kevin Fenzi <kevin@scrye.com> 0.10.2-3
- Replace upstream perl script for mail handler with python version. 
- https://bugzilla.xfce.org/show_bug.cgi?id=9964

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Kevin Fenzi <kevin@scrye.com> 0.10.2-1
- Update to 0.10.2
- Fix changelog dates. 

* Sun Dec 09 2012 Kevin Fenzi <kevin@scrye.com> 0.10.1-1
- Update to 0.10.1

* Tue Dec 04 2012 Kevin Fenzi <kevin@scrye.com> 0.10.0-1
- Update to 0.10.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 (Xfce 4.10 final)
- Make build verbose
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.3-1
- Update to 0.7.3 (Xfce 4.10pre2)

* Sun Apr 01 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.2-1
- Update to 0.7.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-3
- Add Thunar as default file manager (#748277)

* Thu Jul 21 2011 Orion Poplawski <orion@cora.nwra.com> - 0.6.2-2
- Don't run gio-quuerymodules on post in EL6 (bug #722335)

* Fri Jun 10 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Thu May 19 2011 Orion Poplawski <orion@cora.nwra.com> - 0.6.1-2
- EL6 does not have gio-querymodules

* Mon May 09 2011 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1

* Sun May 08 2011 Kevin Fenzi <kevin@scrye.com> - 0.6.0-6
- Add patch to remove mime types from desktop files. 
- Fixes bug #674321

- https://bugzilla.xfce.org/show_bug.cgi?id=7257
* Tue Apr 26 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-5
- Remove the hal-devel BuildRequires, too

* Sat Apr 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-4
- exo-devel no longer requires hal-devel

* Sat Apr 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-3
- Add xfce4-mail icon for exo-mail-reader (#678706)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Kevin Fenzi <kevin@tummy.com> - 0.6.0-1
- Update to 0.6.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6
- Drop obsolete BR for dbus-glib

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5
- Fix directory ownership
- Run gio-querymodules to update giomodule.cache

* Sun Nov 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Fri Nov 05 2010 Kevin Fenzi <kevin@tummy.com> - 0.3.107-5
- Rebuild for new libnotify

* Mon Aug 23 2010 Kevin Fenzi <kevin@tummy.com> - 0.3.107-4
- Remove unneeded gtk-doc dep. Fixes bug #604350

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.107-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 07 2010 Kevin Fenzi <kevin@tummy.com> - 0.3.107-2
- Drop patch1 as it doublefixed bug 6230

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 0.3.107-1
- Update to 0.3.107

* Sat Apr 24 2010 Kevin Fenzi <kevin@tummy.com> - 0.3.106-3
- Add patch for xfce bug 6230

* Thu Dec 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.106-2
- Remove libtool archive from python-exo package

* Thu Dec 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.106-1
- Update to 0.3.106
- Remove upstreamed sync patch

* Mon Oct 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.105-1
- Update to 0.3.105
- Tweak mount.rc to use UTF-8 (to not bring back #508823 again)

* Sat Oct 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.104-1
- Update to 0.3.104

* Sat Oct 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.103-2
- Disable parallel make due to multilib conflicts.

* Sat Oct 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.103-1
- Update to 0.3.103
- Drop patches for URL quoting and default mount options (fixed upstream)
- Revert useless touch -r trick

* Wed Sep 30 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.101-5
- Use touch -r trick to fix multilib issue

* Thu Sep 10 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.101-4
- Mount vfat and ntfs volumes with UTF-8 (#508823)
- Mount ntfs with ntfs-3g

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.101-2
- Add patch to fix url quoting (bug #509730)

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.101-1
- Update to 0.3.101

* Mon Mar 02 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.100-2
- Fix directory ownership problems
- Move exo-csource into devel package
- Make devel package require pkgconfig and gtk-doc
- Mark gtk-doc files as %%doc

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.100-1
- Update to 0.3.100
- Remove some unneeded BuildRequires

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.99.1-1
- Update to 0.3.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> 0.3.93-1
- Update to 0.3.93

* Tue Dec 23 2008 Kevin Fenzi <kevin@tummy.com> 0.3.92-1
- Update to 0.3.92

* Tue Dec 16 2008 Kevin Fenzi <kevin@tummy.com> 0.3.4-5
- Add hal-devel Requires to devel package. 

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.4-4
- Rebuild for Python 2.6

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.4-3
- Add two Debian patches to fix broken regex and gcc_hardening
- Fix rpm group
- Update gtk-update-icon-cache scriptlets
- Configure with --disable-static

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 0.3.4-2
- Rebuild for gcc43

* Sun Dec  2 2007 Kevin Fenzi <kevin@tummy.com> - 0.3.4-1
- Update to 0.3.4

* Tue Aug 21 2007 Kevin Fenzi <kevin@tummy.com> - 0.3-2-3
- Update license tag. 

* Thu Feb  8 2007 Kevin Fenzi <kevin@tummy.com> - 0.3.2-2
- Add hal-devel and libnotify-devel BuildRequires. Fixes #225135

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 0.3.2-1
- Upgrade to 0.3.2

* Fri Dec  8 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.12-0.3.rc2
- Rebuild for new python

* Thu Nov 16 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.12-0.2.rc2
- Rebuild with fixed xfce-mcs-manager-devel
- Add exo-preferred-applicatons-settings.so

* Thu Nov  9 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.12-0.1.rc2
- Update to 0.3.1.12rc2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.10-0.6.rc1
- Added libxfce4util-devel Requires for the devel package

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.10-0.5.rc1
- Added gtk-update-icon-cache

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.10-0.4.rc1
- Bump release for devel checkin

* Thu Sep 28 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.10-0.3.rc1
- Remove libxfce4gui/libxfce4gui-devel Requires/BuildRequires

* Thu Sep  7 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.10-0.1.rc1
- Upgrade to 0.3.1.10-0.1.rc1

* Tue Aug 29 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.8-0.3.beta2
- Add perl-URI BuildRequires

* Wed Aug  2 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.8-0.1.beta2
- Fix release numbering
- General cleanup for devel push
- Mark helpers.rc as a configfile

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.8-0.beta2
- Upgrade to 0.3.1.8beta2
- Removed unneeded patch

* Mon May  8 2006 Kevin Fenzi <kevin@tummy.com> - 0.3.1.6beta1
- Upgrade to 0.3.1.6beta1

* Sat Jan 21 2006 Kevin Fenzi <kevin@scrye.com> - 0.3.0-11.fc5
- Add imake to BR to allow detection of modular xorg

* Wed Aug 17 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-10.fc5
- Rebuild for new libcairo and libpixman

* Fri Jul  1 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-9.fc5
- Bump release for a new build

* Mon Jun 20 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-8.fc5
- Add patch to make x86_64 package build

* Thu Jun  2 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-7.fc5
- Change python_sitelib to python_sitearch

* Tue May 31 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-6
- Add python_sitelib to build on x86_64
- Add dist to release

* Tue May 31 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-5
- Add python-devel buildrequires

* Mon May 30 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-4
- Fixed exo gtk-doc directory not being included in devel
- Changed pygtk defs dir 
- Added Requires to devel for pkg-config dependency

* Mon May 30 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-3
- Added gettext to buildrequires
- Moved devel docs to devel package only
- Added find_lang for locale files
- Added more docs to base package

* Fri May 27 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-2
- Added lang to files
- Fixed some file paths
- Remove unneeded la files
- Added pygtk2-devel buildrequires

* Sat Mar 19 2005 Kevin Fenzi <kevin@tummy.com> - 0.3.0-1
- Upgraded to 0.3.0 version

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.0-3
- Removed generic INSTALL doc from %%doc

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 0.2.0-2
- Inital Fedora Extras version
