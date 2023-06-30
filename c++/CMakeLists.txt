# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)
if (UNIX)
    if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "IntelLLVM" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")
    message(WARNING "Intel tools ${CMAKE_CXX_COMPILER_ID}")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -qopenmp -qopenmp-simd -qopt-report=5 -qopt-assume-safe-padding -xCORE-AVX512 -qopt-zmm-usage=high")
        #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -qopenmp")
    else()
    message(WARNING "Other tools ${CMAKE_CXX_COMPILER_ID}")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64 -ffast-math -fassociative-math -mfma -ffp-contract=fast -fopenmp=libomp -Rpass=loop-vectorize -Rpass-missed=loop-vectorize -Rpass-analysis=loop-vectorize -fsave-optimization-record -gline-tables-only -gcolumn-info -march=skylake-avx512")
    endif()
endif()

set( BASE_FOLDER "Applications" )
add_subdirectory(luDecomp) 
#add_subdirectory(jacobiSolve) 
#add_subdirectory(sfComp) 