# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-synctex
Version:	20111103
Release:	1
Summary:	TeXLive synctex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-synctex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive synctex package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/synctex.1*
%doc %{_texmfdir}/doc/man/man1/synctex.man1.pdf
%doc %{_mandir}/man5/synctex.5*
%doc %{_texmfdir}/doc/man/man5/synctex.man5.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
