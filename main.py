import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QFileDialog, QGraphicsDropShadowEffect
from ux import main_ux, file_frame, chostata_item_ux, file_item_ux, yondosh_word_ux
from pdfminer.high_level import extract_text
from docx import Document
from libs.Loading import LoadingScreen
class FileFrame(QFrame, file_frame.Ui_Frame):
    def __init__(self, name):
        super(FileFrame, self).__init__()
        self.setupUi(self)
        self.file_name.setText(name)

        effect = QGraphicsDropShadowEffect()

        effect.setOffset(0, 0)

        effect.setBlurRadius(8)

        self.setGraphicsEffect(effect)


class ChostataItem(QFrame, chostata_item_ux.Ui_Frame):
    def __init__(self, word, count):
        super(ChostataItem, self).__init__()
        self.setupUi(self)
        self.label_word.setText(word)
        self.label_word_count.setText(str(count))
        effect = QGraphicsDropShadowEffect()

        effect.setOffset(0, 0)

        effect.setBlurRadius(5)

        self.setGraphicsEffect(effect)


class FileItem(QFrame, file_item_ux.Ui_Frame):
    def __init__(self, word, count, file):
        super(FileItem, self).__init__()
        self.setupUi(self)
        self.label_word.setText(word)
        self.label_word_count.setText(str(count))
        self.label_file.setText(file)
        effect = QGraphicsDropShadowEffect()

        effect.setOffset(0, 0)

        effect.setBlurRadius(5)

        self.setGraphicsEffect(effect)


class YondoshWord(QFrame, yondosh_word_ux.Ui_Frame):
    def __init__(self, word, word_before, word_after):
        super(YondoshWord, self).__init__()
        self.setupUi(self)
        self.label_word.setText(word)
        self.label_word_before.setText(word_before)
        self.label_word_after.setText(word_after)
        effect = QGraphicsDropShadowEffect()

        effect.setOffset(0, 0)

        effect.setBlurRadius(5)

        self.setGraphicsEffect(effect)


