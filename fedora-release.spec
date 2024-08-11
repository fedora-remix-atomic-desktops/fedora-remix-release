
%define release_name Rawhide
%define is_rawhide 1

%define eol_date 2025-05-13

%define dist_version 42
%define rhel_dist_version 11

%if %{is_rawhide}
%define bug_version rawhide
%if 0%{?eln}
  %define releasever eln
%else
  %define releasever rawhide
%endif
%define doc_version rawhide
%else
%define bug_version %{dist_version}
%define releasever %{dist_version}
%define doc_version f%{dist_version}
%endif

%bcond basic %[%{undefined eln}]
%bcond cinnamon %[%{undefined eln}]
%bcond cloud %[%{undefined eln}]
%bcond compneuro %[%{undefined eln}]
%bcond container %[%{undefined eln}]
%bcond coreos %[%{undefined eln}]
%bcond designsuite %[%{undefined eln}]
%bcond eln %[%{defined eln}]
%bcond iot %[%{undefined eln}]
%bcond kde %[%{undefined eln}]
%bcond kde_mobile %[%{undefined eln}]
%bcond matecompiz %[%{undefined eln}]
%bcond server %[%{undefined eln}]
%bcond silverblue %[%{undefined eln}]
%bcond kinoite %[%{undefined eln}]
%bcond kinoite_mobile %[%{undefined eln}]
%bcond snappy %[%{undefined eln}]
%bcond soas %[%{undefined eln}]
%bcond toolbx %[%{undefined eln}]
%bcond workstation %[%{undefined eln}]
%bcond xfce %[%{undefined eln}]
%bcond i3 %[%{undefined eln}]
%bcond lxqt %[%{undefined eln}]
%bcond budgie %[%{undefined eln}]
%bcond budgie_atomic %[%{undefined eln}]
%bcond sway %[%{undefined eln}]
%bcond sway_atomic %[%{undefined eln}]
%bcond mobility %[%{undefined eln}]
%bcond miraclewm %[%{undefined eln}]
%bcond miraclewm_atomic %[%{undefined eln}]

%if %{with silverblue} || %{with kinoite} || %{with kinoite_mobile} || %{with sway_atomic} || %{with budgie_atomic} || %{with miraclewm_atomic}
%global with_ostree_desktop 1
%endif

%global dist %{?eln:.eln%{eln}}

# Changes should be submitted as pull requests under
#     https://src.fedoraproject.org/rpms/fedora-release

Summary:        Fedora release files
Name:           fedora-release
Version:        42
# The numbering is 0.<r> before a given Fedora Linux release is released,
# with r starting at 1, and then just <r>, with r starting again at 1.
# Use '%%autorelease -p' before final, and then drop the '-p'.
Release:        %autorelease -p
License:        MIT
URL:            https://fedoraproject.org/

Source1:        LICENSE
Source2:        Fedora-Legal-README.txt

Source10:       85-display-manager.preset
Source11:       90-default.preset
Source12:       90-default-user.preset
Source13:       99-default-disable.preset
Source14:       80-server.preset
Source15:       80-workstation.preset
Source16:       org.gnome.shell.gschema.override
Source17:       org.projectatomic.rpmostree1.rules
Source18:       80-iot.preset
Source19:       distro-template.swidtag
Source20:       distro-edition-template.swidtag
Source21:       fedora-workstation.conf
Source22:       80-coreos.preset
Source23:       zezere-ignition-url
Source24:       80-iot-user.preset
Source25:       plasma-desktop.conf
Source26:       80-kde.preset
Source27:       81-desktop.preset
Source28:       longer-default-shutdown-timeout.conf
Source29:       org.gnome.settings-daemon.plugins.power.gschema.override
Source30:       fedora-sway.conf
Source31:       20-fedora-defaults.conf
Source32:       75-eln.preset
Source33:       plasma-mobile.conf
Source34:       80-kde-mobile.preset
Source35:       fedora-miraclewm.conf

BuildArch:      noarch

Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}

Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-basic if nothing else is already doing so.
Recommends:     fedora-release-identity-basic


BuildRequires:  redhat-rpm-config > 121-1
BuildRequires:  systemd-rpm-macros

%description
Fedora release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/DefaultServices/ for details.


%package common
Summary: Fedora release files

Requires:   fedora-release-variant = %{version}-%{release}
Suggests:   fedora-release

%if %{with eln}
Requires:   fedora-repos-eln = %{version}
%else
Requires:   fedora-repos(%{version})
%endif
Requires:   fedora-release-identity = %{version}-%{release}

%if %{is_rawhide}
# Make $releasever return "rawhide" on Rawhide
# and "eln" on ELN.
# https://pagure.io/releng/issue/7445
Provides:       system-release(releasever) = %{releasever}
%endif

# Fedora ships a generic-release package to make the creation of Remixes
# easier, but it cannot coexist with the fedora-release[-*] packages, so we
# will explicitly conflict with it.
Conflicts:  generic-release

# rpm-ostree count me is now enabled in 90-default.preset
Obsoletes: fedora-release-ostree-counting <= 36-0.7

%description common
Release files common to all Editions and Spins of Fedora


%if %{with basic}
%package identity-basic
Summary:        Package providing the basic Fedora identity

RemovePathPostfixes: .basic
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity


%description identity-basic
Provides the necessary files for a Fedora installation that is not identifying
itself as a particular Edition or Spin.
%endif


%if %{with cinnamon}
%package cinnamon
Summary:        Base package for Fedora Cinnamon-specific default configurations

RemovePathPostfixes: .cinnamon
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-cinnamon if nothing else is already doing so.
Recommends:     fedora-release-identity-cinnamon


%description cinnamon
Provides a base package for Fedora Cinnamon-specific configuration files to
depend on as well as Cinnamon system defaults.


%package identity-cinnamon
Summary:        Package providing the identity for Fedora Cinnamon Spin

RemovePathPostfixes: .cinnamon
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-cinnamon = %{version}-%{release}


%description identity-cinnamon
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Cinnamon.
%endif


%if %{with cloud}
%package cloud
Summary:        Base package for Fedora Cloud-specific default configurations

RemovePathPostfixes: .cloud
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-cloud if nothing else is already doing so.
Recommends:     fedora-release-identity-cloud


%description cloud
Provides a base package for Fedora Cloud-specific configuration files to
depend on.


%package identity-cloud
Summary:        Package providing the identity for Fedora Cloud Edition

RemovePathPostfixes: .cloud
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-cloud = %{version}-%{release}


%description identity-cloud
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Cloud Edition.
%endif


%if %{with compneuro}
%package compneuro
Summary:        Base package for Fedora Comp Neuro specific default configurations

RemovePathPostfixes: .compneuro
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-compneuro if nothing else is already doing so.
Recommends:     fedora-release-identity-compneuro


