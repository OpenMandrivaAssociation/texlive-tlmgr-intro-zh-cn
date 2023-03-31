Name:		texlive-tlmgr-intro-zh-cn
Version:	59100
Release:	2
Summary:	A short tutorial on using tlmgr in Chinese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tlmgr-intro-zh-cn
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a Chinese translation of the tlmgr documentation. It
introduces some of the common usage of the TeX Live Manager.
The original can be found in the tlmgrbasics package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/tlmgr-intro-zh-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
