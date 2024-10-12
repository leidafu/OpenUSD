/********************************************************************************
** Form generated from reading UI file 'preferencesUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PREFERENCESUI_H
#define PREFERENCESUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAbstractButton>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Preferences
{
public:
    QVBoxLayout *verticalLayout;
    QVBoxLayout *prefsOverButtonsLayout;
    QHBoxLayout *horizontalLayout_3;
    QLabel *fontSizeLabel;
    QSpinBox *fontSizeSpinBox;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer;
    QFrame *line;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Preferences)
    {
        if (Preferences->objectName().isEmpty())
            Preferences->setObjectName("Preferences");
        Preferences->resize(295, 99);
        verticalLayout = new QVBoxLayout(Preferences);
        verticalLayout->setObjectName("verticalLayout");
        prefsOverButtonsLayout = new QVBoxLayout();
        prefsOverButtonsLayout->setObjectName("prefsOverButtonsLayout");
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        fontSizeLabel = new QLabel(Preferences);
        fontSizeLabel->setObjectName("fontSizeLabel");

        horizontalLayout_3->addWidget(fontSizeLabel);

        fontSizeSpinBox = new QSpinBox(Preferences);
        fontSizeSpinBox->setObjectName("fontSizeSpinBox");
        fontSizeSpinBox->setMinimum(6);
        fontSizeSpinBox->setValue(10);

        horizontalLayout_3->addWidget(fontSizeSpinBox);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_2);


        prefsOverButtonsLayout->addLayout(horizontalLayout_3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        prefsOverButtonsLayout->addItem(verticalSpacer);

        line = new QFrame(Preferences);
        line->setObjectName("line");
        line->setFrameShape(QFrame::Shape::HLine);
        line->setFrameShadow(QFrame::Shadow::Sunken);

        prefsOverButtonsLayout->addWidget(line);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        buttonBox = new QDialogButtonBox(Preferences);
        buttonBox->setObjectName("buttonBox");
        buttonBox->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        horizontalLayout_2->addWidget(buttonBox);


        prefsOverButtonsLayout->addLayout(horizontalLayout_2);


        verticalLayout->addLayout(prefsOverButtonsLayout);


        retranslateUi(Preferences);

        QMetaObject::connectSlotsByName(Preferences);
    } // setupUi

    void retranslateUi(QDialog *Preferences)
    {
        Preferences->setWindowTitle(QCoreApplication::translate("Preferences", "Preferences", nullptr));
        Preferences->setProperty("comment", QVariant(QCoreApplication::translate("Preferences", "\n"
"     Copyright 2020 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
        fontSizeLabel->setText(QCoreApplication::translate("Preferences", "Font Size", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Preferences: public Ui_Preferences {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PREFERENCESUI_H
