/********************************************************************************
** Form generated from reading UI file 'adjustDefaultMaterialUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef ADJUSTDEFAULTMATERIALUI_H
#define ADJUSTDEFAULTMATERIALUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_AdjustDefaultMaterial
{
public:
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_4;
    QLabel *ambientInt;
    QDoubleSpinBox *ambientIntSpinBox;
    QSpacerItem *horizontalSpacer_5;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer_6;
    QLabel *specularInt;
    QDoubleSpinBox *specularIntSpinBox;
    QSpacerItem *horizontalSpacer_7;
    QHBoxLayout *horizontalLayout_3;
    QPushButton *resetButton;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *doneButton;

    void setupUi(QDialog *AdjustDefaultMaterial)
    {
        if (AdjustDefaultMaterial->objectName().isEmpty())
            AdjustDefaultMaterial->setObjectName("AdjustDefaultMaterial");
        AdjustDefaultMaterial->resize(280, 123);
        QSizePolicy sizePolicy(QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(AdjustDefaultMaterial->sizePolicy().hasHeightForWidth());
        AdjustDefaultMaterial->setSizePolicy(sizePolicy);
        verticalLayout = new QVBoxLayout(AdjustDefaultMaterial);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName("verticalLayout_4");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_4);

        ambientInt = new QLabel(AdjustDefaultMaterial);
        ambientInt->setObjectName("ambientInt");
        ambientInt->setFocusPolicy(Qt::NoFocus);

        horizontalLayout->addWidget(ambientInt);

        ambientIntSpinBox = new QDoubleSpinBox(AdjustDefaultMaterial);
        ambientIntSpinBox->setObjectName("ambientIntSpinBox");
        ambientIntSpinBox->setDecimals(1);
        ambientIntSpinBox->setMaximum(1.000000000000000);
        ambientIntSpinBox->setSingleStep(0.100000000000000);

        horizontalLayout->addWidget(ambientIntSpinBox);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_5);


        verticalLayout_4->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);

        specularInt = new QLabel(AdjustDefaultMaterial);
        specularInt->setObjectName("specularInt");
        specularInt->setFocusPolicy(Qt::NoFocus);

        horizontalLayout_2->addWidget(specularInt);

        specularIntSpinBox = new QDoubleSpinBox(AdjustDefaultMaterial);
        specularIntSpinBox->setObjectName("specularIntSpinBox");
        specularIntSpinBox->setDecimals(1);
        specularIntSpinBox->setMaximum(1.000000000000000);
        specularIntSpinBox->setSingleStep(0.100000000000000);

        horizontalLayout_2->addWidget(specularIntSpinBox);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_7);


        verticalLayout_4->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        resetButton = new QPushButton(AdjustDefaultMaterial);
        resetButton->setObjectName("resetButton");
        resetButton->setAutoDefault(false);

        horizontalLayout_3->addWidget(resetButton);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_2);

        doneButton = new QPushButton(AdjustDefaultMaterial);
        doneButton->setObjectName("doneButton");

        horizontalLayout_3->addWidget(doneButton);


        verticalLayout_4->addLayout(horizontalLayout_3);


        verticalLayout->addLayout(verticalLayout_4);


        retranslateUi(AdjustDefaultMaterial);

        QMetaObject::connectSlotsByName(AdjustDefaultMaterial);
    } // setupUi

    void retranslateUi(QDialog *AdjustDefaultMaterial)
    {
        AdjustDefaultMaterial->setWindowTitle(QCoreApplication::translate("AdjustDefaultMaterial", "Adjust Default Material", nullptr));
        AdjustDefaultMaterial->setProperty("comment", QVariant(QCoreApplication::translate("AdjustDefaultMaterial", "\n"
"     Copyright 2017 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        ambientInt->setText(QCoreApplication::translate("AdjustDefaultMaterial", "Ambient Intensity", nullptr));
        specularInt->setText(QCoreApplication::translate("AdjustDefaultMaterial", "Specular Intensity", nullptr));
        resetButton->setText(QCoreApplication::translate("AdjustDefaultMaterial", "Reset", nullptr));
        doneButton->setText(QCoreApplication::translate("AdjustDefaultMaterial", "Done", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdjustDefaultMaterial: public Ui_AdjustDefaultMaterial {};
} // namespace Ui

QT_END_NAMESPACE

#endif // ADJUSTDEFAULTMATERIALUI_H
