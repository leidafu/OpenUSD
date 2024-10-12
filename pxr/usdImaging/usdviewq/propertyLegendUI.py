/********************************************************************************
** Form generated from reading UI file 'propertyLegendUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PROPERTYLEGENDUI_H
#define PROPERTYLEGENDUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PropertyLegend
{
public:
    QGridLayout *gridLayout;
    QGridLayout *gridLayout_2;
    QHBoxLayout *horizontalLayout;
    QGraphicsView *propertyLegendColorNoValue;
    QLabel *propertyLegendLabelNoValue;
    QSpacerItem *horizontalSpacer_8;
    QHBoxLayout *horizontalLayout_2;
    QGraphicsView *propertyLegendColorDefault;
    QLabel *propertyLegendLabelDefault;
    QSpacerItem *horizontalSpacer_10;
    QHBoxLayout *horizontalLayout_5;
    QGraphicsView *propertyLegendColorTimeSample;
    QLabel *propertyLegendLabelTimeSample;
    QSpacerItem *horizontalSpacer_12;
    QHBoxLayout *horizontalLayout_3;
    QGraphicsView *propertyLegendColorFallback;
    QLabel *propertyLegendLabelFallback;
    QSpacerItem *horizontalSpacer_9;
    QHBoxLayout *horizontalLayout_4;
    QGraphicsView *propertyLegendColorCustom;
    QLabel *propertyLegendLabelCustom;
    QSpacerItem *horizontalSpacer_11;
    QHBoxLayout *horizontalLayout_6;
    QGraphicsView *propertyLegendColorValueClips;
    QLabel *propertyLegendLabelValueClips;
    QSpacerItem *horizontalSpacer_13;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_9;
    QLabel *propertyLegendAttrPlainIcon;
    QLabel *propertyLegendAttrPlainDesc;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout_10;
    QLabel *propertyLegendRelPlainIcon;
    QLabel *propertyLegendRelPlainDesc;
    QSpacerItem *horizontalSpacer_2;
    QHBoxLayout *horizontalLayout_11;
    QLabel *propertyLegendCompIcon;
    QLabel *propertyLegendCompDesc;
    QSpacerItem *horizontalSpacer_3;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_12;
    QLabel *propertyLegendConnIcon;
    QLabel *propertyLegendConnDesc;
    QSpacerItem *horizontalSpacer_4;
    QHBoxLayout *horizontalLayout_13;
    QLabel *propertyLegendTargetIcon;
    QLabel *propertyLegendTargetDesc;
    QSpacerItem *horizontalSpacer_5;
    QHBoxLayout *horizontalLayout_14;
    QLabel *inheritedPropertyIcon;
    QLabel *inheritedPropertyText;
    QSpacerItem *horizontalSpacer_14;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_8;
    QLabel *propertyLegendAttrWithConnIcon;
    QLabel *propertyLegendAttrWithConnDesc;
    QSpacerItem *horizontalSpacer_6;
    QHBoxLayout *horizontalLayout_7;
    QLabel *propertyLegendRelWithTargetIcon;
    QLabel *propertyLegendRelWithTargetDesc;
    QSpacerItem *horizontalSpacer_7;
    QSpacerItem *horizontalSpacer_15;

    void setupUi(QWidget *PropertyLegend)
    {
        if (PropertyLegend->objectName().isEmpty())
            PropertyLegend->setObjectName("PropertyLegend");
        PropertyLegend->setWindowModality(Qt::NonModal);
        PropertyLegend->resize(654, 151);
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(PropertyLegend->sizePolicy().hasHeightForWidth());
        PropertyLegend->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(PropertyLegend);
        gridLayout->setObjectName("gridLayout");
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(3);
        gridLayout_2->setObjectName("gridLayout_2");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        propertyLegendColorNoValue = new QGraphicsView(PropertyLegend);
        propertyLegendColorNoValue->setObjectName("propertyLegendColorNoValue");
        propertyLegendColorNoValue->setMaximumSize(QSize(20, 15));

        horizontalLayout->addWidget(propertyLegendColorNoValue);

        propertyLegendLabelNoValue = new QLabel(PropertyLegend);
        propertyLegendLabelNoValue->setObjectName("propertyLegendLabelNoValue");
        QFont font;
        font.setBold(false);
        font.setItalic(false);
        propertyLegendLabelNoValue->setFont(font);

        horizontalLayout->addWidget(propertyLegendLabelNoValue);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_8);


        gridLayout_2->addLayout(horizontalLayout, 0, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        propertyLegendColorDefault = new QGraphicsView(PropertyLegend);
        propertyLegendColorDefault->setObjectName("propertyLegendColorDefault");
        propertyLegendColorDefault->setMaximumSize(QSize(20, 15));

        horizontalLayout_2->addWidget(propertyLegendColorDefault);

        propertyLegendLabelDefault = new QLabel(PropertyLegend);
        propertyLegendLabelDefault->setObjectName("propertyLegendLabelDefault");
        propertyLegendLabelDefault->setFont(font);

        horizontalLayout_2->addWidget(propertyLegendLabelDefault);

        horizontalSpacer_10 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_10);


        gridLayout_2->addLayout(horizontalLayout_2, 0, 1, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName("horizontalLayout_5");
        propertyLegendColorTimeSample = new QGraphicsView(PropertyLegend);
        propertyLegendColorTimeSample->setObjectName("propertyLegendColorTimeSample");
        propertyLegendColorTimeSample->setMaximumSize(QSize(20, 15));

        horizontalLayout_5->addWidget(propertyLegendColorTimeSample);

        propertyLegendLabelTimeSample = new QLabel(PropertyLegend);
        propertyLegendLabelTimeSample->setObjectName("propertyLegendLabelTimeSample");
        propertyLegendLabelTimeSample->setFont(font);

        horizontalLayout_5->addWidget(propertyLegendLabelTimeSample);

        horizontalSpacer_12 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_12);


        gridLayout_2->addLayout(horizontalLayout_5, 0, 2, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        propertyLegendColorFallback = new QGraphicsView(PropertyLegend);
        propertyLegendColorFallback->setObjectName("propertyLegendColorFallback");
        propertyLegendColorFallback->setMaximumSize(QSize(20, 15));

        horizontalLayout_3->addWidget(propertyLegendColorFallback);

        propertyLegendLabelFallback = new QLabel(PropertyLegend);
        propertyLegendLabelFallback->setObjectName("propertyLegendLabelFallback");
        propertyLegendLabelFallback->setFont(font);

        horizontalLayout_3->addWidget(propertyLegendLabelFallback);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_9);


        gridLayout_2->addLayout(horizontalLayout_3, 1, 0, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        propertyLegendColorCustom = new QGraphicsView(PropertyLegend);
        propertyLegendColorCustom->setObjectName("propertyLegendColorCustom");
        propertyLegendColorCustom->setMaximumSize(QSize(20, 15));

        horizontalLayout_4->addWidget(propertyLegendColorCustom);

        propertyLegendLabelCustom = new QLabel(PropertyLegend);
        propertyLegendLabelCustom->setObjectName("propertyLegendLabelCustom");

        horizontalLayout_4->addWidget(propertyLegendLabelCustom);

        horizontalSpacer_11 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_11);


        gridLayout_2->addLayout(horizontalLayout_4, 1, 1, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName("horizontalLayout_6");
        propertyLegendColorValueClips = new QGraphicsView(PropertyLegend);
        propertyLegendColorValueClips->setObjectName("propertyLegendColorValueClips");
        propertyLegendColorValueClips->setMaximumSize(QSize(20, 15));

        horizontalLayout_6->addWidget(propertyLegendColorValueClips);

        propertyLegendLabelValueClips = new QLabel(PropertyLegend);
        propertyLegendLabelValueClips->setObjectName("propertyLegendLabelValueClips");
        propertyLegendLabelValueClips->setFont(font);

        horizontalLayout_6->addWidget(propertyLegendLabelValueClips);

        horizontalSpacer_13 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_13);


        gridLayout_2->addLayout(horizontalLayout_6, 1, 2, 1, 1);


        gridLayout->addLayout(gridLayout_2, 0, 0, 1, 3);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(3);
        verticalLayout->setObjectName("verticalLayout");
        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setSpacing(3);
        horizontalLayout_9->setObjectName("horizontalLayout_9");
        propertyLegendAttrPlainIcon = new QLabel(PropertyLegend);
        propertyLegendAttrPlainIcon->setObjectName("propertyLegendAttrPlainIcon");

        horizontalLayout_9->addWidget(propertyLegendAttrPlainIcon);

        propertyLegendAttrPlainDesc = new QLabel(PropertyLegend);
        propertyLegendAttrPlainDesc->setObjectName("propertyLegendAttrPlainDesc");
        propertyLegendAttrPlainDesc->setFont(font);

        horizontalLayout_9->addWidget(propertyLegendAttrPlainDesc);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer);


        verticalLayout->addLayout(horizontalLayout_9);

        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setSpacing(3);
        horizontalLayout_10->setObjectName("horizontalLayout_10");
        propertyLegendRelPlainIcon = new QLabel(PropertyLegend);
        propertyLegendRelPlainIcon->setObjectName("propertyLegendRelPlainIcon");

        horizontalLayout_10->addWidget(propertyLegendRelPlainIcon);

        propertyLegendRelPlainDesc = new QLabel(PropertyLegend);
        propertyLegendRelPlainDesc->setObjectName("propertyLegendRelPlainDesc");
        propertyLegendRelPlainDesc->setFont(font);

        horizontalLayout_10->addWidget(propertyLegendRelPlainDesc);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_10->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout_10);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setSpacing(3);
        horizontalLayout_11->setObjectName("horizontalLayout_11");
        propertyLegendCompIcon = new QLabel(PropertyLegend);
        propertyLegendCompIcon->setObjectName("propertyLegendCompIcon");

        horizontalLayout_11->addWidget(propertyLegendCompIcon);

        propertyLegendCompDesc = new QLabel(PropertyLegend);
        propertyLegendCompDesc->setObjectName("propertyLegendCompDesc");
        propertyLegendCompDesc->setFont(font);

        horizontalLayout_11->addWidget(propertyLegendCompDesc);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_3);


        verticalLayout->addLayout(horizontalLayout_11);


        gridLayout->addLayout(verticalLayout, 1, 0, 1, 1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setSpacing(3);
        horizontalLayout_12->setObjectName("horizontalLayout_12");
        propertyLegendConnIcon = new QLabel(PropertyLegend);
        propertyLegendConnIcon->setObjectName("propertyLegendConnIcon");

        horizontalLayout_12->addWidget(propertyLegendConnIcon);

        propertyLegendConnDesc = new QLabel(PropertyLegend);
        propertyLegendConnDesc->setObjectName("propertyLegendConnDesc");
        propertyLegendConnDesc->setFont(font);

        horizontalLayout_12->addWidget(propertyLegendConnDesc);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_12->addItem(horizontalSpacer_4);


        verticalLayout_2->addLayout(horizontalLayout_12);

        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setSpacing(3);
        horizontalLayout_13->setObjectName("horizontalLayout_13");
        propertyLegendTargetIcon = new QLabel(PropertyLegend);
        propertyLegendTargetIcon->setObjectName("propertyLegendTargetIcon");

        horizontalLayout_13->addWidget(propertyLegendTargetIcon);

        propertyLegendTargetDesc = new QLabel(PropertyLegend);
        propertyLegendTargetDesc->setObjectName("propertyLegendTargetDesc");
        propertyLegendTargetDesc->setMinimumSize(QSize(20, 20));
        propertyLegendTargetDesc->setFont(font);

        horizontalLayout_13->addWidget(propertyLegendTargetDesc);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_13->addItem(horizontalSpacer_5);


        verticalLayout_2->addLayout(horizontalLayout_13);

        horizontalLayout_14 = new QHBoxLayout();
        horizontalLayout_14->setObjectName("horizontalLayout_14");
        inheritedPropertyIcon = new QLabel(PropertyLegend);
        inheritedPropertyIcon->setObjectName("inheritedPropertyIcon");
        inheritedPropertyIcon->setTextFormat(Qt::RichText);

        horizontalLayout_14->addWidget(inheritedPropertyIcon);

        inheritedPropertyText = new QLabel(PropertyLegend);
        inheritedPropertyText->setObjectName("inheritedPropertyText");
        QFont font1;
        font1.setItalic(false);
        inheritedPropertyText->setFont(font1);
        inheritedPropertyText->setFrameShape(QFrame::NoFrame);
        inheritedPropertyText->setTextFormat(Qt::RichText);
        inheritedPropertyText->setAlignment(Qt::AlignCenter);
        inheritedPropertyText->setWordWrap(false);

        horizontalLayout_14->addWidget(inheritedPropertyText);

        horizontalSpacer_14 = new QSpacerItem(13, 13, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_14->addItem(horizontalSpacer_14);


        verticalLayout_2->addLayout(horizontalLayout_14);


        gridLayout->addLayout(verticalLayout_2, 1, 1, 1, 1);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setSpacing(3);
        horizontalLayout_8->setObjectName("horizontalLayout_8");
        propertyLegendAttrWithConnIcon = new QLabel(PropertyLegend);
        propertyLegendAttrWithConnIcon->setObjectName("propertyLegendAttrWithConnIcon");

        horizontalLayout_8->addWidget(propertyLegendAttrWithConnIcon);

        propertyLegendAttrWithConnDesc = new QLabel(PropertyLegend);
        propertyLegendAttrWithConnDesc->setObjectName("propertyLegendAttrWithConnDesc");
        propertyLegendAttrWithConnDesc->setFont(font);

        horizontalLayout_8->addWidget(propertyLegendAttrWithConnDesc);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_6);


        verticalLayout_3->addLayout(horizontalLayout_8);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(3);
        horizontalLayout_7->setObjectName("horizontalLayout_7");
        propertyLegendRelWithTargetIcon = new QLabel(PropertyLegend);
        propertyLegendRelWithTargetIcon->setObjectName("propertyLegendRelWithTargetIcon");

        horizontalLayout_7->addWidget(propertyLegendRelWithTargetIcon);

        propertyLegendRelWithTargetDesc = new QLabel(PropertyLegend);
        propertyLegendRelWithTargetDesc->setObjectName("propertyLegendRelWithTargetDesc");
        propertyLegendRelWithTargetDesc->setFont(font);

        horizontalLayout_7->addWidget(propertyLegendRelWithTargetDesc);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_7);


        verticalLayout_3->addLayout(horizontalLayout_7);

        horizontalSpacer_15 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        verticalLayout_3->addItem(horizontalSpacer_15);


        gridLayout->addLayout(verticalLayout_3, 1, 2, 1, 1);


        retranslateUi(PropertyLegend);

        QMetaObject::connectSlotsByName(PropertyLegend);
    } // setupUi

    void retranslateUi(QWidget *PropertyLegend)
    {
        PropertyLegend->setProperty("comment", QVariant(QCoreApplication::translate("PropertyLegend", "\n"
"     Copyright 2017 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        propertyLegendLabelNoValue->setText(QCoreApplication::translate("PropertyLegend", "No Value", nullptr));
        propertyLegendLabelDefault->setText(QCoreApplication::translate("PropertyLegend", "Default", nullptr));
        propertyLegendLabelTimeSample->setText(QCoreApplication::translate("PropertyLegend", "Time Samples (Interpolated) ", nullptr));
        propertyLegendLabelFallback->setText(QCoreApplication::translate("PropertyLegend", "Fallback", nullptr));
        propertyLegendLabelCustom->setText(QCoreApplication::translate("PropertyLegend", "Custom", nullptr));
        propertyLegendLabelValueClips->setText(QCoreApplication::translate("PropertyLegend", "Value Clips (Interpolated)", nullptr));
        propertyLegendAttrPlainDesc->setText(QCoreApplication::translate("PropertyLegend", "Attribute", nullptr));
        propertyLegendRelPlainDesc->setText(QCoreApplication::translate("PropertyLegend", "Relationship", nullptr));
        propertyLegendCompDesc->setText(QCoreApplication::translate("PropertyLegend", "Computed Value", nullptr));
        propertyLegendConnDesc->setText(QCoreApplication::translate("PropertyLegend", "Connection", nullptr));
        propertyLegendTargetDesc->setText(QCoreApplication::translate("PropertyLegend", "Target", nullptr));
        inheritedPropertyIcon->setText(QCoreApplication::translate("PropertyLegend", "<small><i>(i)</i></small>", nullptr));
        inheritedPropertyText->setText(QCoreApplication::translate("PropertyLegend", "Inherited Property", nullptr));
        propertyLegendAttrWithConnDesc->setText(QCoreApplication::translate("PropertyLegend", "Attribute w/Connection(s)", nullptr));
        propertyLegendRelWithTargetDesc->setText(QCoreApplication::translate("PropertyLegend", "Relationship w/Target(s)", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PropertyLegend: public Ui_PropertyLegend {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PROPERTYLEGENDUI_H
