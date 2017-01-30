Name     : jdk-libfb303
Version  : 0.9.2
Release  : 2
URL      : http://repo1.maven.org/maven2/org/apache/thrift/libfb303/0.9.2/libfb303-0.9.2.jar
Source0  : http://repo1.maven.org/maven2/org/apache/thrift/libfb303/0.9.2/libfb303-0.9.2.jar
Source1  : http://repo1.maven.org/maven2/org/apache/thrift/libfb303/0.9.2/libfb303-0.9.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-libfb303-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-libfb303 package.
Group: Data

%description data
data components for the jdk-libfb303 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/libfb303.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/libfb303.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/libfb303.xml \
%{buildroot}/usr/share/maven-poms/libfb303.pom \
%{buildroot}/usr/share/java/libfb303.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/libfb303.jar
/usr/share/maven-metadata/libfb303.xml
/usr/share/maven-poms/libfb303.pom