%description compneuro
Provides a base package for Fedora Comp Neuro specific configuration files to
depend on as well as Comp Neuro system defaults.


%package identity-compneuro
Summary:        Package providing the identity for Fedora Comp Neuro Lab

RemovePathPostfixes: .compneuro
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-compneuro = %{version}-%{release}


%description identity-compneuro
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Comp Neuro Lab.
%endif


%if %{with container}
%package container
Summary:        Base package for Fedora container specific default configurations

RemovePathPostfixes: .container
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-container if nothing else is already doing so.
Recommends:     fedora-release-identity-container


%description container
Provides a base package for Fedora container specific configuration files to
depend on as well as container system defaults.


%package identity-container
Summary:        Package providing the identity for Fedora Container Base Image

RemovePathPostfixes: .container
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-container = %{version}-%{release}


%description identity-container
Provides the necessary files for a Fedora installation that is identifying
itself as the Fedora Container Base Image.
%endif


%if %{with coreos}
%package coreos
Summary:        Base package for Fedora CoreOS-specific default configurations

RemovePathPostfixes: .coreos
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-coreos if nothing else is already doing so.
Recommends:     fedora-release-identity-coreos


%description coreos
Provides a base package for Fedora CoreOS Host-specific configuration files to
depend.


%package identity-coreos
Summary:        Package providing the identity for Fedora CoreOS

RemovePathPostfixes: .coreos
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-coreos = %{version}-%{release}


%description identity-coreos
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora CoreOS.
%endif


%if %{with designsuite}
%package designsuite
Summary:        Base package for Fedora Design Suite specific default configurations

RemovePathPostfixes: .designsuite
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Provides:       system-release-product

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-designsuite if nothing else is already doing so.
Recommends:     fedora-release-identity-designsuite


%description designsuite
Provides a base package for Fedora Design Suite specific configuration files to
depend on.


%package identity-designsuite
Summary:        Package providing the identity for Fedora Design Suite Lab

RemovePathPostfixes: .designsuite
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-designsuite = %{version}-%{release}


%description identity-designsuite
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Design Suite Lab.
%endif


%if %{with eln}
%package eln
Summary:        Base package for Fedora ELN specific default configurations

RemovePathPostfixes: .eln
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Provides:       system-release-product
Requires:       fedora-repos-eln

Obsoletes:      redhat-release
Provides:       redhat-release

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-eln if nothing else is already doing so.
Recommends:     fedora-release-identity-eln


%description eln
Provides a base package for Fedora ELN specific configuration files to
depend on.


%package identity-eln
Summary:        Package providing the identity for Fedora ELN

# When running a compose for ELN, we want to make sure that we pull in the
# correct templates when lorax is installed. This Suggests: will clue
# libdnf to use this set of templates instead of lorax-templates-generic.
Suggests: lorax-templates-rhel

# Both netcat and nmap-ncat provide /usr/bin/nc, so prefer the latter like
# RHEL does.
Suggests: nmap-ncat

# Prefer over original standalone versions (without pipewire- prefix)
Suggests: pipewire-jack-audio-connection-kit
Suggests: pipewire-jack-audio-connection-kit-devel
Suggests: pipewire-pulseaudio

# Prefer over Lmod for Provides: environment(modules)
Suggests: environment-modules

# Prefer over elinks, w3m for Provides: text-www-browser
Suggests: lynx

# Prefer over bind9-next and its subpackages
Suggests: bind
Suggests: bind-devel
Suggests: bind-dnssec-utils
Suggests: bind-utils

# Default OpenJDK version, prefer over other versions for
# Provides: java, java-devel, java-headless, maven-jdk-binding, etc.
Suggests: java-21-openjdk
Suggests: java-21-openjdk-devel
Suggests: java-21-openjdk-headless
Suggests: maven-openjdk21

# Prefer over Fedora freeipa (same code, different name, each Provides the other)
Suggests: ipa-client
Suggests: ipa-client-common
Suggests: ipa-client-epn
Suggests: ipa-client-samba
Suggests: ipa-common
Suggests: ipa-selinux
Suggests: ipa-server
Suggests: ipa-server-common
Suggests: ipa-server-dns
Suggests: ipa-server-trust-ad
Suggests: ipa-healthcheck
Suggests: ipa-healthcheck-core

# Prefer over exim, opensmtpd, sendmail for Provides: MTA smtpd smtpdaemon server(smtp)
Suggests: postfix

# Prefer over cdrkit/genisoimage for /usr/bin/mkisofs
Suggests: xorriso

# Prefer over sdubby which also Provides: grubby
Suggests: grubby

# Prefer over arptables-legacy, ebtables-legacy, and iptables-legacy
# for Provides: arptables-helper, ebtables, or iptables
Suggests: iptables-nft

# Prefer over blis for libblas*.so.3()(64bit)
Suggests: blas
Suggests: blas64

RemovePathPostfixes: .eln
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-eln = %{version}-%{release}


%description identity-eln
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora ELN.
%endif


%if %{with iot}
%package iot
Summary:        Base package for Fedora IoT specific default configurations

RemovePathPostfixes: .iot
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires(meta): fedora-iot-config

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-iot if nothing else is already doing so.
Recommends:     fedora-release-identity-iot


%description iot
Provides a base package for Fedora IoT specific configuration files to
depend on as well as IoT system defaults.


%package identity-iot
Summary:        Package providing the identity for Fedora IoT Edition

RemovePathPostfixes: .iot
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-iot = %{version}-%{release}


%description identity-iot
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora IoT Edition.
%endif


%if %{with kde}
%package kde
Summary:        Base package for Fedora KDE Plasma-specific default configurations

RemovePathPostfixes: .kde
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-kde if nothing else is already doing so.
Recommends:     fedora-release-identity-kde


%description kde
Provides a base package for Fedora KDE Plasma-specific configuration files to
depend on as well as KDE Plasma system defaults.


%package identity-kde
Summary:        Package providing the identity for Fedora KDE Plasma Spin

RemovePathPostfixes: .kde
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-kde = %{version}-%{release}


%description identity-kde
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora KDE Plasma Spin.
%endif

%if %{with kde_mobile}
%package kde-mobile
Summary:        Base package for Fedora KDE Plasma Mobile specific default configurations

RemovePathPostfixes: .kde-mobile
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-kde-mobile if nothing else is already doing so.
Recommends:     fedora-release-identity-kde-mobile


%description kde-mobile
Provides a base package for Fedora KDE Plasma Mobile specific configuration files to
depend on as well as KDE Plasma Mobile system defaults.


%package identity-kde-mobile
Summary:        Package providing the identity for Fedora KDE Plasma Mobile Spin

RemovePathPostfixes: .kde-mobile
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-kde-mobile = %{version}-%{release}


%description identity-kde-mobile
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora KDE Plasma Mobile Spin.
%endif

