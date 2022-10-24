#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-azure_mgmt_core
Version  : 1.3.2
Release  : 14
URL      : https://files.pythonhosted.org/packages/ae/18/6f79cfddbf08f233de5a51961323c0b1b2174e06ae9460988091fd012043/azure-mgmt-core-1.3.2.zip
Source0  : https://files.pythonhosted.org/packages/ae/18/6f79cfddbf08f233de5a51961323c0b1b2174e06ae9460988091fd012043/azure-mgmt-core-1.3.2.zip
Summary  : Microsoft Azure Management Core Library for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-azure_mgmt_core-license = %{version}-%{release}
Requires: pypi-azure_mgmt_core-python = %{version}-%{release}
Requires: pypi-azure_mgmt_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(azure_core)

%description
# Azure Management Core Library
        
        Azure management core library defines extensions to Azure Core that are specific to ARM (Azure Resource Management) needed when you use client libraries.
        
        As an end user, you don't need to manually install azure-mgmt-core because it will be installed automatically when you install other SDKs.

%package license
Summary: license components for the pypi-azure_mgmt_core package.
Group: Default

%description license
license components for the pypi-azure_mgmt_core package.


%package python
Summary: python components for the pypi-azure_mgmt_core package.
Group: Default
Requires: pypi-azure_mgmt_core-python3 = %{version}-%{release}

%description python
python components for the pypi-azure_mgmt_core package.


%package python3
Summary: python3 components for the pypi-azure_mgmt_core package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_core)
Requires: pypi(azure_core)

%description python3
python3 components for the pypi-azure_mgmt_core package.


%prep
%setup -q -n azure-mgmt-core-1.3.2
cd %{_builddir}/azure-mgmt-core-1.3.2
pushd ..
cp -a azure-mgmt-core-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660230364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_core
cp %{_builddir}/azure-mgmt-core-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_core/579cbb785bfbb1c60b923fc50948313e74cb168c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-azure_mgmt_core/579cbb785bfbb1c60b923fc50948313e74cb168c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
