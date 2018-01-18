# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import threading
from os.path import expanduser
import zipfile, os
import paramiko
#import SSHLibrary
import csv
import shutil
import fnmatch
import time
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import re
import glob
from random import randrange
from sys import argv, exit
from PyQt5.QtWidgets import QListWidgetItem, QListWidget, QApplication, QGroupBox, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import subprocess
import platform
import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction,QMessageBox, QFileDialog, QApplication,QPushButton,QInputDialog,QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget



def resource_path(relative_path):
#""" Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def backupToZip(folder,type):
    # Backup the entire contents of "folder" into a ZIP file.
    if (type == "Component"):
        folder = os.path.abspath(folder)  # make sure folder is absolute
        print(folder)
        # Figure out the filename this code should use based on
        # what files already exist.
        number = 1
        while True:
            zipFilename1 = "/Users/Backup_Components(Logic)" + '_' + str(number)
            zipFilename = "/Users/" + '_' + str(number)
            #zipFilename1 = "~/Desktop/" + '_' + str(number)
            zipFilename = "/Users/Backup_Components(Logic)" + '_' + str(number) + '.zip'
            if not os.path.exists(zipFilename):
                break
            number = number + 1

        # TODO: Create the ZIP file.
        # Walk the entire folder tree and compress the files in each folder.
        print('Creating %s...' % (zipFilename))
        print('Done.')
        logger.info('Creating Zip: ' + zipFilename)


        shutil.make_archive(zipFilename1, 'zip', folder)
        if os.path.exists(zipFilename):
            logger.info('Done')
            return 1
        return 0

    if (type == "VST"):
        folder = os.path.abspath(folder)  # make sure folder is absolute
        print(folder)
        # Figure out the filename this code should use based on
        # what files already exist.
        number = 1
        while True:
            zipFilename1 = "/Users/Backup_VST" + '_' + str(number)
            zipFilename = "/Users/" + '_' + str(number)
            #zipFilename1 = "~/Desktop/" + '_' + str(number)
            zipFilename = "/Users/Backup_VST" + '_' + str(number) + '.zip'
            if not os.path.exists(zipFilename):
                break
            number = number + 1

        # TODO: Create the ZIP file.
        # Walk the entire folder tree and compress the files in each folder.
        print('Creating %s...' % (zipFilename))
        print('Done.')
        logger.info('Creating Zip: ' + zipFilename)


        shutil.make_archive(zipFilename1, 'zip', folder)
        if os.path.exists(zipFilename):
            logger.info('Done')
            return 1
        return 0

    if (type == "aax"):
        folder = os.path.abspath(folder)  # make sure folder is absolute
        print(folder)
        # Figure out the filename this code should use based on
        # what files already exist.
        number = 1
        while True:
            zipFilename1 = "/Users/Backup_aax(ProTools)" + '_' + str(number)
            zipFilename = "/Users/" + '_' + str(number)
            #zipFilename1 = "~/Desktop/" + '_' + str(number)
            zipFilename = "/Users/Backup_aax(ProTools)" + '_' + str(number) + '.zip'
            if not os.path.exists(zipFilename):
                break
            number = number + 1

        # TODO: Create the ZIP file.
        # Walk the entire folder tree and compress the files in each folder.
        print('Creating %s...' % (zipFilename))
        print('Done.')
        logger.info('Creating Zip: ' + zipFilename)


        shutil.make_archive(zipFilename1, 'zip', folder)
        if os.path.exists(zipFilename):
            logger.info('Done')
            return 1
        return 0

    if (type == "dpm"):
        folder = os.path.abspath(folder)  # make sure folder is absolute
        print(folder)
        # Figure out the filename this code should use based on
        # what files already exist.
        number = 1
        while True:
            zipFilename1 = "/Users/Backup_dpm(ProTools)" + '_' + str(number)
            zipFilename = "/Users/" + '_' + str(number)
            #zipFilename1 = "~/Desktop/" + '_' + str(number)
            zipFilename = "/Users/Backup_dpm(ProTools)" + '_' + str(number) + '.zip'
            if not os.path.exists(zipFilename):
                break
            number = number + 1

        # TODO: Create the ZIP file.
        # Walk the entire folder tree and compress the files in each folder.
        print('Creating %s...' % (zipFilename))
        print('Done.')
        logger.info('Creating Zip: ' + zipFilename)


        shutil.make_archive(zipFilename1, 'zip', folder)
        if os.path.exists(zipFilename):
            logger.info('Done')
            return 1
        return 0


    return 1

def setcombo(self,combo_box_options,array_matched_plugins,currentfile):
    combo_box_options = ["Hidden", "Shown"]
    #print(array_matched_plugins)

    counter_my = len(array_matched_plugins)

    i = 0
    j = 1
    #print(counter_my)
    #print(currentfile)
    #time.sleep(3)
    while i < counter_my:
        j = 1

        #print(array_matched_plugins[i][1])
        #print(currentfile)
        while j < 5:
            if (array_matched_plugins[i][j] == currentfile):
                combo_box_options = ["Shown", "Hidden"]
                #print("matcheeeeee")
                # print(array_my_plugins[i])
                # print(all_plugins_list[j][0])
                #if (array_my_plugins[i][0] == all_plugins_list[j][0] and array_my_plugins[i][1] != " Demo not started"):
                #    array_matched_plugins.append(all_plugins_list[j])
            j = j + 1
            #print(i)
            #print(array_matched_plugins[i][j])

        i = i + 1







    return combo_box_options


