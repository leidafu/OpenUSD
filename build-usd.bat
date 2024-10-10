"C:\Program Files\CMake\bin\cmake.exe"      ^
-G "Visual Studio 16 2019"            ^
-A x64      ^
-DTBB_ROOT_DIR="C:\oneapi-tbb-2021.13.0"               ^
-DTBB_USE_DEBUG_BUILD=ON ^
-DOPENSUBDIV_ROOT_DIR="C:\Program Files\OpenSubdiv" ^
-DOPENSUBDIV_INCLUDE_DIR="C:\Program Files\OpenSubdiv\include" ^
-DOPENSUBDIV_LIBRARIES="C:\Program Files\OpenSubdiv\lib" ^
-DBOOST_ROOT="C:\local\boost_1_86_0"               ^
D:\work\OpenUSD

cmake --build . --target install -- /m:%NUMBER_OF_PROCESSORS%