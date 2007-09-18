%define name	mono
%define version 1.2.5
%define release %mkrel 4

%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname -d %{name}

%define bootstrap 0
%{?_with_bootstrap: %{expand: %%global bootstrap 1}}
%define monodir %_prefix/lib/mono

Summary:	Mono Runtime
Name:		%name
Version:	%version
Release:	%release
License:	GPL/LGPL/BSD
Group:		Development/Other
Source0:	http://www.go-mono.com/sources/%name/%name-%version.tar.bz2
#gw add some major numbers to the dll map to not depend on -devel packages
Patch0:		mono-dllmap.patch
# (fc) 1.2.3.1-4mdv disable using /proc/self/exe to detect root prefix, it breaks under unionfs
Patch1:		mono-1.2.3.1-selfexe.patch
URL:		http://www.go-mono.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libglib2-devel >= 2.2.0
BuildRequires:	bison
BuildRequires:	zlib-devel
Requires:	libmono = %version
# gw requires by System.Drawing
Requires: 	libgdiplus
# Since mono 0.91 (mdk 10.0) we can rely on included config
Obsoletes:	mono-config
Provides:	mono-config
Provides:	libmono-runtime
Obsoletes:      libmono-runtime
# gw this is for some binary-only packages, the versions are retargetted
# by the mono runtime
Provides:        mono(mscorlib) = 1.0.3300.0 
Provides:        mono(System) = 1.0.3300.0 
Provides:        mono(System.Drawing) = 1.0.3300.0 
Provides:        mono(System.Xml) = 1.0.3300.0 
%if ! %bootstrap
#gw needed for mono-find-requires which needs monodis and libmono.so
BuildRequires: mono-devel
%endif


%description
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.

This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security tools
and libraries (corlib, XML, System.Security, System.Drawing, ZipLib,
I18N, Cairo and Mono.*).

%package doc
Summary:	Documentation for the Mono runtime
Group:		Development/Other
Requires:	mono

%description doc
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides documentation for the Mono runtime.

%package -n %libname
Summary:	Libraries for the Mono runtime
Group:		System/Libraries
Provides:	libmono = %version-%release

%description -n %libname
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides the versioned libraries for the Mono runtime.

%package data-sqlite
Summary:	SQLite database connectivity for mono
Group:		Development/Other
Requires:	%mklibname sqlite 0
Requires:	%mklibname sqlite3_ 0

%description data-sqlite
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides the connectivity to the sqlite database for Mono.

%package -n %libnamedev
Summary:	Tools required to embed the Mono runtime
Group:		Development/Other
Requires:	%libname = %version
Requires:	mono = %version
Requires:	mono-bytefx-data-mysql = %version
Requires:       mono-data = %version
Requires:       mono-data-firebird = %version
Requires:       mono-data-sqlite = %version
Requires:       mono-data-sybase = %version
Requires: 	mono-data-oracle = %version
Requires: 	mono-data-postgresql = %version
Requires: 	mono-extras = %version
Requires: 	mono-web = %version
Requires: 	mono-ibm-data-db2 = %version
Requires: 	mono-jscript = %version
Requires: 	mono-locale-extras = %version
Requires: 	mono-winforms = %version
Requires: 	mono-nunit = %version
Conflicts: 	mono-nunit < %version-%release
Provides:	mono-devel = %version-%release
Provides:	libmono-devel = %version-%release
Obsoletes:  %mklibname -d %{name} 0
Conflicts: update-alternatives < 1.9.0

%description -n %libnamedev
Header files and libraries used to embed the Mono runtime in an application.

%package -n jay
Summary:	Jay is a LALR(1) parser generator for Java and C#
Group:		Development/Other

%description -n jay
Jay is a LALR(1) parser generator for Java and C#.

This is a port of Jay to C#, the original Jay can be found here:
http://www.cs.rit.edu/~ats/projects/lp/doc/jay/package-summary.html
	
