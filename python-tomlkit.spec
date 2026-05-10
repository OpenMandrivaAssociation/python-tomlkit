%define module tomlkit
%bcond tests 1

Name:		python-tomlkit
Version:	0.15.0
Release:	1
Summary:	Style preserving TOML library
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tomlkit/
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyyaml)
%endif

%description
Style preserving TOML library

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
