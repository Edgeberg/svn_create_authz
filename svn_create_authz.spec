Name:    svn_create_authz
Version: 1
Release: 1%{?dist}
BuildArch: noarch
Summary: Create a Subversion authz file with group-based access from LDAP information

License: GPLv2+
Source0: svn_create_authz

%description
Creates a usable multi-repository Subversion authz file with group-based access from LDAP information.

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}

%files
%{_bindir}/svn_create_authz

%changelog
* Fri Sep 10 2021 Edgeberg <Edgeberg@outlook.com.au> - 1.0-1
- Initial RPM spec file
