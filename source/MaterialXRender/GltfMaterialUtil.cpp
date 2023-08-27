
#include <MaterialXRender/GltfMaterialUtill.h>

#include <fstream>
#include <limits>
#include <unordered_set>

MATERIALX_NAMESPACE_BEGIN

DocumentPtr GltfMaterialUtil::glTF2Mtlx(
                const FilePath& filename, DocumentPtr definitions, 
                bool createAssignments, bool fullDefinition,
                StringVec& logger)
{
    MaterialHandlerPtr gltfMTLXLoader = GltfMaterialHandler::create();
    gltfMTLXLoader->setDefinitions(definitions);
    gltfMTLXLoader->setGenerateAssignments(createAssignments);
    gltfMTLXLoader->setGenerateFullDefinitions(fullDefinition);
    
    bool loadedMaterial = gltfMTLXLoader->load(filename, logger);
    DocumentPtr materials = loadedMaterial ? gltfMTLXLoader->getMaterials() : nullptr;
    
    return materials;
}    

bool GltfMaterialUtil::mtlx2glTF(MaterialHandlerPtr gltfMTLXLoader, 
                                 const FilePath& filename, DocumentPtr materials,
                                 StringVec& logger)
{    
    gltfMTLXLoader->setMaterials(materials);
    return gltfMTLXLoader->save(filename, logger);
}

MATERIALX_NAMESPACE_END

