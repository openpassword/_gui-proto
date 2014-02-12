import sys
# from openpassword_gui import Ui_MainWindow
from PySide import QtCore, QtGui, QtUiTools
from openpassword import AgileKeychain
from openpassword.exceptions import InvalidPasswordException


class OpenPasswordGUI(QtGui.QWidget):
    def __init__(self, keychain):
        super(OpenPasswordGUI, self).__init__(None)

        self.keychain = keychain

    def load_ui(self, loader, directory):
        self.main_ui = loader.load('{0}/op_main.ui'.format(directory))

        self.keychain_view = self._find_child_by_name('keychainWidget')
        self.lockscreen_view = self._find_child_by_name('lockScreenWidget')
        self.password_edit = self._find_child_by_name('passwordEdit')

        self.list_view = self._find_child_by_name('listView')
        self.list_view.activated.connect(self._item_selected)
        self.list_view.clicked.connect(self._item_selected)

        self.main_ui.actionUnlock.triggered.connect(self.unlock)
        self.main_ui.actionLock.triggered.connect(self.lock)

    def lock(self):
        self.password_edit.setText("")
        self.lockscreen_view.show()
        self.keychain_view.hide()
        self._clear_items()

    def unlock(self):
        password = self.password_edit.text()

        try:
            self.keychain.unlock(password)
            self.lockscreen_view.hide()
            self.keychain_view.show()
            self._get_items()
            self._show_items()
        except InvalidPasswordException:
            print("invalid password!")

    def _find_child_by_name(self, name):
        return self.main_ui.mainViewWidget.findChild(QtGui.QWidget, name)

    def _get_items(self):
        self._items = self.keychain.all_items()

    def _show_items(self):
        model = QtGui.QStandardItemModel()

        for item in self._items:
            qi = QtGui.QStandardItem()
            qi.setText(item.title)
            model.appendRow(qi)

        self.list_view.setModel(model)

    def _item_selected(self, index):
        unique_id = self._items[index.row()].uuid
        print(self.keychain.get_item_by_unique_id(unique_id))

    def _clear_items(self):
        self._items = []

    def run(self):
        self.main_ui.show()

        self.keychain_view.hide()
        self.lockscreen_view.show()
        # print(dir(keychain_widget))
        # self.main_ui.mainViewWidget.keychainWidget.hide()
        # self.main_ui.mainViewWidget.lockScreenWidget.show()


        # pw_edit = self.unlock_ui.passwordEdit
        # pw_edit.returnPressed.connect(self.on_password_edit_enter)

    @QtCore.Slot()
    def on_password_edit_enter(self):
        password = self.sender().text()





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    keychain = AgileKeychain('test.agilekeychain')

    op = OpenPasswordGUI(keychain)
    op.load_ui(QtUiTools.QUiLoader(), 'ui')
    op.run()

    sys.exit(app.exec_())
