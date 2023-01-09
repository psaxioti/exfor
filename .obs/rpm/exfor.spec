%define my_inst_dir /opt/EXFOR

%define dashed_version %(echo %{version} | sed "s|\\.|\\-|g")

Name:           exfor
Version:        2021.11.10
Release:        0
Summary:        EXFOR in C4 format
License:        GPL-3.0
Group:          Productivity/Scientific/Physics
Url:            https://www-nds.iaea.org/public/exfor/x4toc4/

Source0:        https://www-nds.iaea.org/public/exfor/x4toc4/C4-2021-11-10.zip
Source1:        exfor_extract

BuildArch:      noarch

BuildRequires:  unzip

%description
EXFOR in C4 format for usage

%package	c4
Summary:        EXFOR in C4 format
BuildArch:      noarch
%description	c4
EXFOR in C4 format for usage

%package	dat
Summary:        EXFOR in ASCII format
BuildArch:      noarch
%description	dat
EXFOR in ASCII format extracted from the C4

%prep

%build

%install
mkdir -p %{buildroot}%{my_inst_dir}/data

install -Dm755  %{SOURCE1} %{buildroot}%{_bindir}/exfor_extract
unzip -qq %{_sourcedir}/C4-%{dashed_version}.zip -d %{buildroot}%{my_inst_dir}/C4all
chmod 775 %{SOURCE1}
%{SOURCE1} --exfor_dir="%{buildroot}%{my_inst_dir}/C4all" --data_dir="%{buildroot}%{my_inst_dir}/data" --reaction=*\(\[ap\],g\)
%{SOURCE1} --exfor_dir="%{buildroot}%{my_inst_dir}/C4all" --data_dir="%{buildroot}%{my_inst_dir}/data" --reaction=*\(g,\[ap\]\)
%{SOURCE1} --exfor_dir="%{buildroot}%{my_inst_dir}/C4all" --data_dir="%{buildroot}%{my_inst_dir}/data" --reaction=*\(a,el\)

%files		c4
%{_bindir}/exfor_extract
%dir %{my_inst_dir}
%dir %{my_inst_dir}/C4all
%{my_inst_dir}/C4all/*

%files		dat
%dir %{my_inst_dir}
%dir %{my_inst_dir}/data
%{my_inst_dir}/data/*
