#line 1 "D:/work/OpenUSD/pxr/base/pegtl/pegtl/rewind_mode.hpp"
// Copyright (c) 2016-2022 Dr. Colin Hirsch and Daniel Frey
// Please see LICENSE for license or visit https://github.com/taocpp/PEGTL/

#ifndef PXR_PEGTL_REWIND_MODE_HPP
#define PXR_PEGTL_REWIND_MODE_HPP

#include "config.hpp"

namespace PXR_PEGTL_NAMESPACE
{
   enum class rewind_mode : char
   {
      active,
      required,
      dontcare
   };

}  // namespace PXR_PEGTL_NAMESPACE

#endif
