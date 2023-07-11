# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)

##set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D__ALGORITHM__=SOLVE_OPT")


set( TARGET_NAME "JacobiSolve" )

file(GLOB SOURCES
    grid.cpp
    critical.cpp
    jacobi.cpp
    jacobiSolve.cpp
)

#env.Append(CPPFLAGS=['-std=c++14', '-stdlib=libc++', '-m64', '-flto', '-ffast-math', '-fassociative-math', '-mfma', '-ffp-contract=fast', '-fopenmp=libomp', '-Rpass=loop-vectorize', '-Rpass-missed=loop-vectorize', '-Rpass-analysis=loop-vectorize','-fsave-optimization-record', '-gline-tables-only', '-gcolumn-info'] + pollyFlags)
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "IntelLLVM")
    #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -flto")
    SET(GCC_COVERAGE_LINK_FLAGS "-flto -fuse-ld=lld")
    SET(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}")
endif()

add_executable(${TARGET_NAME} ${SOURCES})
# We need hello.h and the hello library
#target_link_libraries(${TARGET_NAME}
#    PRIVATE ${MPI_impi_LIBRARY})

# Tell C++ compiler to use C++20 features. We don't actually use any of them.
target_compile_features(${TARGET_NAME} PUBLIC cxx_std_14)
#target_include_directories (${TARGET_NAME} PUBLIC ${MPI_CXX_INCLUDE_DIRS})