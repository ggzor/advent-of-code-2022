cmake_minimum_required(VERSION 3.24)

project(
  "AoC2022"
  VERSION 0.0.1
  LANGUAGES C CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# This is required to pick up library headers
# See: https://gitlab.kitware.com/cmake/cmake/-/issues/20912
if(CMAKE_EXPORT_COMPILE_COMMANDS)
    set(CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES ${CMAKE_CXX_IMPLICIT_INCLUDE_DIRECTORIES})
endif()

find_package(range-v3 REQUIRED)
find_package(fmt REQUIRED)

add_executable(01 01/01.cpp)
target_link_libraries(01 PRIVATE fmt::fmt range-v3::range-v3)
