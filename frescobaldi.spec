Summary:	LilyPond sheet music text editor for KDE4
Summary(pl.UTF-8):	Edytor arkuszy muzycznych LilyPond pod KDE4
Name:		frescobaldi
Version:	1.2.0
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://lilykde.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	e5dbc9425e3aae9890d54649b3d60166
URL:		http://www.frescobaldi.org/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	gettext-devel
BuildRequires:	lilypond
BuildRequires:	python-PyKDE4 >= 4.0.2
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	TiMidity++
Requires:	konsole >= 4.1.2
Requires:	okular >= 4.1.2
Requires:	lilypond
Requires:	python-PyKDE4 >= 4.0.2
Requires:	python-PyQt4 >= 4.4.3
Requires:	rumor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frescobaldi is a LilyPond sheet music text editor for KDE4. It aims to
be powerful, yet lightweight and easy to use.

%description -l pl.UTF-8
Edytor arkuszy muzycznych LilyPond pod KDE4. Ma być potężny, lecz
lekki i łatwy w użyciu.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/frescobaldi
%{_desktopdir}/kde4/frescobaldi.desktop
%{_datadir}/apps/frescobaldi
%{_iconsdir}/hicolor/scalable/apps/frescobaldi*
