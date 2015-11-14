import os
import fileinput
#these are ifndef

config_equivalence={"FT_CONFIG_CONFIG_H":"<ftconfig.h>",
"FT_CONFIG_STANDARD_LIBRARY_H":"<ftstdlib.h>",
"FT_CONFIG_OPTIONS_H":"<ftoption.h>",
"FT_CONFIG_MODULES_H":"<ftmodule.h>"}

define_equivalence = {"FT_FREETYPE_H":"<freetype.h>",
"FT_ERRORS_H":"<fterrors.h>",
"FT_MODULE_ERRORS_H":"<ftmoderr.h>",
"FT_SYSTEM_H":"<ftsystem.h>",
"FT_IMAGE_H":"<ftimage.h>",
"FT_TYPES_H":"<fttypes.h>",
"FT_LIST_H":"<ftlist.h>",
"FT_OUTLINE_H":"<ftoutln.h>",
"FT_SIZES_H":"<ftsizes.h>",
"FT_MODULE_H":"<ftmodapi.h>",
"FT_RENDER_H":"<ftrender.h>",
"FT_AUTOHINTER_H":"<ftautoh.h>",
"FT_CFF_DRIVER_H":"<ftcffdrv.h>",
"FT_SERVICE_FONT_FORMAT_H":"<svfntfmt.h>",
"FT_TRUETYPE_DRIVER_H":"<ftttdrv.h>",
"FT_TYPE1_TABLES_H":"<t1tables.h>",
"FT_TRUETYPE_IDS_H":"<ttnameid.h>",
"FT_TRUETYPE_TABLES_H":"<tttables.h>",
"FT_TRUETYPE_TAGS_H":"<tttags.h>",
"FT_BDF_H":"<ftbdf.h>",
"FT_CID_H":"<ftcid.h>",
"FT_GZIP_H":"<ftgzip.h>",
"FT_LZW_H":"<ftlzw.h>",
"FT_BZIP2_H":"<ftbzip2.h>",
"FT_WINFONTS_H":"<ftwinfnt.h>",
"FT_GLYPH_H":"<ftglyph.h>",
"FT_BITMAP_H":"<ftbitmap.h>",
"FT_BBOX_H":"<ftbbox.h>",
"FT_CACHE_H":"<ftcache.h>",
"FT_CACHE_IMAGE_H":"<ftcache.h>",
"FT_CACHE_SMALL_BITMAPS_H":"<ftcache.h>",
"FT_CACHE_CHARMAP_H":"<ftcache.h>",
"FT_MAC_H":"<ftmac.h>",
"FT_MULTIPLE_MASTERS_H":"<ftmm.h>",
"FT_SFNT_NAMES_H":"<ftsnames.h>",
"FT_OPENTYPE_VALIDATE_H":"<ftotval.h>",
"FT_GX_VALIDATE_H":"<ftgxval.h>",
"FT_PFR_H":"<ftpfr.h>",
"FT_STROKER_H":"<ftstroke.h>",
"FT_SYNTHESIS_H":"<ftsynth.h>",
"FT_XFREE86_H":"<ftxf86.h>",
"FT_TRIGONOMETRY_H":"<fttrigon.h>",
"FT_LCD_FILTER_H":"<ftlcdfil.h>",
"FT_UNPATENTED_HINTING_H":"<ttunpat.h>",
"FT_INCREMENTAL_H":"<ftincrem.h>",
"FT_GASP_H":"<ftgasp.h>",
"FT_ADVANCES_H":"<ftadvanc.h>",
"FT_ERROR_DEFINITIONS_H":"<fterrdef.h>",
"FT_CACHE_MANAGER_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_MRU_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_MANAGER_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_CACHE_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_GLYPH_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_IMAGE_H":"<ftcache.h>",
"FT_CACHE_INTERNAL_SBITS_H":"<ftcache.h>",
"FT_INCREMENTAL_H":"<ftincrem.h>",
"FT_TRUETYPE_UNPATENTED_H":"<ttunpat.h>",
"FT_INTERNAL_INTERNAL_H":"<internal.h>",
"FT_INTERNAL_OBJECTS_H":"<ftobjs.h>",
"FT_INTERNAL_PIC_H":"<ftpic.h>",
"FT_INTERNAL_STREAM_H":"<ftstream.h>",
"FT_INTERNAL_MEMORY_H":"<ftmemory.h>",
"FT_INTERNAL_DEBUG_H":"<ftdebug.h>",
"FT_INTERNAL_CALC_H":"<ftcalc.h>",
"FT_INTERNAL_DRIVER_H":"<ftdriver.h>",
"FT_INTERNAL_TRACE_H":"<fttrace.h>",
"FT_INTERNAL_GLYPH_LOADER_H":"<ftgloadr.h>",
"FT_INTERNAL_SFNT_H":"<sfnt.h>",
"FT_INTERNAL_SERVICE_H":"<ftserv.h>",
"FT_INTERNAL_RFORK_H":"<ftrfork.h>",
"FT_INTERNAL_VALIDATE_H":"<ftvalid.h>",
"FT_INTERNAL_TRUETYPE_TYPES_H":"<tttypes.h>",
"FT_INTERNAL_TYPE1_TYPES_H":"<t1types.h>",
"FT_INTERNAL_POSTSCRIPT_AUX_H":"<psaux.h>",
"FT_INTERNAL_POSTSCRIPT_HINTS_H":"<pshints.h>",
"FT_INTERNAL_POSTSCRIPT_GLOBALS_H":"<psglobal.h>",
"FT_INTERNAL_AUTOHINT_H":"<autohint.h>",
"FT_SERVICE_BDF_H":"<svbdf.h>",
"FT_SERVICE_CID_H":"<svcid.h>",
"FT_SERVICE_GLYPH_DICT_H":"<svgldict.h>",
"FT_SERVICE_GX_VALIDATE_H":"<svgxval.h>",
"FT_SERVICE_KERNING_H":"<svkern.h>",
"FT_SERVICE_MULTIPLE_MASTERS_H":   "<svmm.h>",
"FT_SERVICE_OPENTYPE_VALIDATE_H":  "<svotval.h>",
"FT_SERVICE_PFR_H":                "<svpfr.h>",
"FT_SERVICE_POSTSCRIPT_CMAPS_H":   "<svpscmap.h>",
"FT_SERVICE_POSTSCRIPT_INFO_H":    "<svpsinfo.h>",
"FT_SERVICE_POSTSCRIPT_NAME_H":    "<svpostnm.h>",
"FT_SERVICE_PROPERTIES_H":         "<svprop.h>",
"FT_SERVICE_SFNT_H":               "<svsfnt.h>",
"FT_SERVICE_TRUETYPE_ENGINE_H":    "<svtteng.h>",
"FT_SERVICE_TT_CMAP_H":            "<svttcmap.h>",
"FT_SERVICE_WINFNT_H":             "<svwinfnt.h>",
"FT_SERVICE_XFREE86_NAME_H":       "<svxf86nm.h>",
"FT_SERVICE_TRUETYPE_GLYF_H":      "<svttglyf.h>"}

