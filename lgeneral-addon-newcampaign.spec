Summary:	LGeneral game - Gerold Treitler's new campaign for Panzer General
Summary(pl.UTF-8):	Gra Linux General - nowa kampania Gerolda Treitlera dla gry Panzer General
Name:		lgeneral-addon-newcampaign
Version:	20110830
Release:	1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/newcampaign.zip
# Source0-md5:	355fc59a7be63f0a23f97b08e70a53b6
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
Requires:	lgeneral-data-pg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Gerold Treitler's new campaign for
Panzer General. A bit unpolished, since the victory conditions might
be weird.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera nową kampanię Gerolda Treitlera dla gry Panzer
General. Jest nieco niewygładzona, jako że warunki zwycięstwa mogą być
dziwne.

%prep
%setup -q -n NewCampaign

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a campaigns gfx scenarios $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HOWTO.txt README.txt changelog.txt DOC
%{_datadir}/lgeneral/campaigns/NewCampaign
%{_datadir}/lgeneral/gfx/units/newcampaign.bmp
%{_datadir}/lgeneral/scenarios/NewCampaign
