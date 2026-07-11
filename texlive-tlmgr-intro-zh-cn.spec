%global tl_name tlmgr-intro-zh-cn
%global tl_revision 59100

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A short tutorial on using tlmgr in Chinese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tlmgr-intro-zh-cn
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgr-intro-zh-cn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a Chinese translation of the tlmgr documentation. It introduces
some of the common usage of the TeX Live Manager. The original can be
found in the tlmgrbasics package.

