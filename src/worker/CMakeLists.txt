cmake_minimum_required(VERSION 3.2.0)
project(worker VERSION 0.1.0)

set(JSON_BuildTests OFF CACHE INTERNAL "")
set(JSON_Install OFF CACHE INTERNAL "")
add_subdirectory(libs/json)

add_library(worker STATIC worker.cpp)
target_link_libraries(worker PUBLIC nlohmann_json::nlohmann_json)

add_executable(BuildWorkerPyramid main.cpp)
target_link_libraries(BuildWorkerPyramid PRIVATE worker)

enable_testing()
add_test(NAME full COMMAND BuildWorkerPyramid test/full.json ${CMAKE_BINARY_DIR}/fullRst.json)
add_test(NAME medium COMMAND BuildWorkerPyramid test/medium.json ${CMAKE_BINARY_DIR}/mediumRst.json)
