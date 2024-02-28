Name:		python-tomlkit
Version:	0.12.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
Summary:	Style preserving TOML library
URL:		https://pypi.org/project/tomlkit/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Style preserving TOML library

%prep
%autosetup -p1 -n tomlkit-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/tomlkit
%{py_sitedir}/tomlkit-*.dist-info
