git submodule update --init --recursive
mkdir build
mkdir build/render
cd build
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
cmake -DCMAKE_OSX_ARCHITECTURES=arm64 -DMATERIALX_BUILD_GRAPH_EDITOR=ON -DMATERIALX_BUILD_PYTHON=ON -DMATERIALX_WARNINGS_AS_ERRORS=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo -DMATERIALX_BUILD_DOCS=OFF -DMATERIALX_BUILD_VIEWER=ON -DMATERIALX_TEST_RENDER=ON -DMATERIALX_TESTOSLC_EXECUTABLE="" -DMATERIALX_TESTRENDER_EXECUTABLE="" -DMATERIALX_OSL_INCLUDE_PATH="" -DMATERIALX_BUILD_OIIO=OFF -DOPENIMAGEIO_INCLUDE_DIR="" -DOPENIMAGEIO_LIBRARY="" -DOPENIMAGEIO_LIBRARY_DIRS="" -DOPENIMAGEIO_ROOT_DIR="" -DMATERIALX_MDLC_EXECUTABLE="" ..
cmake --build . --target MaterialXDocs --config RelWithDebInfo
cmake --build . --target install --config RelWithDebInfo
ctest -VV --output-on-failure --build-config RelWithDebInfo -j0
cmake -E chdir ../python/MaterialXTest python main.py
cmake -E chdir ../python/MaterialXTest python genshader.py
cmake -E chdir ../python/Scripts python mxupdate.py ../../resources/Materials/TestSuite/stdlib/upgrade --yes
cmake -E chdir ../python/Scripts python mxvalidate.py ../../resources/Materials/Examples/StandardSurface/standard_surface_marble_solid.mtlx --verbose
cmake -E chdir ../python/Scripts python mxdoc.py ../../libraries/pbrlib/pbrlib_defs.mtlx
cmake -E chdir ../python/Scripts python baketextures.py ../../resources/Materials/Examples/StandardSurface/standard_surface_brass_tiled.mtlx build/render/brass_tiled_baked.mtlx --path .
cd ..

