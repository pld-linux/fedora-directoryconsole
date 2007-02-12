# http://directory.fedora.redhat.com/wiki/BuildingConsole#Building_Fedora_Directory_Server_Console
Summary:	Fedora DS Java Remote Management Console
Summary(pl.UTF-8):   Konsola w Javie do zdalnego zarządzania serwerem Fedora DS
Name:		fedora-directoryconsole
Version:	1.0.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	a062fded54e7205e2eec600f3a18bcad
Patch0:		%{name}-path.patch
URL:		http://directory.fedora.redhat.com/wiki/Client_software
BuildRequires:	ant
BuildRequires:	fedora-console >= 1.0
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	ldapsdk >= 4.17
BuildRequires:	rpmbuild(macros) >= 1.294
Requires:	fedora-console >= 1.0
Requires:	ldapsdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fedora Management Console as it is used in Fedora Directory Server
is truly made up of multiple pieces. The Fedora Management Console
application itself is really much more than just a Java application.
It was designed as a toolkit that can be extended to manage many
different server applications. It provides many common Java classes
that can be used to manage new applications. Fedora Directory Server
users are most familiar with is the Fedora Directory Server Console.
This is made up of all of the panels that allow to you manage your
Fedora Directory Server; basically it's what comes up when you open up
a Fedora Directory Server instance from the topology panel. The Fedora
Directory Server Console is loaded by the Fedora Management Console
application.

%description -l pl.UTF-8
Fedora Management Console używana przez Fedora Directory Server w
rzeczywistości składa się z wielu części. Sama aplikacja Fedora
Management Console jest więcej niż tylko aplikacją w Javie. Została
zaprojektowana jako zestaw narzędzi, które można rozszerzać do
zarządzania wieloma różnymi aplikacjami serwerowymi. Udostępnia wiele
wspólnych klas Javy, które można używać do zarządzania nowymi
aplikacjami. Użytkownicy Fedora Directory Servera najlepiej znają
Fedora Directory Server Console. Konsola ta składa się z paneli
umożliwiających zarządzanie Fedora Directory Serverem. Fedora
Directory Server Console jest wczytywana przez aplikację Fedora
Management Console.

%prep
%setup -q
%patch0 -p1

%build
%ant \
	-Dconsole.location=%{_datadir}/fedora-console \
	-Dldapjdk.location=%{_javadir} \
	-Dldapconsole.root=`pwd`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install built/package/fedora-ds-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
install built/package/fedora-ds-%{version}_en.jar $RPM_BUILD_ROOT%{_datadir}/%{name}

ln -sf fedora-ds-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/fedora-ds-1.0.jar
ln -sf fedora-ds-%{version}_en.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/fedora-ds-1.0_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fedora-ds-%{version}.jar
%{_datadir}/%{name}/fedora-ds-%{version}_en.jar
%{_datadir}/%{name}/fedora-ds-1.0.jar
%{_datadir}/%{name}/fedora-ds-1.0_en.jar