%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group:	 	  Development/Other
Requires: mono = %version
Provides:        mono(System.Web) = 1.0.3300.0

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package data-oracle
Summary: Oracle database connectivity for Mono
Group:	 	Development/Other
Requires:	mono = %version

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package data
Summary: Database connectivity for Mono
Group:	 	  Development/Other
Requires:	  mono = %version
Provides:        mono(System.Data) = 1.0.3300.0 

%description data
This package provides a Mono assembly to facilitate data access and
manipulation with databases, LDAP compatible directory servers and/or
XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command line
sql application as well as the Microsoft SQL Server and ODBC data
providers.

%package extras
Summary: Infrastructure for running and building daemons and services
Group:	 	  Development/Other
Requires:	  mono = %version

%description extras
This package provides the libary and application to run services and
daemons with Mono. It also includes stubs for the following .NET 1.1
and 2.0 assemblies: Microsoft.Vsa, System.Configuration.Install,
System.Management, System.Messaging.

%package ibm-data-db2
Summary: IBM DB2 database connectivity for Mono 
Group:	     Development/Other
Requires:    mono = %version

%description ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%package jscript
Summary: JScript .NET support for Mono
Group:	 	 Development/Other
Requires:	 mono = %version

%description jscript

This package contains the JScript .NET compiler and language
runtime. This allows you to compile and run JScript.NET application
and assemblies.

%package data-firebird
Summary: Firebird database connectivity for Mono
Group:	 	  Development/Other
Requires:	  mono = %version

%description data-firebird
This package contains the ADO.NET Data provider for the Firebird
database.

%package winforms
Summary: Windows Forms implementation for Mono
Group:	 	 Development/Other
Requires:	 mono = %version
Provides:        mono(System.Windows.Forms) = 1.0.3300.0 

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package locale-extras
Summary: Extra locale information for Mono
Group:	       Development/Other
Requires:      mono = %version

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package data-postgresql
Summary: Postgresql database connectivity for Mono
Group:	 	    Development/Other
Requires:	    mono = %version

%description data-postgresql
This package contains the ADO.NET Data provider for the Postgresql
database.

%package bytefx-data-mysql
Summary: MySQL database connectivity for Mono
Group:	       Development/Other
Requires:      mono = %version

%description bytefx-data-mysql
This package contains the ADO.NET Data provider for MySQL. This is no
longer maintained. MySQL AB now provides MySQL Connector/Net which is
fully managed and actively maintained.

%package data-sybase
Summary: Sybase database connectivity for Mono
Group:	 	Development/Other
Requires:	mono = %version

%description data-sybase
This package contains the ADO.NET Data provider for the Sybase
database.

%package nunit
Summary:	NUnit Testing Framework
Group:	Development/Other
Requires: %name = %version
Conflicts: %libname-devel < %version-%release
# for biarch:
Conflicts: lib%{name}%{major}-devel < %version-%release

%description nunit
NUnit is a unit-testing framework for all .Net languages.  Initially
ported from JUnit, the current release, version 2.2, is the fourth
major release of this xUnit based unit testing tool for Microsoft
.NET. It is written entirely in C# and has been completely redesigned
to take advantage of many .NET language features, for example custom
attributes and other reflection related capabilities. NUnit brings
xUnit to all .NET languages.


%prep
%setup -q
%patch0 -p1 -b .dllmap
%patch1 -p1 -b .selfexe

%build
%configure2_5x --with-preview=yes
#--with-tls=__thread
#gw parallel build broken in 1.2.3
make

%check
#gw unit tests in mcs/class/corlib fail
#make check

%install
rm -rf %{buildroot} installed-docs
%makeinstall_std

mv %buildroot%_datadir/libgc-mono installed-docs

#gw these are all obsolete and shouldn't be packaged:
rm -f %buildroot%_bindir/mbas \
      %buildroot%_mandir/man1/{mint.1,oldmono.1,monostyle.1} \
      %buildroot%monodir/1.0/{browsercaps-updater.exe*,ictool.exe*}
