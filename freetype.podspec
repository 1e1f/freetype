#
# Be sure to run `pod lib lint NodeKitten.podspec" to ensure this is a
# valid spec and remove all comments before submitting the spec.
#
# Any lines starting with a # are optional, but encouraged
#
# To learn more about a Podspec see http://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|

s.name             = "freetype"
s.version          = "2.6.0"
s.summary          = "FreeType is a freely available software library to render fonts."
s.homepage         = "http://www.freetype.org"
s.license          = "BSD"
s.author           = { "structuresound" => "leif@structuresound.com" }
s.source           = {:git => 'https://github.com/structuresound/freetype.git',
                      :tag => '2.6.0'
                     }
s.ios.deployment_target = "6.0"
s.osx.deployment_target = "10.9"

s.source_files =  "src/base/ftadvanc.c",
                  "src/base/ftadvanc.c",
                  "src/base/ftbbox.c",
                  "src/base/ftbitmap.c",
                  "src/base/ftcalc.c",
                  "src/base/ftcid.c",
                  "src/base/ftdbgmem.c",
                  "src/base/ftfstype.c",
                  "src/base/ftgasp.c",
                  "src/base/ftgloadr.c",
                  "src/base/ftglyph.c",
                  "src/base/ftgxval.c",
                  "src/base/ftinit.c",
                  "src/base/ftlcdfil.c",
                  "src/base/ftmm.c",
                  "src/base/ftobjs.c",
                  "src/base/ftotval.c",
                  "src/base/ftoutln.c",
                  "src/base/ftpatent.c",
                  "src/base/ftpfr.c",
                  "src/base/ftrfork.c",
                  "src/base/ftsnames.c",
                  "src/base/ftstream.c",
                  "src/base/ftstroke.c",
                  "src/base/ftsynth.c",
                  "src/base/ftsystem.c",
                  "src/base/fttrigon.c",
                  "src/base/fttype1.c",
                  "src/base/ftutil.c",
                  "src/base/ftwinfnt.c",
                  "include/*.h",
                  "src/truetype/*.h",
                  "src/sfnt/*.h",
                  "src/autofit/*.h",
                  "src/smooth/*.h",
                  "src/raster/*.h",
                  "src/psaux/*.h",
                  "src/psnames/*.h",
                  "src/autofit/autofit.{h,c}",
                  "src/bdf/bdf.{h,c}",
                  "src/cff/cff.{h,c}",
                  "src/cid/type1cid.{h,c}",
                  "src/gzip/ftgzip.{h,c}",
                  "src/lzw/ftlzw.{h,c}",
                  "src/pcf/pcf.{h,c}",
                  "src/pfr/pfr.{h,c}",
                  "src/psaux/psaux.{h,c}",
                  "src/pshinter/pshinter.{h,c}",
                  "src/psnames/psmodule.{h,c}",
                  "src/raster/raster.{h,c}",
                  "src/sfnt/sfnt.{h,c}",
                  "src/smooth/smooth.{h,c}",
                  "src/truetype/truetype.{h,c}",
                  "src/type1/type1.{h,c}",
                  "src/type42/type42.{h,c}",
                  "src/winfonts/winfnt.{h,c}"

s.compiler_flags = '-DFT2_BUILD_LIBRARY=1 -DDARWIN_NO_CARBON -DFT_CONFIG_OPTION_SYSTEM_ZLIB=1'
s.xcconfig = { "HEADER_SEARCH_PATHS" => "$(PODS_ROOT)/include" }
s.libraries = "z"
s.xcconfig  =  { "CLANG_CXX_LIBRARY" => "libc++",
                 "CLANG_CXX_LANGUAGE_STANDARD" => "c++14",
                 "GCC_OPTIMIZATION_LEVEL" => "3"
                 }

end
