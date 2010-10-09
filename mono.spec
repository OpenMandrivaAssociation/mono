%define name	mono
%define version 2.8
%define release %mkrel 3

%define major 0
%define major1 1
%define libname %mklibname %{name} %{major}
%define libnamellvm %mklibname %{name}llvm %{major}
%define libname1 %mklibname %{name} 2.0 %{major1}
%define libnamedev %mklibname -d %{name}

%define bootstrap 1
%{?_with_bootstrap: %{expand: %%global bootstrap 1}}
%define monodir %_prefix/lib/mono

%define llvm no
%define sgen yes

%ifnarch %ix86 x86_64
%define llvm no
%define sgen no
%endif

Summary:	Mono Runtime
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2 and LGPLv2+ and MIT
Group:		Development/Other
Source0:	http://www.go-mono.com/sources/%name/%name-%version.tar.bz2
#gw add some major numbers to the dll map to not depend on -devel packages
Patch0:		mono-dllmap.patch
# (fc) 1.2.3.1-4mdv disable using /proc/self/exe to detect root prefix, it breaks under unionfs
Patch1:		mono-2.6-selfexe.patch
Patch2:		mono-CVE-2007-5197.patch
Patch4: mono-wapi_glop.patch
URL:		http://www.go-mono.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	bison
BuildRequires:	zlib-devel
%if %mdvver >= 201010
BuildRequires:  oprofile-devel
%endif	
%if %llvm == yes
#gw mono 2.8 does not build with our llvm 2.7
BuildRequires: llvm > 2.7
Recommends: %libnamellvm = %version-%release
%endif
Requires:	%libname1 = %version
Requires:	%libname = %version
# gw requires by System.Drawing
Requires: 	libgdiplus
# Since mono 0.91 (mdk 10.0) we can rely on included config
Obsoletes:	mono-config
Provides:	mono-config
Provides:	libmono-runtime
Obsoletes:      libmono-runtime
# gw this is for some binary-only packages, the versions are retargetted
# by the mono runtime
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
Buildarch:	noarch

%description doc
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides documentation for the Mono runtime.

%package -n %libname
Summary:	Libraries for the Mono runtime
Group:		System/Libraries

%description -n %libname
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides the versioned libraries for the Mono runtime.

%package -n %libname1
Summary:	Libraries for the Mono runtime
Group:		System/Libraries

%description -n %libname1
Mono is an implementation of the ECMA Common Language Infrastructure,
it contains both a just-in-time compiler for maximum performance, and
an interpeter.  It can also be used to run programs from the .NET
Framework.
This package provides the versioned libraries for the Mono runtime.

%if %llvm == yes
%package -n %libnamellvm
License:        LGPLv2
Summary:	Loadable LLVM libary for mono
Group:          System/Libraries

%description -n %libnamellvm
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Loadable LLVM libary for mono.
%endif

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
Requires:	%libname1 = %version
%if %llvm == yes
Requires:       %libnamellvm = %version-%release
%endif
Requires:	mono = %version
Requires:       mono-data = %version
Requires:       mono-data-sqlite = %version
Requires: 	mono-data-oracle = %version
Requires: 	mono-data-postgresql = %version
Requires: 	mono-extras = %version
Requires: 	mono-web = %version
Requires: 	mono-ibm-data-db2 = %version
Requires: 	mono-locale-extras = %version
Requires: 	mono-winforms = %version
Requires: 	mono-nunit = %version
Requires: 	monodoc-core = %version
Requires:	mono-wcf = %version
Requires:	mono-winfxcore = %version
Conflicts: 	mono-nunit < %version-%release
Provides:	mono-devel = %version-%release
Provides:	libmono-devel = %version-%release
Obsoletes:  %mklibname -d %{name} 0
Conflicts: update-alternatives < 1.9.0

%description -n %libnamedev
Header files and libraries used to embed the Mono runtime in an application.

%package winfxcore
Summary: Mono implementation of core WinFX APIs
Group: Development/Other
Requires: mono = %version

%description winfxcore
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of core WinFX APIs

	
%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group:	 	  Development/Other
Requires: mono = %version

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

%package winforms
Summary: Windows Forms implementation for Mono
Group:	 	 Development/Other
Requires:	 mono = %version
Requires: gluezilla >= 2.0

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
Provides:       mono(Npgsql) = 1.0.5000.0

