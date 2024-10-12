/********************************************************************************
** Form generated from reading UI file 'mainWindowUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINWINDOWUI_H
#define MAINWINDOWUI_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QActionGroup>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include ".attributeValueEditor"
#include ".frameSlider"
#include ".primLegend"
#include ".primTreeWidget"
#include ".propertyLegend"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen;
    QAction *actionQuit;
    QAction *actionPause;
    QAction *actionStop;
    QAction *actionReset_View;
    QAction *actionToggle_Framed_View;
    QAction *actionWatch_Window;
    QAction *actionReopen_Stage;
    QAction *actionDump_RIB;
    QAction *actionLevel_1;
    QAction *actionLevel_2;
    QAction *actionLevel_3;
    QAction *actionLevel_4;
    QAction *actionLevel_5;
    QAction *actionExpand_All;
    QAction *actionCollapse_All;
    QAction *actionAmbient_Only;
    QAction *actionDomeLight;
    QAction *actionDomeLightTexturesVisible;
    QAction *actionLevel_6;
    QAction *actionLevel_7;
    QAction *actionLevel_8;
    QAction *actionWireframe;
    QAction *actionWireframeOnSurface;
    QAction *actionSmooth_Shaded;
    QAction *actionFlat_Shaded;
    QAction *actionPoints;
    QAction *actionGeom_Only;
    QAction *actionRedrawOnScrub;
    QAction *actionIncrementComplexity1;
    QAction *actionDecrementComplexity;
    QAction *actionPRMan;
    QAction *actionBlack;
    QAction *actionWhite;
    QAction *actionGrey_Light;
    QAction *actionGrey_Dark;
    QAction *actionGeom_Smooth;
    QAction *actionGeom_Flat;
    QAction *actionHidden_Surface_Wireframe;
    QAction *actionNoColorCorrection;
    QAction *actionSRGBColorCorrection;
    QAction *actionOpenColorIO;
    QAction *actionFreeCam;
    QAction *actionSave_Overrides_As;
    QAction *actionSave_Flattened_As;
    QAction *actionSave_Viewer_Image;
    QAction *actionCopy_Viewer_Image;
    QAction *showInterpreter;
    QAction *showDebugFlags;
    QAction *actionHUD_VBOInfo;
    QAction *actionHUD_Info;
    QAction *actionHUD_VBO;
    QAction *actionHUD_Complexity;
    QAction *actionHUD_Performance;
    QAction *actionHUD_GPUstats;
    QAction *actionHUD;
    QAction *actionCameraMask_Outline;
    QAction *actionDisplay_Guide;
    QAction *actionDisplay_Render;
    QAction *actionDisplay_PrimId;
    QAction *actionEnable_Scene_Materials;
    QAction *actionEnable_Scene_Lights;
    QAction *actionShow_Inactive_Prims;
    QAction *showAABBox;
    QAction *showOBBox;
    QAction *showBBoxPlayback;
    QAction *showBBoxes;
    QAction *actionVersion_Info;
    QAction *actionAdjust_Free_Camera;
    QAction *actionIncrementComplexity2;
    QAction *actionCull_Backfaces;
    QAction *actionSave_Overrides_To_Scene;
    QAction *actionMake_Visible;
    QAction *actionMake_Invisible;
    QAction *actionRemove_Session_Visibility;
    QAction *actionActivate;
    QAction *actionDeactivate;
    QAction *actionSelect_Model_Root;
    QAction *actionRefresh_Procedurals;
    QAction *actionReload_All_Layers;
    QAction *actionHD_Flags;
    QAction *actionHD_Flags_2;
    QAction *actionHD_Flags_3;
    QAction *actionMenu;
    QAction *actionSdf;
    QAction *actionGeom_Id;
    QAction *actionShow_All_Prototype_Prims;
    QAction *actionShow_Undefined_Prims;
    QAction *actionShow_Abstract_Prims;
    QAction *actionShow_Prim_DisplayName;
    QAction *actionPick_Prims;
    QAction *actionPick_Models;
    QAction *actionPick_Instances;
    QAction *actionPick_Prototypes;
    QAction *actionToggle_Viewer_Mode;
    QAction *useExtentsHint;
    QAction *actionNever;
    QAction *actionOnly_when_paused;
    QAction *actionAlways;
    QAction *actionSelYellow;
    QAction *actionSelWhite;
    QAction *actionSelCyan;
    QAction *actionVis_Only;
    QAction *actionReset_All_Session_Visibility;
    QAction *actionLoad;
    QAction *actionUnload;
    QAction *actionSelect_Bound_Preview_Material;
    QAction *actionRollover_Prim_Info;
    QAction *actionAuto_Compute_Clipping_Planes;
    QAction *actionFind_Prims;
    QAction *actionSelect_Stage_Root;
    QAction *actionDisplay_Camera_Oracles;
    QAction *actionDisplay_Proxy;
    QAction *actionAdjust_Default_Material;
    QAction *actionCameraReticles_Inside;
    QAction *actionCameraReticles_Outside;
    QAction *actionCameraReticles_Color;
    QAction *actionLow;
    QAction *actionMedium;
    QAction *actionHigh;
    QAction *actionVery_High;
    QAction *actionSelect_Bound_Full_Material;
    QAction *actionSelect_Preview_Binding_Relationship;
    QAction *actionSelect_Full_Binding_Relationship;
    QAction *actionPreferences;
    QAction *actionSave_State_To;
    QAction *actiond;
    QAction *actiond_2;
    QAction *actionSave_State_As_New_Config;
    QAction *actionFrame_Selected;
    QAction *showHydraSceneBrowser;
    QActionGroup *actionGroupCameraMask;
    QAction *actionCameraMask_Full;
    QAction *actionCameraMask_Partial;
    QAction *actionCameraMask_None;
    QAction *actionCameraMask_Color;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_4;
    QLineEdit *currentPathWidget;
    QSplitter *topBottomSplitter;
    QSplitter *primStageSplitter;
    QFrame *primFrame;
    QVBoxLayout *verticalLayout_2;
    QMenuBar *primViewMenuBar;
    QMenu *menuNavigation;
    QMenu *menuShow;
    QMenu *menuPrim_View_Depth;
    PrimTreeWidget *primView;
    PrimLegend *primLegendContainer;
    QHBoxLayout *primFindContainer;
    QPushButton *primLegendQButton;
    QLineEdit *primViewLineEdit;
    QPushButton *primViewFindNext;
    QFrame *renderFrame;
    QVBoxLayout *verticalLayout_5;
    QMenuBar *renderMenuBar;
    QMenu *menuRender;
    QMenu *menuRendererSettings;
    QMenu *menuRendererAovs;
    QMenu *menuRendererCommands;
    QMenu *menuViewer;
    QMenu *menuShading_Mode;
    QMenu *menuColorCorrection;
    QMenu *menuComplexity;
    QMenu *menuBBox;
    QMenu *menuDisplay;
    QMenu *menuHUD;
    QMenu *menuSelection_Highlighting;
    QMenu *menuHighlightColor;
    QMenu *menuBackground_Color;
    QMenu *menuCamera;
    QMenu *menuCameraSelect;
    QMenu *menuCameraGuides;
    QMenu *menuCamera_Masking;
    QMenu *menuCamera_Reticles;
    QMenu *menuPick;
    QMenu *menuLights;
    QFrame *glFrame;
    QSplitter *attribBrowserInspectorSplitter;
    QFrame *attributeBrowserFrame;
    QVBoxLayout *verticalLayout_7;
    QTreeWidget *propertyView;
    PropertyLegend *propertyLegendContainer;
    QHBoxLayout *propertyFindContainer;
    QPushButton *propertyLegendQButton;
    QLineEdit *attrViewLineEdit;
    QPushButton *attrViewFindNext;
    QFrame *propertyInspectorFrame;
    QVBoxLayout *verticalLayout_8;
    QFrame *propertyInspectorContainer;
    QVBoxLayout *verticalLayout_3;
    QTabWidget *propertyInspector;
    QWidget *value;
    QVBoxLayout *verticalLayout;
    AttributeValueEditor *attributeValueEditor;
    QWidget *metadata;
    QHBoxLayout *horizontalLayout;
    QFrame *attributeBrowserFrame_1;
    QVBoxLayout *verticalLayout_71;
    QTableWidget *metadataView;
    QWidget *layerstack;
    QHBoxLayout *layerStackFrameLayout;
    QFrame *layerStackFrame;
    QVBoxLayout *layerStackViewLayout;
    QTableWidget *layerStackView;
    QWidget *tab;
    QHBoxLayout *horizontalLayout_4;
    QTreeWidget *compositionTreeWidget;
    QHBoxLayout *frameChangeContainer;
    QVBoxLayout *sliderContainer;
    QHBoxLayout *sliderTopContainer;
    QLabel *stageBegin;
    QVBoxLayout *rangeBeginLayout;
    QSpacerItem *verticalSpacer;
    QLineEdit *rangeBegin;
    QSpacerItem *verticalSpacer_2;
    FrameSlider *frameSlider;
    QVBoxLayout *rangeEndLayout;
    QSpacerItem *verticalSpacer_3;
    QLineEdit *rangeEnd;
    QSpacerItem *verticalSpacer_4;
    QLabel *stageEnd;
    QHBoxLayout *sliderBottomContainer;
    QSpacerItem *horizontalSpacer_4;
    QCheckBox *redrawOnScrub;
    QSpacerItem *horizontalSpacer_9;
    QLabel *stepSizeLabel;
    QLineEdit *stepSize;
    QSpacerItem *horizontalSpacer;
    QFrame *line;
    QVBoxLayout *playContainer;
    QHBoxLayout *playButtonContainer;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *playButton;
    QSpacerItem *horizontalSpacer_3;
    QHBoxLayout *frameContainer;
    QSpacerItem *horizontalSpacer_5;
    QLabel *frameLabel;
    QLineEdit *frameField;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuSave_State_As;
    QMenu *menuLoad_New_State;
    QMenu *menuEdit;
    QMenu *menuInterpolation;
    QMenu *menuWindow;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1145, 1002);
        MainWindow->setStyleSheet(QString::fromUtf8(""));
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName("actionOpen");
        actionOpen->setShortcutContext(Qt::ApplicationShortcut);
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName("actionQuit");
        actionQuit->setShortcutContext(Qt::ApplicationShortcut);
        actionPause = new QAction(MainWindow);
        actionPause->setObjectName("actionPause");
        actionPause->setCheckable(true);
        actionPause->setShortcutContext(Qt::ApplicationShortcut);
        actionStop = new QAction(MainWindow);
        actionStop->setObjectName("actionStop");
        actionStop->setCheckable(true);
        actionStop->setShortcutContext(Qt::ApplicationShortcut);
        actionReset_View = new QAction(MainWindow);
        actionReset_View->setObjectName("actionReset_View");
        actionReset_View->setShortcutContext(Qt::ApplicationShortcut);
        actionToggle_Framed_View = new QAction(MainWindow);
        actionToggle_Framed_View->setObjectName("actionToggle_Framed_View");
        actionToggle_Framed_View->setShortcutContext(Qt::ApplicationShortcut);
        actionWatch_Window = new QAction(MainWindow);
        actionWatch_Window->setObjectName("actionWatch_Window");
        actionWatch_Window->setCheckable(true);
        actionWatch_Window->setEnabled(false);
        actionWatch_Window->setShortcutContext(Qt::ApplicationShortcut);
        actionReopen_Stage = new QAction(MainWindow);
        actionReopen_Stage->setObjectName("actionReopen_Stage");
        actionDump_RIB = new QAction(MainWindow);
        actionDump_RIB->setObjectName("actionDump_RIB");
        actionLevel_1 = new QAction(MainWindow);
        actionLevel_1->setObjectName("actionLevel_1");
        actionLevel_1->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_2 = new QAction(MainWindow);
        actionLevel_2->setObjectName("actionLevel_2");
        actionLevel_2->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_3 = new QAction(MainWindow);
        actionLevel_3->setObjectName("actionLevel_3");
        actionLevel_3->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_4 = new QAction(MainWindow);
        actionLevel_4->setObjectName("actionLevel_4");
        actionLevel_4->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_5 = new QAction(MainWindow);
        actionLevel_5->setObjectName("actionLevel_5");
        actionLevel_5->setShortcutContext(Qt::ApplicationShortcut);
        actionExpand_All = new QAction(MainWindow);
        actionExpand_All->setObjectName("actionExpand_All");
        actionExpand_All->setShortcutContext(Qt::ApplicationShortcut);
        actionCollapse_All = new QAction(MainWindow);
        actionCollapse_All->setObjectName("actionCollapse_All");
        actionCollapse_All->setShortcutContext(Qt::ApplicationShortcut);
        actionAmbient_Only = new QAction(MainWindow);
        actionAmbient_Only->setObjectName("actionAmbient_Only");
        actionAmbient_Only->setCheckable(true);
        actionAmbient_Only->setChecked(true);
        actionDomeLight = new QAction(MainWindow);
        actionDomeLight->setObjectName("actionDomeLight");
        actionDomeLight->setCheckable(true);
        actionDomeLight->setChecked(true);
        actionDomeLightTexturesVisible = new QAction(MainWindow);
        actionDomeLightTexturesVisible->setObjectName("actionDomeLightTexturesVisible");
        actionDomeLightTexturesVisible->setCheckable(true);
        actionDomeLightTexturesVisible->setChecked(true);
        actionLevel_6 = new QAction(MainWindow);
        actionLevel_6->setObjectName("actionLevel_6");
        actionLevel_6->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_7 = new QAction(MainWindow);
        actionLevel_7->setObjectName("actionLevel_7");
        actionLevel_7->setShortcutContext(Qt::ApplicationShortcut);
        actionLevel_8 = new QAction(MainWindow);
        actionLevel_8->setObjectName("actionLevel_8");
        actionLevel_8->setShortcutContext(Qt::ApplicationShortcut);
        actionWireframe = new QAction(MainWindow);
        actionWireframe->setObjectName("actionWireframe");
        actionWireframe->setCheckable(true);
        actionWireframe->setChecked(false);
        actionWireframe->setShortcutContext(Qt::ApplicationShortcut);
        actionWireframeOnSurface = new QAction(MainWindow);
        actionWireframeOnSurface->setObjectName("actionWireframeOnSurface");
        actionWireframeOnSurface->setCheckable(true);
        actionWireframeOnSurface->setChecked(false);
        actionWireframeOnSurface->setShortcutContext(Qt::ApplicationShortcut);
        actionSmooth_Shaded = new QAction(MainWindow);
        actionSmooth_Shaded->setObjectName("actionSmooth_Shaded");
        actionSmooth_Shaded->setCheckable(true);
        actionSmooth_Shaded->setChecked(true);
        actionSmooth_Shaded->setShortcutContext(Qt::ApplicationShortcut);
        actionFlat_Shaded = new QAction(MainWindow);
        actionFlat_Shaded->setObjectName("actionFlat_Shaded");
        actionFlat_Shaded->setCheckable(true);
        actionFlat_Shaded->setShortcutContext(Qt::ApplicationShortcut);
        actionPoints = new QAction(MainWindow);
        actionPoints->setObjectName("actionPoints");
        actionPoints->setCheckable(true);
        actionPoints->setShortcutContext(Qt::ApplicationShortcut);
        actionGeom_Only = new QAction(MainWindow);
        actionGeom_Only->setObjectName("actionGeom_Only");
        actionGeom_Only->setCheckable(true);
        actionGeom_Only->setShortcutContext(Qt::ApplicationShortcut);
        actionRedrawOnScrub = new QAction(MainWindow);
        actionRedrawOnScrub->setObjectName("actionRedrawOnScrub");
        actionRedrawOnScrub->setCheckable(true);
        actionRedrawOnScrub->setChecked(true);
        actionIncrementComplexity1 = new QAction(MainWindow);
        actionIncrementComplexity1->setObjectName("actionIncrementComplexity1");
        actionDecrementComplexity = new QAction(MainWindow);
        actionDecrementComplexity->setObjectName("actionDecrementComplexity");
        actionPRMan = new QAction(MainWindow);
        actionPRMan->setObjectName("actionPRMan");
        actionPRMan->setAutoRepeat(false);
        actionBlack = new QAction(MainWindow);
        actionBlack->setObjectName("actionBlack");
        actionBlack->setCheckable(true);
        actionBlack->setChecked(false);
        actionWhite = new QAction(MainWindow);
        actionWhite->setObjectName("actionWhite");
        actionWhite->setCheckable(true);
        actionGrey_Light = new QAction(MainWindow);
        actionGrey_Light->setObjectName("actionGrey_Light");
        actionGrey_Light->setCheckable(true);
        actionGrey_Dark = new QAction(MainWindow);
        actionGrey_Dark->setObjectName("actionGrey_Dark");
        actionGrey_Dark->setCheckable(true);
        actionGrey_Dark->setChecked(true);
        actionGeom_Smooth = new QAction(MainWindow);
        actionGeom_Smooth->setObjectName("actionGeom_Smooth");
        actionGeom_Smooth->setCheckable(true);
        actionGeom_Flat = new QAction(MainWindow);
        actionGeom_Flat->setObjectName("actionGeom_Flat");
        actionGeom_Flat->setCheckable(true);
        actionHidden_Surface_Wireframe = new QAction(MainWindow);
        actionHidden_Surface_Wireframe->setObjectName("actionHidden_Surface_Wireframe");
        actionHidden_Surface_Wireframe->setCheckable(true);
        actionHidden_Surface_Wireframe->setChecked(false);
        actionNoColorCorrection = new QAction(MainWindow);
        actionNoColorCorrection->setObjectName("actionNoColorCorrection");
        actionNoColorCorrection->setCheckable(true);
        actionNoColorCorrection->setChecked(false);
        actionSRGBColorCorrection = new QAction(MainWindow);
        actionSRGBColorCorrection->setObjectName("actionSRGBColorCorrection");
        actionSRGBColorCorrection->setCheckable(true);
        actionSRGBColorCorrection->setChecked(true);
        actionOpenColorIO = new QAction(MainWindow);
        actionOpenColorIO->setObjectName("actionOpenColorIO");
        actionOpenColorIO->setCheckable(true);
        actionOpenColorIO->setChecked(false);
        actionFreeCam = new QAction(MainWindow);
        actionFreeCam->setObjectName("actionFreeCam");
        actionFreeCam->setCheckable(true);
        actionFreeCam->setChecked(true);
        actionSave_Overrides_As = new QAction(MainWindow);
        actionSave_Overrides_As->setObjectName("actionSave_Overrides_As");
        actionSave_Overrides_As->setEnabled(true);
        actionSave_Flattened_As = new QAction(MainWindow);
        actionSave_Flattened_As->setObjectName("actionSave_Flattened_As");
        actionSave_Flattened_As->setEnabled(true);
        actionSave_Viewer_Image = new QAction(MainWindow);
        actionSave_Viewer_Image->setObjectName("actionSave_Viewer_Image");
        actionSave_Viewer_Image->setEnabled(true);
        actionCopy_Viewer_Image = new QAction(MainWindow);
        actionCopy_Viewer_Image->setObjectName("actionCopy_Viewer_Image");
        actionCopy_Viewer_Image->setEnabled(true);
        showInterpreter = new QAction(MainWindow);
        showInterpreter->setObjectName("showInterpreter");
        showInterpreter->setCheckable(false);
        showDebugFlags = new QAction(MainWindow);
        showDebugFlags->setObjectName("showDebugFlags");
        showDebugFlags->setCheckable(false);
        actionHUD_VBOInfo = new QAction(MainWindow);
        actionHUD_VBOInfo->setObjectName("actionHUD_VBOInfo");
        actionHUD_VBOInfo->setCheckable(true);
        actionHUD_VBOInfo->setChecked(true);
        actionHUD_Info = new QAction(MainWindow);
        actionHUD_Info->setObjectName("actionHUD_Info");
        actionHUD_Info->setCheckable(true);
        actionHUD_Info->setChecked(true);
        actionHUD_VBO = new QAction(MainWindow);
        actionHUD_VBO->setObjectName("actionHUD_VBO");
        actionHUD_VBO->setCheckable(true);
        actionHUD_VBO->setChecked(true);
        actionHUD_Complexity = new QAction(MainWindow);
        actionHUD_Complexity->setObjectName("actionHUD_Complexity");
        actionHUD_Complexity->setCheckable(true);
        actionHUD_Complexity->setChecked(true);
        actionHUD_Performance = new QAction(MainWindow);
        actionHUD_Performance->setObjectName("actionHUD_Performance");
        actionHUD_Performance->setCheckable(true);
        actionHUD_Performance->setChecked(true);
        actionHUD_GPUstats = new QAction(MainWindow);
        actionHUD_GPUstats->setObjectName("actionHUD_GPUstats");
        actionHUD_GPUstats->setCheckable(true);
        actionHUD_GPUstats->setChecked(false);
        actionHUD = new QAction(MainWindow);
        actionHUD->setObjectName("actionHUD");
        actionHUD->setCheckable(true);
        actionHUD->setChecked(true);
        actionCameraMask_Outline = new QAction(MainWindow);
        actionCameraMask_Outline->setObjectName("actionCameraMask_Outline");
        actionCameraMask_Outline->setCheckable(true);
        actionCameraMask_Outline->setChecked(false);
        actionDisplay_Guide = new QAction(MainWindow);
        actionDisplay_Guide->setObjectName("actionDisplay_Guide");
        actionDisplay_Guide->setCheckable(true);
        actionDisplay_Render = new QAction(MainWindow);
        actionDisplay_Render->setObjectName("actionDisplay_Render");
        actionDisplay_Render->setCheckable(true);
        actionDisplay_PrimId = new QAction(MainWindow);
        actionDisplay_PrimId->setObjectName("actionDisplay_PrimId");
        actionDisplay_PrimId->setCheckable(true);
        actionEnable_Scene_Materials = new QAction(MainWindow);
        actionEnable_Scene_Materials->setObjectName("actionEnable_Scene_Materials");
        actionEnable_Scene_Materials->setCheckable(true);
        actionEnable_Scene_Materials->setChecked(true);
        actionEnable_Scene_Lights = new QAction(MainWindow);
        actionEnable_Scene_Lights->setObjectName("actionEnable_Scene_Lights");
        actionEnable_Scene_Lights->setCheckable(true);
        actionEnable_Scene_Lights->setChecked(true);
        actionShow_Inactive_Prims = new QAction(MainWindow);
        actionShow_Inactive_Prims->setObjectName("actionShow_Inactive_Prims");
        actionShow_Inactive_Prims->setCheckable(true);
        showAABBox = new QAction(MainWindow);
        showAABBox->setObjectName("showAABBox");
        showAABBox->setCheckable(true);
        showAABBox->setChecked(true);
        showOBBox = new QAction(MainWindow);
        showOBBox->setObjectName("showOBBox");
        showOBBox->setCheckable(true);
        showBBoxPlayback = new QAction(MainWindow);
        showBBoxPlayback->setObjectName("showBBoxPlayback");
        showBBoxPlayback->setCheckable(true);
        showBBoxes = new QAction(MainWindow);
        showBBoxes->setObjectName("showBBoxes");
        showBBoxes->setCheckable(true);
        showBBoxes->setChecked(true);
        showBBoxes->setEnabled(true);
        actionVersion_Info = new QAction(MainWindow);
        actionVersion_Info->setObjectName("actionVersion_Info");
        actionVersion_Info->setCheckable(true);
        actionVersion_Info->setShortcutContext(Qt::ApplicationShortcut);
        actionAdjust_Free_Camera = new QAction(MainWindow);
        actionAdjust_Free_Camera->setObjectName("actionAdjust_Free_Camera");
        actionAdjust_Free_Camera->setCheckable(true);
        actionIncrementComplexity2 = new QAction(MainWindow);
        actionIncrementComplexity2->setObjectName("actionIncrementComplexity2");
        actionCull_Backfaces = new QAction(MainWindow);
        actionCull_Backfaces->setObjectName("actionCull_Backfaces");
        actionCull_Backfaces->setCheckable(true);
        actionCull_Backfaces->setChecked(true);
        actionSave_Overrides_To_Scene = new QAction(MainWindow);
        actionSave_Overrides_To_Scene->setObjectName("actionSave_Overrides_To_Scene");
        actionSave_Overrides_To_Scene->setEnabled(false);
        actionSave_Overrides_To_Scene->setVisible(false);
        actionMake_Visible = new QAction(MainWindow);
        actionMake_Visible->setObjectName("actionMake_Visible");
        actionMake_Invisible = new QAction(MainWindow);
        actionMake_Invisible->setObjectName("actionMake_Invisible");
        actionRemove_Session_Visibility = new QAction(MainWindow);
        actionRemove_Session_Visibility->setObjectName("actionRemove_Session_Visibility");
        actionActivate = new QAction(MainWindow);
        actionActivate->setObjectName("actionActivate");
        actionDeactivate = new QAction(MainWindow);
        actionDeactivate->setObjectName("actionDeactivate");
        actionSelect_Model_Root = new QAction(MainWindow);
        actionSelect_Model_Root->setObjectName("actionSelect_Model_Root");
        actionSelect_Model_Root->setEnabled(true);
        actionRefresh_Procedurals = new QAction(MainWindow);
        actionRefresh_Procedurals->setObjectName("actionRefresh_Procedurals");
        actionReload_All_Layers = new QAction(MainWindow);
        actionReload_All_Layers->setObjectName("actionReload_All_Layers");
        actionHD_Flags = new QAction(MainWindow);
        actionHD_Flags->setObjectName("actionHD_Flags");
        actionHD_Flags_2 = new QAction(MainWindow);
        actionHD_Flags_2->setObjectName("actionHD_Flags_2");
        actionHD_Flags_3 = new QAction(MainWindow);
        actionHD_Flags_3->setObjectName("actionHD_Flags_3");
        actionMenu = new QAction(MainWindow);
        actionMenu->setObjectName("actionMenu");
        actionSdf = new QAction(MainWindow);
        actionSdf->setObjectName("actionSdf");
        actionGeom_Id = new QAction(MainWindow);
        actionGeom_Id->setObjectName("actionGeom_Id");
        actionShow_All_Prototype_Prims = new QAction(MainWindow);
        actionShow_All_Prototype_Prims->setObjectName("actionShow_All_Prototype_Prims");
        actionShow_All_Prototype_Prims->setCheckable(true);
        actionShow_Undefined_Prims = new QAction(MainWindow);
        actionShow_Undefined_Prims->setObjectName("actionShow_Undefined_Prims");
        actionShow_Undefined_Prims->setCheckable(true);
        actionShow_Abstract_Prims = new QAction(MainWindow);
        actionShow_Abstract_Prims->setObjectName("actionShow_Abstract_Prims");
        actionShow_Abstract_Prims->setCheckable(true);
        actionShow_Prim_DisplayName = new QAction(MainWindow);
        actionShow_Prim_DisplayName->setObjectName("actionShow_Prim_DisplayName");
        actionShow_Prim_DisplayName->setCheckable(true);
        actionPick_Prims = new QAction(MainWindow);
        actionPick_Prims->setObjectName("actionPick_Prims");
        actionPick_Prims->setCheckable(true);
        actionPick_Models = new QAction(MainWindow);
        actionPick_Models->setObjectName("actionPick_Models");
        actionPick_Models->setCheckable(true);
        actionPick_Instances = new QAction(MainWindow);
        actionPick_Instances->setObjectName("actionPick_Instances");
        actionPick_Instances->setCheckable(true);
        actionPick_Prototypes = new QAction(MainWindow);
        actionPick_Prototypes->setObjectName("actionPick_Prototypes");
        actionPick_Prototypes->setCheckable(true);
        actionToggle_Viewer_Mode = new QAction(MainWindow);
        actionToggle_Viewer_Mode->setObjectName("actionToggle_Viewer_Mode");
        useExtentsHint = new QAction(MainWindow);
        useExtentsHint->setObjectName("useExtentsHint");
        useExtentsHint->setCheckable(true);
        useExtentsHint->setChecked(true);
        actionNever = new QAction(MainWindow);
        actionNever->setObjectName("actionNever");
        actionNever->setCheckable(true);
        actionOnly_when_paused = new QAction(MainWindow);
        actionOnly_when_paused->setObjectName("actionOnly_when_paused");
        actionOnly_when_paused->setCheckable(true);
        actionOnly_when_paused->setChecked(true);
        actionAlways = new QAction(MainWindow);
        actionAlways->setObjectName("actionAlways");
        actionAlways->setCheckable(true);
        actionSelYellow = new QAction(MainWindow);
        actionSelYellow->setObjectName("actionSelYellow");
        actionSelYellow->setCheckable(true);
        actionSelYellow->setChecked(true);
        actionSelWhite = new QAction(MainWindow);
        actionSelWhite->setObjectName("actionSelWhite");
        actionSelWhite->setCheckable(true);
        actionSelCyan = new QAction(MainWindow);
        actionSelCyan->setObjectName("actionSelCyan");
        actionSelCyan->setCheckable(true);
        actionVis_Only = new QAction(MainWindow);
        actionVis_Only->setObjectName("actionVis_Only");
        actionReset_All_Session_Visibility = new QAction(MainWindow);
        actionReset_All_Session_Visibility->setObjectName("actionReset_All_Session_Visibility");
        actionLoad = new QAction(MainWindow);
        actionLoad->setObjectName("actionLoad");
        actionUnload = new QAction(MainWindow);
        actionUnload->setObjectName("actionUnload");
        actionSelect_Bound_Preview_Material = new QAction(MainWindow);
        actionSelect_Bound_Preview_Material->setObjectName("actionSelect_Bound_Preview_Material");
        actionRollover_Prim_Info = new QAction(MainWindow);
        actionRollover_Prim_Info->setObjectName("actionRollover_Prim_Info");
        actionRollover_Prim_Info->setCheckable(true);
        actionAuto_Compute_Clipping_Planes = new QAction(MainWindow);
        actionAuto_Compute_Clipping_Planes->setObjectName("actionAuto_Compute_Clipping_Planes");
        actionAuto_Compute_Clipping_Planes->setCheckable(true);
        actionFind_Prims = new QAction(MainWindow);
        actionFind_Prims->setObjectName("actionFind_Prims");
        actionSelect_Stage_Root = new QAction(MainWindow);
        actionSelect_Stage_Root->setObjectName("actionSelect_Stage_Root");
        actionDisplay_Camera_Oracles = new QAction(MainWindow);
        actionDisplay_Camera_Oracles->setObjectName("actionDisplay_Camera_Oracles");
        actionDisplay_Camera_Oracles->setCheckable(true);
        actionDisplay_Proxy = new QAction(MainWindow);
        actionDisplay_Proxy->setObjectName("actionDisplay_Proxy");
        actionDisplay_Proxy->setCheckable(true);
        actionAdjust_Default_Material = new QAction(MainWindow);
        actionAdjust_Default_Material->setObjectName("actionAdjust_Default_Material");
        actionAdjust_Default_Material->setCheckable(true);
        actionCameraReticles_Inside = new QAction(MainWindow);
        actionCameraReticles_Inside->setObjectName("actionCameraReticles_Inside");
        actionCameraReticles_Inside->setCheckable(true);
        actionCameraReticles_Inside->setChecked(false);
        actionCameraReticles_Outside = new QAction(MainWindow);
        actionCameraReticles_Outside->setObjectName("actionCameraReticles_Outside");
        actionCameraReticles_Outside->setCheckable(true);
        actionCameraReticles_Outside->setChecked(false);
        actionCameraReticles_Color = new QAction(MainWindow);
        actionCameraReticles_Color->setObjectName("actionCameraReticles_Color");
        actionLow = new QAction(MainWindow);
        actionLow->setObjectName("actionLow");
        actionLow->setCheckable(true);
        actionMedium = new QAction(MainWindow);
        actionMedium->setObjectName("actionMedium");
        actionMedium->setCheckable(true);
        actionHigh = new QAction(MainWindow);
        actionHigh->setObjectName("actionHigh");
        actionHigh->setCheckable(true);
        actionVery_High = new QAction(MainWindow);
        actionVery_High->setObjectName("actionVery_High");
        actionVery_High->setCheckable(true);
        actionSelect_Bound_Full_Material = new QAction(MainWindow);
        actionSelect_Bound_Full_Material->setObjectName("actionSelect_Bound_Full_Material");
        actionSelect_Preview_Binding_Relationship = new QAction(MainWindow);
        actionSelect_Preview_Binding_Relationship->setObjectName("actionSelect_Preview_Binding_Relationship");
        actionSelect_Full_Binding_Relationship = new QAction(MainWindow);
        actionSelect_Full_Binding_Relationship->setObjectName("actionSelect_Full_Binding_Relationship");
        actionPreferences = new QAction(MainWindow);
        actionPreferences->setObjectName("actionPreferences");
        actionPreferences->setCheckable(true);
        actionSave_State_To = new QAction(MainWindow);
        actionSave_State_To->setObjectName("actionSave_State_To");
        actiond = new QAction(MainWindow);
        actiond->setObjectName("actiond");
        actiond_2 = new QAction(MainWindow);
        actiond_2->setObjectName("actiond_2");
        actionSave_State_As_New_Config = new QAction(MainWindow);
        actionSave_State_As_New_Config->setObjectName("actionSave_State_As_New_Config");
        actionFrame_Selected = new QAction(MainWindow);
        actionFrame_Selected->setObjectName("actionFrame_Selected");
        showHydraSceneBrowser = new QAction(MainWindow);
        showHydraSceneBrowser->setObjectName("showHydraSceneBrowser");
        actionGroupCameraMask = new QActionGroup(MainWindow);
        actionGroupCameraMask->setObjectName("actionGroupCameraMask");
        actionCameraMask_Full = new QAction(actionGroupCameraMask);
        actionCameraMask_Full->setObjectName("actionCameraMask_Full");
        actionCameraMask_Full->setCheckable(true);
        actionCameraMask_Full->setChecked(false);
        actionCameraMask_Partial = new QAction(actionGroupCameraMask);
        actionCameraMask_Partial->setObjectName("actionCameraMask_Partial");
        actionCameraMask_Partial->setCheckable(true);
        actionCameraMask_Partial->setChecked(false);
        actionCameraMask_None = new QAction(actionGroupCameraMask);
        actionCameraMask_None->setObjectName("actionCameraMask_None");
        actionCameraMask_None->setCheckable(true);
        actionCameraMask_None->setChecked(true);
        actionCameraMask_Color = new QAction(actionGroupCameraMask);
        actionCameraMask_Color->setObjectName("actionCameraMask_Color");
        actionCameraMask_Color->setCheckable(false);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        verticalLayout_4 = new QVBoxLayout(centralwidget);
        verticalLayout_4->setObjectName("verticalLayout_4");
        currentPathWidget = new QLineEdit(centralwidget);
        currentPathWidget->setObjectName("currentPathWidget");
        currentPathWidget->setFocusPolicy(Qt::StrongFocus);

        verticalLayout_4->addWidget(currentPathWidget);

        topBottomSplitter = new QSplitter(centralwidget);
        topBottomSplitter->setObjectName("topBottomSplitter");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(topBottomSplitter->sizePolicy().hasHeightForWidth());
        topBottomSplitter->setSizePolicy(sizePolicy);
        topBottomSplitter->setFrameShape(QFrame::NoFrame);
        topBottomSplitter->setFrameShadow(QFrame::Plain);
        topBottomSplitter->setLineWidth(0);
        topBottomSplitter->setMidLineWidth(0);
        topBottomSplitter->setOrientation(Qt::Vertical);
        primStageSplitter = new QSplitter(topBottomSplitter);
        primStageSplitter->setObjectName("primStageSplitter");
        primStageSplitter->setOrientation(Qt::Horizontal);
        primFrame = new QFrame(primStageSplitter);
        primFrame->setObjectName("primFrame");
        primFrame->setFrameShape(QFrame::NoFrame);
        primFrame->setFrameShadow(QFrame::Plain);
        primFrame->setLineWidth(0);
        verticalLayout_2 = new QVBoxLayout(primFrame);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setContentsMargins(0, 0, 0, 6);
        primViewMenuBar = new QMenuBar(primFrame);
        primViewMenuBar->setObjectName("primViewMenuBar");
        primViewMenuBar->setLayoutDirection(Qt::LeftToRight);
        primViewMenuBar->setNativeMenuBar(false);
        menuNavigation = new QMenu(primViewMenuBar);
        menuNavigation->setObjectName("menuNavigation");
        menuShow = new QMenu(primViewMenuBar);
        menuShow->setObjectName("menuShow");
        menuPrim_View_Depth = new QMenu(menuShow);
        menuPrim_View_Depth->setObjectName("menuPrim_View_Depth");

        verticalLayout_2->addWidget(primViewMenuBar);

        primView = new PrimTreeWidget(primFrame);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setTextAlignment(2, Qt::AlignLeading|Qt::AlignVCenter);
        primView->setHeaderItem(__qtreewidgetitem);
        primView->setObjectName("primView");
        QFont font;
        font.setFamilies({QString::fromUtf8("Roboto")});
        font.setPointSize(9);
        font.setBold(false);
        font.setItalic(false);
        primView->setFont(font);
        primView->setContextMenuPolicy(Qt::CustomContextMenu);
        primView->setFrameShape(QFrame::NoFrame);
        primView->setFrameShadow(QFrame::Plain);
        primView->setLineWidth(0);
        primView->setMidLineWidth(0);
        primView->setAlternatingRowColors(true);
        primView->setSelectionMode(QAbstractItemView::ExtendedSelection);
        primView->setUniformRowHeights(true);
        primView->setAllColumnsShowFocus(true);
        primView->header()->setCascadingSectionResizes(true);
        primView->header()->setMinimumSectionSize(20);
        primView->header()->setDefaultSectionSize(150);
        primView->header()->setStretchLastSection(false);

        verticalLayout_2->addWidget(primView);

        primLegendContainer = new PrimLegend(primFrame);
        primLegendContainer->setObjectName("primLegendContainer");

        verticalLayout_2->addWidget(primLegendContainer);

        primFindContainer = new QHBoxLayout();
        primFindContainer->setObjectName("primFindContainer");
        primFindContainer->setContentsMargins(-1, 0, -1, -1);
        primLegendQButton = new QPushButton(primFrame);
        primLegendQButton->setObjectName("primLegendQButton");
        QSizePolicy sizePolicy1(QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(primLegendQButton->sizePolicy().hasHeightForWidth());
        primLegendQButton->setSizePolicy(sizePolicy1);
        primLegendQButton->setMaximumSize(QSize(3200, 3200));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Roboto")});
        font1.setPointSize(9);
        font1.setBold(true);
        primLegendQButton->setFont(font1);
        primLegendQButton->setFocusPolicy(Qt::NoFocus);
        primLegendQButton->setIconSize(QSize(12, 12));

        primFindContainer->addWidget(primLegendQButton);

        primViewLineEdit = new QLineEdit(primFrame);
        primViewLineEdit->setObjectName("primViewLineEdit");
        QSizePolicy sizePolicy2(QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(primViewLineEdit->sizePolicy().hasHeightForWidth());
        primViewLineEdit->setSizePolicy(sizePolicy2);
        primViewLineEdit->setMaximumSize(QSize(16777215, 3200));
        primViewLineEdit->setFont(font);

        primFindContainer->addWidget(primViewLineEdit);

        primViewFindNext = new QPushButton(primFrame);
        primViewFindNext->setObjectName("primViewFindNext");
        sizePolicy1.setHeightForWidth(primViewFindNext->sizePolicy().hasHeightForWidth());
        primViewFindNext->setSizePolicy(sizePolicy1);
        primViewFindNext->setMaximumSize(QSize(16777215, 3200));
        primViewFindNext->setFont(font);
        primViewFindNext->setFocusPolicy(Qt::NoFocus);

        primFindContainer->addWidget(primViewFindNext);


        verticalLayout_2->addLayout(primFindContainer);

        primStageSplitter->addWidget(primFrame);
        renderFrame = new QFrame(primStageSplitter);
        renderFrame->setObjectName("renderFrame");
        renderFrame->setLayoutDirection(Qt::LeftToRight);
        renderFrame->setFrameShape(QFrame::NoFrame);
        renderFrame->setFrameShadow(QFrame::Plain);
        renderFrame->setLineWidth(0);
        verticalLayout_5 = new QVBoxLayout(renderFrame);
        verticalLayout_5->setObjectName("verticalLayout_5");
        verticalLayout_5->setContentsMargins(0, 0, 0, 0);
        renderMenuBar = new QMenuBar(renderFrame);
        renderMenuBar->setObjectName("renderMenuBar");
        renderMenuBar->setLayoutDirection(Qt::LeftToRight);
        renderMenuBar->setNativeMenuBar(false);
        menuRender = new QMenu(renderMenuBar);
        menuRender->setObjectName("menuRender");
        menuRendererSettings = new QMenu(menuRender);
        menuRendererSettings->setObjectName("menuRendererSettings");
        menuRendererAovs = new QMenu(menuRender);
        menuRendererAovs->setObjectName("menuRendererAovs");
        menuRendererCommands = new QMenu(menuRender);
        menuRendererCommands->setObjectName("menuRendererCommands");
        menuViewer = new QMenu(renderMenuBar);
        menuViewer->setObjectName("menuViewer");
        menuShading_Mode = new QMenu(menuViewer);
        menuShading_Mode->setObjectName("menuShading_Mode");
        menuColorCorrection = new QMenu(menuViewer);
        menuColorCorrection->setObjectName("menuColorCorrection");
        menuComplexity = new QMenu(menuViewer);
        menuComplexity->setObjectName("menuComplexity");
        menuBBox = new QMenu(menuViewer);
        menuBBox->setObjectName("menuBBox");
        menuDisplay = new QMenu(menuViewer);
        menuDisplay->setObjectName("menuDisplay");
        menuHUD = new QMenu(menuViewer);
        menuHUD->setObjectName("menuHUD");
        menuSelection_Highlighting = new QMenu(menuViewer);
        menuSelection_Highlighting->setObjectName("menuSelection_Highlighting");
        menuHighlightColor = new QMenu(menuSelection_Highlighting);
        menuHighlightColor->setObjectName("menuHighlightColor");
        menuBackground_Color = new QMenu(menuViewer);
        menuBackground_Color->setObjectName("menuBackground_Color");
        menuCamera = new QMenu(renderMenuBar);
        menuCamera->setObjectName("menuCamera");
        menuCameraSelect = new QMenu(menuCamera);
        menuCameraSelect->setObjectName("menuCameraSelect");
        menuCameraSelect->setTearOffEnabled(true);
        menuCameraGuides = new QMenu(menuCamera);
        menuCameraGuides->setObjectName("menuCameraGuides");
        menuCameraGuides->setTearOffEnabled(true);
        menuCamera_Masking = new QMenu(menuCamera);
        menuCamera_Masking->setObjectName("menuCamera_Masking");
        menuCamera_Reticles = new QMenu(menuCamera);
        menuCamera_Reticles->setObjectName("menuCamera_Reticles");
        menuPick = new QMenu(renderMenuBar);
        menuPick->setObjectName("menuPick");
        menuLights = new QMenu(renderMenuBar);
        menuLights->setObjectName("menuLights");

        verticalLayout_5->addWidget(renderMenuBar);

        glFrame = new QFrame(renderFrame);
        glFrame->setObjectName("glFrame");
        QSizePolicy sizePolicy3(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Expanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(glFrame->sizePolicy().hasHeightForWidth());
        glFrame->setSizePolicy(sizePolicy3);
        glFrame->setFrameShape(QFrame::NoFrame);
        glFrame->setFrameShadow(QFrame::Plain);
        glFrame->setLineWidth(0);

        verticalLayout_5->addWidget(glFrame);

        primStageSplitter->addWidget(renderFrame);
        topBottomSplitter->addWidget(primStageSplitter);
        attribBrowserInspectorSplitter = new QSplitter(topBottomSplitter);
        attribBrowserInspectorSplitter->setObjectName("attribBrowserInspectorSplitter");
        attribBrowserInspectorSplitter->setOrientation(Qt::Horizontal);
        attributeBrowserFrame = new QFrame(attribBrowserInspectorSplitter);
        attributeBrowserFrame->setObjectName("attributeBrowserFrame");
        attributeBrowserFrame->setFrameShape(QFrame::NoFrame);
        attributeBrowserFrame->setFrameShadow(QFrame::Plain);
        attributeBrowserFrame->setLineWidth(0);
        verticalLayout_7 = new QVBoxLayout(attributeBrowserFrame);
        verticalLayout_7->setObjectName("verticalLayout_7");
        verticalLayout_7->setContentsMargins(2, 0, 0, 5);
        propertyView = new QTreeWidget(attributeBrowserFrame);
        propertyView->setObjectName("propertyView");
        propertyView->setStyleSheet(QString::fromUtf8(""));
        propertyView->setFrameShape(QFrame::NoFrame);
        propertyView->setFrameShadow(QFrame::Plain);
        propertyView->setAlternatingRowColors(true);
        propertyView->setTextElideMode(Qt::ElideMiddle);
        propertyView->setColumnCount(3);

        verticalLayout_7->addWidget(propertyView);

        propertyLegendContainer = new PropertyLegend(attributeBrowserFrame);
        propertyLegendContainer->setObjectName("propertyLegendContainer");

        verticalLayout_7->addWidget(propertyLegendContainer);

        propertyFindContainer = new QHBoxLayout();
        propertyFindContainer->setObjectName("propertyFindContainer");
        propertyFindContainer->setContentsMargins(5, -1, 5, -1);
        propertyLegendQButton = new QPushButton(attributeBrowserFrame);
        propertyLegendQButton->setObjectName("propertyLegendQButton");
        QSizePolicy sizePolicy4(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(propertyLegendQButton->sizePolicy().hasHeightForWidth());
        propertyLegendQButton->setSizePolicy(sizePolicy4);
        propertyLegendQButton->setMaximumSize(QSize(3200, 3200));
        propertyLegendQButton->setFont(font);
        propertyLegendQButton->setFocusPolicy(Qt::NoFocus);
        propertyLegendQButton->setIconSize(QSize(12, 12));

        propertyFindContainer->addWidget(propertyLegendQButton);

        attrViewLineEdit = new QLineEdit(attributeBrowserFrame);
        attrViewLineEdit->setObjectName("attrViewLineEdit");
        sizePolicy2.setHeightForWidth(attrViewLineEdit->sizePolicy().hasHeightForWidth());
        attrViewLineEdit->setSizePolicy(sizePolicy2);
        attrViewLineEdit->setMaximumSize(QSize(16777215, 3200));
        attrViewLineEdit->setFont(font);

        propertyFindContainer->addWidget(attrViewLineEdit);

        attrViewFindNext = new QPushButton(attributeBrowserFrame);
        attrViewFindNext->setObjectName("attrViewFindNext");
        sizePolicy1.setHeightForWidth(attrViewFindNext->sizePolicy().hasHeightForWidth());
        attrViewFindNext->setSizePolicy(sizePolicy1);
        attrViewFindNext->setMaximumSize(QSize(16777215, 3200));
        attrViewFindNext->setFont(font);
        attrViewFindNext->setFocusPolicy(Qt::NoFocus);
        attrViewFindNext->setIconSize(QSize(24, 24));

        propertyFindContainer->addWidget(attrViewFindNext);

        propertyFindContainer->setStretch(0, 1);
        propertyFindContainer->setStretch(1, 20);
        propertyFindContainer->setStretch(2, 2);

        verticalLayout_7->addLayout(propertyFindContainer);

        attribBrowserInspectorSplitter->addWidget(attributeBrowserFrame);
        propertyInspectorFrame = new QFrame(attribBrowserInspectorSplitter);
        propertyInspectorFrame->setObjectName("propertyInspectorFrame");
        propertyInspectorFrame->setFrameShape(QFrame::NoFrame);
        propertyInspectorFrame->setFrameShadow(QFrame::Plain);
        propertyInspectorFrame->setLineWidth(0);
        verticalLayout_8 = new QVBoxLayout(propertyInspectorFrame);
        verticalLayout_8->setSpacing(0);
        verticalLayout_8->setObjectName("verticalLayout_8");
        verticalLayout_8->setContentsMargins(0, 1, 2, 2);
        propertyInspectorContainer = new QFrame(propertyInspectorFrame);
        propertyInspectorContainer->setObjectName("propertyInspectorContainer");
        propertyInspectorContainer->setFrameShape(QFrame::NoFrame);
        propertyInspectorContainer->setFrameShadow(QFrame::Plain);
        verticalLayout_3 = new QVBoxLayout(propertyInspectorContainer);
        verticalLayout_3->setObjectName("verticalLayout_3");
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        propertyInspector = new QTabWidget(propertyInspectorContainer);
        propertyInspector->setObjectName("propertyInspector");
        value = new QWidget();
        value->setObjectName("value");
        verticalLayout = new QVBoxLayout(value);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(6, 6, 6, 6);
        attributeValueEditor = new AttributeValueEditor(value);
        attributeValueEditor->setObjectName("attributeValueEditor");

        verticalLayout->addWidget(attributeValueEditor);

        propertyInspector->addTab(value, QString());
        metadata = new QWidget();
        metadata->setObjectName("metadata");
        horizontalLayout = new QHBoxLayout(metadata);
        horizontalLayout->setObjectName("horizontalLayout");
        attributeBrowserFrame_1 = new QFrame(metadata);
        attributeBrowserFrame_1->setObjectName("attributeBrowserFrame_1");
        attributeBrowserFrame_1->setFrameShape(QFrame::NoFrame);
        attributeBrowserFrame_1->setFrameShadow(QFrame::Plain);
        attributeBrowserFrame_1->setLineWidth(0);
        verticalLayout_71 = new QVBoxLayout(attributeBrowserFrame_1);
        verticalLayout_71->setObjectName("verticalLayout_71");
        verticalLayout_71->setContentsMargins(2, 0, 0, 5);
        metadataView = new QTableWidget(attributeBrowserFrame_1);
        if (metadataView->columnCount() < 2)
            metadataView->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        metadataView->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        metadataView->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        metadataView->setObjectName("metadataView");
        metadataView->setStyleSheet(QString::fromUtf8(""));
        metadataView->setFrameShape(QFrame::NoFrame);
        metadataView->setFrameShadow(QFrame::Plain);
        metadataView->setLineWidth(0);
        metadataView->setEditTriggers(QAbstractItemView::NoEditTriggers);
        metadataView->setAlternatingRowColors(true);
        metadataView->setSelectionMode(QAbstractItemView::SingleSelection);
        metadataView->setSelectionBehavior(QAbstractItemView::SelectRows);
        metadataView->setShowGrid(false);
        metadataView->setGridStyle(Qt::SolidLine);
        metadataView->setColumnCount(2);
        metadataView->horizontalHeader()->setCascadingSectionResizes(true);
        metadataView->horizontalHeader()->setMinimumSectionSize(30);
        metadataView->horizontalHeader()->setDefaultSectionSize(220);
        metadataView->horizontalHeader()->setProperty("showSortIndicator", QVariant(false));
        metadataView->horizontalHeader()->setStretchLastSection(true);
        metadataView->verticalHeader()->setVisible(false);
        metadataView->verticalHeader()->setMinimumSectionSize(20);
        metadataView->verticalHeader()->setDefaultSectionSize(30);
        metadataView->verticalHeader()->setStretchLastSection(false);

        verticalLayout_71->addWidget(metadataView);


        horizontalLayout->addWidget(attributeBrowserFrame_1);

        propertyInspector->addTab(metadata, QString());
        layerstack = new QWidget();
        layerstack->setObjectName("layerstack");
        layerStackFrameLayout = new QHBoxLayout(layerstack);
        layerStackFrameLayout->setObjectName("layerStackFrameLayout");
        layerStackFrame = new QFrame(layerstack);
        layerStackFrame->setObjectName("layerStackFrame");
        layerStackFrame->setFrameShape(QFrame::NoFrame);
        layerStackFrame->setFrameShadow(QFrame::Plain);
        layerStackFrame->setLineWidth(0);
        layerStackViewLayout = new QVBoxLayout(layerStackFrame);
        layerStackViewLayout->setObjectName("layerStackViewLayout");
        layerStackViewLayout->setContentsMargins(2, 0, 0, 5);
        layerStackView = new QTableWidget(layerStackFrame);
        if (layerStackView->columnCount() < 4)
            layerStackView->setColumnCount(4);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        layerStackView->setHorizontalHeaderItem(0, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        layerStackView->setHorizontalHeaderItem(1, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        layerStackView->setHorizontalHeaderItem(2, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        layerStackView->setHorizontalHeaderItem(3, __qtablewidgetitem5);
        layerStackView->setObjectName("layerStackView");
        layerStackView->setStyleSheet(QString::fromUtf8(""));
        layerStackView->setFrameShape(QFrame::NoFrame);
        layerStackView->setFrameShadow(QFrame::Plain);
        layerStackView->setEditTriggers(QAbstractItemView::NoEditTriggers);
        layerStackView->setAlternatingRowColors(true);
        layerStackView->setSelectionMode(QAbstractItemView::SingleSelection);
        layerStackView->setSelectionBehavior(QAbstractItemView::SelectRows);
        layerStackView->setShowGrid(false);
        layerStackView->setGridStyle(Qt::SolidLine);
        layerStackView->setColumnCount(4);
        layerStackView->horizontalHeader()->setCascadingSectionResizes(true);
        layerStackView->horizontalHeader()->setMinimumSectionSize(30);
        layerStackView->horizontalHeader()->setDefaultSectionSize(220);
        layerStackView->horizontalHeader()->setProperty("showSortIndicator", QVariant(false));
        layerStackView->horizontalHeader()->setStretchLastSection(true);
        layerStackView->verticalHeader()->setVisible(false);
        layerStackView->verticalHeader()->setMinimumSectionSize(20);
        layerStackView->verticalHeader()->setDefaultSectionSize(30);
        layerStackView->verticalHeader()->setStretchLastSection(false);

        layerStackViewLayout->addWidget(layerStackView);


        layerStackFrameLayout->addWidget(layerStackFrame);

        propertyInspector->addTab(layerstack, QString());
        tab = new QWidget();
        tab->setObjectName("tab");
        horizontalLayout_4 = new QHBoxLayout(tab);
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        compositionTreeWidget = new QTreeWidget(tab);
        compositionTreeWidget->setObjectName("compositionTreeWidget");
        compositionTreeWidget->setFrameShape(QFrame::NoFrame);
        compositionTreeWidget->setFrameShadow(QFrame::Plain);
        compositionTreeWidget->setAlternatingRowColors(true);
        compositionTreeWidget->setIndentation(15);
        compositionTreeWidget->header()->setHighlightSections(false);
        compositionTreeWidget->header()->setStretchLastSection(false);

        horizontalLayout_4->addWidget(compositionTreeWidget);

        propertyInspector->addTab(tab, QString());

        verticalLayout_3->addWidget(propertyInspector);


        verticalLayout_8->addWidget(propertyInspectorContainer);

        attribBrowserInspectorSplitter->addWidget(propertyInspectorFrame);
        topBottomSplitter->addWidget(attribBrowserInspectorSplitter);

        verticalLayout_4->addWidget(topBottomSplitter);

        frameChangeContainer = new QHBoxLayout();
        frameChangeContainer->setObjectName("frameChangeContainer");
        sliderContainer = new QVBoxLayout();
        sliderContainer->setObjectName("sliderContainer");
        sliderTopContainer = new QHBoxLayout();
        sliderTopContainer->setObjectName("sliderTopContainer");
        stageBegin = new QLabel(centralwidget);
        stageBegin->setObjectName("stageBegin");
        QSizePolicy sizePolicy5(QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Fixed);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(stageBegin->sizePolicy().hasHeightForWidth());
        stageBegin->setSizePolicy(sizePolicy5);
        stageBegin->setMaximumSize(QSize(9000, 9000));

        sliderTopContainer->addWidget(stageBegin);

        rangeBeginLayout = new QVBoxLayout();
        rangeBeginLayout->setObjectName("rangeBeginLayout");
        rangeBeginLayout->setSizeConstraint(QLayout::SetFixedSize);
        verticalSpacer = new QSpacerItem(20, 7, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Maximum);

        rangeBeginLayout->addItem(verticalSpacer);

        rangeBegin = new QLineEdit(centralwidget);
        rangeBegin->setObjectName("rangeBegin");
        sizePolicy5.setHeightForWidth(rangeBegin->sizePolicy().hasHeightForWidth());
        rangeBegin->setSizePolicy(sizePolicy5);
        rangeBegin->setMaximumSize(QSize(90, 9000));
        rangeBegin->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        rangeBeginLayout->addWidget(rangeBegin);

        verticalSpacer_2 = new QSpacerItem(20, 7, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Maximum);

        rangeBeginLayout->addItem(verticalSpacer_2);


        sliderTopContainer->addLayout(rangeBeginLayout);

        frameSlider = new FrameSlider(centralwidget);
        frameSlider->setObjectName("frameSlider");
        frameSlider->setMinimumSize(QSize(90, 45));
        frameSlider->setPageStep(0);
        frameSlider->setOrientation(Qt::Horizontal);
        frameSlider->setTickPosition(QSlider::NoTicks);
        frameSlider->setTickInterval(0);

        sliderTopContainer->addWidget(frameSlider);

        rangeEndLayout = new QVBoxLayout();
        rangeEndLayout->setObjectName("rangeEndLayout");
        rangeEndLayout->setSizeConstraint(QLayout::SetFixedSize);
        verticalSpacer_3 = new QSpacerItem(10, 7, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Maximum);

        rangeEndLayout->addItem(verticalSpacer_3);

        rangeEnd = new QLineEdit(centralwidget);
        rangeEnd->setObjectName("rangeEnd");
        QSizePolicy sizePolicy6(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Fixed);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(rangeEnd->sizePolicy().hasHeightForWidth());
        rangeEnd->setSizePolicy(sizePolicy6);
        rangeEnd->setMaximumSize(QSize(90, 9000));
        rangeEnd->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        rangeEndLayout->addWidget(rangeEnd);

        verticalSpacer_4 = new QSpacerItem(20, 7, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Maximum);

        rangeEndLayout->addItem(verticalSpacer_4);


        sliderTopContainer->addLayout(rangeEndLayout);

        stageEnd = new QLabel(centralwidget);
        stageEnd->setObjectName("stageEnd");
        sizePolicy5.setHeightForWidth(stageEnd->sizePolicy().hasHeightForWidth());
        stageEnd->setSizePolicy(sizePolicy5);
        stageEnd->setMaximumSize(QSize(9000, 9000));

        sliderTopContainer->addWidget(stageEnd);

        sliderTopContainer->setStretch(2, 200);

        sliderContainer->addLayout(sliderTopContainer);

        sliderBottomContainer = new QHBoxLayout();
        sliderBottomContainer->setSpacing(6);
        sliderBottomContainer->setObjectName("sliderBottomContainer");
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        sliderBottomContainer->addItem(horizontalSpacer_4);

        redrawOnScrub = new QCheckBox(centralwidget);
        redrawOnScrub->setObjectName("redrawOnScrub");
        sizePolicy1.setHeightForWidth(redrawOnScrub->sizePolicy().hasHeightForWidth());
        redrawOnScrub->setSizePolicy(sizePolicy1);
        redrawOnScrub->setMaximumSize(QSize(3500, 16777215));
        redrawOnScrub->setFocusPolicy(Qt::NoFocus);
        redrawOnScrub->setChecked(true);

        sliderBottomContainer->addWidget(redrawOnScrub);

        horizontalSpacer_9 = new QSpacerItem(20, 20, QSizePolicy::Policy::Fixed, QSizePolicy::Policy::Minimum);

        sliderBottomContainer->addItem(horizontalSpacer_9);

        stepSizeLabel = new QLabel(centralwidget);
        stepSizeLabel->setObjectName("stepSizeLabel");

        sliderBottomContainer->addWidget(stepSizeLabel);

        stepSize = new QLineEdit(centralwidget);
        stepSize->setObjectName("stepSize");
        stepSize->setEnabled(true);
        sizePolicy1.setHeightForWidth(stepSize->sizePolicy().hasHeightForWidth());
        stepSize->setSizePolicy(sizePolicy1);
        stepSize->setMaximumSize(QSize(60, 16777215));
        stepSize->setAlignment(Qt::AlignCenter);

        sliderBottomContainer->addWidget(stepSize);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        sliderBottomContainer->addItem(horizontalSpacer);


        sliderContainer->addLayout(sliderBottomContainer);


        frameChangeContainer->addLayout(sliderContainer);

        line = new QFrame(centralwidget);
        line->setObjectName("line");
        line->setFrameShape(QFrame::Shape::VLine);
        line->setFrameShadow(QFrame::Shadow::Sunken);

        frameChangeContainer->addWidget(line);

        playContainer = new QVBoxLayout();
        playContainer->setObjectName("playContainer");
        playButtonContainer = new QHBoxLayout();
        playButtonContainer->setObjectName("playButtonContainer");
        horizontalSpacer_2 = new QSpacerItem(15, 20, QSizePolicy::Policy::Maximum, QSizePolicy::Policy::Minimum);

        playButtonContainer->addItem(horizontalSpacer_2);

        playButton = new QPushButton(centralwidget);
        playButton->setObjectName("playButton");
        QSizePolicy sizePolicy7(QSizePolicy::Policy::Maximum, QSizePolicy::Policy::Minimum);
        sizePolicy7.setHorizontalStretch(0);
        sizePolicy7.setVerticalStretch(0);
        sizePolicy7.setHeightForWidth(playButton->sizePolicy().hasHeightForWidth());
        playButton->setSizePolicy(sizePolicy7);
        playButton->setMaximumSize(QSize(1115, 16777215));
        playButton->setFocusPolicy(Qt::NoFocus);

        playButtonContainer->addWidget(playButton, 0, Qt::AlignHCenter);

        horizontalSpacer_3 = new QSpacerItem(15, 20, QSizePolicy::Policy::Maximum, QSizePolicy::Policy::Minimum);

        playButtonContainer->addItem(horizontalSpacer_3);


        playContainer->addLayout(playButtonContainer);

        frameContainer = new QHBoxLayout();
        frameContainer->setObjectName("frameContainer");
        horizontalSpacer_5 = new QSpacerItem(5, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        frameContainer->addItem(horizontalSpacer_5);

        frameLabel = new QLabel(centralwidget);
        frameLabel->setObjectName("frameLabel");
        sizePolicy4.setHeightForWidth(frameLabel->sizePolicy().hasHeightForWidth());
        frameLabel->setSizePolicy(sizePolicy4);
        frameLabel->setMaximumSize(QSize(9000, 16777215));

        frameContainer->addWidget(frameLabel);

        frameField = new QLineEdit(centralwidget);
        frameField->setObjectName("frameField");
        sizePolicy4.setHeightForWidth(frameField->sizePolicy().hasHeightForWidth());
        frameField->setSizePolicy(sizePolicy4);
        frameField->setMinimumSize(QSize(70, 0));
        frameField->setMaximumSize(QSize(90, 1000));
        frameField->setFont(font);
        frameField->setMaxLength(7);
        frameField->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        frameContainer->addWidget(frameField);


        playContainer->addLayout(frameContainer);


        frameChangeContainer->addLayout(playContainer);

        frameChangeContainer->setStretch(0, 3);

        verticalLayout_4->addLayout(frameChangeContainer);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 1145, 20));
        menubar->setMinimumSize(QSize(0, 0));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName("menuFile");
        menuSave_State_As = new QMenu(menuFile);
        menuSave_State_As->setObjectName("menuSave_State_As");
        menuLoad_New_State = new QMenu(menuFile);
        menuLoad_New_State->setObjectName("menuLoad_New_State");
        menuEdit = new QMenu(menubar);
        menuEdit->setObjectName("menuEdit");
        menuInterpolation = new QMenu(menuEdit);
        menuInterpolation->setObjectName("menuInterpolation");
        menuWindow = new QMenu(menubar);
        menuWindow->setObjectName("menuWindow");
        menuWindow->setMinimumSize(QSize(0, 0));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        statusbar->setSizeGripEnabled(true);
        MainWindow->setStatusBar(statusbar);

        primViewMenuBar->addAction(menuNavigation->menuAction());
        primViewMenuBar->addAction(menuShow->menuAction());
        menuNavigation->addAction(actionFind_Prims);
        menuNavigation->addAction(actionSelect_Stage_Root);
        menuNavigation->addAction(actionSelect_Model_Root);
        menuNavigation->addSeparator();
        menuNavigation->addAction(actionSelect_Bound_Preview_Material);
        menuNavigation->addAction(actionSelect_Bound_Full_Material);
        menuNavigation->addAction(actionSelect_Preview_Binding_Relationship);
        menuNavigation->addAction(actionSelect_Full_Binding_Relationship);
        menuShow->addAction(menuPrim_View_Depth->menuAction());
        menuShow->addSeparator();
        menuShow->addAction(actionShow_Inactive_Prims);
        menuShow->addAction(actionShow_All_Prototype_Prims);
        menuShow->addAction(actionShow_Undefined_Prims);
        menuShow->addAction(actionShow_Abstract_Prims);
        menuShow->addAction(actionShow_Prim_DisplayName);
        menuPrim_View_Depth->addAction(actionLevel_1);
        menuPrim_View_Depth->addAction(actionLevel_2);
        menuPrim_View_Depth->addAction(actionLevel_3);
        menuPrim_View_Depth->addAction(actionLevel_4);
        menuPrim_View_Depth->addAction(actionLevel_5);
        menuPrim_View_Depth->addAction(actionLevel_6);
        menuPrim_View_Depth->addAction(actionLevel_7);
        menuPrim_View_Depth->addAction(actionLevel_8);
        menuPrim_View_Depth->addSeparator();
        menuPrim_View_Depth->addAction(actionExpand_All);
        menuPrim_View_Depth->addAction(actionCollapse_All);
        renderMenuBar->addAction(menuRender->menuAction());
        renderMenuBar->addAction(menuViewer->menuAction());
        renderMenuBar->addAction(menuPick->menuAction());
        renderMenuBar->addAction(menuCamera->menuAction());
        renderMenuBar->addAction(menuLights->menuAction());
        menuRender->addSeparator();
        menuRender->addAction(menuRendererSettings->menuAction());
        menuRender->addAction(menuRendererAovs->menuAction());
        menuRender->addAction(menuRendererCommands->menuAction());
        menuRender->addSeparator();
        menuRender->addAction(actionPause);
        menuRender->addAction(actionStop);
        menuViewer->addAction(menuShading_Mode->menuAction());
        menuViewer->addAction(menuComplexity->menuAction());
        menuViewer->addAction(menuBBox->menuAction());
        menuViewer->addAction(menuDisplay->menuAction());
        menuViewer->addSeparator();
        menuViewer->addAction(menuHUD->menuAction());
        menuViewer->addAction(menuSelection_Highlighting->menuAction());
        menuViewer->addAction(actionRollover_Prim_Info);
        menuViewer->addSeparator();
        menuViewer->addAction(actionEnable_Scene_Materials);
        menuViewer->addAction(actionAdjust_Default_Material);
        menuViewer->addSeparator();
        menuViewer->addAction(menuColorCorrection->menuAction());
        menuViewer->addSeparator();
        menuViewer->addAction(menuBackground_Color->menuAction());
        menuViewer->addAction(actionCull_Backfaces);
        menuViewer->addAction(actionDomeLightTexturesVisible);
        menuShading_Mode->addAction(actionWireframe);
        menuShading_Mode->addAction(actionWireframeOnSurface);
        menuShading_Mode->addAction(actionSmooth_Shaded);
        menuShading_Mode->addAction(actionFlat_Shaded);
        menuShading_Mode->addAction(actionPoints);
        menuShading_Mode->addAction(actionGeom_Only);
        menuShading_Mode->addAction(actionGeom_Smooth);
        menuShading_Mode->addAction(actionGeom_Flat);
        menuShading_Mode->addAction(actionHidden_Surface_Wireframe);
        menuColorCorrection->addAction(actionNoColorCorrection);
        menuColorCorrection->addAction(actionSRGBColorCorrection);
        menuColorCorrection->addAction(actionOpenColorIO);
        menuComplexity->addAction(actionLow);
        menuComplexity->addAction(actionMedium);
        menuComplexity->addAction(actionHigh);
        menuComplexity->addAction(actionVery_High);
        menuBBox->addAction(showBBoxes);
        menuBBox->addSeparator();
        menuBBox->addAction(showAABBox);
        menuBBox->addAction(showOBBox);
        menuBBox->addAction(showBBoxPlayback);
        menuBBox->addSeparator();
        menuBBox->addAction(useExtentsHint);
        menuDisplay->addAction(actionDisplay_Guide);
        menuDisplay->addAction(actionDisplay_Proxy);
        menuDisplay->addAction(actionDisplay_Render);
        menuHUD->addAction(actionHUD);
        menuHUD->addSeparator();
        menuHUD->addAction(actionHUD_Info);
        menuHUD->addAction(actionHUD_Complexity);
        menuHUD->addAction(actionHUD_Performance);
        menuHUD->addAction(actionHUD_GPUstats);
        menuSelection_Highlighting->addAction(actionNever);
        menuSelection_Highlighting->addAction(actionOnly_when_paused);
        menuSelection_Highlighting->addAction(actionAlways);
        menuSelection_Highlighting->addAction(menuHighlightColor->menuAction());
        menuHighlightColor->addAction(actionSelYellow);
        menuHighlightColor->addAction(actionSelWhite);
        menuHighlightColor->addAction(actionSelCyan);
        menuBackground_Color->addAction(actionBlack);
        menuBackground_Color->addAction(actionGrey_Dark);
        menuBackground_Color->addAction(actionGrey_Light);
        menuBackground_Color->addAction(actionWhite);
        menuCamera->addAction(menuCameraGuides->menuAction());
        menuCamera->addAction(menuCamera_Masking->menuAction());
        menuCamera->addAction(menuCamera_Reticles->menuAction());
        menuCamera->addAction(menuCameraSelect->menuAction());
        menuCamera->addSeparator();
        menuCamera->addAction(actionFrame_Selected);
        menuCamera->addAction(actionToggle_Framed_View);
        menuCamera->addAction(actionReset_View);
        menuCamera->addSeparator();
        menuCamera->addAction(actionCopy_Viewer_Image);
        menuCamera->addAction(actionSave_Viewer_Image);
        menuCamera->addSeparator();
        menuCamera->addAction(actionAuto_Compute_Clipping_Planes);
        menuCamera->addAction(actionAdjust_Free_Camera);
        menuCameraSelect->addAction(actionFreeCam);
        menuCameraGuides->addAction(actionCameraMask_Outline);
        menuCameraGuides->addAction(actionDisplay_Camera_Oracles);
        menuCamera_Masking->addAction(actionCameraMask_Full);
        menuCamera_Masking->addAction(actionCameraMask_Partial);
        menuCamera_Masking->addAction(actionCameraMask_None);
        menuCamera_Masking->addSeparator();
        menuCamera_Masking->addAction(actionCameraMask_Color);
        menuCamera_Reticles->addAction(actionCameraReticles_Inside);
        menuCamera_Reticles->addAction(actionCameraReticles_Outside);
        menuCamera_Reticles->addSeparator();
        menuCamera_Reticles->addAction(actionCameraReticles_Color);
        menuPick->addAction(actionPick_Prims);
        menuPick->addAction(actionPick_Models);
        menuPick->addAction(actionPick_Instances);
        menuPick->addAction(actionPick_Prototypes);
        menuLights->addAction(actionEnable_Scene_Lights);
        menuLights->addAction(actionAmbient_Only);
        menuLights->addAction(actionDomeLight);
        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuEdit->menuAction());
        menubar->addAction(menuWindow->menuAction());
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionReopen_Stage);
        menuFile->addAction(actionReload_All_Layers);
        menuFile->addSeparator();
        menuFile->addAction(actionSave_Overrides_As);
        menuFile->addAction(actionSave_Flattened_As);
        menuFile->addSeparator();
        menuFile->addAction(menuLoad_New_State->menuAction());
        menuFile->addAction(actionSave_State_To);
        menuFile->addAction(menuSave_State_As->menuAction());
        menuFile->addAction(actionSave_State_As_New_Config);
        menuFile->addAction(actionQuit);
        menuEdit->addAction(menuInterpolation->menuAction());
        menuEdit->addSeparator();
        menuEdit->addAction(actionLoad);
        menuEdit->addAction(actionUnload);
        menuEdit->addSeparator();
        menuEdit->addAction(actionActivate);
        menuEdit->addAction(actionDeactivate);
        menuEdit->addSeparator();
        menuEdit->addAction(actionMake_Visible);
        menuEdit->addAction(actionVis_Only);
        menuEdit->addAction(actionMake_Invisible);
        menuEdit->addAction(actionRemove_Session_Visibility);
        menuEdit->addAction(actionReset_All_Session_Visibility);
        menuWindow->addAction(actionToggle_Viewer_Mode);
        menuWindow->addSeparator();
        menuWindow->addAction(showInterpreter);
        menuWindow->addAction(actionPreferences);
        menuWindow->addAction(showDebugFlags);
        menuWindow->addAction(showHydraSceneBrowser);

        retranslateUi(MainWindow);

        propertyInspector->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        MainWindow->setProperty("comment", QVariant(QCoreApplication::translate("MainWindow", "\n"
"     PLEASE DO NOT HAND EDIT THIS FILE, AS ITS XML FORMAT IS FRAGILE AND QT'S\n"
"     TOOLS ARE INCONSISTENT ACROSS PLATFORMS ON TOLERANCE TO BAD CONSTRUCTS.\n"
"     \n"
"     Instead prefer qdesigner5 to make edits to the document.  If you are \n"
"     allergic to gui tools, then AT LEAST, after making hand edits, prior to\n"
"     checking them in, load this file in qdesigner5, ensure it loads without \n"
"     error, and then SAVE THE FILE BACK OUT, AND CHECK THAT IN, so that the\n"
"     next developer using qdesigner5 does not contend with unrelated diffs.\n"
"     \n"
"     Copyright 2016 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        actionOpen->setText(QCoreApplication::translate("MainWindow", "Open", nullptr));
#if QT_CONFIG(shortcut)
        actionOpen->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        actionQuit->setText(QCoreApplication::translate("MainWindow", "Quit", nullptr));
#if QT_CONFIG(shortcut)
        actionQuit->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+Q", nullptr));
#endif // QT_CONFIG(shortcut)
        actionPause->setText(QCoreApplication::translate("MainWindow", "Pause Render", nullptr));
#if QT_CONFIG(shortcut)
        actionPause->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+P", nullptr));
#endif // QT_CONFIG(shortcut)
        actionStop->setText(QCoreApplication::translate("MainWindow", "Stop Render", nullptr));
#if QT_CONFIG(shortcut)
        actionStop->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+\\", nullptr));
#endif // QT_CONFIG(shortcut)
        actionReset_View->setText(QCoreApplication::translate("MainWindow", "Reset View", nullptr));
        actionToggle_Framed_View->setText(QCoreApplication::translate("MainWindow", "Toggle Framed View", nullptr));
#if QT_CONFIG(tooltip)
        actionToggle_Framed_View->setToolTip(QCoreApplication::translate("MainWindow", "Toggle camera with view saved before last Frame operation", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionToggle_Framed_View->setShortcut(QCoreApplication::translate("MainWindow", "J", nullptr));
#endif // QT_CONFIG(shortcut)
        actionWatch_Window->setText(QCoreApplication::translate("MainWindow", "Watch Window", nullptr));
#if QT_CONFIG(shortcut)
        actionWatch_Window->setShortcut(QCoreApplication::translate("MainWindow", "W", nullptr));
#endif // QT_CONFIG(shortcut)
        actionReopen_Stage->setText(QCoreApplication::translate("MainWindow", "Reopen Stage", nullptr));
#if QT_CONFIG(shortcut)
        actionReopen_Stage->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+Shift+R", nullptr));
#endif // QT_CONFIG(shortcut)
        actionDump_RIB->setText(QCoreApplication::translate("MainWindow", "Dump RIB...", nullptr));
        actionLevel_1->setText(QCoreApplication::translate("MainWindow", "Level 1", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_1->setShortcut(QCoreApplication::translate("MainWindow", "Alt+1", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_2->setText(QCoreApplication::translate("MainWindow", "Level 2", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_2->setShortcut(QCoreApplication::translate("MainWindow", "Alt+2", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_3->setText(QCoreApplication::translate("MainWindow", "Level 3", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_3->setShortcut(QCoreApplication::translate("MainWindow", "Alt+3", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_4->setText(QCoreApplication::translate("MainWindow", "Level 4", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_4->setShortcut(QCoreApplication::translate("MainWindow", "Alt+4", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_5->setText(QCoreApplication::translate("MainWindow", "Level 5", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_5->setShortcut(QCoreApplication::translate("MainWindow", "Alt+5", nullptr));
#endif // QT_CONFIG(shortcut)
        actionExpand_All->setText(QCoreApplication::translate("MainWindow", "Expand All", nullptr));
#if QT_CONFIG(shortcut)
        actionExpand_All->setShortcut(QCoreApplication::translate("MainWindow", "Alt+9", nullptr));
#endif // QT_CONFIG(shortcut)
        actionCollapse_All->setText(QCoreApplication::translate("MainWindow", "Collapse All", nullptr));
#if QT_CONFIG(shortcut)
        actionCollapse_All->setShortcut(QCoreApplication::translate("MainWindow", "Alt+0", nullptr));
#endif // QT_CONFIG(shortcut)
        actionAmbient_Only->setText(QCoreApplication::translate("MainWindow", "Enable Default Camera Light", nullptr));
        actionDomeLight->setText(QCoreApplication::translate("MainWindow", "Enable Default Dome Light", nullptr));
        actionDomeLightTexturesVisible->setText(QCoreApplication::translate("MainWindow", "Show Dome Light Textures", nullptr));
        actionLevel_6->setText(QCoreApplication::translate("MainWindow", "Level 6", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_6->setShortcut(QCoreApplication::translate("MainWindow", "Alt+6", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_7->setText(QCoreApplication::translate("MainWindow", "Level 7", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_7->setShortcut(QCoreApplication::translate("MainWindow", "Alt+7", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLevel_8->setText(QCoreApplication::translate("MainWindow", "Level 8", nullptr));
#if QT_CONFIG(shortcut)
        actionLevel_8->setShortcut(QCoreApplication::translate("MainWindow", "Alt+8", nullptr));
#endif // QT_CONFIG(shortcut)
        actionWireframe->setText(QCoreApplication::translate("MainWindow", "Wireframe", nullptr));
#if QT_CONFIG(shortcut)
        actionWireframe->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+0", nullptr));
#endif // QT_CONFIG(shortcut)
        actionWireframeOnSurface->setText(QCoreApplication::translate("MainWindow", "WireframeOnSurface", nullptr));
#if QT_CONFIG(shortcut)
        actionWireframeOnSurface->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+1", nullptr));
#endif // QT_CONFIG(shortcut)
        actionSmooth_Shaded->setText(QCoreApplication::translate("MainWindow", "Smooth Shaded", nullptr));
#if QT_CONFIG(shortcut)
        actionSmooth_Shaded->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+2", nullptr));
#endif // QT_CONFIG(shortcut)
        actionFlat_Shaded->setText(QCoreApplication::translate("MainWindow", "Flat Shaded", nullptr));
#if QT_CONFIG(shortcut)
        actionFlat_Shaded->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+3", nullptr));
#endif // QT_CONFIG(shortcut)
        actionPoints->setText(QCoreApplication::translate("MainWindow", "Points", nullptr));
#if QT_CONFIG(shortcut)
        actionPoints->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+4", nullptr));
#endif // QT_CONFIG(shortcut)
        actionGeom_Only->setText(QCoreApplication::translate("MainWindow", "Geom Only", nullptr));
#if QT_CONFIG(shortcut)
        actionGeom_Only->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+6", nullptr));
#endif // QT_CONFIG(shortcut)
        actionRedrawOnScrub->setText(QCoreApplication::translate("MainWindow", "Redraw While Frame Scrubbing", nullptr));
        actionIncrementComplexity1->setText(QCoreApplication::translate("MainWindow", "IncrementComplexity", nullptr));
#if QT_CONFIG(shortcut)
        actionIncrementComplexity1->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+=", nullptr));
#endif // QT_CONFIG(shortcut)
        actionDecrementComplexity->setText(QCoreApplication::translate("MainWindow", "DecrementComplexity", nullptr));
#if QT_CONFIG(shortcut)
        actionDecrementComplexity->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+-", nullptr));
#endif // QT_CONFIG(shortcut)
        actionPRMan->setText(QCoreApplication::translate("MainWindow", "Render View", nullptr));
#if QT_CONFIG(shortcut)
        actionPRMan->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+R", nullptr));
#endif // QT_CONFIG(shortcut)
        actionBlack->setText(QCoreApplication::translate("MainWindow", "Black", nullptr));
#if QT_CONFIG(statustip)
        actionBlack->setStatusTip(QString());
#endif // QT_CONFIG(statustip)
        actionWhite->setText(QCoreApplication::translate("MainWindow", "White", nullptr));
#if QT_CONFIG(statustip)
        actionWhite->setStatusTip(QString());
#endif // QT_CONFIG(statustip)
        actionGrey_Light->setText(QCoreApplication::translate("MainWindow", "Grey (Light)", nullptr));
#if QT_CONFIG(statustip)
        actionGrey_Light->setStatusTip(QString());
#endif // QT_CONFIG(statustip)
        actionGrey_Dark->setText(QCoreApplication::translate("MainWindow", "Grey (Dark)", nullptr));
#if QT_CONFIG(statustip)
        actionGrey_Dark->setStatusTip(QString());
#endif // QT_CONFIG(statustip)
        actionGeom_Smooth->setText(QCoreApplication::translate("MainWindow", "Geom Smooth", nullptr));
#if QT_CONFIG(shortcut)
        actionGeom_Smooth->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+7", nullptr));
#endif // QT_CONFIG(shortcut)
        actionGeom_Flat->setText(QCoreApplication::translate("MainWindow", "Geom Flat", nullptr));
#if QT_CONFIG(shortcut)
        actionGeom_Flat->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+8", nullptr));
#endif // QT_CONFIG(shortcut)
        actionHidden_Surface_Wireframe->setText(QCoreApplication::translate("MainWindow", "Hidden Surface Wireframe", nullptr));
#if QT_CONFIG(shortcut)
        actionHidden_Surface_Wireframe->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+9", nullptr));
#endif // QT_CONFIG(shortcut)
        actionNoColorCorrection->setText(QCoreApplication::translate("MainWindow", "disabled", nullptr));
        actionSRGBColorCorrection->setText(QCoreApplication::translate("MainWindow", "sRGB", nullptr));
        actionOpenColorIO->setText(QCoreApplication::translate("MainWindow", "openColorIO", nullptr));
        actionFreeCam->setText(QCoreApplication::translate("MainWindow", "Free Camera", nullptr));
        actionSave_Overrides_As->setText(QCoreApplication::translate("MainWindow", "Save Overrides As...", nullptr));
        actionSave_Overrides_As->setIconText(QCoreApplication::translate("MainWindow", "Save Overrides As...", nullptr));
#if QT_CONFIG(tooltip)
        actionSave_Overrides_As->setToolTip(QCoreApplication::translate("MainWindow", "Save property and metadata overrides", nullptr));
#endif // QT_CONFIG(tooltip)
        actionSave_Flattened_As->setText(QCoreApplication::translate("MainWindow", "Save Flattened As...", nullptr));
        actionSave_Flattened_As->setIconText(QCoreApplication::translate("MainWindow", "Save Flattened As...", nullptr));
#if QT_CONFIG(tooltip)
        actionSave_Flattened_As->setToolTip(QCoreApplication::translate("MainWindow", "Save a flattened version of the current stage", nullptr));
#endif // QT_CONFIG(tooltip)
        actionSave_Viewer_Image->setText(QCoreApplication::translate("MainWindow", "Save Viewer Image...", nullptr));
        actionSave_Viewer_Image->setIconText(QCoreApplication::translate("MainWindow", "Save Viewer Image...", nullptr));
#if QT_CONFIG(tooltip)
        actionSave_Viewer_Image->setToolTip(QCoreApplication::translate("MainWindow", "Saves the viewer render of the current frame", nullptr));
#endif // QT_CONFIG(tooltip)
        actionCopy_Viewer_Image->setText(QCoreApplication::translate("MainWindow", "Copy Viewer Image", nullptr));
        actionCopy_Viewer_Image->setIconText(QCoreApplication::translate("MainWindow", "Copy Viewer Image", nullptr));
#if QT_CONFIG(tooltip)
        actionCopy_Viewer_Image->setToolTip(QCoreApplication::translate("MainWindow", "Copies the viewer render of the current frame to the clipboard", nullptr));
#endif // QT_CONFIG(tooltip)
        showInterpreter->setText(QCoreApplication::translate("MainWindow", "Interpreter", nullptr));
#if QT_CONFIG(tooltip)
        showInterpreter->setToolTip(QCoreApplication::translate("MainWindow", "Show Python interpreter console", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        showInterpreter->setShortcut(QCoreApplication::translate("MainWindow", "I", nullptr));
#endif // QT_CONFIG(shortcut)
        showDebugFlags->setText(QCoreApplication::translate("MainWindow", "Debug Flags", nullptr));
#if QT_CONFIG(tooltip)
        showDebugFlags->setToolTip(QCoreApplication::translate("MainWindow", "Show Debug Flags Window", nullptr));
#endif // QT_CONFIG(tooltip)
        actionHUD_VBOInfo->setText(QCoreApplication::translate("MainWindow", "VBO Info (Quads/Tris)", nullptr));
        actionHUD_Info->setText(QCoreApplication::translate("MainWindow", "Subtree Info (Slow)", nullptr));
        actionHUD_VBO->setText(QCoreApplication::translate("MainWindow", "VBO Info", nullptr));
        actionHUD_Complexity->setText(QCoreApplication::translate("MainWindow", "Camera/Complexity", nullptr));
        actionHUD_Performance->setText(QCoreApplication::translate("MainWindow", "Performance", nullptr));
        actionHUD_GPUstats->setText(QCoreApplication::translate("MainWindow", "GPU stats", nullptr));
        actionHUD->setText(QCoreApplication::translate("MainWindow", "Show HUD", nullptr));
#if QT_CONFIG(shortcut)
        actionHUD->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+D", nullptr));
#endif // QT_CONFIG(shortcut)
        actionCameraMask_Outline->setText(QCoreApplication::translate("MainWindow", "Camera Frame", nullptr));
        actionDisplay_Guide->setText(QCoreApplication::translate("MainWindow", "Guide", nullptr));
        actionDisplay_Render->setText(QCoreApplication::translate("MainWindow", "Render", nullptr));
        actionDisplay_PrimId->setText(QCoreApplication::translate("MainWindow", "Display Prim Id", nullptr));
        actionEnable_Scene_Materials->setText(QCoreApplication::translate("MainWindow", "Enable Scene Materials", nullptr));
        actionEnable_Scene_Lights->setText(QCoreApplication::translate("MainWindow", "Enable Scene Lights", nullptr));
        actionShow_Inactive_Prims->setText(QCoreApplication::translate("MainWindow", "Inactive Prims", nullptr));
        showAABBox->setText(QCoreApplication::translate("MainWindow", "Show Axis-Aligned", nullptr));
        showOBBox->setText(QCoreApplication::translate("MainWindow", "Show Oriented", nullptr));
        showBBoxPlayback->setText(QCoreApplication::translate("MainWindow", "Show During Playback/Scrub", nullptr));
        showBBoxes->setText(QCoreApplication::translate("MainWindow", "Show Bounding Boxes", nullptr));
#if QT_CONFIG(shortcut)
        showBBoxes->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+B", nullptr));
#endif // QT_CONFIG(shortcut)
        actionVersion_Info->setText(QCoreApplication::translate("MainWindow", "Version Info", nullptr));
#if QT_CONFIG(shortcut)
        actionVersion_Info->setShortcut(QCoreApplication::translate("MainWindow", "V", nullptr));
#endif // QT_CONFIG(shortcut)
        actionAdjust_Free_Camera->setText(QCoreApplication::translate("MainWindow", "Free Camera Settings...", nullptr));
        actionIncrementComplexity2->setText(QCoreApplication::translate("MainWindow", "IncrementComplexity", nullptr));
#if QT_CONFIG(shortcut)
        actionIncrementComplexity2->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl++", nullptr));
#endif // QT_CONFIG(shortcut)
        actionCull_Backfaces->setText(QCoreApplication::translate("MainWindow", "Cull Backfaces (GL)", nullptr));
        actionSave_Overrides_To_Scene->setText(QCoreApplication::translate("MainWindow", "Save Overrides To Scene", nullptr));
        actionMake_Visible->setText(QCoreApplication::translate("MainWindow", "Make Visible", nullptr));
#if QT_CONFIG(shortcut)
        actionMake_Visible->setShortcut(QCoreApplication::translate("MainWindow", "Shift+H", nullptr));
#endif // QT_CONFIG(shortcut)
        actionMake_Invisible->setText(QCoreApplication::translate("MainWindow", "Make Invisible", nullptr));
#if QT_CONFIG(shortcut)
        actionMake_Invisible->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+H", nullptr));
#endif // QT_CONFIG(shortcut)
        actionRemove_Session_Visibility->setText(QCoreApplication::translate("MainWindow", "Remove Session Visibility", nullptr));
#if QT_CONFIG(shortcut)
        actionRemove_Session_Visibility->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+U", nullptr));
#endif // QT_CONFIG(shortcut)
        actionActivate->setText(QCoreApplication::translate("MainWindow", "Activate", nullptr));
        actionDeactivate->setText(QCoreApplication::translate("MainWindow", "Deactivate", nullptr));
        actionSelect_Model_Root->setText(QCoreApplication::translate("MainWindow", "Select Enclosing Model", nullptr));
#if QT_CONFIG(shortcut)
        actionSelect_Model_Root->setShortcut(QCoreApplication::translate("MainWindow", "\\", nullptr));
#endif // QT_CONFIG(shortcut)
        actionRefresh_Procedurals->setText(QCoreApplication::translate("MainWindow", "Refresh Procedurals", nullptr));
        actionReload_All_Layers->setText(QCoreApplication::translate("MainWindow", "Reload All Layers", nullptr));
#if QT_CONFIG(shortcut)
        actionReload_All_Layers->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+R", nullptr));
#endif // QT_CONFIG(shortcut)
        actionHD_Flags->setText(QCoreApplication::translate("MainWindow", "HD Flags", nullptr));
        actionHD_Flags_2->setText(QCoreApplication::translate("MainWindow", "HD Flags", nullptr));
        actionHD_Flags_3->setText(QCoreApplication::translate("MainWindow", "HD Flags", nullptr));
        actionMenu->setText(QCoreApplication::translate("MainWindow", "Menu", nullptr));
        actionSdf->setText(QCoreApplication::translate("MainWindow", "sdf", nullptr));
        actionGeom_Id->setText(QCoreApplication::translate("MainWindow", "Geom Id", nullptr));
        actionShow_All_Prototype_Prims->setText(QCoreApplication::translate("MainWindow", "Prototype Prims", nullptr));
        actionShow_Undefined_Prims->setText(QCoreApplication::translate("MainWindow", "Undefined Prims (Overs)", nullptr));
        actionShow_Abstract_Prims->setText(QCoreApplication::translate("MainWindow", "Abstract Prims (Classes)", nullptr));
        actionShow_Prim_DisplayName->setText(QCoreApplication::translate("MainWindow", "Use Display Name (Prims)", nullptr));
        actionPick_Prims->setText(QCoreApplication::translate("MainWindow", "Select Prims", nullptr));
        actionPick_Models->setText(QCoreApplication::translate("MainWindow", "Select Models", nullptr));
        actionPick_Instances->setText(QCoreApplication::translate("MainWindow", "Select Instances", nullptr));
        actionPick_Prototypes->setText(QCoreApplication::translate("MainWindow", "Select Prototypes", nullptr));
        actionToggle_Viewer_Mode->setText(QCoreApplication::translate("MainWindow", "Toggle Viewer-Only Mode", nullptr));
#if QT_CONFIG(shortcut)
        actionToggle_Viewer_Mode->setShortcut(QCoreApplication::translate("MainWindow", "F11", nullptr));
#endif // QT_CONFIG(shortcut)
        useExtentsHint->setText(QCoreApplication::translate("MainWindow", "Use Extents Hints", nullptr));
        actionNever->setText(QCoreApplication::translate("MainWindow", "Never", nullptr));
        actionOnly_when_paused->setText(QCoreApplication::translate("MainWindow", "Only when paused", nullptr));
#if QT_CONFIG(tooltip)
        actionOnly_when_paused->setToolTip(QCoreApplication::translate("MainWindow", "Do not draw selection highlights during playback", nullptr));
#endif // QT_CONFIG(tooltip)
        actionAlways->setText(QCoreApplication::translate("MainWindow", "Always", nullptr));
#if QT_CONFIG(tooltip)
        actionAlways->setToolTip(QCoreApplication::translate("MainWindow", "Draw selection highlights even during plaback", nullptr));
#endif // QT_CONFIG(tooltip)
        actionSelYellow->setText(QCoreApplication::translate("MainWindow", "Yellow", nullptr));
        actionSelWhite->setText(QCoreApplication::translate("MainWindow", "White", nullptr));
        actionSelCyan->setText(QCoreApplication::translate("MainWindow", "Cyan", nullptr));
        actionVis_Only->setText(QCoreApplication::translate("MainWindow", "Vis Only", nullptr));
#if QT_CONFIG(shortcut)
        actionVis_Only->setShortcut(QCoreApplication::translate("MainWindow", "Alt+H", nullptr));
#endif // QT_CONFIG(shortcut)
        actionReset_All_Session_Visibility->setText(QCoreApplication::translate("MainWindow", "Reset All Session Visibility", nullptr));
#if QT_CONFIG(shortcut)
        actionReset_All_Session_Visibility->setShortcut(QCoreApplication::translate("MainWindow", "Shift+U", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLoad->setText(QCoreApplication::translate("MainWindow", "Load", nullptr));
        actionUnload->setText(QCoreApplication::translate("MainWindow", "Unload", nullptr));
        actionSelect_Bound_Preview_Material->setText(QCoreApplication::translate("MainWindow", "Select Bound Preview Material", nullptr));
#if QT_CONFIG(shortcut)
        actionSelect_Bound_Preview_Material->setShortcut(QCoreApplication::translate("MainWindow", "Shift+L", nullptr));
#endif // QT_CONFIG(shortcut)
        actionRollover_Prim_Info->setText(QCoreApplication::translate("MainWindow", "Show Rollover Prim Info", nullptr));
#if QT_CONFIG(shortcut)
        actionRollover_Prim_Info->setShortcut(QCoreApplication::translate("MainWindow", "Shift+I", nullptr));
#endif // QT_CONFIG(shortcut)
        actionAuto_Compute_Clipping_Planes->setText(QCoreApplication::translate("MainWindow", "Auto Compute Clipping Planes", nullptr));
#if QT_CONFIG(tooltip)
        actionAuto_Compute_Clipping_Planes->setToolTip(QCoreApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Auto Clipping</span></p><p><span style=\" font-weight:400;\">Expansive scenes may show &quot;Z-fighting&quot;, where nearby surfaces pop or shimmer.  </span><span style=\" font-weight:600;\">Auto Compute Clipping Planes</span><span style=\" font-weight:400;\"> adjusts the camera's clipping planes to fix this.  When enabled, the </span><span style=\" font-weight:600;\">Frame Selected</span><span style=\" font-weight:400;\"> command readjusts clip planes too.</span></p><p><span style=\" font-weight:400;\">Leaving and then re-entering this mode will reset the view used to optimize the clipping planes.</span></p><p><span style=\" font-weight:400;\">Auto clipping is not useful in all situations, such as animated scenes in which the &quot;extent&quot; of the scene changes over time, and for close-up work.</span></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionAuto_Compute_Clipping_Planes->setShortcut(QCoreApplication::translate("MainWindow", "C", nullptr));
#endif // QT_CONFIG(shortcut)
        actionFind_Prims->setText(QCoreApplication::translate("MainWindow", "Find Prims", nullptr));
#if QT_CONFIG(shortcut)
        actionFind_Prims->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+F", nullptr));
#endif // QT_CONFIG(shortcut)
        actionSelect_Stage_Root->setText(QCoreApplication::translate("MainWindow", "Select Stage Root", nullptr));
#if QT_CONFIG(shortcut)
        actionSelect_Stage_Root->setShortcut(QCoreApplication::translate("MainWindow", "|", nullptr));
#endif // QT_CONFIG(shortcut)
        actionDisplay_Camera_Oracles->setText(QCoreApplication::translate("MainWindow", "Camera Oracles", nullptr));
        actionDisplay_Proxy->setText(QCoreApplication::translate("MainWindow", "Proxy", nullptr));
        actionAdjust_Default_Material->setText(QCoreApplication::translate("MainWindow", "Default Material Settings...", nullptr));
        actionCameraReticles_Inside->setText(QCoreApplication::translate("MainWindow", "Camera Reticles Inside", nullptr));
        actionCameraReticles_Outside->setText(QCoreApplication::translate("MainWindow", "Camera Reticles Outside", nullptr));
        actionCameraReticles_Color->setText(QCoreApplication::translate("MainWindow", "Select Color...", nullptr));
        actionLow->setText(QCoreApplication::translate("MainWindow", "Low", nullptr));
        actionMedium->setText(QCoreApplication::translate("MainWindow", "Medium", nullptr));
        actionHigh->setText(QCoreApplication::translate("MainWindow", "High", nullptr));
        actionVery_High->setText(QCoreApplication::translate("MainWindow", "Very High", nullptr));
        actionSelect_Bound_Full_Material->setText(QCoreApplication::translate("MainWindow", "Select Bound Full Material", nullptr));
        actionSelect_Preview_Binding_Relationship->setText(QCoreApplication::translate("MainWindow", "Select Preview Binding Relationship", nullptr));
        actionSelect_Full_Binding_Relationship->setText(QCoreApplication::translate("MainWindow", "Select Full Binding Relationship", nullptr));
        actionPreferences->setText(QCoreApplication::translate("MainWindow", "Preferences", nullptr));
        actionSave_State_To->setText(QCoreApplication::translate("MainWindow", "Save State To ", nullptr));
        actiond->setText(QCoreApplication::translate("MainWindow", "d ", nullptr));
        actiond_2->setText(QCoreApplication::translate("MainWindow", "d", nullptr));
        actionSave_State_As_New_Config->setText(QCoreApplication::translate("MainWindow", "Save State As New Config...", nullptr));
        actionFrame_Selected->setText(QCoreApplication::translate("MainWindow", "Frame Selected", nullptr));
#if QT_CONFIG(shortcut)
        actionFrame_Selected->setShortcut(QCoreApplication::translate("MainWindow", "F", nullptr));
#endif // QT_CONFIG(shortcut)
        showHydraSceneBrowser->setText(QCoreApplication::translate("MainWindow", "Hydra Scene Browser", nullptr));
        actionCameraMask_Full->setText(QCoreApplication::translate("MainWindow", "Full Mask", nullptr));
        actionCameraMask_Partial->setText(QCoreApplication::translate("MainWindow", "Partial Mask", nullptr));
        actionCameraMask_None->setText(QCoreApplication::translate("MainWindow", "No Mask", nullptr));
        actionCameraMask_Color->setText(QCoreApplication::translate("MainWindow", "Select Color...", nullptr));
#if QT_CONFIG(statustip)
        centralwidget->setStatusTip(QString());
#endif // QT_CONFIG(statustip)
        menuNavigation->setTitle(QCoreApplication::translate("MainWindow", "&Navigation", nullptr));
        menuShow->setTitle(QCoreApplication::translate("MainWindow", "&Show", nullptr));
        menuPrim_View_Depth->setTitle(QCoreApplication::translate("MainWindow", "Prim View Depth", nullptr));
        QTreeWidgetItem *___qtreewidgetitem = primView->headerItem();
        ___qtreewidgetitem->setText(4, QCoreApplication::translate("MainWindow", "Draw Mode", nullptr));
        ___qtreewidgetitem->setText(3, QCoreApplication::translate("MainWindow", "Guides", nullptr));
        ___qtreewidgetitem->setText(2, QCoreApplication::translate("MainWindow", "Vis", nullptr));
        ___qtreewidgetitem->setText(1, QCoreApplication::translate("MainWindow", "Type", nullptr));
        ___qtreewidgetitem->setText(0, QCoreApplication::translate("MainWindow", "Prim Name", nullptr));
#if QT_CONFIG(tooltip)
        primLegendQButton->setToolTip(QCoreApplication::translate("MainWindow", "Prim legend", nullptr));
#endif // QT_CONFIG(tooltip)
        primLegendQButton->setText(QCoreApplication::translate("MainWindow", "?", nullptr));
        primViewLineEdit->setPlaceholderText(QCoreApplication::translate("MainWindow", "Search for prim by name", nullptr));
#if QT_CONFIG(tooltip)
        primViewFindNext->setToolTip(QCoreApplication::translate("MainWindow", "Find and select the next match (looping)", nullptr));
#endif // QT_CONFIG(tooltip)
        primViewFindNext->setText(QCoreApplication::translate("MainWindow", "Find Prim", nullptr));
        menuRender->setTitle(QCoreApplication::translate("MainWindow", "Renderer", nullptr));
        menuRendererSettings->setTitle(QCoreApplication::translate("MainWindow", "Hydra Settings", nullptr));
        menuRendererAovs->setTitle(QCoreApplication::translate("MainWindow", "Hydra AOVs", nullptr));
        menuRendererCommands->setTitle(QCoreApplication::translate("MainWindow", "Hydra Commands", nullptr));
        menuViewer->setTitle(QCoreApplication::translate("MainWindow", "Display", nullptr));
        menuShading_Mode->setTitle(QCoreApplication::translate("MainWindow", "Shading Mode", nullptr));
        menuColorCorrection->setTitle(QCoreApplication::translate("MainWindow", "Color Management", nullptr));
        menuComplexity->setTitle(QCoreApplication::translate("MainWindow", "Complexity", nullptr));
        menuBBox->setTitle(QCoreApplication::translate("MainWindow", "Bounding Box", nullptr));
        menuDisplay->setTitle(QCoreApplication::translate("MainWindow", "Display Purposes", nullptr));
        menuHUD->setTitle(QCoreApplication::translate("MainWindow", "Heads-Up Display", nullptr));
        menuSelection_Highlighting->setTitle(QCoreApplication::translate("MainWindow", "Selection Highlighting", nullptr));
        menuHighlightColor->setTitle(QCoreApplication::translate("MainWindow", "Highlight Color", nullptr));
        menuBackground_Color->setTitle(QCoreApplication::translate("MainWindow", "Background Color", nullptr));
        menuCamera->setTitle(QCoreApplication::translate("MainWindow", "Camera", nullptr));
        menuCameraSelect->setTitle(QCoreApplication::translate("MainWindow", "Select Camera", nullptr));
        menuCameraGuides->setTitle(QCoreApplication::translate("MainWindow", "Camera Guides", nullptr));
        menuCamera_Masking->setTitle(QCoreApplication::translate("MainWindow", "Camera Masking", nullptr));
        menuCamera_Reticles->setTitle(QCoreApplication::translate("MainWindow", "Camera Reticles", nullptr));
        menuPick->setTitle(QCoreApplication::translate("MainWindow", "Select", nullptr));
        menuLights->setTitle(QCoreApplication::translate("MainWindow", "Lights", nullptr));
        QTreeWidgetItem *___qtreewidgetitem1 = propertyView->headerItem();
        ___qtreewidgetitem1->setText(2, QCoreApplication::translate("MainWindow", "Value", nullptr));
        ___qtreewidgetitem1->setText(1, QCoreApplication::translate("MainWindow", "Property Name", nullptr));
        ___qtreewidgetitem1->setText(0, QCoreApplication::translate("MainWindow", "Type", nullptr));
#if QT_CONFIG(tooltip)
        propertyView->setToolTip(QString());
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        propertyLegendQButton->setToolTip(QCoreApplication::translate("MainWindow", "Property legend", nullptr));
#endif // QT_CONFIG(tooltip)
        propertyLegendQButton->setText(QCoreApplication::translate("MainWindow", "?", nullptr));
        attrViewLineEdit->setPlaceholderText(QCoreApplication::translate("MainWindow", "Search for property by name", nullptr));
        attrViewFindNext->setText(QCoreApplication::translate("MainWindow", "Find Prop", nullptr));
        propertyInspector->setTabText(propertyInspector->indexOf(value), QCoreApplication::translate("MainWindow", "Value", nullptr));
        QTableWidgetItem *___qtablewidgetitem = metadataView->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QCoreApplication::translate("MainWindow", "Field Name", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = metadataView->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QCoreApplication::translate("MainWindow", "Value", nullptr));
#if QT_CONFIG(tooltip)
        metadataView->setToolTip(QString());
#endif // QT_CONFIG(tooltip)
        propertyInspector->setTabText(propertyInspector->indexOf(metadata), QCoreApplication::translate("MainWindow", "Meta Data", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = layerStackView->horizontalHeaderItem(0);
        ___qtablewidgetitem2->setText(QCoreApplication::translate("MainWindow", "Layer", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = layerStackView->horizontalHeaderItem(1);
        ___qtablewidgetitem3->setText(QCoreApplication::translate("MainWindow", "Offset , Scale", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = layerStackView->horizontalHeaderItem(2);
        ___qtablewidgetitem4->setText(QCoreApplication::translate("MainWindow", "Path", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = layerStackView->horizontalHeaderItem(3);
        ___qtablewidgetitem5->setText(QCoreApplication::translate("MainWindow", "Value", nullptr));
#if QT_CONFIG(tooltip)
        layerStackView->setToolTip(QString());
#endif // QT_CONFIG(tooltip)
        propertyInspector->setTabText(propertyInspector->indexOf(layerstack), QCoreApplication::translate("MainWindow", "Layer Stack", nullptr));
        QTreeWidgetItem *___qtreewidgetitem2 = compositionTreeWidget->headerItem();
        ___qtreewidgetitem2->setText(3, QCoreApplication::translate("MainWindow", "Has Spec", nullptr));
        ___qtreewidgetitem2->setText(2, QCoreApplication::translate("MainWindow", "Arc Path", nullptr));
        ___qtreewidgetitem2->setText(1, QCoreApplication::translate("MainWindow", "Arc Type", nullptr));
        ___qtreewidgetitem2->setText(0, QCoreApplication::translate("MainWindow", "Layer", nullptr));
        propertyInspector->setTabText(propertyInspector->indexOf(tab), QCoreApplication::translate("MainWindow", "Composition", nullptr));
#if QT_CONFIG(tooltip)
        stageBegin->setToolTip(QCoreApplication::translate("MainWindow", "Stage Start Frame", nullptr));
#endif // QT_CONFIG(tooltip)
        stageBegin->setText(QCoreApplication::translate("MainWindow", "XXX", nullptr));
#if QT_CONFIG(tooltip)
        rangeBegin->setToolTip(QCoreApplication::translate("MainWindow", "Playback Start Frame", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        rangeEnd->setToolTip(QCoreApplication::translate("MainWindow", "Playback End Frame", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        stageEnd->setToolTip(QCoreApplication::translate("MainWindow", "Stage End Frame", nullptr));
#endif // QT_CONFIG(tooltip)
        stageEnd->setText(QCoreApplication::translate("MainWindow", "XXX", nullptr));
#if QT_CONFIG(tooltip)
        redrawOnScrub->setToolTip(QCoreApplication::translate("MainWindow", "If unchecked, the view will only redraw when scrubbing is done", nullptr));
#endif // QT_CONFIG(tooltip)
        redrawOnScrub->setText(QCoreApplication::translate("MainWindow", "Redraw On Frame Scrub", nullptr));
        stepSizeLabel->setText(QCoreApplication::translate("MainWindow", "Step Size", nullptr));
#if QT_CONFIG(tooltip)
        stepSize->setToolTip(QCoreApplication::translate("MainWindow", "Playback Step-size", nullptr));
#endif // QT_CONFIG(tooltip)
        stepSize->setText(QCoreApplication::translate("MainWindow", "1.0", nullptr));
        playButton->setText(QCoreApplication::translate("MainWindow", "Play", nullptr));
        frameLabel->setText(QCoreApplication::translate("MainWindow", "Frame:", nullptr));
#if QT_CONFIG(tooltip)
        frameField->setToolTip(QCoreApplication::translate("MainWindow", "Current Frame", nullptr));
#endif // QT_CONFIG(tooltip)
        frameField->setText(QCoreApplication::translate("MainWindow", "1.0", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "&File", nullptr));
        menuSave_State_As->setTitle(QCoreApplication::translate("MainWindow", "Save State As", nullptr));
        menuLoad_New_State->setTitle(QCoreApplication::translate("MainWindow", "Reopen With State", nullptr));
        menuEdit->setTitle(QCoreApplication::translate("MainWindow", "&Edit", nullptr));
        menuInterpolation->setTitle(QCoreApplication::translate("MainWindow", "Stage Interpolation", nullptr));
        menuWindow->setTitle(QCoreApplication::translate("MainWindow", "Window", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINWINDOWUI_H
