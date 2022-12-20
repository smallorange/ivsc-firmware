%global debug_package %{nil}

%global commit 29c5eff4cdaf83e90ef2dcd2035a9cdff6343430
%global commitdate 20221102
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Firmware for Intel iVSC
URL:            https://github.com/intel/ivsc-firmware
Version:        0.0
Release:        2.%{commitdate}git%{shortcommit}%{?dist}
License:        Proprietary

Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  systemd-rpm-macros

ExclusiveArch:  x86_64

%description
This provides the necessary firmware for Intel iVSC.

%prep

%setup -q -n %{name}-%{commit}

%build
# Nothing to build

%install
install -p -D -m 0644 firmware/ivsc_pkg_ovti5678_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti2740_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti9738_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti2740_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti02c1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_fw.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti01af_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti01a0_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti9734_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_hi556_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti01as_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti9738_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti5678_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti02c1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti01as_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_ovti01af_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_himx11b1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti9734_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_hi556_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_pkg_ovti01a0_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
install -p -D -m 0644 firmware/ivsc_skucfg_himx11b1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin

%files
#iVSC firmware
%license LICENSE
%dir %{_prefix}/lib/firmware/vsc
%dir %{_prefix}/lib/firmware/vsc/soc_a1_prod
%{_prefix}/lib/firmware/vsc/soc_a1_prod/*.bin

%changelog
* Tue Dec 20 2022 Kate Hsuan <hpa@redhat.com> - 0.0-2.20221102git29c5eff
- Style and format fixes.

* Tue Nov 15 2022 Kate Hsuan <hpa@redhat.com> - 0.0
- Firmware for Intel iVSC
