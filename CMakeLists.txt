# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)

project(
    CompilerCompare
    VERSION 0.1
    DESCRIPTION "Computational Kernels for Comparing Compilers vendors")
set(BLA "$ENV{I_MPI_ROOT}" )
message (STATUS "Found MPI ... ${BLA}")
include(FindMPI)

##set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DVERBOSE")
set(CMAKE_C_COMPILER ${BLA}\\bin\\mpicc.bat)
set (CMAKE_CXX_COMPILER ${BLA}\\bin\\mpiicpc.bat)

add_subdirectory(c++)   # look in hello subdirectory for CMakeLists.txt to process
#add_subdirectory(apps)    # look in apps subdirectory for CMakeLists.txt to process