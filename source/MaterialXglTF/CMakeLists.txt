include_directories(
    ${EXTERNAL_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/../)

file(GLOB materialx_source "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
file(GLOB materialx_headers "${CMAKE_CURRENT_SOURCE_DIR}/*.h*")

if(POLICY CMP0072)
    cmake_policy(SET CMP0072 NEW)
endif()

# Disable OpenGL deprecation warnings on Clang.
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wno-deprecated-declarations)
endif()

add_library(MaterialXglTF ${materialx_source} ${materialx_headers})

target_link_libraries(
    MaterialXglTF
    MaterialXCore
    MaterialXGenShader
    MaterialXRender
    ${CMAKE_DL_LIBS})

set_target_properties(
    MaterialXglTF PROPERTIES
    OUTPUT_NAME MaterialXglTF${MATERIALX_LIBNAME_SUFFIX}
    COMPILE_FLAGS "${EXTERNAL_COMPILE_FLAGS}"
    LINK_FLAGS "${EXTERNAL_LINK_FLAGS}"
    VERSION "${MATERIALX_LIBRARY_VERSION}"
    SOVERSION "${MATERIALX_MAJOR_VERSION}")



install(TARGETS MaterialXglTF
    EXPORT MaterialX
    ARCHIVE DESTINATION ${MATERIALX_INSTALL_LIB_PATH}
    LIBRARY DESTINATION ${MATERIALX_INSTALL_LIB_PATH}
    RUNTIME DESTINATION bin)

 install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/"
    DESTINATION ${MATERIALX_INSTALL_INCLUDE_PATH}/MaterialXglTF/ 
    FILES_MATCHING PATTERN "*.h*")   