%if %{with matecompiz}
%package matecompiz
Summary:        Base package for Fedora MATE-Compiz-specific default configurations

RemovePathPostfixes: .matecompiz
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-matecompiz if nothing else is already doing so.
Recommends:     fedora-release-identity-matecompiz


%description matecompiz
Provides a base package for Fedora MATE-compiz-specific configuration files to
depend on as well as MATE-Compiz system defaults.


%package identity-matecompiz
Summary:        Package providing the identity for Fedora MATE-Compiz Spin

RemovePathPostfixes: .matecompiz
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-matecompiz = %{version}-%{release}


%description identity-matecompiz
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora MATE-Compiz.
%endif


%if %{with server}
%package server
Summary:        Base package for Fedora Server-specific default configurations

RemovePathPostfixes: .server
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-server if nothing else is already doing so.
Recommends:     fedora-release-identity-server


%description server
Provides a base package for Fedora Server-specific configuration files to
depend on.


%package identity-server
Summary:        Package providing the identity for Fedora Server Edition

RemovePathPostfixes: .server
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-server = %{version}-%{release}


%description identity-server
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Server Edition.
%endif


%if %{with silverblue}
%package silverblue
Summary:        Base package for Fedora Silverblue-specific default configurations

RemovePathPostfixes: .silverblue
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-silverblue if nothing else is already doing so.
Recommends:     fedora-release-identity-silverblue


%description silverblue
Provides a base package for Fedora Silverblue-specific configuration files to
depend on as well as Silverblue system defaults.


%package identity-silverblue
Summary:        Package providing the identity for Fedora Silverblue

RemovePathPostfixes: .silverblue
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-silverblue = %{version}-%{release}


%description identity-silverblue
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Silverblue.
%endif


%if %{with kinoite}
%package kinoite
Summary:        Base package for Fedora Kinoite-specific default configurations

RemovePathPostfixes: .kinoite
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-kinoite if nothing else is already doing so.
Recommends:     fedora-release-identity-kinoite


%description kinoite
Provides a base package for Fedora Kinoite-specific configuration files to
depend on as well as Kinoite system defaults.


%package identity-kinoite
Summary:        Package providing the identity for Fedora Kinoite

RemovePathPostfixes: .kinoite
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-kinoite = %{version}-%{release}


%description identity-kinoite
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Kinoite.
%endif

%if %{with kinoite_mobile}
%package kinoite-mobile
Summary:        Base package for Fedora Kinoite Mobile specific default configurations

RemovePathPostfixes: .kinoite-mobile
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-kinoite-mobile if nothing else is already doing so.
Recommends:     fedora-release-identity-kinoite-mobile


%description kinoite-mobile
Provides a base package for Fedora Kinoite Mobile specific configuration files to
depend on as well as Kinoite Mobile system defaults.


%package identity-kinoite-mobile
Summary:        Package providing the identity for Fedora Kinoite Mobile.

RemovePathPostfixes: .kinoite-mobile
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-kinoite-mobile = %{version}-%{release}


%description identity-kinoite-mobile
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Kinoite Mobile.
%endif

%if %{with ostree_desktop}
%package ostree-desktop
Summary:        Configuration package for rpm-ostree variants to add rpm-ostree polkit rules

%description ostree-desktop
Configuration package for rpm-ostree variants to add rpm-ostree polkit rules
%endif


%if %{with snappy}
%package snappy
Summary:        Base package for Fedora snap specific default configurations

RemovePathPostfixes: .snappy
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-snappy if nothing else is already doing so.
Recommends:     fedora-release-identity-snappy


%description snappy
Provides a base package for Fedora snap specific configuration files to
depend on as well as Snappy system defaults.


%package identity-snappy
Summary:        Package providing the identity for Fedora Snappy environments

RemovePathPostfixes: .snappy
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-snappy = %{version}-%{release}


%description identity-snappy
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora's snappy environment.
%endif


%if %{with soas}
%package soas
Summary:        Base package for Fedora Sugar on a Stick-specific default configurations

RemovePathPostfixes: .soas
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-soas if nothing else is already doing so.
Recommends:     fedora-release-identity-soas


%description soas
Provides a base package for Fedora Sugar on a Stick-specific configuration
files to depend on as well as SoaS system defaults.


%package identity-soas
Summary:        Package providing the identity for Fedora Sugar on a Stick

RemovePathPostfixes: .soas
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-soas = %{version}-%{release}


%description identity-soas
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Sugar on a Stick.
%endif


%if %{with toolbx}
%package toolbx
Summary:        Base package for Fedora Toolbx container specific default configurations

RemovePathPostfixes: .toolbx
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-toolbx if nothing else is already doing so.
Recommends:     fedora-release-identity-toolbx


%description toolbx
Provides a base package for Fedora Toolbx container specific configuration files to
depend on as well as Toolbx container system defaults.


%package identity-toolbx
Summary:        Package providing the identity for Fedora Toolbx container image

RemovePathPostfixes: .toolbx
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-toolbx = %{version}-%{release}


%description identity-toolbx
Provides the necessary files for a Fedora installation that is identifying
itself as the Fedora Toolbx container image.
%endif

%if %{with workstation}
%package workstation
Summary:        Base package for Fedora Workstation-specific default configurations

RemovePathPostfixes: .workstation
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Provides:       system-release-product

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-workstation if nothing else is already doing so.
Recommends:     fedora-release-identity-workstation


%description workstation
Provides a base package for Fedora Workstation-specific configuration files to
depend on.


%package identity-workstation
Summary:        Package providing the identity for Fedora Workstation Edition

RemovePathPostfixes: .workstation
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-workstation = %{version}-%{release}


%description identity-workstation
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Workstation Edition.
%endif


%if %{with xfce}
%package xfce
Summary:        Base package for Fedora Xfce specific default configurations

RemovePathPostfixes: .xfce
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-xfce if nothing else is already doing so.
Recommends:     fedora-release-identity-xfce


%description xfce
Provides a base package for Fedora Xfce specific configuration files to
depend on as well as Xfce system defaults.


%package identity-xfce
Summary:        Package providing the identity for Fedora Xfce Spin

RemovePathPostfixes: .xfce
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-xfce = %{version}-%{release}


%description identity-xfce
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Xfce.
%endif


%if %{with i3}
%package i3
Summary:        Base package for Fedora i3 specific default configurations

RemovePathPostfixes: .i3
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-i3 if nothing else is already doing so.
Recommends:     fedora-release-identity-i3


%description i3
Provides a base package for Fedora i3 specific configuration files to
depend on.


%package identity-i3
Summary:        Package providing the identity for Fedora i3 Spin

RemovePathPostfixes: .i3
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-i3 = %{version}-%{release}


%description identity-i3
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora i3.
%endif


%if %{with lxqt}
%package lxqt
Summary:        Base package for Fedora LXQt specific default configurations

