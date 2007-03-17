Summary:	RPM Dependency Tracker
Name:		InDependence
Version:	1.0
Release:	1
Group:		Applications/System
Source0:	%{name}_%{version}.tar.gz
# Source0-md5:	df419e1443683305891060985f723902
Patch0:		%{name}-rpmlib.patch
License:	Artistic License
URL:		http://www.cse.ogi.edu/DISC/projects/independence/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
InDependence is a suite of tools (well two :-) designed to help RPM
packagers and system administrators deal with the dependencies between
RPM packages. InDependence has two major components:

Dep: This tool is for the RPM packager that identifies external files
or RPM packages that a program uses.

RPMTC: "RPM Transitive Closure". This tool is for the RPM system
administrator. "rpmtc foo.rpm" will transitively compute the -
- *entire* set of RPMs necessary to support the foo.rpm package, i.e.
  if foo.rpm depends on bar.rpm, and bar.rpm depends on baz.rpm, RPMTC
  will report both bar and baz.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}
install dep/dep ${RPM_BUILD_ROOT}%{_bindir}/dep
install dep/swrapper.pl ${RPM_BUILD_ROOT}%{_bindir}/swrapper.pl
install rpmtc/rpmtc ${RPM_BUILD_ROOT}%{_bindir}/rpmtc
install rpmtc/rpmdep-pipe ${RPM_BUILD_ROOT}%{_bindir}/rpmdep-pipe
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install dep/dep.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/dep.1
install rpmtc/rpmtc.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/rpmtc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dep
%attr(755,root,root) %{_bindir}/rpmdep-pipe
%attr(755,root,root) %{_bindir}/rpmtc
%attr(755,root,root) %{_bindir}/swrapper.pl
%{_mandir}/man1/dep.1*
%{_mandir}/man1/rpmtc.1*
