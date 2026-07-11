%global tl_name synctex
%global tl_revision 66203

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	engine-level feature synchronizing output and source
Group:		Publishing
URL:		https://www.ctan.org/pkg/synctex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(synctex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
SyncTeX allows navigating between the TeX source and (usually PDF)
output, in both directions, given a SyncTeX-aware front end. It is
compiled into most engines and can be enabled with the --synctex=1
option. It is developed as part of TeX Live.

