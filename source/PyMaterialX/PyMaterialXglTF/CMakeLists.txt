file(GLOB pymaterialxgltf_source "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
file(GLOB pymaterialxgltf_headers "${CMAKE_CURRENT_SOURCE_DIR}/*.h")

pybind11_add_module(PyMaterialXglTF SHARED ${PYBIND11_MODULE_FLAGS} ${pymaterialxgltf_source} ${pymaterialxgltf_headers})

if(APPLE)
    set_target_properties(PyMaterialXglTF PROPERTIES CXX_VISIBILITY_PRESET "default")
endif()

set_target_properties(
    PyMaterialXglTF
    PROPERTIES
    OUTPUT_NAME PyMaterialXglTF
    COMPILE_FLAGS "${EXTERNAL_COMPILE_FLAGS}"
    LINK_FLAGS "${EXTERNAL_LINK_FLAGS}"
    INSTALL_RPATH "${MATERIALX_UP_TWO_RPATH}"
    DEBUG_POSTFIX "${MATERIALX_PYTHON_DEBUG_POSTFIX}")

target_link_libraries(
    PyMaterialXglTF
    PUBLIC PyMaterialXCore
           PyMaterialXFormat
           PyMaterialXGenShader
           PyMaterialXRender
           MaterialXglTF
    PRIVATE ${CMAKE_DL_LIBS})

install(TARGETS PyMaterialXglTF
        DESTINATION "${MATERIALX_PYTHON_FOLDER_NAME}")