RemovePathPostfixes: .lxqt
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-lxqt if nothing else is already doing so.
Recommends:     fedora-release-identity-lxqt


%description lxqt
Provides a base package for Fedora LXQt specific configuration files to
depend on as well as LXQt system defaults.


%package identity-lxqt
Summary:        Package providing the identity for Fedora LXQt Spin

RemovePathPostfixes: .lxqt
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-lxqt = %{version}-%{release}


%description identity-lxqt
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora LXQt.
%endif

%if %{with budgie}
%package budgie
Summary:        Base package for Fedora Budgie specific default configurations

RemovePathPostfixes: .budgie
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-budgie if nothing else is already doing so.
Recommends:     fedora-release-identity-budgie


%description budgie
Provides a base package for Fedora Budgie specific configuration files to
depend on as well as Budgie system defaults.


%package identity-budgie
Summary:        Package providing the identity for Fedora Budgie Spin

RemovePathPostfixes: .budgie
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-budgie = %{version}-%{release}


%description identity-budgie
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Budgie.
%endif


%if %{with sway}
%package sway
Summary:        Base package for Fedora Sway specific default configurations

RemovePathPostfixes: .sway
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-sway if nothing else is already doing so.
Recommends:     fedora-release-identity-sway


%description sway
Provides a base package for Fedora Sway specific configuration files to
depend on.


%package identity-sway
Summary:        Package providing the identity for Fedora Sway Spin

RemovePathPostfixes: .sway
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-sway = %{version}-%{release}


%description identity-sway
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Sway.
%endif


%if %{with sway_atomic}
%package sway-atomic
Summary:        Base package for Fedora Sway Atomic specific default configurations

RemovePathPostfixes: .sway-atomic
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-sway-atomic if nothing else is already doing so.
Recommends:     fedora-release-identity-sway-atomic


%description sway-atomic
Provides a base package for Fedora Sway Atomic specific configuration
files to depend on.


%package identity-sway-atomic
Summary:        Package providing the identity for Fedora Sway Atomic

RemovePathPostfixes: .sway-atomic
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-sway-atomic = %{version}-%{release}


%description identity-sway-atomic
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Sway Atomic.
%endif

%if %{with budgie_atomic}
%package budgie-atomic
Summary:        Base package for Fedora Budgie Atomic specific default configurations

RemovePathPostfixes: .budgie-atomic
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-budgie-atomic if nothing else is already doing so.
Recommends:     fedora-release-identity-budgie-atomic


%description budgie-atomic
Provides a base package for Fedora Budgie Atomic specific configuration
files to depend on.


%package identity-budgie-atomic
Summary:        Package providing the identity for Fedora Budgie Atomic

RemovePathPostfixes: .budgie-atomic
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-budgie-atomic = %{version}-%{release}


%description identity-budgie-atomic
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Budgie Atomic.
%endif


%if %{with mobility}
%package mobility
Summary:        Base package for Fedora Mobility specific default configurations

RemovePathPostfixes: .mobility
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-mobility if nothing else is already doing so.
Recommends:     fedora-release-identity-mobility


%description mobility
Provides a base package for Fedora Mobility specific configuration
files to depend on.


%package identity-mobility
Summary:        Package providing the identity for Fedora Mobility

RemovePathPostfixes: .mobility
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-mobility = %{version}-%{release}


%description identity-mobility
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Mobility.
%endif

%if %{with miraclewm}
%package miraclewm
Summary:        Base package for Fedora MiracleWM specific default configurations

RemovePathPostfixes: .miraclewm
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-miraclewm if nothing else is already doing so.
Recommends:     fedora-release-identity-miraclewm


%description miraclewm
Provides a base package for Fedora Miracle Window Manager specific configuration
files to depend on.


%package identity-miraclewm
Summary:        Package providing the identity for Fedora MiracleWM Spin

RemovePathPostfixes: .miraclewm
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-miraclewm = %{version}-%{release}


%description identity-miraclewm
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Miracle Window Manager.
%endif


%if %{with miraclewm_atomic}
%package miraclewm-atomic
Summary:        Base package for Fedora MiracleWM Atomic specific default configurations

RemovePathPostfixes: .miraclewm-atomic
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Requires:       fedora-release-common = %{version}-%{release}
Requires:       fedora-release-ostree-desktop = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-miraclewm-atomic if nothing else is already doing so.
Recommends:     fedora-release-identity-miraclewm-atomic


%description miraclewm-atomic
Provides a base package for Fedora Miracle Window Manager Atomic specific
configuration files to depend on.


%package identity-miraclewm-atomic
Summary:        Package providing the identity for Fedora MiracleWM Atomic

RemovePathPostfixes: .miraclewm-atomic
Provides:       fedora-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Requires(meta): fedora-release-miraclewm-atomic = %{version}-%{release}


%description identity-miraclewm-atomic
Provides the necessary files for a Fedora installation that is identifying
itself as Fedora Miracle Window Manager Atomic.
%endif

%prep
mkdir -p licenses
sed 's|@@VERSION@@|%{dist_version}|g' %{SOURCE2} >licenses/Fedora-Legal-README.txt

%build

%install
install -d %{buildroot}%{_prefix}/lib
echo "Fedora release %{version} (%{release_name})" > %{buildroot}%{_prefix}/lib/fedora-release
echo "cpe:/o:fedoraproject:fedora:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/fedora-release %{buildroot}%{_sysconfdir}/fedora-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s fedora-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/system-release

