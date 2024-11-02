cmake_minimum_required(VERSION 3.25)

project(ThriftPythonDistributions NONE)

include(ExternalProject)
include(${CMAKE_SOURCE_DIR}/ThriftUrls.cmake)

set(THRIFT_SOURCE_DIR "${CMAKE_BINARY_DIR}/thrift-src")
set(THRIFT_COMPILED_DIR "${CMAKE_BINARY_DIR}/thrift-compiled")

IF (WIN32)
    ExternalProject_add(Thrift-source-download
        SOURCE_DIR "${THRIFT_SOURCE_DIR}"
        URL "${source_url}"
        URL_HASH "SHA256=${source_sha256}"
        DOWNLOAD_DIR ""
        DOWNLOAD_EXTRACT_TIMESTAMP 1
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
    )
    ExternalProject_add(Thrift-windows-download
	    DOWNLOAD_DIR "${THRIFT_SOURCE_DIR}"
	    DOWNLOAD_NAME "thrift.exe"
        URL "${windows_binary_url}"
        URL_HASH "SHA256=${windows_sha256}"
        DOWNLOAD_NO_EXTRACT 1
	    CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
    )
    install(PROGRAMS "${THRIFT_SOURCE_DIR}/thrift.exe" DESTINATION ${SKBUILD_SCRIPTS_DIR})
ELSE()
    ExternalProject_add(Thrift-source-download
        SOURCE_DIR "${THRIFT_SOURCE_DIR}"
        URL "${source_url}"
        URL_HASH "SHA256=${source_sha256}"
        DOWNLOAD_DIR ""
        DOWNLOAD_EXTRACT_TIMESTAMP 1
        CONFIGURE_COMMAND autoreconf -i COMMAND ./bootstrap.sh COMMAND ./configure --disable-debug --disable-libs --prefix "${THRIFT_COMPILED_DIR}"
        BUILD_COMMAND $(MAKE)
        BUILD_IN_SOURCE 1
        INSTALL_COMMAND $(MAKE) install-strip
    )
    install(PROGRAMS "${THRIFT_COMPILED_DIR}/bin/thrift" DESTINATION ${SKBUILD_SCRIPTS_DIR})
ENDIF()
install(FILES "${THRIFT_SOURCE_DIR}/LICENSE" "${THRIFT_SOURCE_DIR}/NOTICE" DESTINATION "${SKBUILD_METADATA_DIR}/licenses/thrift")
