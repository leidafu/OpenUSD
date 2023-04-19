//
// Copyright 2022 Pixar
//
// Licensed under the Apache License, Version 2.0 (the "Apache License")
// with the following modification; you may not use this file except in
// compliance with the Apache License and the following modification to it:
// Section 6. Trademarks. is deleted and replaced with:
//
// 6. Trademarks. This License does not grant permission to use the trade
//    names, trademarks, service marks, or product names of the Licensor
//    and its affiliates, except as required to comply with Section 4(c) of
//    the License and to reproduce the content of the NOTICE file.
//
// You may obtain a copy of the Apache License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the Apache License with the above modification is
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied. See the Apache License for the specific
// language governing permissions and limitations under the Apache License.
//
////////////////////////////////////////////////////////////////////////
// This file is generated by a script.  Do not edit directly.  Edit the
// schema.template.cpp file to make changes.

#include "pxr/imaging/hdar/systemSchema.h"
#include "pxr/imaging/hd/retainedDataSource.h"
#include "pxr/imaging/hd/systemSchema.h"

#include "pxr/base/trace/trace.h"


PXR_NAMESPACE_OPEN_SCOPE

TF_DEFINE_PUBLIC_TOKENS(HdarSystemSchemaTokens,
    HDARSYSTEM_SCHEMA_TOKENS);

// static
HdContainerDataSourceHandle
HdarSystemSchema::GetFromPath(
    HdSceneIndexBaseRefPtr const& inputScene,
    SdfPath const& fromPath,
    SdfPath* outFoundAtPath)
{
    SdfPath foundAtPath;
    HdDataSourceBaseHandle ds = HdSystemSchema::GetFromPath(
            inputScene, fromPath,
            HdarSystemSchemaTokens->assetResolution,
            &foundAtPath);
    if (!ds) {
        return nullptr;
    }

    auto containerDs = HdContainerDataSource::Cast(ds);
    if (!containerDs) {
        TF_CODING_ERROR(
            "system.assetResolution at %s is not a container.",
            foundAtPath.GetText());
        return nullptr;
    }

    if (outFoundAtPath) {
        *outFoundAtPath = foundAtPath;
    }
    return containerDs;
}

HdResolverContextDataSourceHandle
HdarSystemSchema::GetResolverContext()
{
    return _GetTypedDataSource<HdResolverContextDataSource>(
        HdarSystemSchemaTokens->resolverContext);
}

/*static*/
HdContainerDataSourceHandle
HdarSystemSchema::BuildRetained(
        const HdResolverContextDataSourceHandle &resolverContext
)
{
    TfToken names[1];
    HdDataSourceBaseHandle values[1];

    size_t count = 0;
    if (resolverContext) {
        names[count] = HdarSystemSchemaTokens->resolverContext;
        values[count++] = resolverContext;
    }

    return HdRetainedContainerDataSource::New(count, names, values);
}

/*static*/
HdarSystemSchema
HdarSystemSchema::GetFromParent(
        const HdContainerDataSourceHandle &fromParentContainer)
{
    return HdarSystemSchema(
        fromParentContainer
        ? HdContainerDataSource::Cast(fromParentContainer->Get(
                HdarSystemSchemaTokens->assetResolution))
        : nullptr);
}

/*static*/
const HdDataSourceLocator &
HdarSystemSchema::GetDefaultLocator()
{
    static const HdDataSourceLocator locator(
        HdSystemSchemaTokens->system,
        HdarSystemSchemaTokens->assetResolution
    );
    return locator;
} 
HdarSystemSchema::Builder &
HdarSystemSchema::Builder::SetResolverContext(
    const HdResolverContextDataSourceHandle &resolverContext)
{
    _resolverContext = resolverContext;
    return *this;
}

HdContainerDataSourceHandle
HdarSystemSchema::Builder::Build()
{
    return HdarSystemSchema::BuildRetained(
        _resolverContext
    );
}


PXR_NAMESPACE_CLOSE_SCOPE