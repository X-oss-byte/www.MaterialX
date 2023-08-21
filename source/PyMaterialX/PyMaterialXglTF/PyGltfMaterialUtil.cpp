//
// Copyright Bernard Kwok
// SPDX-License-Identifier: Apache-2.0
//

#include <PyMaterialX/PyMaterialX.h>

#include <MaterialXglTF/GltfMaterialUtill.h>

namespace py = pybind11;
namespace mx = MaterialX;


void bindPyGltfMaterialUtil(py::module& mod)
{
    py::class_<mx::GltfMaterialUtil>(mod, "GltfMaterialUtil")
        .def(py::init<>())
        .def_static("glTF2Mtlx", &mx::GltfMaterialUtil::glTF2Mtlx)
        .def_static("mtlx2glTF", &mx::GltfMaterialUtil::mtlx2glTF)
        ;
}
