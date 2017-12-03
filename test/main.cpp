#include "mainwindow.h"
#include <QApplication>
#include <QLabel>
int main(int argc, char *argv[])
{

    QApplication a(argc, argv);

    MainWindow w;

    w.show();
    QLabel *AgeLabel=new QLabel();
    QGridLayout *LeftLayout=new QGridLayout();

    LeftLayout->addWidget(AgeLabel,4,0);
    return a.exec();
}
