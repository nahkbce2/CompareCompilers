# version 3.11 or later of CMake needed later for installing GoogleTest
# so let's require it now.
cmake_minimum_required(VERSION 3.11-3.18)


set( TARGET_NAME "luDecomp" )

file(GLOB SOURCES
    *.h
    *.cpp
)


add_executable(${TARGET_NAME} ${SOURCES})