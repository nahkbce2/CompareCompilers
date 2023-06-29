# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)

set( BASE_FOLDER "Applications" )
add_subdirectory(luDecomp) 
#add_subdirectory(jacobiSolve) 
#add_subdirectory(sfComp) 