def by_imported_file(self,type,fname):
        #self.pushButton6.setIcon(QtGui.QIcon(resource_path("donate.jpg")))
        #with open('/Users/carneiro/Downloads/UAD/final.csv', 'r') as f:
        with open(resource_path("final.csv"), 'r') as f:
            # reader = csv.reader(f)
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            all_plugins_list = list(reader)

        # print(all_plugins_list[2][0])
        #print(fname[0])
        with open(fname[0], 'r') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            array_my_plugins_temp = list(reader)

        #with open('/Users/carneiro/Downloads/UAD/UADSystemProfile.txt', 'r') as f:
        #    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        #    array_my_plugins_temp = list(reader)


        counter = len(array_my_plugins_temp)
        save = 0

        i = 0
        array_my_plugins = []
        while i < counter:
            # print(array_my_plugins_temp[i])
            if "\t\t\t UAD-2 Plug-in Authorizations \t\t\t" in array_my_plugins_temp[i]:
                save = 1
            if save == 1:
                array_my_plugins.append(array_my_plugins_temp[i])
            i = i + 1

        # print(array_my_plugins[2][1])
        # print(len(array_my_plugins))

        array_matched_plugins = []
        counter_my = len(array_my_plugins)
        counter_all = len(all_plugins_list)
        i = 2
        j = 0
        while i < counter_my:
            j = 0
            while j < counter_all:
                # print(array_my_plugins[i])
                # print(all_plugins_list[j][0])
                if (array_my_plugins[i][0] == all_plugins_list[j][0] and array_my_plugins[i][1] != " Demo not started"):
                    array_matched_plugins.append(all_plugins_list[j])
                j = j + 1
            i = i + 1
        print("--------------------------------")
        print(array_matched_plugins)

        #print(type)
        self.tableWidget.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk(path_type):
            files.sort()
            plugins = files
            # logger.info(plugins)
            # print(plugins)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setColumnWidth(0, 703)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        # item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item2)

        combo_box_options = ["Shown", "Hidden"]

        root = path_type
        listplugin = ""
        temp1 = 1
        index = 0
        pattern = '*.txt'
        path = '.'
        os.chdir(path_type)
        #print(path_type)
        #print(root)
        for i in sorted(glob.glob('UAD*')):
            # print(i)
            #temp1 = temp1 + 1
            if (os.path.join(root, i)):
                # print(i)
                i = re.sub(extension, '', i)
                combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                if combo_box_options[0] == "Shown":
                    #print(combo_box_options[0])
                    #print(i)
                    combo = QtWidgets.QComboBox();
                    self.tableWidget.insertRow(self.tableWidget.rowCount())
                    item = QtWidgets.QTableWidgetItem('UAD')
                    item.setText(i)
                    self.tableWidget.setItem(temp1 - 1, 0, item)
                    #combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                    for t in combo_box_options:
                        #print(i)
                        combo.addItem(t)

                    self.tableWidget.setCellWidget(temp1 - 1, 1, combo)
                    temp1 = temp1 + 1
        logger.info('By_Imported tab Populed')

    #Popular Hide

        self.tableWidget_hide.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk(path_type):
            files.sort()
            plugins = files
            # logger.info(plugins)
            # print(plugins)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget_hide.setHorizontalHeaderItem(0, item1)
        self.tableWidget_hide.setColumnWidth(0, 703)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        # item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget_hide.setHorizontalHeaderItem(1, item2)

        self.tabWidget.currentIndex = 1
        combo_box_options = ["Shown", "Hidden"]
        root = path_type
        listplugin = ""
        temp1 = 1
        index = 0
        pattern = '*.txt'
        path = '.'
        os.chdir(path_type)
        print(path_type)
        print(root)
        for i in sorted(glob.glob('UAD*')):
            # print(i)
            #temp1 = temp1 + 1
            if (os.path.join(root, i)):
                # print(i)
                i = re.sub(extension, '', i)
                combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                if combo_box_options[0] == "Hidden":
                    print("by_Imported")
                    print(combo_box_options[0])
                    print(i)
                    combo = QtWidgets.QComboBox();
                    self.tableWidget_hide.insertRow(self.tableWidget_hide.rowCount())
                    item = QtWidgets.QTableWidgetItem('UAD')
                    item.setText(i)
                    self.tableWidget_hide.setItem(temp1 - 1, 0, item)
                    #combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                    for t in combo_box_options:
                        #print(i)
                        combo.addItem(t)

                    self.tableWidget_hide.setCellWidget(temp1 - 1, 1, combo)
                    temp1 = temp1 + 1
        logger.info('By_Imported tab Populed')

def PopUpVersion_CSV_Update(self,status,path):

        if status == "Close_APP":
            name = "\n   New Version Detected.\n   Please Download it in : "
            name = name + path
            self.exPopup = examplePopup(name)
            self.exPopup.setGeometry(500, 300, 415, 55)
            screen = QDesktopWidget().screenGeometry()
            geometry = Dialog.saveGeometry()
            widget = Dialog.geometry()
            # x = screen.width() - widget.width()
            # y = screen.height() - widget.height()
            y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
            x = widget.left() + ((widget.right() - widget.left())/2) - 207
            #x = widget
            #y = screen.height() - widget.height()
            self.exPopup.setGeometry(x, y, 420, 65)


        if status == "Close_CSV":
            name = "\n   Plugin Database Updated!. Please Restart the Application!"
            self.exPopup = examplePopup(name)
            self.exPopup.setGeometry(500, 300, 415, 55)
            screen = QDesktopWidget().screenGeometry()
            geometry = Dialog.saveGeometry()
            widget = Dialog.geometry()
            # x = screen.width() - widget.width()
            # y = screen.height() - widget.height()
            y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
            x = widget.left() + ((widget.right() - widget.left())/2) - 207
            #x = widget
            #y = screen.height() - widget.height()
            self.exPopup.setGeometry(x, y, 380, 55)

        if status == "NotClose":
            name = "\n   You have the latest version!"
            self.exPopup = examplePopup_help(name)
            self.exPopup.setGeometry(500, 300, 415, 55)
            screen = QDesktopWidget().screenGeometry()
            geometry = Dialog.saveGeometry()
            widget = Dialog.geometry()
            # x = screen.width() - widget.width()
            # y = screen.height() - widget.height()
            y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
            x = widget.left() + ((widget.right() - widget.left())/2) - 107
            #x = widget
            #y = screen.height() - widget.height()
            self.exPopup.setGeometry(x, y, 200, 55)

        self.exPopup.setWindowModality(Qt.ApplicationModal)
        self.exPopup.show()


def PopUpVersion_CannotConnect(self, status, path):
    if status == "Close_APP":
        name = "\n   New Version Detected.\n   Please Download it in : "
        name = name + path
        self.exPopup = examplePopup(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top()) / 2) - 50
        x = widget.left() + ((widget.right() - widget.left()) / 2) - 207
        # x = widget
        # y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 420, 65)

    if status == "Close_CSV":
        name = "\n          Cannot Connect to Server. Please Try Again Later!"
        self.exPopup = examplePopup_help(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top()) / 2) - 50
        x = widget.left() + ((widget.right() - widget.left()) / 2) - 207
        # x = widget
        # y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 380, 55)

    if status == "NotClose":
        name = "\n   You have the latest version!"
        self.exPopup = examplePopup_help(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top()) / 2) - 50
        x = widget.left() + ((widget.right() - widget.left()) / 2) - 107
        # x = widget
        # y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 200, 55)

    self.exPopup.setWindowModality(Qt.ApplicationModal)
    self.exPopup.show()


