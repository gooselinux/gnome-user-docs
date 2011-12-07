Summary:        GNOME User Documentation
Name:           gnome-user-docs
Version:        2.28.0
Release:        4%{?dist}
License:        GFDL
Source:         http://download.gnome.org/sources/gnome-user-docs/2.28/gnome-user-docs-%{version}.tar.bz2
URL:            http://www.gnome.org
Group:          Documentation

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): scrollkeeper >= 0.3.11
Requires(postun): scrollkeeper >= 0.3.11
BuildRequires: scrollkeeper >= 0.3.11
BuildRequires: gnome-doc-utils >= 0.5.6
BuildRequires: pkgconfig
BuildRequires: gettext

%description
This package contains end user documentation for the GNOME desktop
environment.

%prep
%setup -q -n gnome-user-docs-%{version}

%build
%configure --disable-scrollkeeper
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
scrollkeeper-update
exit 0

%postun
scrollkeeper-update
exit 0

%files -f %{name}.lang
%defattr(-, root, root,-)
%doc COPYING COPYING-DOCS
%dir %{_datadir}/omf/user-guide
%dir %{_datadir}/omf/system-admin-guide
%dir %{_datadir}/omf/gnome-access-guide

%changelog
* Wed Feb 24 2010 Ray Strode <rstrode@redhat.com> 2.28.0-4
Resolves: #560000
- Add licenses to %%doc

* Tue Feb 23 2010 Ray Strode <rstrode@redhat.com> 2.28.0-3
Resolves: #560000
- Drop gnome-users-guide obsoletes.  It's obsolete

* Fri Jan 29 2010 Ray Strode <rstrode@redhat.com> 2.28.0-2
Resolves: #560000
- Spec file clean up

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-1
- Update to 2.27.2

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-1
- Update to 2.27.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.22.0-2
- fix license tag

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Fri Oct 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1 (Accessibility guide updates and updated translations)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.2-2
- Update the license field
- Use %%find_lang

* Mon Jul  2 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.2-1
- Update to 2.18.2

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Fri Sep  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-2
- Fix directory ownership issues

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.1-1.fc6
- Update to 2.15.1

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> 2.14.2-4
- Add more BuildRequires

* Mon Jun  5 2006 Matthias Clasen <mclasen@redhat.com> 2.14.2-3
- Fix BuildRequires

* Tue Apr 11 2006 Matthias Clasen <mclasen@redhat.com> 2.14.2-2
- Update to 2.14.2

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> 2.14.1-2
- Update to 2.14.1

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> 2.14.0-1
- Update to 2.14.0

* Wed Mar 8 2006 Ray Strode <rstrode@redhat.com> 2.13.1.1-2
- PreReq instead of Requires scrollkeeper.  Reported by
  Bill Nottingham

* Tue Feb 21 2006 Matthias Clasen <mclasen@redhat.com> 2.13.1.1-1
- Update to 2.13.1.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov  6 2004 Marco Pesenti Gritti <mpg@redhat.com> 2.8.1-2
- Remove the section about menu editing. Fix 134119

* Mon Oct 25 2004 Christopher Aillon <caillon@redhat.com> 2.8.1-1
- Update to 2.8.1

* Wed Sep 22 2004 Christopher Aillon <caillon@redhat.com> 2.8.0.1-1
- Update to 2.8.0-1

* Tue Apr 13 2004 Warren Togami <wtogami@redhat.com> 2.6.0.1-2
- BR scrollkeeper

* Fri Apr  2 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0.1-1
- Update to 2.6.0.1

* Mon Mar 15 2004 Alex Larsson <alexl@redhat.com> 2.5.90-1
- update to 2.5.90

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 2.5.0-1
- update to 2.5.0

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 30 2004 Alexander Larsson <alexl@redhat.com> 2.4.1-1
- update to 2.4.1

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- add introduction-to-gnome.xml from CVS so the XML won't be broken

* Fri Dec 13 2002 Tim Powers <timp@redhat.com> 2.0.1-1
- update to 2.0.1

* Thu Aug  8 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0 stable release
- clean up uninstalled file warnings
- blow build root at start of install

* Mon Jun 24 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.93, should fix #67207

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Havoc Pennington <hp@redhat.com>
- prereq scrollkeeper

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- upgrade to gnome 2 docs
- clean up the spec file a bit

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in different environment

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix a scrollkeeper validation bug

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild


* Tue Apr 17 2001 Jonathan Blandford <jrb@redhat.com>
- Moved to red hat build system

* Thu Feb 22 2001 Gregory Leblanc <gleblanc@cu-portland.edu>
- de-uglification, and fixed the macros.

* Mon Nov 27 2000 Kenny Graunke <kwg@teleport.com>
- Initial cut