# Create the common os-release file
%{lua:
  function starts_with(str, start)
   return str:sub(1, #start) == start
  end
}
%define starts_with(str,prefix) (%{expand:%%{lua:print(starts_with(%1, %2) and "1" or "0")}})
%if %{starts_with "a%{release}" "a0"}
  %global prerelease \ Prerelease
%endif

# -------------------------------------------------------------------------
# Definitions for /etc/os-release and for macros in macros.dist.  These
# macros are useful for spec files where distribution-specific identifiers
# are used to customize packages.

# Name of vendor / name of distribution. Typically used to identify where
# the binary comes from in --help or --version messages of programs.
# Examples: gdb.spec, clang.spec
%global dist_vendor Fedora
%global dist_name   Fedora Linux

# URL of the homepage of the distribution
# Example: gstreamer1-plugins-base.spec
%global dist_home_url https://fedoraproject.org/

# Bugzilla / bug reporting URLs shown to users.
# Examples: gcc.spec
%global dist_bug_report_url https://bugzilla.redhat.com/

# debuginfod server, as used in elfutils.spec.
%global dist_debuginfod_url https://debuginfod.fedoraproject.org/
# -------------------------------------------------------------------------

cat << EOF >> os-release
NAME="%{dist_name}"
VERSION="%{dist_version} (%{release_name}%{?prerelease})"
ID=fedora
VERSION_ID=%{dist_version}
VERSION_CODENAME=""
PLATFORM_ID="platform:f%{dist_version}"
PRETTY_NAME="Fedora Linux %{dist_version} (%{release_name}%{?prerelease})"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:%{dist_version}"
DEFAULT_HOSTNAME="fedora"
HOME_URL="%{dist_home_url}"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/%{doc_version}/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="%{dist_bug_report_url}"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
SUPPORT_END=%{eol_date}
EOF

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

mkdir -p %{buildroot}%{_swidtagdir}

# Create os-release files for the different editions

%if %{with basic}
# Basic
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.basic
%endif

%if %{with cinnamon}
# Cinnamon
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.cinnamon
echo "VARIANT=\"Cinnamon\"" >> %{buildroot}%{_prefix}/lib/os-release.cinnamon
echo "VARIANT_ID=cinnamon" >> %{buildroot}%{_prefix}/lib/os-release.cinnamon
sed -i -e "s|(%{release_name}%{?prerelease})|(Cinnamon%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.cinnamon
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cinnamon/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cinnamon
%endif

%if %{with cloud}
# Cloud
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.cloud
echo "VARIANT=\"Cloud Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.cloud
echo "VARIANT_ID=cloud" >> %{buildroot}%{_prefix}/lib/os-release.cloud
sed -i -e "s|(%{release_name}%{?prerelease})|(Cloud Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.cloud
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cloud/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cloud
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.cloud
%endif

%if %{with compneuro}
# Comp Neuro
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.compneuro
echo "VARIANT=\"Comp Neuro\"" >> %{buildroot}%{_prefix}/lib/os-release.compneuro
echo "VARIANT_ID=compneuro" >> %{buildroot}%{_prefix}/lib/os-release.compneuro
sed -i -e "s|(%{release_name}%{?prerelease})|(CompNeuro%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.compneuro
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://neuro.fedoraproject.org"|' %{buildroot}%{_prefix}/lib/os-release.compneuro
sed -i -e 's|HOME_URL=.*|HOME_URL="https://labs.fedoraproject.org"|' %{buildroot}/%{_prefix}/lib/os-release.compneuro
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/CompNeuro/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.compneuro
%endif

%if %{with container}
# Container
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.container
echo "VARIANT=\"Container Image\"" >> %{buildroot}%{_prefix}/lib/os-release.container
echo "VARIANT_ID=container" >> %{buildroot}%{_prefix}/lib/os-release.container
sed -i -e "s|(%{release_name}%{?prerelease})|(Container Image%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.container
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Container/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.container
%endif

%if %{with coreos}
# CoreOS
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.coreos
echo "VARIANT=\"CoreOS\"" >> %{buildroot}%{_prefix}/lib/os-release.coreos
echo "VARIANT_ID=coreos" >> %{buildroot}%{_prefix}/lib/os-release.coreos
sed -i -e "s|(%{release_name}%{?prerelease})|(CoreOS%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.coreos
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-coreos/"|' %{buildroot}%{_prefix}/lib/os-release.coreos
sed -i -e 's|HOME_URL=.*|HOME_URL="https://getfedora.org/coreos/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
sed -i -e 's|SUPPORT_URL=.*|SUPPORT_URL="https://github.com/coreos/fedora-coreos-tracker/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://github.com/coreos/fedora-coreos-tracker/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
sed -i -e 's|PRETTY_NAME=.*|PRETTY_NAME="Fedora CoreOS %{dist_version}"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/CoreOS/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.coreos
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.coreos
install -Dm0644 %{SOURCE22} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE28} -t %{buildroot}%{_prefix}/lib/systemd/system.conf.d/
install -Dm0644 %{SOURCE28} -t %{buildroot}%{_prefix}/lib/systemd/user.conf.d/
%endif


%if %{with designsuite}
# Design Suite
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.designsuite
echo "VARIANT=\"Design Suite\"" >> %{buildroot}%{_prefix}/lib/os-release.designsuite
echo "VARIANT_ID=designsuite" >> %{buildroot}%{_prefix}/lib/os-release.designsuite
sed -i -e "s|(%{release_name}%{?prerelease})|(Design Suite%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.designsuite
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://fedoraproject.org/wiki/Design_Suite"|' %{buildroot}%{_prefix}/lib/os-release.designsuite
sed -i -e 's|HOME_URL=.*|HOME_URL="https://labs.fedoraproject.org"|' %{buildroot}/%{_prefix}/lib/os-release.designsuite
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/DesignSuite/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.designsuite
%endif

%if %{with eln}
# ELN
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.eln
echo "VARIANT=\"ELN\"" >> %{buildroot}%{_prefix}/lib/os-release.eln
echo "VARIANT_ID=eln" >> %{buildroot}%{_prefix}/lib/os-release.eln
sed -i -e 's|PLATFORM_ID=.*|PLATFORM_ID="platform:eln"|' %{buildroot}/%{_prefix}/lib/os-release.eln
sed -i -e 's|PRETTY_NAME=.*|PRETTY_NAME="Fedora ELN"|' %{buildroot}/%{_prefix}/lib/os-release.eln
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/eln/"|' %{buildroot}%{_prefix}/lib/os-release.eln
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.eln
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/ELN/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.eln

# ELN installs the Server presets as well
install -Dm0644 %{SOURCE14} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# ELN may override some presets from Fedora to simplify branching for CentOS Stream
install -Dm0644 %{SOURCE32} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
%endif

%if %{with iot}
# IoT
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.iot
echo "VARIANT=\"IoT Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.iot
echo "VARIANT_ID=iot" >> %{buildroot}%{_prefix}/lib/os-release.iot
sed -i -e "s|(%{release_name}%{?prerelease})|(IoT Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.iot
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/IoT/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.iot
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.iot
install -p %{SOURCE23} %{buildroot}/%{_prefix}/lib/
install -Dm0644 %{SOURCE18} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE24} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
%endif

%if %{with kde}
# KDE Plasma
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.kde
echo "VARIANT=\"KDE Plasma\"" >> %{buildroot}%{_prefix}/lib/os-release.kde
echo "VARIANT_ID=kde" >> %{buildroot}%{_prefix}/lib/os-release.kde
sed -i -e "s|(%{release_name}%{?prerelease})|(KDE Plasma%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.kde
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/KDE/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde
# Add plasma-desktop to dnf protected packages list for KDE
install -Dm0644 %{SOURCE25} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with kde_mobile}
# KDE Plasma Mobile
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.kde-mobile
echo "VARIANT=\"KDE Plasma Mobile\"" >> %{buildroot}%{_prefix}/lib/os-release.kde-mobile
echo "VARIANT_ID=kde-mobile" >> %{buildroot}%{_prefix}/lib/os-release.kde-mobile
sed -i -e "s|(%{release_name}%{?prerelease})|(KDE Plasma Mobile%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.kde-mobile
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/KDE Mobile/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde-mobile
# Add plasma-mobile to dnf protected packages list for KDE  Mobile
install -Dm0644 %{SOURCE33} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with matecompiz}
# MATE-Compiz
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.matecompiz
echo "VARIANT=\"MATE-Compiz\"" >> %{buildroot}%{_prefix}/lib/os-release.matecompiz
echo "VARIANT_ID=matecompiz" >> %{buildroot}%{_prefix}/lib/os-release.matecompiz
sed -i -e "s|(%{release_name}%{?prerelease})|(MATE-Compiz%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.matecompiz
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/MATE-Compiz/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.matecompiz
%endif