flatten_includes = {
"internal/": "",
"services/": "",
"config/": ""
}

import sys

from tempfile import mkstemp
from shutil import move
from os import remove, close
import sys

def replace_includes(source_file_path):
    fh, target_file_path = mkstemp()
    target_file= open(target_file_path, 'w')
    source_file= open(source_file_path, 'r')
    for line in source_file:
    #check only the lines with includes
        if line.startswith("#include"):
        #replacing text
            for key in define_equivalence:
                line = line.replace(key, define_equivalence[key])
            for key in config_equivalence:
                line = line.replace(key, config_equivalence[key])
            for key in flatten_includes:
                line = line.replace(key, flatten_includes[key])
        target_file.write(line)
    target_file.close()
    close(fh)
    source_file.close()

    #move(target_file_path, "%s_out.txt"%source_file_path)
    remove(source_file_path)
    move(target_file_path, source_file_path)

def process_files(src_dir):
    for folder, subs, files in os.walk(src_dir):
        for filename in files:
            if filename.endswith(('.c','.h')):
                replace_includes(os.path.join(folder, filename))

def flattenIncludes(include_dir):
    for folder, subs, files in os.walk(include_dir):
        for filename in files:
            if filename.endswith(('.h')):
                source_path = os.path.join(folder, filename)
                target_path = os.path.join(include_dir, filename)
                move(source_path, target_path)
                print("move " + source_path + " to " + target_path)

def fix_gxvfgen():
    fh, target_file_path = mkstemp()
    source_file_path = "../src/gxvalid/gxvfgen.c"
    target_file= open(target_file_path, 'w')
    source_file= open(source_file_path, 'r')
    file_data = source_file.read()
    new_data = file_data.replace("ft_strncmp","strncmp")
    target_file.write(new_data)
    target_file.close()
    close(fh)
    source_file.close()
    remove(source_file_path)
    move(target_file_path, source_file_path)
#minor bug modification: strncmp ft_strncmp to strncmp  in src/gxvalid/gxvfgen
def fix_zutil():
    fh, target_file_path = mkstemp()
    source_file_path = "../src/gzip/zutil.h"
    target_file= open(target_file_path, 'w')
    source_file= open(source_file_path, 'r')
    file_data = source_file.read()
    new_data = file_data.replace("#ifdef DEBUG","#if defined(DEBUG) && !defined(ANDROID)")
    target_file.write(new_data)
    target_file.close()
    close(fh)
    source_file.close()
    remove(source_file_path)
    move(target_file_path, source_file_path)

if __name__ == '__main__':
   #process_files("test/")
   process_files("../src/")
   process_files("../include/")
   flattenIncludes("../include/")
   fix_gxvfgen()
   fix_zutil()
   print("ADAPTATION DONE!")
