%global pypi_name sphinx-notfound-page
%global srcname sphinx_notfound_page
%global importname notfound
%global project_owner readthedocs
%global github_name sphinx-notfound-page
%global desc Create a custom 404 page with absolute URLs hardcoded

Name:           python-%{pypi_name}
Version:        0.6
Release:        2
Summary:        Create a custom 404 page with absolute URLs hardcoded

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}.tar.gz

# Fix compatibility with Sphinx 3.4
# Resolved upstream: https://github.com/readthedocs/sphinx-notfound-page/pull/127
Patch0:         sphinx-3.4-compatibility.patch
Patch1:         0001-fix-testcase-url-content-mismatch-error.patch

BuildArch:      noarch

%description
%desc

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python3-pytest
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=$PWD py.test-%{python3_version} -v .

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst docs
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{importname}/

%changelog
* Mon Jan 10 2021 Ge Wang <wangge20@huawei.com> - 0.6-2
- Fix testcase url content mismatch error

* Wed Jul 07 2021 wangdi <wangdi@kylinos.cn> - 0.6-1
- Init package

