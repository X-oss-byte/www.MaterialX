//
// Copyright Bernard Kwok
// SPDX-License-Identifier: Apache-2.0
//

#include <PyMaterialX/PyMaterialX.h>

namespace py = pybind11;

void bindPyGltfMaterialHandler(py::module& mod);
void bindPyGltfMaterialUtil(py::module& mod);

PYBIND11_MODULE(PyMaterialXglTF, mod)
{
    mod.doc() = "Module containing Python bindings for the GLTF MaterialX interop";

    bindPyGltfMaterialHandler(mod);
    bindPyGltfMaterialUtil(mod);   
}