%description data-postgresql
This package contains the ADO.NET Data provider for the Postgresql
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

%package -n monodoc-core
Summary:        Monodoc-Documentation tools for C# code
Group:          Development/Other
Provides:       monodoc
Obsoletes:      monodoc

%description -n monodoc-core
Monodoc-core contains documentation tools for C#.

%package wcf
Summary:        Mono implementation of WCF, Windows Communication Foundation
Group:          Development/Other
Requires:	%name = %version

%description wcf
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of WCF, Windows Communication Foundation

%prep
%setup -q
%patch0 -p1 -b .dllmap
%patch1 -p1 -b .selfexe
%patch2 -p0 -b .cve-2007-5197
%patch4 -p1 -b .glop

%build
#gw else the syslog() call will not build
#https://bugzilla.novell.com/show_bug.cgi?id=590967#c16
%define Werror_cflags %nil
#gw else libmonosgen-2.0.la does not build
%define _disable_ld_no_undefined 1
%configure2_5x --with-preview=yes \
  --with-sgen=%{sgen} \
%if %llvm == yes
 --enable-loadedllvm \
%endif
%if %mdvver >= 201010
 --with-oprofile=%_prefix
%endif

#gw parallel build broken in 2.6
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
      %buildroot%_mandir/man1/{mint.1,oldmono.1,monostyle.1} 
# these work on Windows only
rm -fr %buildroot%monodir/*/Mono.Security.Win32*
# remove stuff that we don't package
rm -f %buildroot%_bindir/cilc
rm -f %buildroot%_mandir/man1/cilc.1*
rm -f %buildroot%monodir/*/browsercaps-updater.exe*
rm -f %buildroot%monodir/*/culevel.exe*
rm -f %buildroot%monodir/*/cilc.exe*