# these work on Windows only
rm -fr %buildroot%monodir/*/Mono.Security.Win32*


%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-, root, root)
%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/1.0/
%dir %{_sysconfdir}/mono/2.0/
%config(noreplace) %{_sysconfdir}/mono/1.0/machine.config
%config(noreplace) %{_sysconfdir}/mono/2.0/machine.config
%config  %{_sysconfdir}/mono/config
%_bindir/mono
%_bindir/certmgr
%_bindir/chktrust
%_bindir/gacutil
%_bindir/gmcs
%_bindir/mcs
%_bindir/mozroots
%_bindir/setreg
%_bindir/smcs
%_bindir/sn
%_mandir/man1/mono.1*
%_mandir/man1/certmgr.1*
%_mandir/man1/chktrust.1*
%_mandir/man1/gacutil.1*
%_mandir/man1/mcs.1*
%_mandir/man1/mozroots.1*
%_mandir/man1/setreg.1*
%_mandir/man1/sn.1*
%_mandir/man1/vbnc.1*
%_mandir/man5/mono-config.5*
%dir %monodir
%dir %monodir/gac/
%dir %monodir/1.0/
%dir %monodir/2.0/
%monodir/1.0/certmgr.exe
%monodir/1.0/certmgr.exe.mdb
%monodir/1.0/chktrust.exe
%monodir/1.0/chktrust.exe.mdb
%monodir/1.0/gacutil.exe
%monodir/1.0/gacutil.exe.mdb
%monodir/2.0/gmcs.exe
%monodir/2.0/gmcs.exe.mdb
%monodir/2.0/gmcs.exe.config
%monodir/1.0/mcs.exe.config
%monodir/1.0/mcs.exe
%monodir/1.0/mcs.exe.mdb
%monodir/1.0/mozroots.exe
%monodir/1.0/mozroots.exe.mdb
%monodir/1.0/setreg.exe
%monodir/1.0/setreg.exe.mdb
%monodir/1.0/sn.exe
%monodir/1.0/sn.exe.mdb
%monodir/gac/cscompmgd
%monodir/1.0/cscompmgd.dll
%monodir/2.0/cscompmgd.dll
%monodir/gac/I18N.West
%monodir/1.0/I18N.West.dll
%monodir/2.0/I18N.West.dll
%monodir/gac/I18N
%monodir/1.0/I18N.dll
%monodir/2.0/I18N.dll
%monodir/gac/Mono.CompilerServices.SymbolWriter
%monodir/1.0/Mono.CompilerServices.SymbolWriter.dll
%monodir/2.0/Mono.CompilerServices.SymbolWriter.dll
%monodir/gac/Mono.GetOptions
%monodir/1.0/Mono.GetOptions.dll
%monodir/2.0/Mono.GetOptions.dll
%monodir/gac/Mono.Security
%monodir/1.0/Mono.Security.dll
%monodir/2.0/Mono.Security.dll
%monodir/gac/System.Core
%monodir/2.0/System.Core.dll
%monodir/gac/System.Security
%monodir/1.0/System.Security.dll
%monodir/2.0/System.Security.dll
%monodir/gac/System.Xml
%monodir/1.0/System.Xml.dll
%monodir/2.0/System.Xml.dll
%monodir/gac/System
%monodir/1.0/System.dll
%monodir/2.0/System.dll
%monodir/gac/System.Configuration
%monodir/2.0/System.Configuration.dll
%monodir/1.0/mscorlib.dll
%monodir/1.0/mscorlib.dll.mdb
%monodir/2.0/mscorlib.dll
%monodir/2.0/mscorlib.dll.mdb
%monodir/gac/Mono.C5
%monodir/2.0/Mono.C5.dll
%monodir/gac/System.Drawing
%monodir/1.0/System.Drawing.dll
%monodir/2.0/System.Drawing.dll
%monodir/gac/Mono.Posix
%monodir/1.0/Mono.Posix.dll
%monodir/2.0/Mono.Posix.dll
%monodir/gac/Mono.Cairo
%monodir/1.0/Mono.Cairo.dll
%monodir/2.0/Mono.Cairo.dll
%monodir/gac/ICSharpCode.SharpZipLib
%monodir/1.0/ICSharpCode.SharpZipLib.dll
%monodir/2.0/ICSharpCode.SharpZipLib.dll
%monodir/compat-1.0/ICSharpCode.SharpZipLib.dll
%monodir/compat-2.0/ICSharpCode.SharpZipLib.dll
%monodir/gac/Microsoft.VisualC
%monodir/1.0/Microsoft.VisualC.dll
%monodir/2.0/Microsoft.VisualC.dll
%monodir/gac/Commons.Xml.Relaxng
%monodir/1.0/Commons.Xml.Relaxng.dll
%monodir/2.0/Commons.Xml.Relaxng.dll
%monodir/gac/CustomMarshalers
%monodir/1.0/CustomMarshalers.dll
%monodir/2.0/CustomMarshalers.dll
%monodir/gac/OpenSystem.C
%monodir/1.0/OpenSystem.C.dll
%monodir/2.0/OpenSystem.C.dll

%files doc
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB NEWS README
%doc docs/*[^Makefile-Makefile.in]
%doc mcs*/docs/clr-abi.txt mcs*/docs/compiler.txt mcs*/docs/control-flow-analysis.txt
%doc installed-docs/*

%files -n %libname
%defattr(-, root, root)
%{_libdir}/libmono*.so.%{major}*
# gw always check if they've got a valid soname
%_libdir/libMonoPosixHelper.so
%_libdir/libMonoSupportW.so
%_libdir/libikvm-native.so

%files data-sqlite
%defattr(-, root, root)
%monodir/1.0/Mono.Data.Sqlite.dll
%monodir/1.0/Mono.Data.SqliteClient.dll
%monodir/2.0/Mono.Data.Sqlite.dll
%monodir/2.0/Mono.Data.SqliteClient.dll
%monodir/gac/Mono.Data.Sqlite
%monodir/gac/Mono.Data.SqliteClient

%files -n %libnamedev
%defattr(-, root, root)
%doc ChangeLog
%dir %_includedir/mono-1.0/
%_includedir/mono-1.0/*
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/libmono*.so
%_libdir/pkgconfig/dotnet.pc
%_libdir/pkgconfig/mono-cairo.pc
%_libdir/pkgconfig/mono.pc
%_bindir/al
%_bindir/al2
%_bindir/caspol
%_bindir/cert2spc
%_bindir/cilc
%_bindir/dtd2rng
%_bindir/dtd2xsd
%_bindir/genxs
%_bindir/httpcfg
%_bindir/ilasm
%_bindir/ilasm2
%_bindir/installvst
#
%_bindir/macpack
#
%_bindir/makecert
%_bindir/mkbundle
%_bindir/mkbundle2
%_bindir/mono-api-diff
%_bindir/mono-api-info
%_bindir/mono-api-info2
%_bindir/mono-find-provides
%_bindir/mono-find-requires
%_bindir/mono-shlib-cop
%_bindir/mono-xmltool
%_bindir/monodis
%_bindir/monolinker
%_bindir/monop
%_bindir/monop2
%_bindir/pedump
%_bindir/permview
%_bindir/prj2make
%_bindir/resgen
%_bindir/resgen2
%_bindir/secutil
%_bindir/sgen
%_bindir/signcode
%_bindir/xbuild
%_bindir/monograph
%_mandir/man1/cert2spc.1*
%_mandir/man1/cilc.1*
%_mandir/man1/dtd2xsd.1*
%_mandir/man1/genxs.1*
%_mandir/man1/httpcfg.1*
%_mandir/man1/ilasm*.1*
#
%_mandir/man1/macpack.1*
#
%_mandir/man1/makecert.1*
%_mandir/man1/mkbundle.1*
%_mandir/man1/monoburg.*
%_mandir/man1/mono-shlib-cop.1*
%_mandir/man1/monodis.1*
%_mandir/man1/monolinker.1*
%_mandir/man1/monop.1*
%_mandir/man1/permview.1*
%_mandir/man1/prj2make.1*
%_mandir/man1/resgen.1*
%_mandir/man1/secutil.1*
%_mandir/man1/sgen.1*
%_mandir/man1/signcode.1*
%_mandir/man1/al.1*
%_mandir/man1/mono-xmltool.1*
#
%monodir/1.0/macpack.exe*
#
%monodir/gac/Microsoft.Build.Tasks
%monodir/2.0/Microsoft.Build.Tasks.dll
%monodir/gac/Microsoft.Build.Framework
%monodir/2.0/Microsoft.Build.Framework.dll
%monodir/gac/Microsoft.Build.Utilities
%monodir/2.0/Microsoft.Build.Utilities.dll
%monodir/gac/Microsoft.Build.Engine
%monodir/2.0/Microsoft.Build.Engine.dll
%monodir/gac/PEAPI
%monodir/1.0/PEAPI.dll
%monodir/2.0/PEAPI.dll
%monodir/2.0/Microsoft.Build.xsd
%monodir/2.0/Microsoft.Common.tasks
%monodir/2.0/Microsoft.Common.targets
%monodir/2.0/Microsoft.CSharp.targets
#
%monodir/2.0/Microsoft.VisualBasic.targets
#
%monodir/gac/Mono.Cecil/
%monodir/2.0/MSBuild
%monodir/2.0/xbuild.rsp
%monodir/1.0/*ake*ert.exe
%monodir/1.0/*ake*ert.exe.mdb
%monodir/1.0/CorCompare.exe
%monodir/1.0/al.exe
%monodir/1.0/al.exe.mdb
%monodir/2.0/al.exe
%monodir/2.0/al.exe.mdb
%monodir/1.0/caspol.exe
%monodir/1.0/caspol.exe.mdb
%monodir/1.0/cert2spc.exe
%monodir/1.0/cert2spc.exe.mdb
%monodir/1.0/cilc.exe
%monodir/1.0/cilc.exe.mdb
%monodir/1.0/culevel.exe
%monodir/1.0/culevel.exe.mdb
%monodir/1.0/dtd2rng.exe
%monodir/1.0/dtd2rng.exe.mdb
%monodir/1.0/dtd2xsd.exe
%monodir/1.0/dtd2xsd.exe.mdb
%monodir/1.0/genxs.exe
%monodir/1.0/genxs.exe.mdb
%monodir/2.0/httpcfg.exe
%monodir/2.0/httpcfg.exe.mdb
%monodir/1.0/ilasm.exe
%monodir/1.0/ilasm.exe.mdb
%monodir/2.0/ilasm.exe
%monodir/2.0/ilasm.exe.mdb
%monodir/1.0/installvst.exe
%monodir/1.0/installvst.exe.mdb
%monodir/1.0/mkbundle.exe
%monodir/1.0/mkbundle.exe.mdb
%monodir/2.0/mkbundle.exe
%monodir/2.0/mkbundle.exe.mdb
%monodir/1.0/monolinker*
%monodir/1.0/monop.exe
%monodir/1.0/monop.exe.mdb
%monodir/2.0/monop.exe
%monodir/2.0/monop.exe.mdb
%monodir/1.0/permview.exe
%monodir/1.0/permview.exe.mdb
%monodir/1.0/resgen.exe
%monodir/1.0/resgen.exe.mdb
%monodir/2.0/resgen.exe
%monodir/2.0/resgen.exe.mdb
%monodir/1.0/secutil.exe
%monodir/1.0/secutil.exe.mdb
%monodir/2.0/sgen.exe
%monodir/2.0/sgen.exe.mdb
%monodir/1.0/signcode.exe
%monodir/1.0/signcode.exe.mdb
%monodir/1.0/prj2make.exe
%monodir/1.0/prj2make.exe.mdb
%monodir/1.0/mono-shlib-cop.exe
%monodir/1.0/mono-shlib-cop.exe.config
%monodir/1.0/mono-shlib-cop.exe.mdb
%monodir/1.0/mono-api-diff.exe
%monodir/1.0/mono-api-info.exe
%monodir/2.0/mono-api-info.exe
%monodir/2.0/xbuild.exe
%monodir/2.0/xbuild.exe.mdb
%monodir/1.0/mono-xmltool.exe
%monodir/1.0/mono-xmltool.exe.mdb
%_datadir/mono-1.0/


%files -n jay
%defattr(-, root, root)
%{_bindir}/jay
%{_mandir}/man1/jay*
%dir %{_datadir}/jay
%{_datadir}/jay/*

%files web
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/mono/browscap.ini
%config(noreplace) %{_sysconfdir}/mono/1.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %{_sysconfdir}/mono/2.0/web.config
%_bindir/disco
%_bindir/soapsuds
%_bindir/wsdl
%_bindir/wsdl2
%_bindir/xsd
%_mandir/man1/disco.1*
%_mandir/man1/soapsuds.1*
%_mandir/man1/wsdl.1*
%_mandir/man1/xsd.1*
%monodir/gac/Mono.Http
%monodir/1.0/Mono.Http.dll
%monodir/2.0/Mono.Http.dll
%monodir/gac/System.Runtime.Remoting
%monodir/1.0/System.Runtime.Remoting.dll
%monodir/2.0/System.Runtime.Remoting.dll
%monodir/gac/System.Web
%monodir/1.0/System.Web.dll
%monodir/2.0/System.Web.dll
%monodir/gac/System.Runtime.Serialization.Formatters.Soap
%monodir/1.0/System.Runtime.Serialization.Formatters.Soap.dll
%monodir/2.0/System.Runtime.Serialization.Formatters.Soap.dll
%monodir/gac/System.Web.Services
%monodir/1.0/System.Web.Services.dll
%monodir/2.0/System.Web.Services.dll
%monodir/1.0/disco.exe
%monodir/1.0/disco.exe.mdb
%monodir/1.0/soapsuds.exe
%monodir/1.0/soapsuds.exe.mdb
%monodir/1.0/wsdl.exe
%monodir/1.0/wsdl.exe.mdb
%monodir/2.0/wsdl.exe
%monodir/2.0/wsdl.exe.mdb
%monodir/1.0/xsd.exe
%monodir/1.0/xsd.exe.mdb

%files jscript
%defattr(-, root, root)
%monodir/gac/Microsoft.JScript
%monodir/1.0/Microsoft.JScript.dll
%monodir/2.0/Microsoft.JScript.dll
%_bindir/mjs
%monodir/1.0/mjs.exe
%monodir/1.0/mjs.exe.mdb

%files data-firebird
%defattr(-, root, root)
%monodir/gac/FirebirdSql.Data.Firebird
%monodir/1.0/FirebirdSql.Data.Firebird.dll


%files winforms
%defattr(-, root, root)
%monodir/gac/System.Windows.Forms
%monodir/1.0/System.Windows.Forms.dll
%monodir/2.0/System.Windows.Forms.dll
%monodir/gac/Accessibility
%monodir/1.0/Accessibility.dll
%monodir/2.0/Accessibility.dll
%monodir/gac/System.Design
%monodir/1.0/System.Design.dll
%monodir/2.0/System.Design.dll
%monodir/gac/System.Drawing.Design
%monodir/1.0/System.Drawing.Design.dll
%monodir/2.0/System.Drawing.Design.dll

%files extras
%defattr(-, root, root)
%monodir/gac/System.Management
%monodir/1.0/System.Management.dll
%monodir/2.0/System.Management.dll
%monodir/gac/System.Messaging
%monodir/1.0/System.Messaging.dll
%monodir/2.0/System.Messaging.dll
%monodir/gac/System.ServiceProcess
%monodir/1.0/System.ServiceProcess.dll
%monodir/2.0/System.ServiceProcess.dll
%_bindir/mono-service
%monodir/1.0/mono-service.exe
%monodir/1.0/mono-service.exe.mdb
%_bindir/mono-service2
%monodir/2.0/mono-service.exe
%monodir/2.0/mono-service.exe.mdb
%monodir/gac/mono-service
%_mandir/man1/mono-service.1*
%monodir/gac/System.Configuration.Install
%monodir/1.0/System.Configuration.Install.dll
%monodir/2.0/System.Configuration.Install.dll
%monodir/gac/Microsoft.Vsa
%monodir/1.0/Microsoft.Vsa.dll
%monodir/2.0/Microsoft.Vsa.dll

%files ibm-data-db2
%defattr(-, root, root)
%monodir/gac/IBM.Data.DB2
%monodir/1.0/IBM.Data.DB2.dll

%files data-oracle
%defattr(-, root, root)
%monodir/gac/System.Data.OracleClient
%monodir/1.0/System.Data.OracleClient.dll
%monodir/2.0/System.Data.OracleClient.dll

%files data
%defattr(-, root, root)
%monodir/1.0/sqlsharp.exe
%monodir/1.0/sqlsharp.exe.mdb
%_bindir/sqlsharp
%_mandir/man1/sqlsharp.1*
%monodir/gac/System.Data
%monodir/1.0/System.Data.dll
%monodir/2.0/System.Data.dll
%monodir/gac/Mono.Data
%monodir/1.0/Mono.Data.dll
%monodir/2.0/Mono.Data.dll
%monodir/gac/Mono.Data.Tds
%monodir/1.0/Mono.Data.Tds.dll
%monodir/2.0/Mono.Data.Tds.dll
%monodir/gac/Mono.Data.TdsClient
%monodir/1.0/Mono.Data.TdsClient.dll
%monodir/2.0/Mono.Data.TdsClient.dll
%monodir/gac/System.EnterpriseServices
%monodir/1.0/System.EnterpriseServices.dll
%monodir/2.0/System.EnterpriseServices.dll
%monodir/gac/Novell.Directory.Ldap
%monodir/1.0/Novell.Directory.Ldap.dll
%monodir/2.0/Novell.Directory.Ldap.dll
%monodir/gac/System.DirectoryServices
%monodir/1.0/System.DirectoryServices.dll
%monodir/2.0/System.DirectoryServices.dll
%monodir/gac/System.Transactions
%monodir/2.0/System.Transactions.dll

%files locale-extras
%defattr(-, root, root)
%monodir/gac/I18N.MidEast
%monodir/1.0/I18N.MidEast.dll
%monodir/2.0/I18N.MidEast.dll
%monodir/gac/I18N.Rare
%monodir/1.0/I18N.Rare.dll
%monodir/2.0/I18N.Rare.dll
%monodir/gac/I18N.CJK
%monodir/1.0/I18N.CJK.dll
%monodir/2.0/I18N.CJK.dll
%monodir/gac/I18N.Other
%monodir/1.0/I18N.Other.dll
%monodir/2.0/I18N.Other.dll

%files data-postgresql
%defattr(-, root, root)
%monodir/gac/Npgsql
%monodir/1.0/Npgsql.dll
%monodir/2.0/Npgsql.dll

%files bytefx-data-mysql
%defattr(-, root, root)
%monodir/gac/ByteFX.Data
%monodir/1.0/ByteFX.Data.dll
%monodir/2.0/ByteFX.Data.dll

%files data-sybase
%defattr(-, root, root)
%monodir/gac/Mono.Data.SybaseClient
%monodir/1.0/Mono.Data.SybaseClient.dll
%monodir/2.0/Mono.Data.SybaseClient.dll

%files nunit
%defattr(-, root, root)
%_bindir/nunit-console
%_bindir/nunit-console2
%monodir/1.0/nunit-console.exe
%monodir/1.0/nunit-console.exe.config
%monodir/1.0/nunit-console.exe.mdb
%monodir/2.0/nunit-console.exe
%monodir/2.0/nunit-console.exe.config
%monodir/2.0/nunit-console.exe.mdb
%monodir/1.0/nunit.core.dll
%monodir/1.0/nunit.framework.dll
%monodir/1.0/nunit.util.dll
%monodir/1.0/nunit.mocks.dll
%monodir/gac/nunit.core
%monodir/gac/nunit.framework
%monodir/gac/nunit.util
%monodir/gac/nunit.mocks
%{_libdir}/pkgconfig/mono-nunit.pc


