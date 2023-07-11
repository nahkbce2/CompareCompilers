# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D__ALGORITHM__=KIJ_OPT_REG")

set( TARGET_NAME "luDecomp" )

file(GLOB SOURCES
    *.h
    *.cpp
)


add_executable(${TARGET_NAME} ${SOURCES})
# We need hello.h and the hello library
#target_link_libraries(${TARGET_NAME}
#    PRIVATE ${MPI_impi_LIBRARY})

# Tell C++ compiler to use C++20 features. We don't actually use any of them.
target_compile_features(${TARGET_NAME} PUBLIC cxx_std_14)
#target_include_directories (${TARGET_NAME} PUBLIC ${MPI_CXX_INCLUDE_DIRS})