def by_login(self, type, fname):
        with open(resource_path("final.csv"), 'r') as f:
            # reader = csv.reader(f)
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            all_plugins_list = list(reader)

        # print(all_plugins_list[2][0])
        # print(fname[0])
        with open(fname[0], 'r') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            array_my_plugins_temp = list(reader)

        # with open('/Users/carneiro/Downloads/UAD/UADSystemProfile.txt', 'r') as f:
        #    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        #    array_my_plugins_temp = list(reader)

        counter = len(array_my_plugins_temp)
        save = 0

        i = 0
        array_my_plugins = []
        while i < counter:
            # print(array_my_plugins_temp[i])
            if "\t\t\t UAD-2 Plug-in Authorizations \t\t\t" in array_my_plugins_temp[i]:
                save = 1
            if save == 1:
                array_my_plugins.append(array_my_plugins_temp[i])
            i = i + 1

        # print(array_my_plugins[2][1])
        # print(len(array_my_plugins))

        array_matched_plugins = []
        counter_my = len(array_my_plugins)
        counter_all = len(all_plugins_list)
        i = 2
        j = 0
        while i < counter_my:
            j = 0
            while j < counter_all:
                # print(array_my_plugins[i])
                # print(all_plugins_list[j][0])
                if (array_my_plugins[i][0] == all_plugins_list[j][0] and array_my_plugins[i][1] != " Demo not started"):
                    array_matched_plugins.append(all_plugins_list[j])
                j = j + 1
            i = i + 1

        # print(array_matched_plugins)

        # print(type)
        self.tableWidget.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk(path_type):
            files.sort()
            plugins = files
            # logger.info(plugins)
            # print(plugins)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setColumnWidth(0, 703)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        # item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item2)

        combo_box_options = ["Shown", "Hidden"]

        root = path_type
        listplugin = ""
        temp1 = 1
        index = 0
        pattern = '*.txt'
        path = '.'
        os.chdir(path_type)
        # print(path_type)
        # print(root)
        for i in sorted(glob.glob('UAD*')):
            # print(i)
            # temp1 = temp1 + 1
            if (os.path.join(root, i)):
                # print(i)
                i = re.sub(extension, '', i)
                combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                if combo_box_options[0] == "Shown":
                    # print(combo_box_options[0])
                    # print(i)
                    combo = QtWidgets.QComboBox();
                    self.tableWidget.insertRow(self.tableWidget.rowCount())
                    item = QtWidgets.QTableWidgetItem('UAD')
                    item.setText(i)
                    self.tableWidget.setItem(temp1 - 1, 0, item)
                    # combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                    for t in combo_box_options:
                        # print(i)
                        combo.addItem(t)

                    self.tableWidget.setCellWidget(temp1 - 1, 1, combo)
                    temp1 = temp1 + 1
        logger.info('By_Imported tab Populed')

        # Popular Hide

        self.tableWidget_hide.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk(path_type):
            files.sort()
            plugins = files
            # logger.info(plugins)
            # print(plugins)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget_hide.setHorizontalHeaderItem(0, item1)
        self.tableWidget_hide.setColumnWidth(0, 703)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        # item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget_hide.setHorizontalHeaderItem(1, item2)

        self.tabWidget.currentIndex = 1
        combo_box_options = ["Shown", "Hidden"]
        root = path_type
        listplugin = ""
        temp1 = 1
        index = 0
        pattern = '*.txt'
        path = '.'
        os.chdir(path_type)
        print(path_type)
        print(root)
        for i in sorted(glob.glob('UAD*')):
            # print(i)
            # temp1 = temp1 + 1
            if (os.path.join(root, i)):
                # print(i)
                i = re.sub(extension, '', i)
                combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                if combo_box_options[0] == "Hidden":
                    print("by_Imported")
                    print(combo_box_options[0])
                    print(i)
                    combo = QtWidgets.QComboBox();
                    self.tableWidget_hide.insertRow(self.tableWidget_hide.rowCount())
                    item = QtWidgets.QTableWidgetItem('UAD')
                    item.setText(i)
                    self.tableWidget_hide.setItem(temp1 - 1, 0, item)
                    # combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
                    for t in combo_box_options:
                        # print(i)
                        combo.addItem(t)

                    self.tableWidget_hide.setCellWidget(temp1 - 1, 1, combo)
                    temp1 = temp1 + 1
        logger.info('By_Imported tab Populed')

def check_fileformat(self,type,fname):
    format = "0"
    with open(resource_path("final.csv"), 'r') as f:

        # reader = csv.reader(f)
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        all_plugins_list = list(reader)

    # print(all_plugins_list[2][0])
    #print(fname[0])
    with open(fname[0], 'r') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        array_my_plugins_temp = list(reader)

    #with open('/Users/carneiro/Downloads/UAD/UADSystemProfile.txt', 'r') as f:
    #    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    #    array_my_plugins_temp = list(reader)


    counter = len(array_my_plugins_temp)
    save = 0

    i = 0
    if os.path.getsize(fname[0]) > 0:

        print(array_my_plugins_temp[0])
        #print(array_my_plugins_temp[1])
        logger.info(array_my_plugins_temp[0])
        if "Universal Audio Inc." in str(array_my_plugins_temp[0]):
            logger.info('File Format OK')
            format = 1
            print("11111")



    if format != 1:
        return 1

    return 0

def check_version(self,type,fname):
    version = "0"
    with open(resource_path("final.csv"), 'r') as f:

        # reader = csv.reader(f)
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        all_plugins_list = list(reader)

    # print(all_plugins_list[2][0])
    #print(fname[0])
    with open(fname[0], 'r') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        array_my_plugins_temp = list(reader)

    #with open('/Users/carneiro/Downloads/UAD/UADSystemProfile.txt', 'r') as f:
    #    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    #    array_my_plugins_temp = list(reader)


    counter = len(array_my_plugins_temp)
    save = 0

    i = 0
    array_my_plugins = []
    while i < counter:

        curr_version = "9.4.1"
        current_text = str(array_my_plugins_temp[i])

        if "UAD Software Release Version" in array_my_plugins_temp[i]:
            logger.info('Software Version: ' + current_text)
            logger.info('File Version: ' + curr_version)
            if curr_version in current_text:
                version = 1


        i = i + 1

    # print(array_my_plugins[2][1])
    # print(len(array_my_plugins))

    array_matched_plugins = []
    counter_my = len(array_my_plugins)
    counter_all = len(all_plugins_list)
    i = 2
    j = 0
    print(version)
    if version != 1:
        return 1

    return 0







def check_version_sftp(self):
    notconnect = 0
    version = "0"
    try:
        host = "sheepbox.dlinkddnds.com"  # hard-coded
        #host = "192.168.1.80"  # hard-coded
        port = 8443
        transport = paramiko.Transport((host, port))

        password = "uad123"  # hard-coded
        username = "uad"  # hard-coded
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        # path = './THETARGETDIRECTORY/' + sys.argv[1]  # hard-coded
        # localpath = sys.argv[1]
        # sftp.put(localpath, path)

        sftp.get("/home/uad/final_server.csv", resource_path("final_server.csv"))
        sftp.get("/home/uad/version.txt", resource_path("version.txt"))

        sftp.close()
        transport.close()
    except:
        print ("Cannot Connect to Server to Check Version!")
        logger.info('Cannot Connect to Server to Check Version!')
        notconnect = 1
        PopUpVersion_CannotConnect(self, "Close_CSV", "")


    if notconnect == 0:

        with open(resource_path("version.txt"), 'r') as f:

            # reader = csv.reader(f)
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            server_version_file = list(reader)

        with open(resource_path("current_version.txt"), 'r') as f:
            # reader = csv.reader(f)
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            current_version_file = list(reader)

        save = 0

        i = 0
        array_my_plugins = []

        #self.currentversion = "2.0"
        #self.csv_version = "1.1"
        #self.uad_version = "9.4.0"

        current_version = str(current_version_file[0][1])
        current_csv_version = str(current_version_file[1][1])
        server_version = str(server_version_file[0][1])
        server_csv_version = str(server_version_file[1][1])

        download_path = str(server_version_file[2][1])

        print(self.currentversion)
        print(current_version)

        if current_version != server_version:
            logger.info('Software Version: ' + current_version)
            logger.info('CSV File Version: ' + current_csv_version)
            PopUpVersion_CSV_Update(self,"Close_APP",download_path)

        if current_csv_version != server_csv_version:
            logger.info('Software Version: ' + current_version)
            logger.info('CSV File Version: ' + current_csv_version)
            sourcefile = resource_path("version.txt")
            destfile = resource_path("current_version.txt")
            shutil.move(sourcefile, destfile)
            logger.info('CSV File Updated:  ' + sourcefile + " to " + destfile)
            sourcefile = resource_path("final_server.csv")
            destfile = resource_path("final.csv")
            shutil.move(sourcefile, destfile)
            logger.info('Version File Updated:  ' + sourcefile + " to " + destfile)
            PopUpVersion_CSV_Update(self,"Close_CSV","")




        if current_csv_version == server_csv_version and current_version == server_version:
            logger.info('Software Version: ' + current_version)
            logger.info('CSV File Version: ' + current_csv_version)
            PopUpVersion_CSV_Update(self,"NotClose","")










    # print(array_my_plugins[2][1])
    # print(len(array_my_plugins))

    i = 2
    j = 0
    print(version)
    print("-------------------------")
    if version != 1:
        return 1

    return 0