class Main(QMainWindow, main_ux.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        try:
            # self.loading = LoadingScreen(self)
            # self.loading_timer = QtCore.QTimer()
            # self.loading_timer.setInterval(500)
            # self.loading_timer.timeout.connect(self.loadingAmimationActive)
            self.files = []
            self.effect = QGraphicsDropShadowEffect()
            self.stackedWidget.setCurrentWidget(self.page_file_upload)
            self.tabWidget.setCurrentWidget(self.tab)
            self.effect.setOffset(0, 0)
            self.effect.setBlurRadius(8)
            self.frame.setGraphicsEffect(self.effect)
            self.verticalLayout_side = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
            self.verticalLayout_right = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            self.verticalLayout_chostata = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
            self.verticalLayout_file = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
            self.verticalLayout_yondosh = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
            self.upload_btn.clicked.connect(self.open_file)
            self.next_btn.clicked.connect(self.next_window_open)
            self.return_file_upload.clicked.connect(self.return_file_upload_window)
            self.search_btn.clicked.connect(self.search_word)
        except Exception as err:
            QtWidgets.QMessageBox.about(self, "Info", f'{err}')

    # def loadingAmimationActive(self):
    #     self.loading.startAnimation()
    #     self.loading_timer.stop()

    def search_word(self):
        word = self.lineEdit.text()
        word = word.lower()
        additional_words = ['']
        total_text = ""
        if word != "":
            file_data = []
            # self.loading_timer.start()
            # self.loading.startAnimation()
            for file in self.files:
                if file.endswith(".pdf"):
                    text = extract_text(file)
                    text = text.lower()
                    dt = {
                        "file": file.split("/")[-1],
                        "count": text.count(word),
                        "word": word
                    }
                    file_data.append(dt)
                    total_text += "\n" + text
                elif file.endswith(".docx"):
                    text_doc = ""
                    document = Document(file)
                    for parag in document.paragraphs:
                        print(parag)
                        text_doc += "\n"+parag.text
                    text_doc = text_doc.lower()
                    print(text_doc)
                    dt = {
                        "file": file.split("/")[-1],
                        "count": text_doc.count(word),
                        "word": word
                    }
                    file_data.append(dt)
                    total_text += "\n" + text_doc

            chostata, data_yondosh = self.checking_text(total_text, word)

            self.remove_items(self.verticalLayout_chostata)
            self.remove_items(self.verticalLayout_file)
            self.remove_items(self.verticalLayout_yondosh)
            self.set_chostata_items(chostata)
            self.set_file_items(file_data)
            self.set_yondosh_word(data_yondosh)
            # self.loading.stopAnimation()
            # self.loading_timer.stop()

    def checking_text(self, text, word):
        text = text.lower()
        word = word.lower()
        list_text = text.split()
        data_yondosh = []
        # list_sings = ['.', ',', ':', ';', "?", '[', ']', "{", "}", ')', '(','!', '@', '#', '$', '%', '&', '*']
        list_word = []
        i = 0
        for txt in list_text:
            if txt.startswith(word):
                if txt not in list_word:
                    list_word.append(txt)
                if i == 0 and i < len(list_text):
                    dt = {
                        "word_before": "",
                        "word": txt,
                        "word_after": list_text[i + 1]

                    }
                    data_yondosh.append(dt)

                elif i > 0 and i+1 < len(list_text):
                    dt = {
                        "word_before": list_text[i - 1],
                        "word": txt,
                        "word_after": list_text[i + 1]
                    }
                    data_yondosh.append(dt)

                elif len(list_text) - 1 == i:
                    dt = {
                        "word_before": list_text[i - 1],
                        "word": txt,
                        "word_after": ""
                    }
                    data_yondosh.append(dt)
            i += 1

        chastota = []
        for w in list_word:
            cn = text.count(w)
            dt = {
                "word": w,
                "count": cn
            }
            chastota.append(dt)

        return chastota, data_yondosh

    def open_file(self):
        path = QFileDialog.getOpenFileNames(self, 'Open a file', '',
                                            'Files (*.pdf;*.docx)')
        if path != ('', ''):
            self.remove_widgets()
            self.layout_set_widget(path[0])

    def next_window_open(self):
        if len(self.files) > 0:
            self.remove_files_side()
            self.set_files_side()
            self.stackedWidget.setCurrentWidget(self.page_main)

    def return_file_upload_window(self):
        self.stackedWidget.setCurrentWidget(self.page_file_upload)

    def set_files_side(self):
        for name in self.files:
            v = FileFrame(name.split("/")[-1])
            self.verticalLayout_side.addWidget(v)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_side.addItem(spacerItem)

    def remove_widgets(self):
        self.files = []
        for i in reversed(range(self.verticalLayout_right.count())):
            w = self.verticalLayout_right.itemAt(i).widget()
            self.verticalLayout_right.removeWidget(w)

    def remove_files_side(self):
        for i in reversed(range(self.verticalLayout_side.count())):
            w = self.verticalLayout_side.itemAt(i).widget()
            self.verticalLayout_side.removeWidget(w)

    def layout_set_widget(self, names):
        self.files = names
        for name in names:
            v = FileFrame(name.split("/")[-1])
            self.verticalLayout_right.addWidget(v)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_right.addItem(spacerItem)

    def set_chostata_items(self, data):
        for dt in data:
            v = ChostataItem(dt['word'], dt['count'])
            self.verticalLayout_chostata.addWidget(v)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_chostata.addItem(spacerItem)

    def remove_items(self, layout):
        for i in reversed(range(layout.count())):
            w = layout.itemAt(i).widget()
            layout.removeWidget(w)

    def set_file_items(self, data):
        for dt in data:
            v = FileItem(dt['word'], dt['count'], dt['file'])
            self.verticalLayout_file.addWidget(v)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_file.addItem(spacerItem)

    def set_yondosh_word(self, data):
        for dt in data:
            v = YondoshWord(dt['word'], dt['word_before'], dt['word_after'])
            self.verticalLayout_yondosh.addWidget(v)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_yondosh.addItem(spacerItem)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())
