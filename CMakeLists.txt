cmake_minimum_required(VERSION 3.25)

project(ThriftPythonDistributions NONE)

include(ExternalProject)
include(${CMAKE_SOURCE_DIR}/ThriftUrls.cmake)

set(THRIFT_SOURCE_DIR "${CMAKE_BINARY_DIR}/thrift-src")
set(THRIFT_COMPILED_DIR "${CMAKE_BINARY_DIR}/thrift-compiled")

IF (WIN32)
    ExternalProject_add(Thrift-windows-download
	    DOWNLOAD_DIR "${THRIFT_SOURCE_DIR}"
	    DOWNLOAD_NAME "thrift.exe"
        URL "${windows_binary_url}"
        URL_HASH "SHA256=${windows_sha256}"
        USES_TERMINAL_DOWNLOAD 1
        DOWNLOAD_NO_EXTRACT 1
	    CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
    )
    install(PROGRAMS "${THRIFT_SOURCE_DIR}/thrift.exe" DESTINATION ${SKBUILD_SCRIPTS_DIR})
ELSE()
    ExternalProject_add(Thrift-unix-download
        SOURCE_DIR "${THRIFT_SOURCE_DIR}"
        URL "${unix_source_url}"
        URL_HASH "SHA256=${unix_sha256}"
        DOWNLOAD_DIR ""
        USES_TERMINAL_DOWNLOAD 1
        DOWNLOAD_EXTRACT_TIMESTAMP 1
        CONFIGURE_COMMAND "${CMAKE_SOURCE_DIR}/configure_thrift.sh" ${THRIFT_SOURCE_DIR} ${THRIFT_COMPILED_DIR}
        BUILD_COMMAND $(MAKE)
        BUILD_IN_SOURCE 1
        INSTALL_COMMAND $(MAKE) install-strip
    )
    install(PROGRAMS "${THRIFT_COMPILED_DIR}/bin/thrift" DESTINATION ${SKBUILD_SCRIPTS_DIR})
ENDIF()