%if %{with server}
# Server
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.server
echo "VARIANT=\"Server Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.server
echo "VARIANT_ID=server" >> %{buildroot}%{_prefix}/lib/os-release.server
sed -i -e "s|(%{release_name}%{?prerelease})|(Server Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.server
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Server/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.server
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.server
install -Dm0644 %{SOURCE14} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE29} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
install -Dm0644 %{SOURCE28} -t %{buildroot}%{_prefix}/lib/systemd/system.conf.d/
install -Dm0644 %{SOURCE28} -t %{buildroot}%{_prefix}/lib/systemd/user.conf.d/
%endif

%if %{with silverblue}
# Silverblue
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.silverblue
echo "VARIANT=\"Silverblue\"" >> %{buildroot}%{_prefix}/lib/os-release.silverblue
echo "VARIANT_ID=silverblue" >> %{buildroot}%{_prefix}/lib/os-release.silverblue
sed -i -e "s|(%{release_name}%{?prerelease})|(Silverblue%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.silverblue
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-silverblue/"|' %{buildroot}%{_prefix}/lib/os-release.silverblue
sed -i -e 's|HOME_URL=.*|HOME_URL="https://silverblue.fedoraproject.org"|' %{buildroot}/%{_prefix}/lib/os-release.silverblue
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://github.com/fedora-silverblue/issue-tracker/issues"|' %{buildroot}/%{_prefix}/lib/os-release.silverblue
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Silverblue/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.silverblue
%endif

%if %{with kinoite}
# Kinoite
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.kinoite
echo "VARIANT=\"Kinoite\"" >> %{buildroot}%{_prefix}/lib/os-release.kinoite
echo "VARIANT_ID=kinoite" >> %{buildroot}%{_prefix}/lib/os-release.kinoite
sed -i -e "s|(%{release_name}%{?prerelease})|(Kinoite%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.kinoite
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-kinoite/"|' %{buildroot}%{_prefix}/lib/os-release.kinoite
sed -i -e 's|HOME_URL=.*|HOME_URL="https://kinoite.fedoraproject.org"|' %{buildroot}/%{_prefix}/lib/os-release.kinoite
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://pagure.io/fedora-kde/SIG/issues"|' %{buildroot}/%{_prefix}/lib/os-release.kinoite
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Kinoite/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kinoite
%endif

%if %{with kinoite_mobile}
# Kinoite Mobile
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.kinoite-mobile
echo "VARIANT=\"Kinoite Mobile\"" >> %{buildroot}%{_prefix}/lib/os-release.kinoite-mobile
echo "VARIANT_ID=kinoite-mobile" >> %{buildroot}%{_prefix}/lib/os-release.kinoite-mobile
sed -i -e "s|(%{release_name}%{?prerelease})|(Kinoite Mobile%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.kinoite-mobile
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-kinoite/"|' %{buildroot}%{_prefix}/lib/os-release.kinoite-mobile
sed -i -e 's|HOME_URL=.*|HOME_URL="https://kinoite.fedoraproject.org"|' %{buildroot}/%{_prefix}/lib/os-release.kinoite-mobile
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://pagure.io/fedora-kde/SIG/issues"|' %{buildroot}/%{_prefix}/lib/os-release.kinoite-mobile
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Kinoite Mobile/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kinoite-mobile
%endif

%if %{with snappy}
# Snappy
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.snappy
echo "VARIANT=\"Snappy\"" >> %{buildroot}%{_prefix}/lib/os-release.snappy
echo "VARIANT_ID=snappy" >> %{buildroot}%{_prefix}/lib/os-release.snappy
sed -i -e "s|(%{release_name}%{?prerelease})|(Snappy%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.snappy
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Snappy/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.snappy
%endif

%if %{with soas}
# Sugar on a Stick
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.soas
echo "VARIANT=\"Sugar on a Stick\"" >> %{buildroot}%{_prefix}/lib/os-release.soas
echo "VARIANT_ID=soas" >> %{buildroot}%{_prefix}/lib/os-release.soas
sed -i -e "s|(%{release_name}%{?prerelease})|(Sugar on a Stick%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.soas
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Sugar/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.soas
%endif

%if %{with toolbx}
# Toolbx
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.toolbx
echo "VARIANT=\"Toolbx Container Image\"" >> %{buildroot}%{_prefix}/lib/os-release.toolbx
echo "VARIANT_ID=toolbx" >> %{buildroot}%{_prefix}/lib/os-release.toolbx
sed -i -e "s|(%{release_name}%{?prerelease})|(Toolbx Container Image%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.toolbx
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Toolbx/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.toolbx
%endif

%if %{with workstation}
# Workstation
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT=\"Workstation Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT_ID=workstation" >> %{buildroot}%{_prefix}/lib/os-release.workstation
sed -i -e "s|(%{release_name}%{?prerelease})|(Workstation Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.workstation
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Workstation/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.workstation
# Add Fedora Workstation dnf protected packages list
install -Dm0644 %{SOURCE21} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with silverblue} || %{with workstation}
# Silverblue and Workstation
install -Dm0644 %{SOURCE15} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE27} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# Override the list of enabled gnome-shell extensions for Workstation
install -Dm0644 %{SOURCE16} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
%endif

%if %{with kde} || %{with kinoite}
# Common desktop preset and spin specific preset
install -Dm0644 %{SOURCE26} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE27} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
%endif

%if %{with kde_mobile} || %{with kinoite_mobile}
# Common desktop preset and spin specific preset
install -Dm0644 %{SOURCE34} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE27} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
%endif

%if %{with ostree_desktop}
# Install rpm-ostree polkit rules
install -Dm0644 %{SOURCE17} -t %{buildroot}%{_datadir}/polkit-1/rules.d/
%endif

%if %{with xfce}
# Xfce
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.xfce
echo "VARIANT=\"Xfce\"" >> %{buildroot}%{_prefix}/lib/os-release.xfce
echo "VARIANT_ID=xfce" >> %{buildroot}%{_prefix}/lib/os-release.xfce
sed -i -e "s|(%{release_name}%{?prerelease})|(Xfce%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.xfce
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Xfce/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.xfce
%endif

