cmdUbuntu = [
    "sudo apt update",
    "sudo apt-get install libavahi-client-dev libavahi-glib-dev",
    "sudo apt-get install dos2unix",
    "sudo apt-get install autoconf",
    "sudo apt-get install libtiff5-dev",
    "sudo apt-get install libusb-1.0-0-dev",
    "sudo apt-get install libtool",
    "sudo apt-get install libssl1.1.1",
    "sudo apt-get install xsane",
    "sudo apt-get install libssl-dev"
]

cmdFedora =[
    "dnf upgrade",
    "dnf install libusb-devel @development-tools sane backends-devel",
    "dnf install avahi-devel avahi-glib-devel",
    "dnf install dos2unix",
    "dnf install autoconf",
    "dnf install libtiff-devel",
    "dnf install libusb1-devel",
    "dnf install libtool",
    "dnf install openssl",
    "dnf install xsane",
    "dnf isntall openssl-devel"
]

cmdOpenSUSE = [
    "sudo zypper update",
    "sudo zypper install libusb-deve; sane-backends-devel",
    "sudo zypper install -t pattern devel_C_C++",
    "sudo zypper install dos2unix",
    "sudo zypper install autoconf",
    "sudo zypper install libtiff-devel",
    "sudo zypper install libusb1-devel",
    "sudo zypper install libtool",
    "sudo zypper install openssl",
    "sudo zypper install xsane",
    "sudo zypper install openssl-devel"
]

substring = [
    "Ubuntu",
    "Fedora",
    "OpenSuse"
]