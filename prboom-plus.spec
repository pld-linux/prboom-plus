Summary:	PrBoom-Plus - a modified PrBoom port
Name:		prboom-plus
Version:	2.5.0.8a
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/prboom-plus/%{name}-%{version}.tar.gz
# Source0-md5:	caf135fb2f0fb1a6c91d006ec62f76e7
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://prboom-plus.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	SDL_net-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	smpeg-devel
Obsoletes:	lsdldoom
Obsoletes:	lxdoom
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PrBoom-Plus is a modified PrBoom port with uncapped framerate,
variable gamespeed, re-record, walkcam, chasecam, full mouselook, FOV,
and other features without loss of compatibility with the original
Doom.

Note that some orignal game files are required to use PrBoom-Plus.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* autotools
%{__aclocal} -I autotools
%{__autoconf}
%{__automake}
%configure \
	--disable-cpu-opt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc/{*.txt,README*}
%attr(755,root,root) %{_bindir}/prboom-plus*
%{_datadir}/games/doom
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
