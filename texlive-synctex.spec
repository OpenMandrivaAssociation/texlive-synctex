Name:		texlive-synctex
Version:	66203
Release:	1
Summary:	TeXLive synctex package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synctex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-synctex.bin

%description
TeXLive synctex package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/synctex.1*
%doc %{_texmfdistdir}/doc/man/man1/synctex.man1.pdf
%doc %{_mandir}/man5/synctex.5*
%doc %{_texmfdistdir}/doc/man/man5/synctex.man5.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdistdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
