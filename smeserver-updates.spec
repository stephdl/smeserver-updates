# $Id: smeserver-updates.spec,v 1.3 2013/06/26 13:28:17 unnilennium Exp $
# Authority: dungog
# Name: Stephen Noble

Summary: Update system panel for SMEserver ç
%define name smeserver-updates
Name: %{name}
%define version 1.4
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System/Administration
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-release >= 9.0
BuildRequires: e-smith-devtools
AutoReqProv: no

%description
Update system panel for sme server 9
permitting the uploading and installing of .rpms

%changelog
* Mon Jun 23 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.4-1.sme
- Initial release to sme9

* Wed Jun 26 2013 JP Pialasse <tests@pialasse.com>  1.2-5.sme
- fixing spec file

* Tue Jun 25 2013 JP Pialasse <tests@pialasse.com>  1.2-4.sme
- fix yum path [SME: 7478]
- patch0

* Tue Jan 23 2007 Stephen Noble <support@dungog.net>
- install with 'yum localinstall'
- [1.2-3]

* Mon Mar 13 2006 Stephen Noble <support@dungog.net>
- sme7 version
- uploading and installing an rpm fixed
- [1.2-2]

* Tue Dec 13 2005 Stephen Noble <support@dungog.net>
- sme7 version
- removed all functions except for uploading and installing a rpm
- yum is usually a better option 
- [1.2-1]

* Tue Feb 19 2002 Darrell May <dmay@netsourced.com>
- initial release based on:
- eneo-update-1.0-01.noarch.rpm
- Vendor: Eneo Tecnologia SC.
- Packager: Juan Jesus Prieto <juanprieto@jazzfree.com>
- [0.0.1-1]

%prep
%setup


%build
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f e-smith-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%clean
cd ..
/bin/rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%pre

%post
#new installs

#echo "  If panel doesnt appear run /etc/e-smith/events/actions/navigation-conf"
                                 
# DBS=`find /home/e-smith/db/navigation -type f -name "navigation.*"`
# for db in $DBS ; do            
# r=`/sbin/e-smith/db $db get update-system`
# 	if [ -z "$r" ] ; then
#   	/sbin/e-smith/db $db set update-system panel Description "Update system" DescriptionWeight 4390 Heading "Administration" HeadingWeight 4000
#  	fi
# done

 #if [ -d /etc/e-smith/events/conf-userpanel ] ; then
 #   /sbin/e-smith/signal-event conf-userpanel
 #fi

%preun

%postun
#uninstalls
#if [ $1 = 0 ] ; then
#
#	DBS=`find /home/e-smith/db/navigation -type f -name "navigation.*"`
#	for db in $DBS ; do
#          /sbin/e-smith/db $db delete update-system
#	done
#
# #if [ -d /etc/e-smith/events/conf-userpanel ] ; then
# #   /sbin/e-smith/signal-event conf-userpanel
# #fi
#
#fi
