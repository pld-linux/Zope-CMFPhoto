%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFPhoto
Summary:	CMFPhoto - a Zope product with wrapper objects and a Plone skin for the Photo product
Summary(pl):	CMFPhoto - dodatek dla Zope umo¿liwiaj±cy operacje na obiektach i skórach w Plone
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	56f8fe2d79dbeae6d518a1bc1d55db30
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	CMF
Requires:	ImageMagick
Requires:	Plone
Requires:	Zope
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
%setup -q -c %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.txt
find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

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
%doc %{zope_subname}/*.txt
%{product_dir}/%{zope_subname}
