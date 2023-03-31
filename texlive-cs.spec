Name:		texlive-cs
Version:	41553
Release:	2
Summary:	Czech/Slovak-tuned Computer Modern fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex/base/csfonts.tar.gz
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cs.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The fonts are provided as Metafont source; Type 1 format
versions (csfonts-t1) are also available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/cs/xl2.enc
%{_texmfdistdir}/fonts/enc/dvips/cs/xl2f.enc
%{_texmfdistdir}/fonts/enc/dvips/cs/xt2.enc
%{_texmfdistdir}/fonts/map/dvips/cs/cs-a35-nodownload.map
%{_texmfdistdir}/fonts/map/dvips/cs/cs-a35-urwdownload.map
%{_texmfdistdir}/fonts/map/dvips/cs/cs-charter.map
%{_texmfdistdir}/fonts/map/dvips/cs/csfonts.map
%{_texmfdistdir}/fonts/source/public/cs/csaccent.mf
%{_texmfdistdir}/fonts/source/public/cs/csacutl.mf
%{_texmfdistdir}/fonts/source/public/cs/csacutu.mf
%{_texmfdistdir}/fonts/source/public/cs/csadded.mf
%{_texmfdistdir}/fonts/source/public/cs/csb10.mf
%{_texmfdistdir}/fonts/source/public/cs/csb12.mf
%{_texmfdistdir}/fonts/source/public/cs/csb17.mf
%{_texmfdistdir}/fonts/source/public/cs/csb5.mf
%{_texmfdistdir}/fonts/source/public/cs/csb6.mf
%{_texmfdistdir}/fonts/source/public/cs/csb7.mf
%{_texmfdistdir}/fonts/source/public/cs/csb8.mf
%{_texmfdistdir}/fonts/source/public/cs/csb9.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx10.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx12.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx5.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx6.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx7.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx8.mf
%{_texmfdistdir}/fonts/source/public/cs/csbx9.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl10.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl12.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl5.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl6.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl7.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl8.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxsl9.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxti10.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxti12.mf
%{_texmfdistdir}/fonts/source/public/cs/csbxti17.mf
%{_texmfdistdir}/fonts/source/public/cs/cscode.mf
%{_texmfdistdir}/fonts/source/public/cs/cscsc10.mf
%{_texmfdistdir}/fonts/source/public/cs/cscsc12.mf
%{_texmfdistdir}/fonts/source/public/cs/cscsc17.mf
%{_texmfdistdir}/fonts/source/public/cs/cscsc8.mf
%{_texmfdistdir}/fonts/source/public/cs/cscsc9.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh10.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh12.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh17.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh5.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh6.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh7.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh8.mf
%{_texmfdistdir}/fonts/source/public/cs/csdunh9.mf
%{_texmfdistdir}/fonts/source/public/cs/csff10.mf
%{_texmfdistdir}/fonts/source/public/cs/csfi10.mf
%{_texmfdistdir}/fonts/source/public/cs/csfib10.mf
%{_texmfdistdir}/fonts/source/public/cs/csfib12.mf
%{_texmfdistdir}/fonts/source/public/cs/csfib8.mf
%{_texmfdistdir}/fonts/source/public/cs/csfib9.mf
%{_texmfdistdir}/fonts/source/public/cs/cshachel.mf
%{_texmfdistdir}/fonts/source/public/cs/cshacheu.mf
%{_texmfdistdir}/fonts/source/public/cs/cshyph.mf
%{_texmfdistdir}/fonts/source/public/cs/csiacutl.mf
%{_texmfdistdir}/fonts/source/public/cs/csihachl.mf
%{_texmfdistdir}/fonts/source/public/cs/csinch.mf
%{_texmfdistdir}/fonts/source/public/cs/csiothrl.mf
%{_texmfdistdir}/fonts/source/public/cs/csitt10.mf
%{_texmfdistdir}/fonts/source/public/cs/csitt12.mf
%{_texmfdistdir}/fonts/source/public/cs/csitt17.mf
%{_texmfdistdir}/fonts/source/public/cs/csitt8.mf
%{_texmfdistdir}/fonts/source/public/cs/csitt9.mf
%{_texmfdistdir}/fonts/source/public/cs/csotherl.mf
%{_texmfdistdir}/fonts/source/public/cs/csotheru.mf
%{_texmfdistdir}/fonts/source/public/cs/csr10.mf
%{_texmfdistdir}/fonts/source/public/cs/csr12.mf
%{_texmfdistdir}/fonts/source/public/cs/csr17.mf
%{_texmfdistdir}/fonts/source/public/cs/csr5.mf
%{_texmfdistdir}/fonts/source/public/cs/csr6.mf
%{_texmfdistdir}/fonts/source/public/cs/csr7.mf
%{_texmfdistdir}/fonts/source/public/cs/csr8.mf
%{_texmfdistdir}/fonts/source/public/cs/csr9.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl10.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl12.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl17.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl5.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl6.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl7.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl8.mf
%{_texmfdistdir}/fonts/source/public/cs/cssl9.mf
%{_texmfdistdir}/fonts/source/public/cs/cssltt10.mf
%{_texmfdistdir}/fonts/source/public/cs/cssltt12.mf
%{_texmfdistdir}/fonts/source/public/cs/cssltt8.mf
%{_texmfdistdir}/fonts/source/public/cs/cssltt9.mf
%{_texmfdistdir}/fonts/source/public/cs/csss10.mf
%{_texmfdistdir}/fonts/source/public/cs/csss12.mf
%{_texmfdistdir}/fonts/source/public/cs/csss17.mf
%{_texmfdistdir}/fonts/source/public/cs/csss8.mf
%{_texmfdistdir}/fonts/source/public/cs/csss9.mf
%{_texmfdistdir}/fonts/source/public/cs/csssbx10.mf
%{_texmfdistdir}/fonts/source/public/cs/csssbx12.mf
%{_texmfdistdir}/fonts/source/public/cs/csssbx17.mf
%{_texmfdistdir}/fonts/source/public/cs/csssbx9.mf
%{_texmfdistdir}/fonts/source/public/cs/csssdc10.mf
%{_texmfdistdir}/fonts/source/public/cs/csssi10.mf
%{_texmfdistdir}/fonts/source/public/cs/csssi12.mf
%{_texmfdistdir}/fonts/source/public/cs/csssi17.mf
%{_texmfdistdir}/fonts/source/public/cs/csssi8.mf
%{_texmfdistdir}/fonts/source/public/cs/csssi9.mf
%{_texmfdistdir}/fonts/source/public/cs/csssq8.mf
%{_texmfdistdir}/fonts/source/public/cs/csssqi8.mf
%{_texmfdistdir}/fonts/source/public/cs/cstcsc10.mf
%{_texmfdistdir}/fonts/source/public/cs/cstcsc12.mf
%{_texmfdistdir}/fonts/source/public/cs/cstcsc17.mf
%{_texmfdistdir}/fonts/source/public/cs/cstex10.mf
%{_texmfdistdir}/fonts/source/public/cs/cstex8.mf
%{_texmfdistdir}/fonts/source/public/cs/cstex9.mf
%{_texmfdistdir}/fonts/source/public/cs/csti10.mf
%{_texmfdistdir}/fonts/source/public/cs/csti12.mf
%{_texmfdistdir}/fonts/source/public/cs/csti17.mf
%{_texmfdistdir}/fonts/source/public/cs/csti7.mf
%{_texmfdistdir}/fonts/source/public/cs/csti8.mf
%{_texmfdistdir}/fonts/source/public/cs/csti9.mf
%{_texmfdistdir}/fonts/source/public/cs/cstt10.mf
%{_texmfdistdir}/fonts/source/public/cs/cstt12.mf
%{_texmfdistdir}/fonts/source/public/cs/cstt8.mf
%{_texmfdistdir}/fonts/source/public/cs/cstt9.mf
%{_texmfdistdir}/fonts/source/public/cs/csu10.mf
%{_texmfdistdir}/fonts/source/public/cs/csu12.mf
%{_texmfdistdir}/fonts/source/public/cs/csu17.mf
%{_texmfdistdir}/fonts/source/public/cs/csu7.mf
%{_texmfdistdir}/fonts/source/public/cs/csu8.mf
%{_texmfdistdir}/fonts/source/public/cs/csu9.mf
%{_texmfdistdir}/fonts/source/public/cs/csvtt10.mf
%{_texmfdistdir}/fonts/source/public/cs/csvtt12.mf
%{_texmfdistdir}/fonts/source/public/cs/csvtt8.mf
%{_texmfdistdir}/fonts/source/public/cs/csvtt9.mf
%{_texmfdistdir}/fonts/source/public/cs/icscsc10.mf
%{_texmfdistdir}/fonts/source/public/cs/icstt8.mf
%{_texmfdistdir}/fonts/source/public/cs/ilcsss8.mf
%{_texmfdistdir}/fonts/source/public/cs/ilcsssb8.mf
%{_texmfdistdir}/fonts/source/public/cs/ilcsssi8.mf
%{_texmfdistdir}/fonts/source/public/cs/kmcsc.mf
%{_texmfdistdir}/fonts/source/public/cs/kmroman.mf
%{_texmfdistdir}/fonts/source/public/cs/kmtexset.mf
%{_texmfdistdir}/fonts/source/public/cs/kmtextit.mf
%{_texmfdistdir}/fonts/source/public/cs/kmtitle.mf
%{_texmfdistdir}/fonts/source/public/cs/lcsss8.mf
%{_texmfdistdir}/fonts/source/public/cs/lcsssb8.mf
%{_texmfdistdir}/fonts/source/public/cs/lcsssi8.mf
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/README
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagd8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagdc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagdo8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagk8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagkc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pagko8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbkd8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbkdc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbkdi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbkl8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbklc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pbkli8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrb8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrbc8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrbo8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrr8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrrc8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pcrro8u.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvb8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvbc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvbn8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvbnc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvbo8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvbon8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvr8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvrc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvrn8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvrnc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvro8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/phvron8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncb8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncbc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncbi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncr8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncrc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pncri8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplb8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplbc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplbi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplr8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplrc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pplri8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmb8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmbc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmbi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmr8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmrc8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/ptmri8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-a35/pzcmi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/bchb8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/bchbi8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/bchr8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/bchri8z.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/rbchb.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/rbchbi.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/rbchr.tfm
%{_texmfdistdir}/fonts/tfm/cs/cs-charter/rbchri.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csb9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csbxti17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cscsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cscsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cscsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cscsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cscsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csdunh9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csff10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csfib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csfib12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csfib9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csinch.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csitt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csitt17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csitt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csitt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl5.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl6.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssltt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssltt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cssltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstcsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstcsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/cstt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu17.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu7.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csu9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csvtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csvtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csvtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/csvtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/icscsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/icstt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/ilcsss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/ilcsssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/ilcsssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/lcsss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/lcsssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/cs/lcsssi8.tfm
%{_texmfdistdir}/fonts/type1/public/cs/README
%{_texmfdistdir}/fonts/type1/public/cs/csb10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx5.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx6.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx7.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbx9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbxsl10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csbxti10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cscsc10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csdunh10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csff10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csfi10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csfib8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csinch.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csitt10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr17.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr5.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr6.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr7.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csr9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cssl10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cssl12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cssl8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cssl9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cssltt10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csss10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csss12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csss17.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csss8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csss9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssdc10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssi10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssi12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssi17.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssi8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssi9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssq8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csssqi8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cstcsc10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csti10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csti12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csti7.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csti8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csti9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cstt10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cstt12.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cstt8.pfb
%{_texmfdistdir}/fonts/type1/public/cs/cstt9.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csu10.pfb
%{_texmfdistdir}/fonts/type1/public/cs/csvtt10.pfb
%{_texmfdistdir}/fonts/vf/cs/cs-a35/README
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pagdc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pagkc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pbkdc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pbklc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pcrbc8u.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pcrrc8u.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/phvbc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/phvbnc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/phvrc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/phvrnc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pncbc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pncrc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pplbc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/pplrc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/ptmbc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-a35/ptmrc8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-charter/bchb8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-charter/bchbi8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-charter/bchr8z.vf
%{_texmfdistdir}/fonts/vf/cs/cs-charter/bchri8z.vf
%_texmf_updmap_d/cs

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/cs <<EOF
Map cs-charter.map
Map csfonts.map
EOF