%find_lang mcs

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f mcs.lang
%defattr(-, root, root)
%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/2.0/
%config(noreplace) %{_sysconfdir}/mono/2.0/machine.config
%config(noreplace) %{_sysconfdir}/mono/4.0/machine.config
%config(noreplace) %{_sysconfdir}/mono/2.0/settings.map
%config(noreplace) %{_sysconfdir}/mono/4.0/settings.map
%config  %{_sysconfdir}/mono/config
%_bindir/mono
%_bindir/mono-configuration-crypto
%if %sgen == yes
%_bindir/mono-sgen
%endif
%_bindir/mono-test-install
%_bindir/csharp
%_bindir/csharp2
%_bindir/certmgr
%_bindir/chktrust
%_bindir/dmcs
%_bindir/gacutil
%_bindir/gacutil2
%_bindir/gmcs
%_bindir/mcs
%_bindir/mozroots
%_bindir/peverify
%_bindir/setreg
%_bindir/sn
%_mandir/man1/mono.1*
%_mandir/man1/mono-configuration-crypto.1*
%_mandir/man1/certmgr.1*
%_mandir/man1/chktrust.1*
%_mandir/man1/csharp.1*
%_mandir/man1/gacutil.1*
%_mandir/man1/mcs.1*
%_mandir/man1/mozroots.1*
%_mandir/man1/setreg.1*
%_mandir/man1/sn.1*
%_mandir/man5/mono-config.5*
%dir %monodir
%dir %monodir/gac/
%dir %monodir/2.0/
%dir %monodir/3.5/
%dir %monodir/4.0/
%monodir/mono-configuration-crypto
%monodir/2.0/csharp.exe
%monodir/2.0/csharp.exe.mdb
%monodir/4.0/csharp.exe*
%monodir/4.0/chktrust.exe*
%monodir/4.0/dmcs.exe*
%monodir/2.0/gacutil.exe
%monodir/2.0/gacutil.exe.mdb
%monodir/4.0/gacutil.exe*
%monodir/2.0/gmcs.exe*
%monodir/4.0/certmgr.exe*
%monodir/4.0/mozroots.exe*
%monodir/4.0/setreg.exe*
%monodir/4.0/sn.exe*
%monodir/gac/cscompmgd
%monodir/2.0/cscompmgd.dll
%monodir/4.0/cscompmgd.dll
%monodir/gac/I18N.West
%monodir/2.0/I18N.West.dll
%monodir/4.0/I18N.West.dll
%monodir/gac/I18N
%monodir/2.0/I18N.dll
%monodir/4.0/I18N.dll
%monodir/gac/Microsoft.CSharp
%monodir/4.0/Microsoft.CSharp.dll
%monodir/4.0/Microsoft.VisualC.dll
%monodir/gac/Mono.CompilerServices.SymbolWriter
%monodir/2.0/Mono.CompilerServices.SymbolWriter.dll
%monodir/4.0/Mono.CompilerServices.SymbolWriter.dll
%monodir/gac/Mono.CSharp
%monodir/2.0/Mono.CSharp.dll
%monodir/4.0/Mono.CSharp.dll
%monodir/gac/Mono.Management
%monodir/2.0/Mono.Management.dll
%monodir/4.0/Mono.Management.dll
%monodir/gac/Mono.Security
%monodir/2.0/Mono.Security.dll
%monodir/4.0/Mono.Security.dll
%monodir/gac/Mono.Simd
%monodir/2.0/Mono.Simd.dll
%monodir/4.0/Mono.Simd.dll
%monodir/2.0/Mono.Tasklets.dll
%monodir/4.0/Mono.Tasklets.dll
%monodir/gac/Mono.Tasklets
%monodir/gac/System.Core
%monodir/2.0/System.Core.dll
%monodir/4.0/System.Core.dll
%monodir/gac/System.Security
%monodir/2.0/System.Security.dll
%monodir/4.0/System.Security.dll
%monodir/gac/System.Xml
%monodir/2.0/System.Xml.dll
%monodir/4.0/System.Xml.dll
%monodir/gac/System.Xml.Linq
%monodir/2.0/System.Xml.Linq.dll
%monodir/4.0/System.Xml.Linq.dll
%monodir/gac/System
%monodir/2.0/System.dll
%monodir/4.0/System.dll
%monodir/gac/System.Configuration
%monodir/2.0/System.Configuration.dll
%monodir/4.0/System.Configuration.dll
%monodir/2.0/mscorlib.dll*
%monodir/4.0/mscorlib.dll*
%monodir/gac/Mono.C5
%monodir/2.0/Mono.C5.dll
%monodir/4.0/Mono.C5.dll
%monodir/gac/System.Drawing
%monodir/2.0/System.Drawing.dll
%monodir/4.0/System.Drawing.dll
%monodir/gac/System.Dynamic
%monodir/4.0/System.Dynamic.dll
%monodir/gac/System.Numerics
%monodir/4.0/System.Numerics.dll
%monodir/gac/Mono.Posix
%monodir/2.0/Mono.Posix.dll
%monodir/4.0/Mono.Posix.dll
%monodir/gac/Mono.Cairo
%monodir/2.0/Mono.Cairo.dll
%monodir/4.0/Mono.Cairo.dll
%monodir/gac/ICSharpCode.SharpZipLib
%monodir/2.0/ICSharpCode.SharpZipLib.dll
%monodir/4.0/ICSharpCode.SharpZipLib.dll
%monodir/compat-2.0/ICSharpCode.SharpZipLib.dll
%monodir/compat-4.0/ICSharpCode.SharpZipLib.dll
%monodir/gac/Microsoft.VisualC
%monodir/2.0/Microsoft.VisualC.dll
%monodir/gac/Commons.Xml.Relaxng
%monodir/2.0/Commons.Xml.Relaxng.dll
%monodir/4.0/Commons.Xml.Relaxng.dll
%monodir/gac/CustomMarshalers
%monodir/2.0/CustomMarshalers.dll
%monodir/4.0/CustomMarshalers.dll
%monodir/gac/OpenSystem.C
%monodir/2.0/OpenSystem.C.dll
%monodir/4.0/OpenSystem.C.dll

