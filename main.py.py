import os
import subprocess
from builtins import super
from subprocess import Popen
from tkinter import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor

import pygui2

class ExampleApp(QtWidgets.QMainWindow, pygui2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.treeWidget.setHeaderLabels(['Files'])
        self.treeWidget.setAlternatingRowColors(True)
        self.current_dir = ""
        self.selectBtn.clicked.connect(self.browse_folder)
        self.runBtn.clicked.connect(self.run_checked_tests)
        self.stopBtn.clicked.connect(self.stop_all_tests)
        self.clearBtn.clicked.connect(self.clear)
        self.refreshBtn.clicked.connect(self.print_logs)
        self.runBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.stopBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.selectBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.clearBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.file_types = {
            ".js": "node"
        }
        self.processes = []

        self.stopBtn.setStyleSheet(
            "background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.runBtn.setStyleSheet(
            "background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")

        self.clearBtn.setStyleSheet(
            "background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.selectBtn.setStyleSheet(
            "background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")

        self.refreshBtn.setStyleSheet(
            "background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")

    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder")
        if self.current_dir:
            self.treeWidget.clear()
            for file_name in os.listdir(self.current_dir):
                if file_name.endswith('js'):
                    item = QtWidgets.QTreeWidgetItem(self.treeWidget, [file_name])
                    item.setCheckState(0, QtCore.Qt.Unchecked)
                    print(file_name)

    def run_file_with(self, file_name):
        if not self.file_types:
            return ""
        for eof in self.file_types:
            if file_name.endswith(eof):
                return self.file_types[eof]
        return ""

    def find_checked(self):
        checked_items = list()
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            i_child = root.child(i)
            if i_child.checkState(0) == QtCore.Qt.Checked:
                checked_items.append(i_child.text(0))
        return checked_items

    def is_allowed_file(self, file_name):
        if not self.file_types:
            return True
        for eof in self.file_types:
            if file_name.endswith(eof):
                return True
        return False

    def generate_command_for_file_names(self, file_names):
        command_list = list(map(lambda file_name: f"{self.run_file_with(file_name)} {file_name}", file_names))
        return " && ".join(command_list)

    def run_checked_tests(self):
        checked_files = self.find_checked()
        if not checked_files:
            return ""
        run_command = self.generate_command_for_file_names(checked_files)
        process = subprocess.Popen(run_command, stdout=subprocess.PIPE, shell=True, cwd=self.current_dir)
        self.processes.append({"id": process.pid})
        self.runBtn.setEnabled(False)

    def print_logs(self):
        logger_file_path = self.current_dir + "/log/"
        for file in os.listdir(logger_file_path):
            if file.endswith(".log"):
                logger_file_full_path = logger_file_path + file
                with open(logger_file_full_path, "r") as logger_file:
                    self.listWidget.append(logger_file.read())

    def kill(self, proc_pid):
        Popen("TASKKILL /F /PID {pid} /T".format(pid=proc_pid))

    def clear(self):
        self.listWidget.clear()

    def stop_all_tests(self, proc_pid):
        exit_msg = "To stop press- yes, continue- press no?"
        resp = QtWidgets.QMessageBox.question(self, "save changes", exit_msg, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.No)
        if resp == QtWidgets.QMessageBox.Yes:
            for p in self.processes:
                self.kill(p["id"])
                self.runBtn.setEnabled(True)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()