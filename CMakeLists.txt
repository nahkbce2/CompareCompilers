# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)

project(
    CompilerCompare
    VERSION 0.1
    DESCRIPTION "Computational Kernels for Comparing Compilers vendors: https://colfaxresearch.com/compiler-comparison/")


option(BUILD_WITH_MPI_WRAPPERS "Build the mpi wrappers" OFF)
set(BLA "$ENV{I_MPI_ROOT}" )
message (STATUS "Found MPI ... ${BLA}")
include(FindMPI)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D__ALGORITHM__=KIJ_OPT_REG")

if(BUILD_WITH_MPI_WRAPPERS)
    if (UNIX AND "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")
        set(CMAKE_C_COMPILER ${BLA}/bin/mpiicc)
        set (CMAKE_CXX_COMPILER ${BLA}/bin/mpiicpc)
    elseif(WIN32)
        set(CMAKE_C_COMPILER ${BLA}\\bin\\mpicc.bat)
        set (CMAKE_CXX_COMPILER ${BLA}\\bin\\mpiicpc.bat)
    #else()#for everything else uspe openmpi
    #    set(CMAKE_C_COMPILER $ENV{EBROOTOPENMPI}/bin/mpicc)
    #    set (CMAKE_CXX_COMPILER $ENV{EBROOTOPENMPI}/bin/mpic++)
    endif()
endif()

add_subdirectory(c++)   # look in hello subdirectory for CMakeLists.txt to process
#add_subdirectory(apps)    # look in apps subdirectory for CMakeLists.txt to process