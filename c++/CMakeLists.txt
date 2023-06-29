# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)
if (UNIX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -qopenmp")
endif()
set( BASE_FOLDER "Applications" )
add_subdirectory(luDecomp) 
#add_subdirectory(jacobiSolve) 
#add_subdirectory(sfComp) 