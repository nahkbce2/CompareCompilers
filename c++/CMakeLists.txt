# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)
if (UNIX)
    if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "IntelLLVM" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")
    message(WARNING "Intel tools ${CMAKE_CXX_COMPILER_ID}")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -qopenmp")
    else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp=libomp -m64")
    endif()
endif()

set( BASE_FOLDER "Applications" )
add_subdirectory(luDecomp) 
#add_subdirectory(jacobiSolve) 
#add_subdirectory(sfComp) 