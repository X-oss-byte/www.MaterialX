set(MATERIALX_MODULE_NAME MaterialXglTF)

include_directories(
    ${EXTERNAL_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/../)

file(GLOB materialx_source "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
file(GLOB materialx_headers "${CMAKE_CURRENT_SOURCE_DIR}/*.h*")

assign_source_group("Source Files" ${materialx_source})
assign_source_group("Header Files" ${materialx_headers})

if(POLICY CMP0072)
    cmake_policy(SET CMP0072 NEW)
endif()

# Disable OpenGL deprecation warnings on Clang.
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wno-deprecated-declarations)
endif()

add_library(${MATERIALX_MODULE_NAME} ${materialx_source} ${materialx_headers})

set_target_properties(
    ${MATERIALX_MODULE_NAME} PROPERTIES
    OUTPUT_NAME ${MATERIALX_MODULE_NAME}${MATERIALX_LIBNAME_SUFFIX}
    COMPILE_FLAGS "${EXTERNAL_COMPILE_FLAGS}"
    LINK_FLAGS "${EXTERNAL_LINK_FLAGS}"
    INSTALL_RPATH "${MATERIALX_SAME_DIR_RPATH}"
    VERSION "${MATERIALX_LIBRARY_VERSION}"
    SOVERSION "${MATERIALX_MAJOR_VERSION}")

target_link_libraries(
    ${MATERIALX_MODULE_NAME}
    MaterialXCore
    MaterialXFormat
    MaterialXGenShader
    MaterialXRender
    ${CMAKE_DL_LIBS})

if(NOT SKBUILD)
    install(TARGETS ${MATERIALX_MODULE_NAME}
        EXPORT MaterialX
        ARCHIVE DESTINATION ${MATERIALX_INSTALL_LIB_PATH}
        LIBRARY DESTINATION ${MATERIALX_INSTALL_LIB_PATH}
        RUNTIME DESTINATION bin)

    install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_BUILD_TYPE}/${MATERIALX_MODULE_NAME}.pdb"
        DESTINATION "${MATERIALX_INSTALL_LIB_PATH}/" OPTIONAL)

     install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/"
        DESTINATION ${MATERIALX_INSTALL_INCLUDE_PATH}/${MATERIALX_MODULE_NAME}/ 
        FILES_MATCHING PATTERN "*.h*")   
endif()