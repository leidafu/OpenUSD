/********************************************************************************
** Form generated from reading UI file 'primLegendUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PRIMLEGENDUI_H
#define PRIMLEGENDUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PrimLegend
{
public:
    QVBoxLayout *primLegendLayoutContainer;
    QGridLayout *primLegendLayout;
    QGraphicsView *primLegendColorHasArcs;
    QLabel *primLegendLabelHasArcs;
    QGraphicsView *primLegendColorInstance;
    QLabel *primLegendLabelInstance;
    QGraphicsView *primLegendColorPrototype;
    QLabel *primLegendLabelPrototype;
    QGraphicsView *primLegendColorNormal;
    QLabel *primLegendLabelNormal;
    QVBoxLayout *primLegendLabelContainer;
    QLabel *primLegendLabelDimmed;
    QLabel *primLegendLabelFontsAbstract;
    QLabel *primLegendLabelFontsUndefined;
    QLabel *primLegendLabelFontsDefined;

    void setupUi(QWidget *PrimLegend)
    {
        if (PrimLegend->objectName().isEmpty())
            PrimLegend->setObjectName("PrimLegend");
        PrimLegend->resize(438, 131);
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(PrimLegend->sizePolicy().hasHeightForWidth());
        PrimLegend->setSizePolicy(sizePolicy);
        primLegendLayoutContainer = new QVBoxLayout(PrimLegend);
        primLegendLayoutContainer->setObjectName("primLegendLayoutContainer");
        primLegendLayout = new QGridLayout();
        primLegendLayout->setObjectName("primLegendLayout");
        primLegendColorHasArcs = new QGraphicsView(PrimLegend);
        primLegendColorHasArcs->setObjectName("primLegendColorHasArcs");
        primLegendColorHasArcs->setMaximumSize(QSize(20, 15));

        primLegendLayout->addWidget(primLegendColorHasArcs, 0, 0, 1, 1);

        primLegendLabelHasArcs = new QLabel(PrimLegend);
        primLegendLabelHasArcs->setObjectName("primLegendLabelHasArcs");
        QFont font;
        font.setBold(false);
        font.setItalic(false);
        primLegendLabelHasArcs->setFont(font);

        primLegendLayout->addWidget(primLegendLabelHasArcs, 0, 1, 1, 1);

        primLegendColorInstance = new QGraphicsView(PrimLegend);
        primLegendColorInstance->setObjectName("primLegendColorInstance");
        primLegendColorInstance->setMaximumSize(QSize(20, 15));

        primLegendLayout->addWidget(primLegendColorInstance, 0, 2, 1, 1);

        primLegendLabelInstance = new QLabel(PrimLegend);
        primLegendLabelInstance->setObjectName("primLegendLabelInstance");
        primLegendLabelInstance->setFont(font);

        primLegendLayout->addWidget(primLegendLabelInstance, 0, 3, 1, 1);

        primLegendColorPrototype = new QGraphicsView(PrimLegend);
        primLegendColorPrototype->setObjectName("primLegendColorPrototype");
        primLegendColorPrototype->setMaximumSize(QSize(20, 15));

        primLegendLayout->addWidget(primLegendColorPrototype, 0, 4, 1, 1);

        primLegendLabelPrototype = new QLabel(PrimLegend);
        primLegendLabelPrototype->setObjectName("primLegendLabelPrototype");
        primLegendLabelPrototype->setFont(font);

        primLegendLayout->addWidget(primLegendLabelPrototype, 0, 5, 1, 1);

        primLegendColorNormal = new QGraphicsView(PrimLegend);
        primLegendColorNormal->setObjectName("primLegendColorNormal");
        primLegendColorNormal->setMaximumSize(QSize(20, 15));

        primLegendLayout->addWidget(primLegendColorNormal, 0, 6, 1, 1);

        primLegendLabelNormal = new QLabel(PrimLegend);
        primLegendLabelNormal->setObjectName("primLegendLabelNormal");
        primLegendLabelNormal->setFont(font);

        primLegendLayout->addWidget(primLegendLabelNormal, 0, 7, 1, 1);


        primLegendLayoutContainer->addLayout(primLegendLayout);

        primLegendLabelContainer = new QVBoxLayout();
        primLegendLabelContainer->setObjectName("primLegendLabelContainer");
        primLegendLabelDimmed = new QLabel(PrimLegend);
        primLegendLabelDimmed->setObjectName("primLegendLabelDimmed");

        primLegendLabelContainer->addWidget(primLegendLabelDimmed);

        primLegendLabelFontsAbstract = new QLabel(PrimLegend);
        primLegendLabelFontsAbstract->setObjectName("primLegendLabelFontsAbstract");

        primLegendLabelContainer->addWidget(primLegendLabelFontsAbstract);

        primLegendLabelFontsUndefined = new QLabel(PrimLegend);
        primLegendLabelFontsUndefined->setObjectName("primLegendLabelFontsUndefined");

        primLegendLabelContainer->addWidget(primLegendLabelFontsUndefined);

        primLegendLabelFontsDefined = new QLabel(PrimLegend);
        primLegendLabelFontsDefined->setObjectName("primLegendLabelFontsDefined");

        primLegendLabelContainer->addWidget(primLegendLabelFontsDefined);


        primLegendLayoutContainer->addLayout(primLegendLabelContainer);


        retranslateUi(PrimLegend);

        QMetaObject::connectSlotsByName(PrimLegend);
    } // setupUi

    void retranslateUi(QWidget *PrimLegend)
    {
        PrimLegend->setProperty("comment", QVariant(QCoreApplication::translate("PrimLegend", "\n"
"     Copyright 2017 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        primLegendLabelHasArcs->setText(QCoreApplication::translate("PrimLegend", "HasArcs", nullptr));
        primLegendLabelInstance->setText(QCoreApplication::translate("PrimLegend", "Instance", nullptr));
        primLegendLabelPrototype->setText(QCoreApplication::translate("PrimLegend", "Prototype", nullptr));
        primLegendLabelNormal->setText(QCoreApplication::translate("PrimLegend", "Normal", nullptr));
        primLegendLabelDimmed->setText(QCoreApplication::translate("PrimLegend", "Dimmed colors denote inactive prims", nullptr));
        primLegendLabelFontsAbstract->setText(QCoreApplication::translate("PrimLegend", "Normal font indicates abstract prims(class and children)", nullptr));
        primLegendLabelFontsUndefined->setText(QCoreApplication::translate("PrimLegend", "Italic font indicates undefined prims(declared with over)", nullptr));
        primLegendLabelFontsDefined->setText(QCoreApplication::translate("PrimLegend", "Bold font indicates defined prims(declared with def)", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PrimLegend: public Ui_PrimLegend {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PRIMLEGENDUI_H
