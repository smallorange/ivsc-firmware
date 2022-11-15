%global debug_package %{nil}

%global commit 29c5eff4cdaf83e90ef2dcd2035a9cdff6343430
%global commitdate 20221102
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Binaries firmware for Intel iVSC
Version:        0.0
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
License:        Proprietory

Source0: https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}-%{release}

ExclusiveArch:  x86_64

%description
This provides the necessary binaries for Intel iVSC.

This package contains the binary firmware for %{name}.

%prep

%setup -q -c
cp %{name}-%{commit}/LICENSE ./

%build
# Nothing to build

%install
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti5678_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti2740_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti9738_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti2740_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti02c1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_fw.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti01af_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti01a0_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti9734_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_hi556_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti01as_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti9738_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti5678_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti02c1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti01as_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_ovti01af_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_himx11b1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti9734_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_hi556_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_pkg_ovti01a0_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
install -D -m 0644 %{name}-%{commit}/firmware/ivsc_skucfg_himx11b1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin

%files
#iVSC firmware
%license LICENSE
%{_prefix}/lib/firmware/vsc/soc_a1_prod/*.bin

%changelog
* Tue Nov 15 2022 Kate Hsuan <hpa@redhat.com> - 0.0
- First commit
