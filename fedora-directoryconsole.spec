# http://directory.fedora.redhat.com/wiki/BuildingConsole#Building_Fedora_Directory_Server_Console
Summary:	Fedora DS Java Remote Management Console
Summary(pl):	Konsola w Javie do zdalnego zarz±dzania serwerem Fedora DS
Name:		fedora-directoryconsole
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	7d4229a06ad466c67ae5c7877ec09599
URL:		http://directory.fedora.redhat.com/wiki/Client_software
BuildRequires:	mozldap-devel
BuildRequires:	nss-devel
BuildRequires:	nspr-devel >= 4.4.1
BuildRequires:	rpmbuild(macros) >= 1.228
#build requires Mozilla NSS, NSPR, JSS, and LDAP JDK
#Requires: ldapjdk >= 4.17, jss >= 3.6
#BuildRequires:	ldapjdk >= 4.17, jss >= 3.6
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

%description -l pl
Fedora Management Console u¿ywana przez Fedora Directory Server w
rzeczywisto¶ci sk³ada siê z wielu czê¶ci. Sama aplikacja Fedora
Management Console jest wiêcej ni¿ tylko aplikacj± w Javie. Zosta³a
zaprojektowana jako zestaw narzêdzi, które mo¿na rozszerzaæ do
zarz±dzania wieloma ró¿nymi aplikacjami serwerowymi. Udostêpnia wiele
wspólnych klas Javy, które mo¿na u¿ywaæ do zarz±dzania nowymi
aplikacjami. U¿ytkownicy Fedora Directory Servera najlepiej znaj±
Fedora Directory Server Console. Konsola ta sk³ada siê z paneli
umo¿liwiaj±cych zarz±dzanie Fedora Directory Serverem. Fedora
Directory Server Console jest wczytywana przez aplikacjê Fedora
Management Console.

%prep
%setup -q

%build
ant
#ant [-Dimports.file=FILENAME | -Dconsolesdk.location=PATH]
#ant javadoc

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
#install built/release/jars/fedora-* $RPM_BUILD_ROOT%{_datadir}/%{name}
#install -d $RPM_BUILD_ROOT%{_bindir}
#install console/startconsole $RPM_BUILD_ROOT/%{_bindir}

#cd $RPM_BUILD_ROOT%{_datadir}/%{name}
#ln -s fedora-base-%{version}.jar fedora-base.jar
#ln -s fedora-mcc-%{version}.jar fedora-mcc.jar
#ln -s fedora-mcc-%{version}_en.jar fedora-mcc_en.jar
#ln -s fedora-nmclf-%{version}.jar fedora-nmclf.jar
#ln -s fedora-nmclf-%{version}_en.jar fedora-nmclf_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/startconsole
#%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/fedora-base-%{version}.jar
#%{_datadir}/%{name}/fedora-mcc-%{version}.jar
#%{_datadir}/%{name}/fedora-mcc-%{version}_en.jar
#%{_datadir}/%{name}/fedora-nmclf-%{version}.jar
#%{_datadir}/%{name}/fedora-nmclf-%{version}_en.jar
#%{_datadir}/%{name}/fedora-base.jar
#%{_datadir}/%{name}/fedora-mcc.jar
#%{_datadir}/%{name}/fedora-mcc_en.jar
#%{_datadir}/%{name}/fedora-nmclf.jar
#%{_datadir}/%{name}/fedora-nmclf_en.jar
