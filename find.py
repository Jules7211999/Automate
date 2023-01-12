import os

library = [
    "libjxrglue.so.0",
    "libjpegxr.so.0",
    "libraw.so.16",
    "liblcms2.so.2",
    "libgomp.so.1",
    "libdl.so.2",
    "libwebp.so.6",
    "libIlmImf-2_2.so.22",
    "libIlmThread-2_2.so.12",
    "libHalf.so.12",
    "libIex-2_2.so.12"
]
for x in library:
    
    os.system("find /lib /usr/lib -name 'lib*' "+ x)
