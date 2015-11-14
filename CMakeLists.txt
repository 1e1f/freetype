# CMakeLists.txt
#
# Copyright 2013, 2014 by
# David Turner, Robert Wilhelm, and Werner Lemberg.
#
# Written by John Cary <cary@txcorp.com>
#
# This file is part of the FreeType project, and may only be used, modified,
# and distributed under the terms of the FreeType project license,
# LICENSE.TXT.  By continuing to use, modify, or distribute this file you
# indicate that you have read the license and understand and accept it
# fully.
#
#
# Say
#
#   cmake CMakeLists.txt
#
# to create a Makefile that builds a static version of the library.  For a
# dynamic library, use
#
#   cmake CMakeLists.txt -DBUILD_SHARED_LIBS:BOOL=true
#
# instead.  Please refer to the cmake manual for further options, in
# particular, how to modify compilation and linking parameters.
#
# Some notes.
#
# . `cmake' will overwrite FreeType's original (top-level) `Makefile' file.
#
# . You can use `cmake' directly on a freshly cloned FreeType git
#   repository.
#
# . `CMakeLists.txt'  is provided as-is since it is not used by the
#   developer team.

#This CMakeLists.txt have been modified by Miguel Hernando to include biicode support



cmake_minimum_required(VERSION 2.6)


project(freetype)


set(VERSION_MAJOR "2")
set(VERSION_MINOR "5")
set(VERSION_PATCH "3")
set(PROJECT_VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH})

# Compiler definitions for building the library
add_definitions(-DFT2_BUILD_LIBRARY)

# Specify library include directories
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")




IF(NOT BIICODE)
#this part is removed because there is no a real configuration (no checks) except unix. Biicode uses the default config files
# For the auto-generated ftconfig.h file
# Create the configuration file
message(STATUS "Creating directory, ${CMAKE_CURRENT_BINARY_DIR}/include.")
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/include)
include_directories("${CMAKE_CURRENT_BINARY_DIR}/include")
message(STATUS "Creating ${CMAKE_CURRENT_BINARY_DIR}/include/ftconfig.h.")
execute_process(
  COMMAND sed -e "s/FT_CONFIG_OPTIONS_H/<ftoption.h>/" -e "s/FT_CONFIG_STANDARD_LIBRARY_H/<ftstdlib.h>/" -e "s?/undef ?#undef ?"
  INPUT_FILE ${CMAKE_CURRENT_SOURCE_DIR}/builds/unix/ftconfig.in
  OUTPUT_FILE ${CMAKE_CURRENT_BINARY_DIR}/include/ftconfig.h
)
ENDIF()

set(BASE_SRCS
  src/autofit/autofit.c
  src/base/ftadvanc.c
  src/base/ftbbox.c
  src/base/ftbitmap.c
  src/base/ftcalc.c
  src/base/ftcid.c
  src/base/ftdbgmem.c
  src/base/ftdebug.c
  src/base/ftfstype.c
  src/base/ftgasp.c
  src/base/ftgloadr.c
  src/base/ftglyph.c
  src/base/ftgxval.c
  src/base/ftinit.c
  src/base/ftlcdfil.c
  src/base/ftmm.c
  src/base/ftobjs.c
  src/base/ftotval.c
  src/base/ftoutln.c
  src/base/ftpatent.c
  src/base/ftpfr.c
  src/base/ftrfork.c
  src/base/ftsnames.c
  src/base/ftstream.c
  src/base/ftstroke.c
  src/base/ftsynth.c
  src/base/ftsystem.c
  src/base/fttrigon.c
  src/base/fttype1.c
  src/base/ftutil.c
  src/base/ftwinfnt.c
  src/base/ftxf86.c
  src/bdf/bdf.c
  src/bzip2/ftbzip2.c
  src/cache/ftcache.c
  src/cff/cff.c
  src/cid/type1cid.c
  src/gzip/ftgzip.c
  src/lzw/ftlzw.c
  src/pcf/pcf.c
  src/pfr/pfr.c
  src/psaux/psaux.c
  src/pshinter/pshinter.c
  src/psnames/psmodule.c
  src/raster/raster.c
  src/sfnt/sfnt.c
  src/smooth/smooth.c
  src/truetype/truetype.c
  src/type1/type1.c
  src/type42/type42.c
  src/winfonts/winfnt.c
)

include_directories("src/truetype")
include_directories("src/sfnt")
include_directories("src/autofit")
include_directories("src/smooth")
include_directories("src/raster")
include_directories("src/psaux")
include_directories("src/psnames")

IF(WIN32)
    IF(BII_BLOCK_EXES)
    list(REMOVE_ITEM BII_BLOCK_EXES  src_tools_ftrandom_ftrandom)
    ENDIF()
ENDIF()

IF(BIICODE)
    #prueba
    ##SET(BII_LIB_SRC ${BASE_SRCS})
    DISABLE_BII_IMPLICIT_RULES()
    SET(BII_IMPLICIT_RULES_ENABLED OFF PARENT_SCOPE)
    BII_FILTER_LIB_SRC(BASE_SRCS)
    ADD_BIICODE_TARGETS()
    # Specify library include directories
    target_include_directories(${BII_LIB_TARGET} PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")
ELSE(BIICODE)
    add_library(freetype ${BASE_SRCS})

    # Installations
    # Note the trailing slash in the argument to the `DIRECTORY' directive
    install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
      DESTINATION include/freetype2
      PATTERN "internal" EXCLUDE
    )
    install(TARGETS freetype
      RUNTIME DESTINATION bin
      LIBRARY DESTINATION lib
      ARCHIVE DESTINATION lib
    )

    # Packaging
    # CPack version numbers for release tarball name.
    set(CPACK_PACKAGE_VERSION_MAJOR ${VERSION_MAJOR})
    set(CPACK_PACKAGE_VERSION_MINOR ${VERSION_MINOR})
    set(CPACK_PACKAGE_VERSION_PATCH ${VERSION_PATCH}})
    if (NOT DEFINED CPACK_PACKAGE_DESCRIPTION_SUMMARY)
      set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "${CMAKE_PROJECT_NAME}")
    endif ()
    if (NOT DEFINED CPACK_SOURCE_PACKAGE_FILE_NAME)
      set(CPACK_SOURCE_PACKAGE_FILE_NAME
        "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION}-r${PROJECT_REV}"
        CACHE INTERNAL "tarball basename"
      )
    endif ()
    set(CPACK_SOURCE_GENERATOR TGZ)
    set(CPACK_SOURCE_IGNORE_FILES
      "/CVS/;/.svn/;.swp$;.#;/#;/build/;/serial/;/ser/;/parallel/;/par/;~;/preconfig.out;/autom4te.cache/;/.config")
    set(CPACK_GENERATOR TGZ)
    include(CPack)

    # add make dist target
    add_custom_target(dist COMMAND ${CMAKE_MAKE_PROGRAM} package_source)
ENDIF(BIICODE)
# eof