%if %{with i3}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.i3
echo "VARIANT=\"i3\"" >> %{buildroot}%{_prefix}/lib/os-release.i3
echo "VARIANT_ID=i3" >> %{buildroot}%{_prefix}/lib/os-release.i3
sed -i -e "s|(%{release_name}%{?prerelease})|(i3%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.i3
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/i3/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.i3
%endif

%if %{with lxqt}
# LXQt
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.lxqt
echo "VARIANT=\"LXQt\"" >> %{buildroot}%{_prefix}/lib/os-release.lxqt
echo "VARIANT_ID=lxqt" >> %{buildroot}%{_prefix}/lib/os-release.lxqt
sed -i -e "s|(%{release_name}%{?prerelease})|(LXQt%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.lxqt
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/LXQt/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.lxqt
%endif

%if %{with budgie}
# Budgie
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.budgie
echo "VARIANT=\"Budgie\"" >> %{buildroot}%{_prefix}/lib/os-release.budgie
echo "VARIANT_ID=budgie" >> %{buildroot}%{_prefix}/lib/os-release.budgie
sed -i -e "s|(%{release_name}%{?prerelease})|(Budgie%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.budgie
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Budgie/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.budgie
%endif

%if %{with sway}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.sway
echo "VARIANT=\"Sway\"" >> %{buildroot}%{_prefix}/lib/os-release.sway
echo "VARIANT_ID=sway" >> %{buildroot}%{_prefix}/lib/os-release.sway
sed -i -e "s|(%{release_name}%{?prerelease})|(Sway%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.sway
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://gitlab.com/fedora/sigs/sway/SIG/-/issues"|' %{buildroot}/%{_prefix}/lib/os-release.sway
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Sway/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.sway
# Add Fedora Sway dnf protected packages list
install -Dm0644 %{SOURCE30} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with sway_atomic}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.sway-atomic
echo "VARIANT=\"Sway Atomic\"" >> %{buildroot}%{_prefix}/lib/os-release.sway-atomic
echo "VARIANT_ID=sway-atomic" >> %{buildroot}%{_prefix}/lib/os-release.sway-atomic
sed -i -e "s|(%{release_name}%{?prerelease})|(Sway Atomic%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.sway-atomic
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-sericea/"|' %{buildroot}%{_prefix}/lib/os-release.sway-atomic
sed -i -e 's|HOME_URL=.*|HOME_URL="https://fedoraproject.org/atomic-desktops/sway/"|' %{buildroot}/%{_prefix}/lib/os-release.sway-atomic
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://gitlab.com/fedora/sigs/sway/SIG/-/issues"|' %{buildroot}/%{_prefix}/lib/os-release.sway-atomic
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/SwayAtomic/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.sway-atomic
%endif

%if %{with budgie_atomic}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.budgie-atomic
echo "VARIANT=\"Budgie Atomic\"" >> %{buildroot}%{_prefix}/lib/os-release.budgie-atomic
echo "VARIANT_ID=budgie-atomic" >> %{buildroot}%{_prefix}/lib/os-release.budgie-atomic
sed -i -e "s|(%{release_name}%{?prerelease})|(Budgie Atomic%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.budgie-atomic
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-onyx/"|' %{buildroot}%{_prefix}/lib/os-release.budgie-atomic
sed -i -e 's|HOME_URL=.*|HOME_URL="https://fedoraproject.org/atomic-desktops/budgie/"|' %{buildroot}/%{_prefix}/lib/os-release.budgie-atomic
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://pagure.io/fedora-budgie/project/issues"|' %{buildroot}/%{_prefix}/lib/os-release.budgie-atomic
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/BudgieAtomic/;s/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.budgie-atomic
%endif

%if %{with mobility}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.mobility
echo "VARIANT=\"Mobility\"" >> %{buildroot}%{_prefix}/lib/os-release.mobility
echo "VARIANT_ID=mobility" >> %{buildroot}%{_prefix}/lib/os-release.mobility
sed -i -e "s|(%{release_name}%{?prerelease})|(Mobility%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.mobility
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Mobility/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.mobility
%endif

%if %{with miraclewm}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.miraclewm
echo "VARIANT=\"MiracleWM\"" >> %{buildroot}%{_prefix}/lib/os-release.miraclewm
echo "VARIANT_ID=miraclewm" >> %{buildroot}%{_prefix}/lib/os-release.miraclewm
sed -i -e "s|(%{release_name}%{?prerelease})|(MiracleWM%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.miraclewm
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://pagure.io/fedora-miracle/SIG/issues"|' %{buildroot}/%{_prefix}/lib/os-release.miraclewm
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/MiracleWM/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.miraclewm
# Add Fedora MiracleWM dnf protected packages list
install -Dm0644 %{SOURCE35} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with miraclewm_atomic}
cp -p os-release %{buildroot}%{_prefix}/lib/os-release.miraclewm-atomic
echo "VARIANT=\"MiracleWM Atomic\"" >> %{buildroot}%{_prefix}/lib/os-release.miraclewm-atomic
echo "VARIANT_ID=miraclewm-atomic" >> %{buildroot}%{_prefix}/lib/os-release.miraclewm-atomic
sed -i -e "s|(%{release_name}%{?prerelease})|(MiracleWM Atomic%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.miraclewm-atomic
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-sericea/"|' %{buildroot}%{_prefix}/lib/os-release.miraclewm-atomic
sed -i -e 's|HOME_URL=.*|HOME_URL="https://fedoraproject.org/atomic-desktops/miraclewm/"|' %{buildroot}/%{_prefix}/lib/os-release.miraclewm-atomic
sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://pagure.io/fedora-miracle/SIG/issues"|' %{buildroot}/%{_prefix}/lib/os-release.miraclewm-atomic
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/MiracleWMAtomic/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.miraclewm-atomic
%endif

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%__bootstrap         ~bootstrap
%if 0%{?eln}
%%rhel              %{rhel_dist_version}
%%el%{rhel_dist_version}                1
# Although eln is set in koji tags, we put it in the macros.dist file for local and mock builds.
%%eln              %{eln}
%%distcore            .eln%%{eln}
%else
%%fedora              %{dist_version}
%%fc%{dist_version}                1
%%distcore            .fc%%{fedora}
%endif
%%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?with_bootstrap:%%{__bootstrap}}
%%dist_vendor         %{dist_vendor}
%%dist_name           %{dist_name}
%%dist_home_url       %{dist_home_url}
%%dist_bug_report_url %{dist_bug_report_url}
%%dist_debuginfod_url %{dist_debuginfod_url}
EOF

# Install licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE

# Default system wide
install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
# The same file is installed in two places with identical contents
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/

# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%{bug_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-%{bug_version}.swidtag
install -d %{buildroot}%{_sysconfdir}/swid/swidtags.d
ln -s --relative %{buildroot}%{_swidtagdir} %{buildroot}%{_sysconfdir}/swid/swidtags.d/fedoraproject.org