%files doc
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB NEWS README
%doc docs/*[^Makefile-Makefile.in]
%doc mcs*/docs/clr-abi.txt mcs*/docs/compiler.txt mcs*/docs/control-flow-analysis.txt
%doc installed-docs/*

%files -n %libname
%defattr(-, root, root)
%{_libdir}/libmono-profiler*.so.%{major}*
%if %sgen == yes
%{_libdir}/libmonosgen-2.0.so.%{major}*
%endif
# gw always check if they've got a valid soname
%_libdir/libMonoPosixHelper.so
%_libdir/libMonoSupportW.so
%_libdir/libikvm-native.so

%files -n %libname1
%defattr(-, root, root)
%{_libdir}/libmono-2.0.so.%{major1}*

%if %llvm == yes
%files -n %libnamellvm
%defattr(-, root, root)
%{_libdir}/libmono-llvm.so.%{major}*
%endif

%files data-sqlite
%defattr(-, root, root)
%monodir/2.0/Mono.Data.Sqlite.dll
%monodir/4.0/Mono.Data.Sqlite.dll
%monodir/gac/Mono.Data.Sqlite

%files -n %libnamedev
%defattr(-, root, root)
%doc ChangeLog
%dir %_includedir/mono-2.0/
%_includedir/mono-2.0/*
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
%_libdir/libmono*.so
%_libdir/pkgconfig/cecil.pc
%_libdir/pkgconfig/dotnet.pc
%_libdir/pkgconfig/dotnet35.pc
%_libdir/pkgconfig/mono-cairo.pc
%_libdir/pkgconfig/mono-lineeditor.pc
%_libdir/pkgconfig/mono-options.pc
%_libdir/pkgconfig/mono.pc
%_libdir/pkgconfig/mono-2.pc
%_libdir/pkgconfig/mono.web.pc
%_libdir/pkgconfig/system.web.extensions.design_1.0.pc
%_libdir/pkgconfig/system.web.extensions_1.0.pc
%_libdir/pkgconfig/system.web.mvc.pc
%_libdir/pkgconfig/system.web.mvc2.pc
%_libdir/pkgconfig/mono-nunit.pc
%_libdir/pkgconfig/monodoc.pc
%_libdir/pkgconfig/wcf.pc
%_bindir/al
%_bindir/al2
%_bindir/caspol
%_bindir/ccrewrite
%_bindir/cert2spc
%_bindir/dtd2rng
%_bindir/dtd2xsd
%_bindir/genxs
%_bindir/httpcfg
%_bindir/ilasm
%_bindir/installvst
%_bindir/lc
#
%_bindir/macpack
#
%_bindir/makecert
%_bindir/mkbundle
%_bindir/mono-api-info
%_bindir/mono-cil-strip
%_bindir/mono-find-provides
%_bindir/mono-find-requires
%_bindir/mono-gdb.py
%_bindir/mono-heapviz
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
%_bindir/pdb2mdb
%_bindir/xbuild
%_bindir/monograph
%_mandir/man1/ccrewrite.1*
%_mandir/man1/cert2spc.1*
%_mandir/man1/dtd2xsd.1*
%_mandir/man1/genxs.1*
%_mandir/man1/httpcfg.1*
%_mandir/man1/ilasm*.1*
%_mandir/man1/lc.1*
#
%_mandir/man1/macpack.1*
#
%_mandir/man1/makecert.1*
%_mandir/man1/mkbundle.1*
%_mandir/man1/mono-api-info.1*
%_mandir/man1/mono-cil-strip.1*
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
%_mandir/man1/pdb2mdb.1*
%_mandir/man1/xbuild.1*
%_prefix/lib/mono-source-libs/
%monodir/4.0/dtd2rng.exe*
%monodir/4.0/dtd2xsd.exe*
%monodir/4.0/httpcfg.exe*
%monodir/4.0/macpack.exe*
%monodir/4.0/makecert.exe*
%monodir/4.0/mono-api-info.exe*
%monodir/4.0/mono-cil-strip.exe*
%monodir/2.0/monolinker.exe
%monodir/2.0/monolinker.exe.mdb
%monodir/4.0/monolinker.exe*
%monodir/4.0/pdb2mdb.exe*
%monodir/4.0/permview.exe*
%monodir/4.0/resgen.exe*
%monodir/4.0/secutil.exe*
%monodir/4.0/sgen.exe*
%monodir/4.0/signcode.exe*
%monodir/4.0/Microsoft.Build.xsd
%monodir/gac/Microsoft.Build.Tasks
%monodir/2.0/Microsoft.Build.Tasks.dll
%monodir/gac/Microsoft.Build.Framework
%monodir/2.0/Microsoft.Build.Framework.dll
%monodir/3.5/Microsoft.Build.Framework.dll
%monodir/4.0/Microsoft.Build.Framework.dll
%monodir/gac/Microsoft.Build.Utilities
%monodir/2.0/Microsoft.Build.Utilities.dll
%monodir/gac/Microsoft.Build.Engine
%monodir/2.0/Microsoft.Build.Engine.dll
%monodir/3.5/Microsoft.Build.Engine.dll
%monodir/4.0/Microsoft.Build.Engine.dll
%monodir/3.5/Microsoft.Build.Tasks.v3.5.dll
%monodir/gac/Microsoft.Build.Tasks.v3.5
%monodir/gac/Microsoft.Build.Tasks.v4.0
%monodir/4.0/Microsoft.Build.Tasks.v4.0.dll
%monodir/gac/Microsoft.Build.Utilities.v3.5
%monodir/3.5/Microsoft.Build.Utilities.v3.5.dll
%monodir/gac/Microsoft.Build.Utilities.v4.0
%monodir/4.0/Microsoft.Build.Utilities.v4.0.dll
%monodir/4.0/Microsoft.CSharp.targets
%monodir/4.0/Microsoft.Common.targets
%monodir/4.0/Microsoft.Common.tasks
%monodir/4.0/Microsoft.VisualBasic.targets
%monodir/gac/PEAPI
%monodir/2.0/PEAPI.dll
%monodir/4.0/PEAPI.dll
%monodir/2.0/Microsoft.Build.xsd
%monodir/2.0/Microsoft.Common.tasks
%monodir/2.0/Microsoft.Common.targets
%monodir/2.0/Microsoft.CSharp.targets
#
%monodir/2.0/Microsoft.VisualBasic.targets
#
%monodir/gac/Mono.Cecil/
%monodir/gac/Mono.Cecil.Mdb/
%monodir/gac/Mono.CodeContracts
%monodir/4.0/Mono.CodeContracts.dll
%monodir/gac/Mono.Debugger*
%monodir/2.0/Mono.Debugger*
%monodir/2.0/MSBuild
%monodir/3.5/MSBuild
%monodir/4.0/MSBuild
%monodir/2.0/xbuild.rsp
%monodir/2.0/al.exe
%monodir/2.0/al.exe.mdb
%monodir/4.0/al.exe*
%monodir/4.0/caspol.exe*
%monodir/4.0/ccrewrite.exe*
%monodir/4.0/cert2spc.exe*
%monodir/2.0/genxs.exe*
%monodir/4.0/genxs.exe*
%monodir/4.0/ictool.exe*
%monodir/2.0/ilasm.exe
%monodir/2.0/ilasm.exe.mdb
%monodir/4.0/ilasm.exe*
%monodir/4.0/installvst.exe*
%monodir/4.0/lc.exe*
%monodir/2.0/mkbundle.exe*
%monodir/4.0/mkbundle.exe*
%monodir/2.0/monop.exe
%monodir/2.0/monop.exe.mdb
%monodir/4.0/monop.exe*
%monodir/4.0/mono-shlib-cop.exe*
%monodir/4.0/mono-xmltool.exe*
%monodir/2.0/resgen.exe
%monodir/2.0/resgen.exe.mdb
%monodir/2.0/xbuild.exe
%monodir/2.0/xbuild.exe.mdb
%monodir/4.0/xbuild.exe*
%monodir/4.0/xbuild.rsp
%monodir/3.5/*.tasks
%monodir/3.5/*.targets
%monodir/3.5/xbuild.*
%monodir/3.5/Microsoft.Build.xsd
%monodir/xbuild/
%_datadir/mono-2.0/



%files -n mono-winfxcore
%defattr(-, root, root)
%monodir/gac/System.Data.Services.Client
%monodir/gac/WindowsBase
%monodir/2.0/WindowsBase.dll*
%monodir/4.0/WindowsBase.dll*

%files web
%defattr(-, root, root)
%dir %{_sysconfdir}/mono/mconfig
%config(noreplace) %{_sysconfdir}/mono/browscap.ini
%config(noreplace) %{_sysconfdir}/mono/2.0/Browsers/Compat.browser
%config(noreplace) %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %{_sysconfdir}/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %{_sysconfdir}/mono/2.0/web.config
%config(noreplace) %{_sysconfdir}/mono/4.0/web.config
%config(noreplace) %{_sysconfdir}/mono/mconfig/config.xml
%_bindir/disco
%_bindir/mconfig
%_bindir/soapsuds
%_bindir/wsdl
%_bindir/wsdl2
%_bindir/xsd
%_mandir/man1/disco.1*
%_mandir/man1/mconfig.1*
%_mandir/man1/soapsuds.1*
%_mandir/man1/wsdl.1*
%_mandir/man1/xsd.1*
%monodir/gac/Mono.Http
%monodir/2.0/Mono.Http.dll
%monodir/4.0/Mono.Http.dll
%monodir/gac/Mono.Web
%monodir/2.0/Mono.Web.dll
%monodir/4.0/Mono.Web.dll
%monodir/gac/System.ComponentModel.Composition
%monodir/4.0/System.ComponentModel.Composition.dll
%monodir/gac/System.ComponentModel.DataAnnotations
%monodir/2.0/System.ComponentModel.DataAnnotations.dll
%monodir/4.0/System.ComponentModel.DataAnnotations.dll
%monodir/gac/System.Web.Abstractions
%monodir/2.0/System.Web.Abstractions.dll
%monodir/4.0/System.Web.Abstractions.dll
%monodir/gac/System.Web.ApplicationServices
%monodir/4.0/System.Web.ApplicationServices.dll
%monodir/gac/System.Web.DynamicData
%monodir/2.0/System.Web.DynamicData.dll
%monodir/4.0/System.Web.DynamicData.dll
%monodir/gac/System.Web.Extensions
%monodir/2.0/System.Web.Extensions.dll
%monodir/4.0/System.Web.Extensions.dll
%monodir/compat-2.0/System.Web.Extensions.dll
%monodir/gac/System.Web.Extensions.Design
%monodir/2.0/System.Web.Extensions.Design.dll
%monodir/3.5/System.Web.Extensions.Design.dll
%monodir/4.0/System.Web.Extensions.Design.dll
%monodir/compat-2.0/System.Web.Extensions.Design.dll
%monodir/gac/System.Web.Mvc
%monodir/2.0/System.Web.Mvc.dll
%monodir/compat-2.0/System.Web.Mvc.dll
%monodir/gac/System.Web.Routing
%monodir/2.0/System.Web.Routing.dll
%monodir/4.0/System.Web.Routing.dll
%monodir/gac/System.Runtime.Remoting
%monodir/2.0/System.Runtime.Remoting.dll
%monodir/4.0/System.Runtime.Remoting.dll
%monodir/gac/System.Web
%monodir/2.0/System.Web.dll
%monodir/4.0/System.Web.dll
%monodir/gac/System.Runtime.Serialization.Formatters.Soap
%monodir/2.0/System.Runtime.Serialization.Formatters.Soap.dll
%monodir/4.0/System.Runtime.Serialization.Formatters.Soap.dll
%monodir/gac/System.Web.Services
%monodir/2.0/System.Web.Services.dll
%monodir/4.0/System.Web.Services.dll
%monodir/4.0/disco.exe*
%monodir/4.0/mconfig.exe*
%monodir/4.0/soapsuds.exe*
%monodir/2.0/wsdl.exe
%monodir/2.0/wsdl.exe.mdb
%monodir/4.0/wsdl.exe*
%monodir/2.0/xsd.exe
%monodir/2.0/xsd.exe.mdb
%monodir/4.0/xsd.exe*

%files winforms
%defattr(-, root, root)
%monodir/gac/System.Windows.Forms
%monodir/2.0/System.Windows.Forms.dll
%monodir/4.0/System.Windows.Forms.dll
%monodir/gac/System.Windows.Forms.DataVisualization
%monodir/4.0/System.Windows.Forms.DataVisualization.dll
%monodir/gac/Accessibility
%monodir/2.0/Accessibility.dll
%monodir/4.0/Accessibility.dll
%monodir/gac/System.Design
%monodir/2.0/System.Design.dll
%monodir/4.0/System.Design.dll
%monodir/gac/System.Drawing.Design
%monodir/2.0/System.Drawing.Design.dll
%monodir/4.0/System.Drawing.Design.dll
%monodir/gac/Mono.WebBrowser
%monodir/2.0/Mono.WebBrowser.dll
%monodir/4.0/Mono.WebBrowser.dll

%files extras
%defattr(-, root, root)
%monodir/gac/System.Management
%monodir/2.0/System.Management.dll
%monodir/4.0/System.Management.dll
%monodir/gac/RabbitMQ.Client
%monodir/2.0/RabbitMQ.Client.dll
%monodir/4.0/RabbitMQ.Client.dll
%monodir/2.0/RabbitMQ.Client.Apigen.exe*
%monodir/4.0/RabbitMQ.Client.Apigen.exe*
%monodir/gac/System.Messaging
%monodir/2.0/System.Messaging.dll
%monodir/4.0/System.Messaging.dll
%monodir/gac/Mono.Messaging
%monodir/2.0/Mono.Messaging.dll
%monodir/4.0/Mono.Messaging.dll
%monodir/gac/Mono.Messaging.RabbitMQ
%monodir/2.0/Mono.Messaging.RabbitMQ.dll
%monodir/4.0/Mono.Messaging.RabbitMQ.dll
%monodir/gac/System.Runtime.Caching
%monodir/4.0/System.Runtime.Caching.dll
%monodir/gac/System.ServiceProcess
%monodir/2.0/System.ServiceProcess.dll
%monodir/4.0/System.ServiceProcess.dll
%_bindir/mono-service
%_bindir/mono-service2
%monodir/4.0/installutil.exe*
%monodir/2.0/mono-service.exe
%monodir/2.0/mono-service.exe.mdb
%monodir/4.0/mono-service.exe*
%monodir/gac/mono-service
%_mandir/man1/mono-service.1*
%monodir/gac/System.Configuration.Install
%monodir/2.0/System.Configuration.Install.dll
%monodir/4.0/System.Configuration.Install.dll
%monodir/gac/System.Xaml
%monodir/4.0/System.Xaml.dll*

%files ibm-data-db2
%defattr(-, root, root)
%monodir/gac/IBM.Data.DB2
%monodir/2.0/IBM.Data.DB2.dll
%monodir/4.0/IBM.Data.DB2.dll

%files data-oracle
%defattr(-, root, root)
%monodir/gac/System.Data.OracleClient
%monodir/2.0/System.Data.OracleClient.dll
%monodir/4.0/System.Data.OracleClient.dll

%files data
%defattr(-, root, root)
%_bindir/sqlmetal
%_bindir/sqlsharp
%_mandir/man1/sqlsharp.1*
%monodir/4.0/sqlmetal.exe*
%monodir/4.0/sqlsharp.exe*
%monodir/gac/System.Data
%monodir/2.0/System.Data.dll
%monodir/4.0/System.Data.dll
%monodir/gac/System.Data.DataSetExtensions
%monodir/2.0/System.Data.DataSetExtensions.dll
%monodir/4.0/System.Data.DataSetExtensions.dll
%monodir/gac/System.Data.Linq
%monodir/2.0/System.Data.Linq.dll
%monodir/4.0/System.Data.Linq.dll
%monodir/gac/System.Data.Services
%monodir/2.0/System.Data.Services.dll
%monodir/4.0/System.Data.Services.dll
%monodir/gac/Mono.Data.Tds
%monodir/2.0/Mono.Data.Tds.dll
%monodir/4.0/Mono.Data.Tds.dll
%monodir/gac/System.EnterpriseServices
%monodir/2.0/System.EnterpriseServices.dll
%monodir/4.0/System.EnterpriseServices.dll
%monodir/gac/Novell.Directory.Ldap
%monodir/2.0/Novell.Directory.Ldap.dll
%monodir/4.0/Novell.Directory.Ldap.dll
%monodir/gac/System.DirectoryServices
%monodir/2.0/System.DirectoryServices.dll
%monodir/4.0/System.DirectoryServices.dll
%monodir/gac/System.Runtime.Serialization
%monodir/2.0/System.Runtime.Serialization.dll
%monodir/4.0/System.Runtime.Serialization.dll
%monodir/gac/System.Transactions
%monodir/2.0/System.Transactions.dll
%monodir/4.0/System.Transactions.dll


%files locale-extras
%defattr(-, root, root)
%monodir/gac/I18N.MidEast
%monodir/2.0/I18N.MidEast.dll
%monodir/4.0/I18N.MidEast.dll
%monodir/gac/I18N.Rare
%monodir/2.0/I18N.Rare.dll
%monodir/4.0/I18N.Rare.dll
%monodir/gac/I18N.CJK
%monodir/2.0/I18N.CJK.dll
%monodir/4.0/I18N.CJK.dll
%monodir/gac/I18N.Other
%monodir/2.0/I18N.Other.dll
%monodir/4.0/I18N.Other.dll

%files data-postgresql
%defattr(-, root, root)
%monodir/gac/Npgsql
%monodir/2.0/Npgsql.dll
%monodir/4.0/Npgsql.dll

%files nunit
%defattr(-, root, root)
%_bindir/nunit-console
%_bindir/nunit-console2
%monodir/2.0/nunit-console.exe
%monodir/2.0/nunit-console.exe.config
%monodir/2.0/nunit-console.exe.mdb
%monodir/4.0/nunit-console.exe*
%monodir/gac/nunit-console-runner
%monodir/2.0/nunit-console-runner.dll
%monodir/4.0/nunit-console-runner.dll
%monodir/2.0/nunit.core.dll
%monodir/4.0/nunit.core.dll
%monodir/gac/nunit.core.extensions
%monodir/2.0/nunit.core.extensions.dll
%monodir/4.0/nunit.core.extensions.dll
%monodir/gac/nunit.core.interfaces
%monodir/2.0/nunit.core.interfaces.dll
%monodir/4.0/nunit.core.interfaces.dll
%monodir/2.0/nunit.framework.dll
%monodir/4.0/nunit.framework.dll
%monodir/gac/nunit.framework.extensions
%monodir/2.0/nunit.framework.extensions.dll
%monodir/4.0/nunit.framework.extensions.dll
%monodir/2.0/nunit.mocks.dll
%monodir/4.0/nunit.mocks.dll
%monodir/2.0/nunit.util.dll
%monodir/4.0/nunit.util.dll
%monodir/gac/nunit.core
%monodir/gac/nunit.framework
%monodir/gac/nunit.util
%monodir/gac/nunit.mocks

%files -n monodoc-core
%defattr(-, root, root)
%monodir/gac/monodoc
%monodir/monodoc
%monodir/4.0/mdoc.exe*
%monodir/4.0/mod.exe*
%{_bindir}/mdassembler
%{_bindir}/mdoc
%{_bindir}/mdoc-assemble
%{_bindir}/mdoc-export-html
%{_bindir}/mdoc-export-msxdoc
%{_bindir}/mdoc-update
%{_bindir}/mdoc-validate
%{_bindir}/mdvalidater
%{_bindir}/mod
%{_bindir}/monodocer
%{_bindir}/monodocs2html
%{_bindir}/monodocs2slashdoc
%{_prefix}/lib/monodoc
%{_mandir}/man1/mdassembler.1*
%{_mandir}/man1/mdoc-assemble.1*
%{_mandir}/man1/mdoc-export-html.1*
%{_mandir}/man1/mdoc-export-msxdoc.1*
%{_mandir}/man1/mdoc-update.1*
%{_mandir}/man1/mdoc-validate.1*
%{_mandir}/man1/mdoc.1*
%{_mandir}/man1/mdvalidater.1*
%{_mandir}/man1/monodocer.1*
%{_mandir}/man1/monodocs2html.1*
%{_mandir}/man5/mdoc.5*

%files wcf
%defattr(-, root, root)
%_bindir/svcutil
%monodir/4.0/svcutil.exe*
%monodir/gac/System.IdentityModel
%monodir/2.0/System.IdentityModel.dll
%monodir/4.0/System.IdentityModel.dll
%monodir/gac/System.IdentityModel.Selectors
%monodir/2.0/System.IdentityModel.Selectors.dll
%monodir/4.0/System.IdentityModel.Selectors.dll
%monodir/gac/System.Runtime.DurableInstancing
%monodir/4.0/System.Runtime.DurableInstancing.dll
%monodir/gac/System.ServiceModel
%monodir/2.0/System.ServiceModel.dll
%monodir/4.0/System.ServiceModel.dll
%monodir/gac/System.ServiceModel.Discovery
%monodir/4.0/System.ServiceModel.Discovery.dll
%monodir/gac/System.ServiceModel.Routing
%monodir/4.0/System.ServiceModel.Routing.dll
%monodir/gac/System.ServiceModel.Web
%monodir/2.0/System.ServiceModel.Web.dll
%monodir/4.0/System.ServiceModel.Web.dll

