%define		zope_subname	CMFPhoto
%define		sub_ver rc2
Summary:	A Zope product with wrapper objects and a Plone skin for the Photo product
Summary(pl):	Dodatek dla Zope umo¿liwiaj±cy operacje na obiektach i skórach w Plone
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	0.%{sub_ver}.3
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}%{sub_ver}.tar.gz
# Source0-md5:	b175ab4acf27fde98c61c03698ed1cbf
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope-CMF >= 1:1.4
Requires:	ImageMagick
Requires:	Zope-CMFPlone >= 1.0.1
Requires:	Zope >= 2.6.1
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%description
CMFPhoto is a Zope product with wrapper objects and a Plone skin for
the Photo product.

%description -l pl
CMFPhoto jest dodatkiem dla Zope umo¿liwiaj±cym operacje na obiektach
i skórach w Plone.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt
%{_datadir}/%{name}