def showDialog(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

    if fname[0]:
        f = open(fname[0], 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

def popula_hide_tab(self,type,fname):
    self.tableWidget_hide.setRowCount(0)
    path_type = "/Library/Audio/Plug-Ins/Unused/Components"
    extension = "\.component"
    if type == "PT":
        path_type = "/Library/Application Support/Avid/Audio/Unused"
        extension = "\.aaxplugin"

    if type == "VST":
        path_type = "/Library/Audio/Plug-Ins/Unused/VST"
        extension = "\.vst"

    #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
    #        self.tableWidget.move(30, 30)
    #        self.tableWidget.resize(400, 300)
    for root, dirs, files in os.walk(path_type):
        #files.sort()
        plugins = files
        # print(plugins)
    item11 = QtWidgets.QTableWidgetItem('Plugin')
    font = QtGui.QFont()
    font.setPointSize(15)
    font.setFamily("Times New Roman")
    item11.setFont(font)
    # item1.setBackground(QtGui.QColor(255, 0, 0))
    self.tableWidget_hide.setHorizontalHeaderItem(0, item11)
    self.tableWidget_hide.setColumnWidth(0, 743)
    item21 = QtWidgets.QTableWidgetItem('Status')
    font = QtGui.QFont()
    font.setPointSize(15)
    font.setFamily("Times New Roman")
    item21.setFont(font)
    # item2.setBackground(QtGui.QColor(0, 255, 0))
    self.tableWidget_hide.setHorizontalHeaderItem(1, item21)

    combo_box_options = ["Hidden", "Shown"]

    root = path_type
    listplugin = ""
    temp1 = 0
    index = 0
    pattern = '*.txt'
    path = '.'
    os.chdir(path_type)
    for i in sorted(glob.glob('UAD*')):
        
        temp1 = temp1 + 1
        if (os.path.join(root, i)):
            i = re.sub(extension, '', i)
            combo = QtWidgets.QComboBox();
            self.tableWidget_hide.insertRow(self.tableWidget_hide.rowCount())
            item = QtWidgets.QTableWidgetItem('UAD')
            item.setText(i)
            self.tableWidget_hide.setItem(temp1 - 1, 0, item)
            for t in combo_box_options:
                combo.addItem(t)
            self.tableWidget_hide.setCellWidget(temp1 - 1, 1, combo)
    logger.info('Hidden tab Populed')

    #print(self.tableWidget_hide.rowCount())

def popula_branco(self, type):
        self.tableWidget.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setColumnWidth(0, 743)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item2)

        combo_box_options = ["Shown", "Hidden"]

def popula_tab(self,type,fname):
        self.tableWidget.setRowCount(0)
        path_type = "/Library/Audio/Plug-Ins/Components"
        extension = "\.component"
        if type == "PT":
            path_type = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            extension = "\.aaxplugin"

        if type == "VST":
            path_type = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            extension = "\.vst"

        #        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
        #        self.tableWidget.move(30, 30)
        #        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk(path_type):
            files.sort()
            plugins = files
            #logger.info(plugins)
            #print(plugins)
        item1 = QtWidgets.QTableWidgetItem('Plugin')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item1.setFont(font)
        # item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setColumnWidth(0, 743)
        item2 = QtWidgets.QTableWidgetItem('Status')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Times New Roman")
        item2.setFont(font)
        # item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item2)


        combo_box_options = ["Shown", "Hidden"]
        
        root = path_type
        listplugin = ""
        temp1 = 0
        index = 0
        pattern = '*.txt'
        path = '.'
        os.chdir(path_type)
        print(path_type)
        print(root)
        for i in sorted(glob.glob('UAD*')):
            #print(i)
            temp1 = temp1 + 1
            if (os.path.join(root, i)):
                #print(i)
                i = re.sub(extension, '', i)
                combo = QtWidgets.QComboBox();
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                item = QtWidgets.QTableWidgetItem('UAD')
                item.setText(i)
                self.tableWidget.setItem(temp1 - 1, 0, item)
                for t in combo_box_options:
                    combo.addItem(t)
                self.tableWidget.setCellWidget(temp1 - 1, 1, combo)
        logger.info('Shown tab Populed')

def Hide(self, type, fname):
    # Move the Hided to Unsused folder.
    print(self.tabWidget.currentIndex)
    print(self.tabWidget.currentIndex)
    print(self.tabWidget.currentIndex)
    if (self.tabWidget.currentIndex == 0 and type == "Logic"):
        logger.info('--Hided AU Plugins--')
        root = "/Library/Audio/Plug-Ins/Components"
        root_backup = "/Library/Audio/Plug-Ins/Unused/Components"

        for i in range(0, self.tableWidget.rowCount()):
            combo = self.tableWidget.cellWidget(i, 1)
            print(combo.currentText())
            if (combo.currentText() == "Hidden"):
                self.tableWidget.setCurrentCell(i, 0)
                curItem = self.tableWidget.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(sourcefile, destfile)
                        logger.info('Hided:  ' + sourcefile + " to " + destfile)

    if (self.tabWidget.currentIndex == 0 and type == "PT"):
        logger.info('--Hided ProTools Plugins--')
        root = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
        root_backup = "/Library/Application Support/Avid/Audio/Unused/"

        for i in range(0, self.tableWidget.rowCount()):
            combo = self.tableWidget.cellWidget(i, 1)
            print(combo.currentText())
            if (combo.currentText() == "Hidden"):
                self.tableWidget.setCurrentCell(i, 0)
                curItem = self.tableWidget.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(sourcefile, destfile)
                        logger.info('Hided:  ' + sourcefile + " to " + destfile)

    if (self.tabWidget.currentIndex == 1 and type == "PT"):

        root_backup = "/Library/Application Support/Avid/Audio/Unused/"
        root = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
        logger.info('--Showed AU Plugins--')
        for i in range(0, self.tableWidget_hide.rowCount()):
            combo = self.tableWidget_hide.cellWidget(i, 1)
            if (combo.currentText() == "Shown"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)

    if (self.tabWidget.currentIndex == 1 and type == "Logic"):
        root_backup = "/Library/Audio/Plug-Ins/Unused/Components"
        root = "/Library/Audio/Plug-Ins/Components"
        logger.info('--Showed AU Plugins--')
        for i in range(0, self.tableWidget_hide.rowCount()):
            combo = self.tableWidget_hide.cellWidget(i, 1)
            if (combo.currentText() == "Shown"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)


    if (self.tabWidget.currentIndex == 0 and type == "VST"):
        logger.info('--Hided VST Plugins--')
        root = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
        root_backup = "/Library/Audio/Plug-Ins/Unused/VST"
        root_mono = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/Mono"
        root_mono_backup = "/Library/Audio/Plug-Ins/Unused/VST/Mono"

        for i in range(0, self.tableWidget.rowCount()):
            combo = self.tableWidget.cellWidget(i, 1)
            print(combo.currentText())
            if (combo.currentText() == "Hidden"):
                self.tableWidget.setCurrentCell(i, 0)
                curItem = self.tableWidget.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(sourcefile, destfile)
                        logger.info('Hided:  ' + sourcefile + " to " + destfile)
                for file in os.listdir(root_mono):
                    if fnmatch.fnmatch(file, curItem.text() + "(m).*"):
                        sourcefile = root_mono + "/" + str(file)
                        destfile = root_mono_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(sourcefile, destfile)
                        logger.info('Hided:  ' + sourcefile + " to " + destfile)

    if (self.tabWidget.currentIndex == 1 and type == "VST"):

        root_backup = "/Library/Audio/Plug-Ins/Unused/VST"
        root = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
        root_mono_backup = "/Library/Audio/Plug-Ins/Unused/VST/Mono"
        root_mono = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/Mono"

        logger.info('--VST AU Plugins--')
        for i in range(0, self.tableWidget_hide.rowCount()):
            combo = self.tableWidget_hide.cellWidget(i, 1)
            if (combo.currentText() == "Shown"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)
                for file in os.listdir(root_mono_backup):
                    if fnmatch.fnmatch(file, curItem.text() + "(m).*"):
                        sourcefile = root_mono + "/" + str(file)
                        destfile = root_mono_backup + "/" + str(file)
                        #print(sourcefile)
                        #print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)



    # print(self.tabWidget.currentIndex())
    popula_tab(self, type,fname)
    popula_hide_tab(self, type,fname)
    return 1

def Hide_new(self,type,fname):
        # Move the Hided to Unsused folder.
        print(self.tabWidget.currentIndex)
        print(self.tabWidget.currentIndex)
        print(self.tabWidget.currentIndex)
        if (type == "Logic"):
            logger.info('--Hided AU Plugins--')
            root = "/Library/Audio/Plug-Ins/Components"
            root_backup = "/Library/Audio/Plug-Ins/Unused/Components"

            for i in range(0, self.tableWidget_hide.rowCount()):
                combo = self.tableWidget_hide.cellWidget(i, 1)
                print(combo.currentText())
                if (combo.currentText() == "Hidden"):
                    self.tableWidget_hide.setCurrentCell(i, 0)
                    curItem = self.tableWidget_hide.currentItem()
                    # print(curItem.text())
                    caminho = root + '_' + "\\" + str(curItem.text())
                    # print(caminho)
                    for file in os.listdir(root):
                        if fnmatch.fnmatch(file, curItem.text() + ".*"):
                            sourcefile = root + "/" + str(file)
                            destfile = root_backup + "/" + str(file)
                            # print(sourcefile)
                            # print(destfile)
                            shutil.move(sourcefile, destfile)
                            logger.info('Hided:  ' + sourcefile + " to " + destfile)

        if (type == "PT"):
            logger.info('--Hided ProTools Plugins--')
            root = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
            root_backup = "/Library/Application Support/Avid/Audio/Unused/"

            for i in range(0, self.tableWidget_hide.rowCount()):
                combo = self.tableWidget_hide.cellWidget(i, 1)
                print(combo.currentText())
                if (combo.currentText() == "Hidden"):
                    self.tableWidget_hide.setCurrentCell(i, 0)
                    curItem = self.tableWidget_hide.currentItem()
                    # print(curItem.text())
                    caminho = root + '_' + "\\" + str(curItem.text())
                    # print(caminho)
                    for file in os.listdir(root):
                        if fnmatch.fnmatch(file, curItem.text() + ".*"):
                            sourcefile = root + "/" + str(file)
                            destfile = root_backup + "/" + str(file)
                            # print(sourcefile)
                            # print(destfile)
                            shutil.move(sourcefile, destfile)
                            logger.info('Hided:  ' + sourcefile + " to " + destfile)


        if (type == "VST"):
            logger.info('--Hided VST Plugins--')
            root = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
            root_backup = "/Library/Audio/Plug-Ins/Unused/VST"
            root_mono = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/Mono"
            root_mono_backup = "/Library/Audio/Plug-Ins/Unused/VST/Mono"

            for i in range(0, self.tableWidget_hide.rowCount()):
                combo = self.tableWidget_hide.cellWidget(i, 1)
                print(combo.currentText())
                if (combo.currentText() == "Hidden"):
                    self.tableWidget_hide.setCurrentCell(i, 0)
                    curItem = self.tableWidget_hide.currentItem()
                    # print(curItem.text())
                    caminho = root + '_' + "\\" + str(curItem.text())
                    # print(caminho)
                    for file in os.listdir(root):
                        if fnmatch.fnmatch(file, curItem.text() + ".*"):
                            sourcefile = root + "/" + str(file)
                            destfile = root_backup + "/" + str(file)
                            # print(sourcefile)
                            # print(destfile)
                            shutil.move(sourcefile, destfile)
                            logger.info('Hided:  ' + sourcefile + " to " + destfile)
                    for file in os.listdir(root_mono):
                        if fnmatch.fnmatch(file, curItem.text() + "(m).*"):
                            sourcefile = root_mono + "/" + str(file)
                            destfile = root_mono_backup + "/" + str(file)
                            # print(sourcefile)
                            # print(destfile)
                            shutil.move(sourcefile, destfile)
                            logger.info('Hided:  ' + sourcefile + " to " + destfile)


        # print(self.tabWidget.currentIndex())
        #popula_tab(self, type, fname)
        #popula_hide_tab(self, type, fname)
        return 1

def Reset_all(self, type,fname):
    # Move the Hided to Unsused folder.
    #popula_hide_tab(self,"PT")
    #popula_hide_tab(self, "Logic")
    #popula_hide_tab(self, "VST")
    self.tabWidget.currentIndex = 1

    if (type == "PT"):

        root_backup = "/Library/Application Support/Avid/Audio/Unused/"
        root = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
        logger.info('--Showed AU Plugins--')
        for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, "*.*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)

    if (type == "Logic"):
        root_backup = "/Library/Audio/Plug-Ins/Unused/Components"
        root = "/Library/Audio/Plug-Ins/Components"
        logger.info('--Showed AU Plugins--')
        for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, "*.*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)


    if (type == "VST"):

        root_backup = "/Library/Audio/Plug-Ins/Unused/VST"
        root = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
        root_mono_backup = "/Library/Audio/Plug-Ins/Unused/VST/Mono"
        root_mono = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/Mono"

        logger.info('--VST AU Plugins--')
        for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, "*.*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)
        for file in os.listdir(root_mono_backup):
                    if fnmatch.fnmatch(file, "*.*"):
                        sourcefile = root_mono + "/" + str(file)
                        destfile = root_mono_backup + "/" + str(file)
                        #print(sourcefile)
                        #print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)



    # print(self.tabWidget.currentIndex())
    self.tabWidget.currentIndex = 0
    #popula_tab(self, type)
    #popula_hide_tab(self, type)
    #self.tabWidget.currentIndex = 0
    return 1

def UnHide_all(self, type,fname):
    # Move the Hided to Unsused folder.
    #popula_hide_tab(self,"PT")
    #popula_hide_tab(self, "Logic")
    #popula_hide_tab(self, "VST")
    self.tabWidget.currentIndex = 1

    if (type == "PT"):

        root_backup = "/Library/Application Support/Avid/Audio/Unused/"
        root = "/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/"
        logger.info('--Showed AU Plugins--')
        for i in range(0, self.tableWidget_hide.rowCount()):
            combo = self.tableWidget_hide.cellWidget(i, 1)


            if (combo.currentText() != "All"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)

    if (type == "Logic"):
        root_backup = "/Library/Audio/Plug-Ins/Unused/Components"
        root = "/Library/Audio/Plug-Ins/Components"
        logger.info('--Showed AU Plugins--')
        self.tabWidget.currentIndex = 1
        #print(self.tableWidget_hide.rowCount())
        for i in range(0, self.tableWidget_hide.rowCount()):

            combo = self.tableWidget_hide.cellWidget(i, 1)
            if (combo.currentText() != "All"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)


    if (type == "VST"):

        root_backup = "/Library/Audio/Plug-Ins/Unused/VST"
        root = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/"
        root_mono_backup = "/Library/Audio/Plug-Ins/Unused/VST/Mono"
        root_mono = "/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/Mono"

        logger.info('--VST AU Plugins--')
        for i in range(0, self.tableWidget_hide.rowCount()):
            combo = self.tableWidget_hide.cellWidget(i, 1)
            if (combo.currentText() != "All"):
                self.tableWidget_hide.setCurrentCell(i, 0)
                curItem = self.tableWidget_hide.currentItem()
                # print(curItem.text())
                caminho = root + '_' + "\\" + str(curItem.text())
                # print(caminho)
                for file in os.listdir(root_backup):
                    if fnmatch.fnmatch(file, curItem.text() + ".*"):
                        sourcefile = root + "/" + str(file)
                        destfile = root_backup + "/" + str(file)
                        # print(sourcefile)
                        # print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)
                for file in os.listdir(root_mono_backup):
                    if fnmatch.fnmatch(file, curItem.text() + "(m).*"):
                        sourcefile = root_mono + "/" + str(file)
                        destfile = root_mono_backup + "/" + str(file)
                        #print(sourcefile)
                        #print(destfile)
                        shutil.move(destfile, sourcefile)
                        logger.info('Showed:  ' + destfile + " to " + sourcefile)



    # print(self.tabWidget.currentIndex())
    self.tabWidget.currentIndex = 0
    #popula_tab(self, type)
    #popula_hide_tab(self, type)
    #self.tabWidget.currentIndex = 0
    return 1


def popula_all(self,fname,type):
    if type == "imported":
        popula_tab(self, "PT",fname)
        popula_hide_tab(self, "PT",fname)
        UnHide_all(self, "PT",fname)
        by_imported_file(self, "PT",fname)
        popula_tab(self, "VST",fname)
        popula_hide_tab(self, "VST",fname)
        UnHide_all(self, "VST",fname)
        by_imported_file(self, "VST",fname)
        popula_tab(self, "Logic",fname)
        popula_hide_tab(self, "Logic",fname)
        UnHide_all(self, "Logic",fname)
        by_imported_file(self, "Logic",fname)

    if type == "Login":
        popula_tab(self, "PT", fname)
        popula_hide_tab(self, "PT", fname)
        UnHide_all(self, "PT", fname)
        by_imported_file(self, "PT", fname)
        popula_tab(self, "VST", fname)
        popula_hide_tab(self, "VST", fname)
        UnHide_all(self, "VST", fname)
        by_imported_file(self, "VST", fname)
        popula_tab(self, "Logic", fname)
        popula_hide_tab(self, "Logic", fname)
        UnHide_all(self, "Logic", fname)
        by_imported_file(self, "Logic", fname)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        global logger
        logger = logging.getLogger('myapp')
        hdlr = logging.FileHandler('/var/tmp/myapp.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
        logger.info('\n------------------------------------------------------------------------------')
        logger.info('App Initalized')


        Dialog.setObjectName("Dialog")



        Dialog.resize(867, 500)
        Dialog.setMinimumSize(QtCore.QSize(867, 500))
        Dialog.setMaximumSize(QtCore.QSize(867, 500))
        Dialog.setAutoFillBackground(False)

        self.currentversion = "2.3"
        self.csv_version = "1.1"
        self.uad_version = "9.4.1"


        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(7, 100, 851, 311))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        p = Dialog.palette()
        p.setColor(Dialog.backgroundRole(), QtCore.Qt.black)
        Dialog.setPalette(p)



        #pixmap = QPixmap(resource_path("uad.jpg"))
        #label.setPixmap(pixmap)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 22, 100, 60))
        self.label.setPixmap(QtGui.QPixmap(resource_path("uad.jpg")))

        #self.label_7 = QLabel(Dialog)
        #self.label_7.setGeometry(QtCore.QRect(25, 400, 100, 60))
        #self.label_7.setPixmap(QtGui.QPixmap(resource_path("uad.jpg")))
        #self.label_7.setOpenExternalLinks(True)


        #logger.info(resource_path("uad.jpg"))
        #print(resource_path("uad.jpg"))

        directory = "/Library/Audio/Plug-Ins/Unused/Components"
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory = "/Library/Application Support/Avid/Audio/Unused"
        if not os.path.exists(directory):
            os.makedirs(directory)

        directory = "/Library/Audio/Plug-Ins/Unused/VST"
        if not os.path.exists(directory):
            os.makedirs(directory)

        directory = "/Library/Audio/Plug-Ins/Unused/VST/Mono"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Optional, resize window to image size
        #self.resize(pixmap.width(), pixmap.height())s


        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(15, 50, 115, 86))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 21, 99, 65))
        self.groupBox.setStyleSheet("background-color: rgb(0, 0, 0);\n" "color: rgb(255, 255, 255);\n" "font: 12pt \"MS Shell Dlg 2\";")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"MS Shell Dlg 2\";")
        #self.radioButton_3.setDisabled(1)
        #self.groupBox.setDisabled(1)
        self.groupBox.setHidden(1)




        # self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        # self.tabWidget_2.setGeometry(QtCore.QRect(560, 25, 300, 111))
        # self.tabWidget_2.setSizeIncrement(QtCore.QSize(0, 0))
        # self.tabWidget_2.setBaseSize(QtCore.QSize(0, 0))
        # self.tabWidget_2.setAutoFillBackground(False)
        # self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        # self.tabWidget_2.setIconSize(QtCore.QSize(16, 16))
        # self.tabWidget_2.setMovable(False)
        # self.tabWidget_2.setObjectName("tabWidget_2")
        # self.tab_4 = QtWidgets.QWidget()
        # self.tab_4.setObjectName("tab_4")
        # self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        # self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 291))
        # self.tableWidget_2.setObjectName("tableWidget_4")
        # self.tableWidget_2.setColumnCount(0)
        # self.tableWidget_2.setRowCount(0)
        # self.tabWidget_2.addTab(self.tab_4, "")
        # self.tableWidget_2.setStyleSheet("background-color: rgb(50, 50, 50);")
        # self.tab_3 = QtWidgets.QWidget()
        # self.tab_3.setObjectName("tab_3")
        # self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        # self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 291))
        # self.tableWidget_2.setObjectName("tableWidget_2")
        # self.tableWidget_2.setColumnCount(0)
        # self.tableWidget_2.setRowCount(0)
        # self.tableWidget_2.setStyleSheet("background-color: rgb(50, 50, 50);")
        # self.tabWidget_2.addTab(self.tab_3, "")







        # self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        # self.pushButton_3.setGeometry(QtCore.QRect(210, 56, 75, 23))
        # self.pushButton_3.setObjectName("pushButton_2")
        # # self.pushButton_3.setToolTip('Login')
        # self.pushButton_3.clicked.connect(self.on_click_login)
        # self.pushButton_3.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")
        #
        # self.user = QtWidgets.QLineEdit(Dialog)
        # self.user.setGeometry(QtCore.QRect(105, 15, 180, 17))
        # self.user.setObjectName("User")
        # self.password = QtWidgets.QLineEdit(Dialog)
        # self.password.setGeometry(QtCore.QRect(105, 35, 180, 17))
        # self.password.setObjectName("Pass")
        # self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(33, 4, 60, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(90)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(33, 23, 60, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(90)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_3")


        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 850, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tableWidget_hide = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_hide.setGeometry(QtCore.QRect(0, 0, 850, 291))
        self.tableWidget_hide.setObjectName("tableWidget1")
        self.tableWidget_hide.setColumnCount(2)
        self.tableWidget_hide.setRowCount(0)

        self.radioButton_2.click()
        if self.radioButton.isChecked():
            type = "PT"
        if self.radioButton_2.isChecked():
            type = "Logic"

        if self.radioButton_3.isChecked():
            type = "VST"

        #self.tableWidget = QtWidgets.QTableWidget(self.tab)
        #self.textEdit = QTextEdit()
        #self.ter =
        #self.setCentralWidget(self.textEdit)
        #self.statusBar()
        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialog)

        #self.showDialog
        popula_branco(self,"Logic")
        self.tabWidget.setDisabled(1)

        #popula_all(self)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 30, 450, 41))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(90)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(605, 23, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(90)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_3")



        # self.label_11 = QtWidgets.QLabel(Dialog)
        # self.label_11.setGeometry(QtCore.QRect(210, 50, 550, 41))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(90)
        # self.label_11.setFont(font)
        # self.label_11.setStyleSheet("color: red;")
        # self.label_11.setObjectName("label_3")
        #
        # self.label_12 = QtWidgets.QLabel(Dialog)
        # self.label_12.setGeometry(QtCore.QRect(427, 90, 550, 41))
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # font.setBold(True)
        # font.setWeight(90)
        # self.label_12.setFont(font)
        # self.label_12.setStyleSheet("color: red;")
        # self.label_12.setObjectName("label_3")


        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(660, 470, 600, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(128, 128, 128);")
        self.label_5.setObjectName("label_4")




        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 420, 400, 21))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setToolTip('Backup Plugin Folder to your Desktop')
        self.pushButton.clicked.connect(self.on_click)
        #self.pushButton.setStyleSheet("background - color: qlineargradient(spread:pad, x1: 0.5, y1: 1, x2: 0.5, y2: 0, stop: 0.350282 rgba(0, 0, 255, 255), stop: 1 rgba(192, 199, 255, 255));")
        self.pushButton.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(715, 49, 135, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.setToolTip('Open UADSystemProfile')
        self.pushButton_2.clicked.connect(self.on_click_openfile)
        self.pushButton_2.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(715, 90, 105, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        #self.pushButton_5.setToolTip('Open UADSystemProfile')
        self.pushButton_5.clicked.connect(self.on_click_reset)
        self.pushButton_5.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")


        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(825, 90, 25, 25))
        self.pushButton_4.setObjectName("pushButton_2")
        #self.pushButton_4.setToolTip('Open UADSystemProfile')
        self.pushButton_4.clicked.connect(self.PopUpVersion_help)
        self.pushButton_4.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")



        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(750, 420, 70, 21))
        self.pushButton1.setObjectName("pushButton")
        #self.pushButton1.setToolTip('Apply')
        self.pushButton1.clicked.connect(self.on_click_Apply)
        self.pushButton1.setText("Apply")
        self.pushButton1.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(70, 70, 70), stop:1 rgb(100,103,109));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")
        #self.pushButton1.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")
        self.pushButton1.setDisabled(1)

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(37, 90, 135, 21))
        self.pushButton_8.setObjectName("pushButton")
        self.pushButton_8.clicked.connect(self.on_click_check_version_sftp)
        self.pushButton_8.setText("Check for Updates")
        #self.pushButton_8.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(70, 70, 70), stop:1 rgb(100,103,109));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")
        self.pushButton_8.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")



        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(18, 447, 630, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_4.setObjectName("label_4")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 473, 630, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(128, 128, 128);")
        self.label_8.setObjectName("label_4")
        self.label_8.setText("Contribute if it helped you!")


        #self.pushButton.clicked.connect(self.on_click)
        self.radioButton_2.clicked.connect(self.radio_LOGIC_click)
        self.radioButton.clicked.connect(self.radio_PT_click)
        self.radioButton_3.clicked.connect(self.radio_VST_click)

        self.pushButton6 = QtWidgets.QPushButton(Dialog)
        self.pushButton6.setGeometry(QtCore.QRect(10, 467, 120, 30))
        self.pushButton6.setObjectName("pushButton")
        self.pushButton6.setToolTip('Donate')
        self.pushButton6.clicked.connect(self.on_click_Donate)
        self.pushButton6.setText("")
        self.pushButton6.setIcon(QtGui.QIcon(resource_path("donate.jpg")))
        self.pushButton6.setIconSize(QtCore.QSize(120, 150))
        #self.label.setPixmap(QtGui.QPixmap(resource_path("uad.jpg")))













        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)










    def showdialog():
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hide & Seek UAD Plugins"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog",   " Authorized / Demo  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", " Not Authorized     "))
        #self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Dialog", "    By UAD Login    "))
        #self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Dialog", "By UADSystemProfile "))
        self.label_3.setText(_translate("Dialog", "Hide & Seek UAD Plugins"))
        self.label_7.setText(_translate("Dialog", "V2.3"))

        #self.label_9.setText(_translate("Dialog", "UAD User"))
        #self.label_10.setText(_translate("Dialog", "Password"))
        #self.label_11.setText(_translate("Dialog", "Please Choose one the Following Methods to Retreive Your Plugins"))
        #self.label_12.setText(_translate("Dialog", "OR"))
        self.pushButton.setText(_translate("Dialog", 'Backup all Plugin Folders "/Users"     (This can take a while)'))
        self.pushButton1.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "Open \nUADSystemProfile"))
        #self.pushButton_3.setText(_translate("Dialog", "Login"))
        self.pushButton_4.setText(_translate("Dialog", "?"))
        self.pushButton_5.setText(_translate("Dialog", "Reset All"))

        self.label_4.setText(_translate("Dialog", " "))
        self.groupBox.setTitle(_translate("Dialog", "Plugin Type"))
        self.radioButton_2.setText(_translate("Dialog", "Logic - AU"))
        self.radioButton.setText(_translate("Dialog", "ProTools - AAX"))
        self.radioButton_3.setText(_translate("Dialog", "Others - VST"))
        self.label_5.setText(_translate("Dialog", "Logs at /var/tmp/myapp.log"))
        #self.label_5.setText("sdf")



    #@pyqtSlot()
    def on_click(self):
        temp = 0
        if os.path.exists('/Library/Audio/Plug-Ins/Components/'):
            result =  backupToZip('/Library/Audio/Plug-Ins/Components/',"Component")
        if os.path.exists('/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/'):
            result1 = backupToZip('/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/',"VST")
        if os.path.exists('/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/'):
            result2 = backupToZip('/Library/Application Support/Avid/Audio/Plug-Ins/Universal Audio/', "aax")
        if os.path.exists('/Library/Audio/Plug-Ins/VST/Powered Plug-Ins/'):
            result3 = backupToZip('/Library/Application Support/Digidesign/Plug-Ins/Universal Audio/', "dpm")

        self.label_4.setText('Backup done in folder /Users/ ! ' )

    def on_click_openfile(self):
        #fname = QFileDialog.getOpenFileName()
        fname = ""
        dir = sys.argv[1]
        filters = "Text files (*.txt);;UAD File (*.txt)"
        selected_filter = "UAD File (*.txt)"
        options = " "
        fname = QFileDialog.getOpenFileName(Dialog, " File dialog ", dir, filters, selected_filter)
        if fname[0] != "":
            result_format = check_fileformat(self, type, fname)
            print("adsd")
            print(result_format)
            if result_format == 1:
                self.PopUpFileFormat()
            if result_format != 1:
                result = check_version(self, type, fname)
                print(result)
                if result == 1:
                    self.PopUpVersion()
                if result != 1:
                    popula_all(self,fname,"imported")
                    self.tabWidget.setDisabled(0)
                    self.pushButton1.setDisabled(0)
                    self.pushButton1.setStyleSheet("color: rgb(255,255,255);" "background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.150282 rgb(21, 123, 255), stop:1 rgb(118,183,249));" "border-style: solid;" "border-color: rgb(70, 70, 70) ;" "border-width: 0px;" "border-radius: 7px;")
                    self.label_4.setText("File Format OK! ")

    def on_click_reset(self):
        fname = "reset"
        Reset_all(self, "PT",fname)
        Reset_all(self, "VST",fname)
        Reset_all(self, "Logic",fname)
        self.label_4.setText("Reset OK! All Plugins Back. ")




    def on_click_login(self):
        print("login")

    def radio_VST_click(self):
        logger.info('VST Plugin Type Selected')
        type = "VST"
        popula_tab(self,type)
        popula_hide_tab(self,type)
        by_imported_file(self, type)

    def radio_PT_click(self):
        logger.info('ProTools Plugin Type Selected')
        type = "PT"
        popula_tab(self,type)
        popula_hide_tab(self,type)
        by_imported_file(self, type)

    def radio_LOGIC_click(self):
        logger.info('AU(Logic) Plugin Type Selected')
        type = "LOGIC"
        popula_tab(self,type)
        popula_hide_tab(self,type)
        by_imported_file(self, type)



    def on_click_check_version_sftp(self):
            check_version_sftp(self)
            #self.label_4.setText("Done! Please re-open your DAW and if needed, re-scan you Plugins! ")



    def on_click_Apply(self,fname):
            if self.radioButton.isChecked():
                type = "PT"


            if self.radioButton_2.isChecked():
                type = "Logic"
            if self.radioButton_3.isChecked():
                type = "VST"

            Hide_new(self,"Logic",fname)
            Hide_new(self,"PT",fname)
            Hide_new(self,"VST",fname)
            self.label_4.setText("Done! Please re-open your DAW and if needed, re-scan you Plugins! ")






    def PopUpVersion(self):


        name = "\n   This App was Designed to work with UAD Software Version 9.4.1\n   Please wait for new release.\n   You can contact Daniel (dcarneiro@hotmail.com) about it.\n   Program will close."
        self.exPopup = examplePopup(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
        x = widget.left() + ((widget.right() - widget.left())/2) - 207
        #x = widget
        #y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 415, 95)

        self.exPopup.setWindowModality(Qt.ApplicationModal)
        self.exPopup.show()

    def PopUpFileFormat(self):
        name = "\n   This file seems not correct. Please export you Plugins. \n   Go to UAD Control Panel -> Save Detailed System Profile."
        self.exPopup = examplePopup_help(name)
        self.exPopup.setGeometry(500, 300, 450, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
        x = widget.left() + ((widget.right() - widget.left())/2) - 207
        #x = widget
        #y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 385, 60)

        self.exPopup.setWindowModality(Qt.ApplicationModal)
        self.exPopup.show()





    def PopUpVersion_CSV_Update(self):

        name = "\n   To export you Plugins, go to UAD Control Panel -> Save Detailed System Profile"
        self.exPopup = examplePopup_help(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
        x = widget.left() + ((widget.right() - widget.left())/2) - 207
        #x = widget
        #y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 504, 50)

        self.exPopup.setWindowModality(Qt.ApplicationModal)
        self.exPopup.show()





    def PopUpVersion_help(self):


        name = "\n   To export you Plugins, go to UAD Control Panel -> Save Detailed System Profile"
        self.exPopup = examplePopup_help(name)
        self.exPopup.setGeometry(500, 300, 415, 55)
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        widget = Dialog.geometry()
        # x = screen.width() - widget.width()
        # y = screen.height() - widget.height()
        y = widget.top() + ((widget.bottom() - widget.top())/2) - 50
        x = widget.left() + ((widget.right() - widget.left())/2) - 207
        #x = widget
        #y = screen.height() - widget.height()
        self.exPopup.setGeometry(x, y, 504, 50)

        self.exPopup.setWindowModality(Qt.ApplicationModal)
        self.exPopup.show()




    def on_click_Donate(self):
        url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8QLLW4HLB433J'
        if sys.platform == 'darwin':  # in case of OS X
            subprocess.Popen(['open', url])

    def location_on_the_screen(self):
        screen = QDesktopWidget().screenGeometry()
        geometry = Dialog.saveGeometry()
        x = screen.width() - Dialog.width()
        y = screen.height() - Dialog.height()
        #self.move(x, y)
        #Dialog.move(50, 450)
        #print(x)
        #print(y)



class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI1()
        self.setGeometry(700, 120, 100, 100)
        self.resize(867, 500)




    def initUI1(self):
        lblName = QLabel(self.name, self)

    def closeEvent(self, event):
        sys.exit()

class examplePopup_help(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI1()
        self.setGeometry(700, 120, 100, 100)
        self.resize(867, 500)




    def initUI1(self):
        lblName = QLabel(self.name, self)





if __name__ == '__main__':


    GUI = 0
    string = resource_path("main")

    if GUI != 1:
        if platform.system() == 'Darwin':
            try:
               os.setuid(0)
            except OSError:
               dir_path = os.path.dirname(os.path.realpath(__file__))
               string = string.replace(" ","\\\ ")
               string = string.replace("&","\\\&")
               path_original = string
               #path_original = path_original.replace('Hide\\\ \\\&\\\ Seek\\\ UAD\\\ Plugins.app/Contents/MacOS/main','')
               path_original = path_original[:-57]
               path_original = expanduser("~/Desktop")


               applescript = ('do shell script "' + string + ' ' + path_original +'" ' 'with administrator privileges')
               print(applescript)
               #print("-----")
               print(path_original)
               exit_code = subprocess.Popen(['osascript','-e',applescript],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               sys.exit(exit_code)

    #print(resource_path("main"))

    logger1 = logging.getLogger('myapp')
    hdlr1 = logging.FileHandler('/var/tmp/myapp.log')
    formatter1 = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr1.setFormatter(formatter1)
    logger1.addHandler(hdlr1)
    logger1.setLevel(logging.INFO)
    logger1.info('Path Original')
    logger1.info(sys.argv[1])

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.location_on_the_screen()
    Dialog.show()

    sys.exit(app.exec_())

#     build
#     rm -rf ./build; rm -rf ./dist/; pyinstaller --onedir --windowed --icon=HideSeek.icns main.py; cp uad.jpg ./dist/main.app/Contents/MacOS/; cp donate.jpg ./dist/main.app/Contents/MacOS/; cp current_version.txt ./dist/main.app/Contents/MacOS/ ;cp final.csv ./dist/main.app/Contents/MacOS/; mv ./dist/main.app/ ./dist/Hide\ \&\ Seek\ UAD\ Plugins.app/
