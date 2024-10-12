/********************************************************************************
** Form generated from reading UI file 'attributeValueEditorUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef ATTRIBUTEVALUEEDITORUI_H
#define ATTRIBUTEVALUEEDITORUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AttributeValueEditor
{
public:
    QVBoxLayout *verticalLayout;
    QStackedWidget *stackedWidget;
    QTextBrowser *valueViewer;

    void setupUi(QWidget *AttributeValueEditor)
    {
        if (AttributeValueEditor->objectName().isEmpty())
            AttributeValueEditor->setObjectName("AttributeValueEditor");
        AttributeValueEditor->resize(400, 300);
        verticalLayout = new QVBoxLayout(AttributeValueEditor);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        stackedWidget = new QStackedWidget(AttributeValueEditor);
        stackedWidget->setObjectName("stackedWidget");
        stackedWidget->setLineWidth(0);
        valueViewer = new QTextBrowser();
        valueViewer->setObjectName("valueViewer");
        stackedWidget->addWidget(valueViewer);

        verticalLayout->addWidget(stackedWidget);


        retranslateUi(AttributeValueEditor);

        stackedWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(AttributeValueEditor);
    } // setupUi

    void retranslateUi(QWidget *AttributeValueEditor)
    {
        AttributeValueEditor->setWindowTitle(QCoreApplication::translate("AttributeValueEditor", "Form", nullptr));
        AttributeValueEditor->setProperty("comment", QVariant(QCoreApplication::translate("AttributeValueEditor", "\n"
"     Copyright 2016 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the terms set forth in the LICENSE.txt file available at\n"
"     https://openusd.org/license.\n"
"  ", nullptr)));
    } // retranslateUi

};

namespace Ui {
    class AttributeValueEditor: public Ui_AttributeValueEditor {};
} // namespace Ui

QT_END_NAMESPACE

#endif // ATTRIBUTEVALUEEDITORUI_H