# Install DNF 5 configuration defaults
install -Dm0644 %{SOURCE31} -t %{buildroot}%{_prefix}/share/dnf5/libdnf.conf.d/


%files common
%license licenses/LICENSE licenses/Fedora-Legal-README.txt
%{_prefix}/lib/fedora-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/fedora-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_prefix}/lib/systemd/user-preset/
%{_prefix}/lib/systemd/user-preset/90-default-user.preset
%{_prefix}/lib/systemd/user-preset/99-default-disable.preset
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%dir %{_swidtagdir}
%{_swidtagdir}/org.fedoraproject.Fedora-%{bug_version}.swidtag
%dir %{_sysconfdir}/swid
%{_sysconfdir}/swid/swidtags.d
%{_prefix}/share/dnf5/libdnf.conf.d/20-fedora-defaults.conf


%if %{with basic}
%files
%files identity-basic
%{_prefix}/lib/os-release.basic
%endif


%if %{with cinnamon}
%files cinnamon
%files identity-cinnamon
%{_prefix}/lib/os-release.cinnamon
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cinnamon
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with cloud}
%files cloud
%files identity-cloud
%{_prefix}/lib/os-release.cloud
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cloud
%endif


%if %{with compneuro}
%files compneuro
%files identity-compneuro
%{_prefix}/lib/os-release.compneuro
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.compneuro
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with container}
%files container
%files identity-container
%{_prefix}/lib/os-release.container
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.container
%endif


%if %{with coreos}
%files coreos
%files identity-coreos
%{_prefix}/lib/systemd/system-preset/80-coreos.preset
%{_prefix}/lib/systemd/system.conf.d/longer-default-shutdown-timeout.conf
%{_prefix}/lib/systemd/user.conf.d/longer-default-shutdown-timeout.conf
%{_prefix}/lib/os-release.coreos
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.coreos
%endif


%if %{with designsuite}
%files designsuite
%files identity-designsuite
%{_prefix}/lib/os-release.designsuite
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.designsuite
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with eln}
%files eln
%files identity-eln
%{_prefix}/lib/os-release.eln
%{_prefix}/lib/systemd/system-preset/80-server.preset
%{_prefix}/lib/systemd/system-preset/75-eln.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.eln
%endif


%if %{with iot}
%files iot
%files identity-iot
%{_prefix}/lib/os-release.iot
%{_prefix}/lib/systemd/system-preset/80-iot.preset
%{_prefix}/lib/systemd/user-preset/80-iot-user.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.iot
%{_prefix}/lib/zezere-ignition-url
%endif


%if %{with kde}
%files kde
%files identity-kde
%{_prefix}/lib/os-release.kde
%{_prefix}/lib/systemd/system-preset/80-kde.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde
%{_sysconfdir}/dnf/protected.d/plasma-desktop.conf
%endif

%if %{with kde_mobile}
%files kde-mobile
%files identity-kde-mobile
%{_prefix}/lib/os-release.kde-mobile
%{_prefix}/lib/systemd/system-preset/80-kde-mobile.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde-mobile
%{_sysconfdir}/dnf/protected.d/plasma-mobile.conf
%endif

%if %{with matecompiz}
%files matecompiz
%files identity-matecompiz
%{_prefix}/lib/os-release.matecompiz
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.matecompiz
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with server}
%files server
%files identity-server
%{_prefix}/lib/os-release.server
%{_prefix}/lib/systemd/system-preset/80-server.preset
%{_prefix}/lib/systemd/system.conf.d/longer-default-shutdown-timeout.conf
%{_prefix}/lib/systemd/user.conf.d/longer-default-shutdown-timeout.conf
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.server
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.override
%endif


%if %{with silverblue}
%files silverblue
%files identity-silverblue
%{_prefix}/lib/os-release.silverblue
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.silverblue
# Keep this in sync with workstation below
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%{_prefix}/lib/systemd/system-preset/80-workstation.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with kinoite}
%files kinoite
%files identity-kinoite
%{_prefix}/lib/os-release.kinoite
%{_prefix}/lib/systemd/system-preset/80-kde.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kinoite
%endif

%if %{with kinoite_mobile}
%files kinoite-mobile
%files identity-kinoite-mobile
%{_prefix}/lib/os-release.kinoite-mobile
%{_prefix}/lib/systemd/system-preset/80-kde-mobile.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kinoite-mobile
%endif

%if %{with ostree_desktop}
%files ostree-desktop
%attr(0644,root,root) %{_prefix}/share/polkit-1/rules.d/org.projectatomic.rpmostree1.rules
%endif


%if %{with snappy}
%files snappy
%files identity-snappy
%{_prefix}/lib/os-release.snappy
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.snappy
%endif


%if %{with soas}
%files soas
%files identity-soas
%{_prefix}/lib/os-release.soas
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.soas
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with toolbx}
%files toolbx
%files identity-toolbx
%{_prefix}/lib/os-release.toolbx
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.toolbx
%endif


%if %{with workstation}
%files workstation
%files identity-workstation
%{_prefix}/lib/os-release.workstation
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.workstation
%{_sysconfdir}/dnf/protected.d/fedora-workstation.conf
# Keep this in sync with silverblue above
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%{_prefix}/lib/systemd/system-preset/80-workstation.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with xfce}
%files xfce
%files identity-xfce
%{_prefix}/lib/os-release.xfce
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.xfce
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with i3}
%files i3
%files identity-i3
%{_prefix}/lib/os-release.i3
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.i3
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with lxqt}
%files lxqt
%files identity-lxqt
%{_prefix}/lib/os-release.lxqt
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.lxqt
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif

%if %{with budgie}
%files budgie
%files identity-budgie
%{_prefix}/lib/os-release.budgie
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.budgie
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with sway}
%files sway
%files identity-sway
%{_prefix}/lib/os-release.sway
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.sway
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%{_sysconfdir}/dnf/protected.d/fedora-sway.conf
%endif


%if %{with sway_atomic}
%files sway-atomic
%files identity-sway-atomic
%{_prefix}/lib/os-release.sway-atomic
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.sway-atomic
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif

%if %{with budgie_atomic}
%files budgie-atomic
%files identity-budgie-atomic
%{_prefix}/lib/os-release.budgie-atomic
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.budgie-atomic
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with mobility}
%files mobility
%files identity-mobility
%{_prefix}/lib/os-release.mobility
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.mobility
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%if %{with miraclewm}
%files miraclewm
%files identity-miraclewm
%{_prefix}/lib/os-release.miraclewm
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.miraclewm
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%{_sysconfdir}/dnf/protected.d/fedora-miraclewm.conf
%endif


%if %{with miraclewm_atomic}
%files miraclewm-atomic
%files identity-miraclewm-atomic
%{_prefix}/lib/os-release.miraclewm-atomic
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.miraclewm-atomic
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%changelog
%autochangelog
