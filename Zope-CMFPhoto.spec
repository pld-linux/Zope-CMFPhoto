%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFPhoto
Summary:	CMFPhoto - a Zope product with wrapper objects and a Plone skin for the Photo product
Summary(pl):	CMFPhoto - dodatek dla Zope umo¿liwiaj±cy operacje na obiektach i skórach w Plone
Name:		Zope-%{zope_subname}
Version:	0.3
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	1adfbc47d6ccccff38f64e3a3f8106fc
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF >= 1.3
Requires:	ImageMagick
Requires:	Zope-CMFPlone >= 1.0.1
Requires:	Zope >= 2.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

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
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af {Extensions,i18n,skins,*.py} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt
%{product_dir}/%{zope_subname}
