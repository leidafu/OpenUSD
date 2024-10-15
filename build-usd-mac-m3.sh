cmake                                       \
-G "Xcode"                                  \
-DTBB_ROOT_DIR=/Users/dafu/oneapi-tbb-2021.13.0                 \
-DOPENSUBDIV_ROOT_DIR=/usr/local   \
-DBOOST_ROOT="/opt/homebrew/opt/boost"   \
-DBOOST_PYTHON_VERSION=3.12   \
/Users/dafu/work/OpenUSD

cmake --build . --target install -- -j 10