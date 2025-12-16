%define module tomlkit

Name:		python-tomlkit
Version:	0.13.3
Release:	1
Summary:	Style preserving TOML library
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tomlkit/
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)

%description
Style preserving TOML library

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
