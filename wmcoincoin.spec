%define name	wmcoincoin
%define Summary	WindowMaker dock application for linuxfr-addicted people
%define version	2.5.1
%define pre	d
%define release	%mkrel 0.%{pre}.2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/dacode/%{name}-%{version}%{pre}.tar.bz2
Source11:	%{name}-icon-16.png
Source12:	%{name}-icon-32.png
Source13:	%{name}-icon-48.png
URL:		http://hules.free.fr/wmcoincoin/wmcoincoin.html
Group:		Networking/Chat
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	imlib2-devel
BuildRequires:	freetype-devel

%description
Funny dockapp for browsing DaCode sites news and board
WMcoincoin allows you to browse linuxfr.org, and any other site based
on DaCode 1.2+. It handles:

* the website news scrolling, warning of new ones, and with an ability
  to display them in a window;
* the private messages, bringing to the appropriate webpage when you
  receive new ones;
* tabbed browsing of multiple DaCode or Templeet sites;
* the board, with ability to view the contents and post messages,
  featuring advanced functions designed to detect, enhance or kill
  the trolls.
  
WMcoincoin, while being full of stupid things, is a real advanced
chatting client, working all over HTTP, with a low bandwidth
consumption.


%description -l fr
La fonctionnalité centrale (le gros bouton rouge), permet de poster "coin
coin!" sur la tribune libre. Autour de ce bouton, différentes fonctionnalités
annexes gravitent:
* Affichage de l'heure du dernier post sur la tribune
* Affichage défilant des titres des dernières news de DaLinuxFrenchPage
  Visionnage du contenu des news (sans les commentaires)
* Trollometre incorporé, de qualité professionnelle.
* Un véritable Trolloscope d'un modèle proche de celui qui équipe les services
  secrets chinois.
* Des ballons d'aide pour toujours plus de convivialité.
* Des stats sur le nombre de personnes qui fréquentent la tribune.
* Le Palmipède Editor qui permet d'éditer le messages/useragent à poster avec
  un confort maximal.
* Une fonction flamophone, parce que vous le valez bien.
* Le Pinnipède Télétype, un véritable outil de décideur.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%configure
%make

%install
rm -rf %{buildroot}
perl -pi -e 's/README\ wmcoincoin.spec//' Makefile

%makeinstall
%find_lang %{name}

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Wmcoincoin
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;X-MandrivaLinux-Internet-Chat;
Encoding=UTF-8
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

