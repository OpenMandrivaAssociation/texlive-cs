%global tl_name cs
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Czech/Slovak-tuned Computer Modern fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/cstex/base/csfonts.tar.gz
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cs.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cmexb)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are provided as Metafont source; Type 1 format versions
(csfonts-t1) are also available.

