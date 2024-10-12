/********************************************************************************
** Form generated from reading UI file 'adjustFreeCameraUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef ADJUSTFREECAMERAUI_H
#define ADJUSTFREECAMERAUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_AdjustFreeCamera
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_2;
    QCheckBox *overrideNear;
    QCheckBox *overrideFar;
    QVBoxLayout *verticalLayout_3;
    QDoubleSpinBox *nearSpinBox;
    QDoubleSpinBox *farSpinBox;
    QHBoxLayout *horizontalLayout_2;
    QCheckBox *lockFreeCamAspect;
    QDoubleSpinBox *freeCamAspect;
    QHBoxLayout *horizontalLayout_3;
    QLabel *freeCamFovLabel;
    QDoubleSpinBox *freeCamFov;

    void setupUi(QDialog *AdjustFreeCamera)
    {
        if (AdjustFreeCamera->objectName().isEmpty())
            AdjustFreeCamera->setObjectName("AdjustFreeCamera");
        AdjustFreeCamera->resize(331, 140);
        verticalLayout = new QVBoxLayout(AdjustFreeCamera);
        verticalLayout->setObjectName("verticalLayout");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        overrideNear = new QCheckBox(AdjustFreeCamera);
        overrideNear->setObjectName("overrideNear");
        overrideNear->setFocusPolicy(Qt::NoFocus);

        verticalLayout_2->addWidget(overrideNear);

        overrideFar = new QCheckBox(AdjustFreeCamera);
        overrideFar->setObjectName("overrideFar");
        overrideFar->setFocusPolicy(Qt::NoFocus);

        verticalLayout_2->addWidget(overrideFar);


        horizontalLayout->addLayout(verticalLayout_2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        nearSpinBox = new QDoubleSpinBox(AdjustFreeCamera);
        nearSpinBox->setObjectName("nearSpinBox");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(nearSpinBox->sizePolicy().hasHeightForWidth());
        nearSpinBox->setSizePolicy(sizePolicy);
        nearSpinBox->setDecimals(3);
        nearSpinBox->setMinimum(0.000000000000000);
        nearSpinBox->setMaximum(1000000000000.000000000000000);
        nearSpinBox->setSingleStep(1.000000000000000);

        verticalLayout_3->addWidget(nearSpinBox);

        farSpinBox = new QDoubleSpinBox(AdjustFreeCamera);
        farSpinBox->setObjectName("farSpinBox");
        sizePolicy.setHeightForWidth(farSpinBox->sizePolicy().hasHeightForWidth());
        farSpinBox->setSizePolicy(sizePolicy);
        farSpinBox->setDecimals(3);
        farSpinBox->setMinimum(0.000000000000000);
        farSpinBox->setMaximum(1000000000000.000000000000000);
        farSpinBox->setSingleStep(1.000000000000000);

        verticalLayout_3->addWidget(farSpinBox);


        horizontalLayout->addLayout(verticalLayout_3);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        lockFreeCamAspect = new QCheckBox(AdjustFreeCamera);
        lockFreeCamAspect->setObjectName("lockFreeCamAspect");
        lockFreeCamAspect->setFocusPolicy(Qt::NoFocus);

        horizontalLayout_2->addWidget(lockFreeCamAspect);

        freeCamAspect = new QDoubleSpinBox(AdjustFreeCamera);
        freeCamAspect->setObjectName("freeCamAspect");
        freeCamAspect->setDecimals(3);
        freeCamAspect->setMinimum(0.000000000000000);
        freeCamAspect->setSingleStep(0.100000000000000);

        horizontalLayout_2->addWidget(freeCamAspect);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        freeCamFovLabel = new QLabel(AdjustFreeCamera);
        freeCamFovLabel->setObjectName("freeCamFovLabel");
        freeCamFovLabel->setFocusPolicy(Qt::NoFocus);

        horizontalLayout_3->addWidget(freeCamFovLabel);

        freeCamFov = new QDoubleSpinBox(AdjustFreeCamera);
        freeCamFov->setObjectName("freeCamFov");
        freeCamFov->setDecimals(3);
        freeCamFov->setMinimum(0.000000000000000);
        freeCamFov->setMaximum(180.000000000000000);
        freeCamFov->setSingleStep(1.000000000000000);

        horizontalLayout_3->addWidget(freeCamFov);


        verticalLayout->addLayout(horizontalLayout_3);


        retranslateUi(AdjustFreeCamera);

        QMetaObject::connectSlotsByName(AdjustFreeCamera);
    } // setupUi

    void retranslateUi(QDialog *AdjustFreeCamera)
    {
        AdjustFreeCamera->setWindowTitle(QCoreApplication::translate("AdjustFreeCamera", "Adjust Free Camera", nullptr));
        AdjustFreeCamera->setProperty("comment", QVariant(QCoreApplication::translate("AdjustFreeCamera", "\n"
"     Copyright 2016 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        overrideNear->setText(QCoreApplication::translate("AdjustFreeCamera", "Override Near", nullptr));
        overrideFar->setText(QCoreApplication::translate("AdjustFreeCamera", "Override Far", nullptr));
        lockFreeCamAspect->setText(QCoreApplication::translate("AdjustFreeCamera", "Aspect Ratio", nullptr));
        freeCamFovLabel->setText(QCoreApplication::translate("AdjustFreeCamera", "FOV (degrees)", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdjustFreeCamera: public Ui_AdjustFreeCamera {};
} // namespace Ui

QT_END_NAMESPACE

#endif // ADJUSTFREECAMERAUI_H
