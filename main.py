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
import zipfile, os
import csv
import shutil
import fnmatch
import time
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
        while j < 4:
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

def by_imported_file(self,type):
    with open('/Users/carneiro/Downloads/UAD/final.csv', 'r') as f:
        # reader = csv.reader(f)
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        all_plugins_list = list(reader)

    # print(all_plugins_list[2][0])

    with open('/Users/carneiro/Downloads/UAD/UADSystemProfile.txt', 'r') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        array_my_plugins_temp = list(reader)

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

    #print(array_matched_plugins)


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
    self.tableWidget.setColumnWidth(0, 600)
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
        # print(i)
        temp1 = temp1 + 1
        if (os.path.join(root, i)):
            # print(i)
            i = re.sub(extension, '', i)
            combo = QtWidgets.QComboBox();
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            item = QtWidgets.QTableWidgetItem('UAD')
            item.setText(i)
            self.tableWidget.setItem(temp1 - 1, 0, item)
            combo_box_options = setcombo(self, combo_box_options, array_matched_plugins, i)
            for t in combo_box_options:
                #print(i)
                combo.addItem(t)

            self.tableWidget.setCellWidget(temp1 - 1, 1, combo)
    logger.info('Shown tab Populed')


def popula_hide_tab(self,type):
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
    self.tableWidget_hide.setColumnWidth(0, 600)
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

def popula_tab(self,type):
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
        self.tableWidget.setColumnWidth(0, 600)
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

def Hide(self, type):
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
    popula_tab(self, type)
    popula_hide_tab(self, type)
    return 1

def UnHide_all(self, type):
    # Move the Hided to Unsused folder.
    #popula_hide_tab(self,"PT")
    #popula_hide_tab(self, "Logic")
    #popula_hide_tab(self, "VST")
    self.tabWidget.currentIndex = 1
    #print(self.tableWidget_hide.rowCount())

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
    #self.tabWidget.currentIndex = 0
    #popula_tab(self, type)
    #popula_hide_tab(self, type)
    #self.tabWidget.currentIndex = 0
    return 1

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



        Dialog.resize(767, 470)
        Dialog.setMinimumSize(QtCore.QSize(767, 470))
        Dialog.setMaximumSize(QtCore.QSize(767, 470))
        Dialog.setAutoFillBackground(False)
        #Dialog.setStyleSheet("border-image:url(./uad.jpg);\n""")
        self.cb = QtWidgets.QComboBox()
        self.cb.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        #self.cb.currentIndexChanged.connect(self.selectionchange)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(5, 60, 761, 311))
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
        self.label.setGeometry(QtCore.QRect(25, 12, 100, 60))
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
        self.groupBox.setGeometry(QtCore.QRect(615, -1, 115, 86))
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



        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 751, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tableWidget_hide = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_hide.setGeometry(QtCore.QRect(0, 0, 751, 291))
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

        #popula_tab(self,type)
        #UnHide_all(self,"Logic")
        by_imported_file(self,"Logic")
        by_imported_file(self,"VST")
        by_imported_file(self,"PT")
        popula_tab(self, type)
        popula_hide_tab(self,type)
        UnHide_all(self, "Logic")
        UnHide_all(self, "VST")
        UnHide_all(self, "PT")
        by_imported_file(self,"Logic")
        by_imported_file(self,"VST")
        by_imported_file(self,"PT")
        popula_tab(self, type)
        popula_hide_tab(self,type)





        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(135, 10, 450, 41))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(90)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 10, 450, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(90)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_3")



        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(560, 440, 600, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(128, 128, 128);")
        self.label_5.setObjectName("label_4")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 380, 400, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip('Backup Plugin Folder to your Desktop')
        self.pushButton.clicked.connect(self.on_click)



        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(650, 380, 70, 30))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setToolTip('Apply')
        self.pushButton1.clicked.connect(self.on_click_Apply)
        self.pushButton1.setText("Apply")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 415, 630, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 443, 630, 16))
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
        self.pushButton6.setGeometry(QtCore.QRect(10, 437, 120, 30))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Currently Shown"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Currently Hidden"))
        self.label_3.setText(_translate("Dialog", "Hide & Seek UAD Plugins"))
        self.label_7.setText(_translate("Dialog", "V1.1"))
        self.pushButton.setText(_translate("Dialog", 'Backup alll Plugin Folders "/Users"     (This can take a while)'))
        self.pushButton1.setText(_translate("Dialog", "Apply"))
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


    def radio_VST_click(self):
        logger.info('VST Plugin Type Selected')
        type = "VST"
        popula_tab(self,type)
        popula_hide_tab(self,type)

    def radio_PT_click(self):
        logger.info('ProTools Plugin Type Selected')
        type = "PT"
        popula_tab(self,type)
        popula_hide_tab(self,type)

    def radio_LOGIC_click(self):
        logger.info('AU(Logic) Plugin Type Selected')
        type = "LOGIC"
        popula_tab(self,type)
        popula_hide_tab(self,type)

    def on_click_Apply(self):
            if self.radioButton.isChecked():
                type = "PT"
            if self.radioButton_2.isChecked():
                type = "Logic"
            if self.radioButton_3.isChecked():
                type = "VST"

            result = Hide(self,type)
            if result:
                if type == "Logic":
                    self.label_4.setText("Succeed! If need, in Logic, go to: Logic > Preferences > Plug-ins Manager > Reset & Rescan")
                    logger.info("Succeed! If need, in Logic, go to: Logic > Preferences > Plug-ins Manager > Reset & Rescan")
                if type == "PT":
                    logger.info("Succeed! If need, Please rescan your plugins inside ProTools")
                    self.label_4.setText("Succeed! If need, Please rescan your plugins inside ProTools")
                if type == "VST":
                    logger.info("Succeed! If need, Please rescan your plugins inside your DAW")
                    self.label_4.setText("Succeed! If need, Please rescan your plugins inside your DAW")

            if not result:
                self.label_4.setText("Failed!")


    def on_click_Donate(self):
        url = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8QLLW4HLB433J'
        if sys.platform == 'darwin':  # in case of OS X
            subprocess.Popen(['open', url])

if __name__ == '__main__':

    GUI = 1
    string = resource_path("main")

    if GUI != 1:
        if platform.system() == 'Darwin':
            try:
               os.setuid(0)
            except OSError:
               dir_path = os.path.dirname(os.path.realpath(__file__))
               string = string.replace(" ","\\\ ")
               string = string.replace("&","\\\&")
               applescript = ('do shell script "' + string + '" ' 'with administrator privileges')
               print(applescript)
               print(applescript)
               exit_code = subprocess.Popen(['osascript','-e',applescript],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               sys.exit(exit_code)

    #print(resource_path("main"))


    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

#     build
#     rm -rf ./build; rm -rf ./dist/; pyinstaller --onedir --windowed --icon=HideSeek.icns main.py; cp uad.jpg ./dist/main.app/Contents/MacOS/; cp donate.jpg ./dist/main.app/Contents/MacOS/; mv ./dist/main.app/ ./dist/Hide\ \&\ Seek\ UAD\ Plugins.app/

