#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QFileDialog,
                             QTextEdit, QMessageBox, QDialog, QVBoxLayout,
                             QLineEdit, QPushButton, QLabel, QHBoxLayout,
                             QInputDialog, QStyle)
from PyQt5.QtGui import QIcon, QTextCharFormat, QTextCursor, QColor, QFont
from PyQt5.QtCore import Qt

# Betiğin çalıştığı dizini al
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, 'Lintextor.png')

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Bul ve Değiştir")
        self.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()
        
        find_layout = QHBoxLayout()
        self.find_label = QLabel("Aranacak:")
        self.find_input = QLineEdit()
        find_layout.addWidget(self.find_label)
        find_layout.addWidget(self.find_input)
        
        replace_layout = QHBoxLayout()
        self.replace_label = QLabel("Değiştirilecek:")
        self.replace_input = QLineEdit()
        replace_layout.addWidget(self.replace_label)
        replace_layout.addWidget(self.replace_input)
        
        button_layout = QHBoxLayout()
        self.find_button = QPushButton("Bul")
        self.replace_button = QPushButton("Değiştir")
        self.replace_all_button = QPushButton("Tümünü Değiştir")
        self.close_button = QPushButton("Kapat")
        
        button_layout.addWidget(self.find_button)
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.replace_all_button)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(find_layout)
        layout.addLayout(replace_layout)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

        self.find_button.clicked.connect(self.find_clicked)
        self.replace_button.clicked.connect(self.replace_clicked)
        self.replace_all_button.clicked.connect(self.replace_all_clicked)
        self.close_button.clicked.connect(self.close)

        self.button_action = None
        self.update_texts()

    def update_texts(self):
        # Dil değişimine göre pencere metinlerini güncelle
        texts = self.parent.get_language_texts()['find_replace_dialog']
        self.setWindowTitle(texts['title'])
        self.find_label.setText(texts['find_label'])
        self.replace_label.setText(texts['replace_label'])
        self.find_button.setText(texts['find_button'])
        self.replace_button.setText(texts['replace_button'])
        self.replace_all_button.setText(texts['replace_all_button'])
        self.close_button.setText(texts['close_button'])

    # Eksik olan metodlar buraya eklendi
    def find_clicked(self):
        self.button_action = 'find'
        self.accept()
    
    def replace_clicked(self):
        self.button_action = 'replace'
        self.accept()
        
    def replace_all_clicked(self):
        self.button_action = 'replace_all'
        self.accept()

# Metinleri tutan sözlük
LANGUAGES = {
    'tr': {
        'title_new': 'Lintextor - Yeni Dosya',
        'file_dialog_title_open': 'Dosya Aç',
        'file_dialog_title_save': 'Farklı Kaydet',
        'file_filter': 'Metin Dosyaları (*.txt);;Tüm Dosyalar (*.*)',
        'file_error_title': 'Hata',
        'file_error_text': 'Dosya açılırken bir hata oluştu: {}',
        'save_error_text': 'Dosya kaydedilirken bir hata oluştu: {}',
        'save_prompt_title': 'Lintextor',
        'save_prompt_text': 'Değişiklikleri kaydetmek istiyor musunuz?',
        'find_input_title': 'Bul',
        'find_input_label': 'Aranacak metni girin:',
        'find_not_found_title': 'Bul',
        'find_not_found_text': '"{}" metni bulunamadı.',
        'replace_title': 'Değiştir',
        'replace_no_more_text': 'Başka eşleşme bulunamadı.',
        'replace_all_text': 'Tüm eşleşmeler değiştirildi.',
        'about_title': 'Hakkında: Lintextor',
        'about_text': """
        <h3>Lintextor Hakkında</h3>
        <p>Lisans: GNU GPLv3</p>
        <p>Programlama Dili: Python</p>
        <p>Arayüz: Qt</p>
        <p>Geliştirici: Aydın Serhat Kılıçoğlu</p>
        <p>Github: www.github.com/shampuan</p>
        <p>
            Bu program, linux sistemlerde windows uyumlu txt belgeleri oluşturur.
        </p>
        <p>Bu program hiçbir garanti getirmez.</p>
        """,
        'menu': {
            'file': 'Dosya',
            'edit': 'Düzen',
            'search': 'Ara',
            'help': 'Hakkında',
            'new': 'Yeni',
            'open': 'Aç...',
            'save': 'Kaydet',
            'save_as': 'Farklı Kaydet...',
            'exit': 'Çıkış',
            'undo': 'Geri Al',
            'redo': 'Yinele',
            'find': 'Bul...',
            'replace': 'Bul ve Değiştir...',
            'about': 'Hakkında'
        },
        'find_replace_dialog': {
            'title': 'Bul ve Değiştir',
            'find_label': 'Aranacak:',
            'replace_label': 'Değiştirilecek:',
            'find_button': 'Bul',
            'replace_button': 'Değiştir',
            'replace_all_button': 'Tümünü Değiştir',
            'close_button': 'Kapat'
        }
    },
    'en': {
        'title_new': 'Lintextor - New File',
        'file_dialog_title_open': 'Open File',
        'file_dialog_title_save': 'Save As',
        'file_filter': 'Text Files (*.txt);;All Files (*.*)',
        'file_error_title': 'Error',
        'file_error_text': 'An error occurred while opening the file: {}',
        'save_error_text': 'An error occurred while saving the file: {}',
        'save_prompt_title': 'Lintextor',
        'save_prompt_text': 'Do you want to save the changes?',
        'find_input_title': 'Find',
        'find_input_label': 'Enter text to find:',
        'find_not_found_title': 'Find',
        'find_not_found_text': 'Text "{}" not found.',
        'replace_title': 'Replace',
        'replace_no_more_text': 'No more matches found.',
        'replace_all_text': 'All matches have been replaced.',
        'about_title': 'About: Lintextor',
        'about_text': """
        <h3>About Lintextor</h3>
        <p>License: GNU GPLv3</p>
        <p>Programming Language: Python</p>
        <p>Interface: Qt</p>
        <p>Developer: Aydın Serhat Kılıçoğlu</p>
        <p>Github: www.github.com/shampuan</p>
        <p>
            This program creates windows-compatible txt documents on Linux systems.
        </p>
        <p>This program comes with no warranty.</p>
        """,
        'menu': {
            'file': 'File',
            'edit': 'Edit',
            'search': 'Search',
            'help': 'About',
            'new': 'New',
            'open': 'Open...',
            'save': 'Save',
            'save_as': 'Save As...',
            'exit': 'Exit',
            'undo': 'Undo',
            'redo': 'Redo',
            'find': 'Find...',
            'replace': 'Find and Replace...',
            'about': 'About'
        },
        'find_replace_dialog': {
            'title': 'Find and Replace',
            'find_label': 'Find:',
            'replace_label': 'Replace:',
            'find_button': 'Find',
            'replace_button': 'Replace',
            'replace_all_button': 'Replace All',
            'close_button': 'Close'
        }
    }
}

class Lintextor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.find_dialog = None
        self.last_find_text = ""
        self.initial_text = ""
        self.lang = 'tr'  # Varsayılan dil
        self.initUI()

    def get_language_texts(self):
        return LANGUAGES[self.lang]

    def update_language(self, lang_code):
        self.lang = lang_code
        self.retranslateUi()
        if self.find_dialog:
            self.find_dialog.update_texts()

    def retranslateUi(self):
        texts = self.get_language_texts()
        
        # Pencere başlığını güncelle
        current_title = self.windowTitle()
        if self.current_file:
            self.setWindowTitle(f'Lintextor - {self.current_file}')
        else:
            self.setWindowTitle(texts['title_new'])
        
        # Menü ve aksiyon metinlerini güncelle
        self.file_menu.setTitle(texts['menu']['file'])
        self.edit_menu.setTitle(texts['menu']['edit'])
        self.search_menu.setTitle(texts['menu']['search'])
        self.help_menu.setTitle(texts['menu']['help'])
        self.new_action.setText(texts['menu']['new'])
        self.open_action.setText(texts['menu']['open'])
        self.save_action.setText(texts['menu']['save'])
        self.save_as_action.setText(texts['menu']['save_as'])
        self.exit_action.setText(texts['menu']['exit'])
        self.undo_action.setText(texts['menu']['undo'])
        self.redo_action.setText(texts['menu']['redo'])
        self.find_action.setText(texts['menu']['find'])
        self.replace_action.setText(texts['menu']['replace'])
        self.about_action.setText(texts['menu']['about'])

    def initUI(self):
        texts = self.get_language_texts()
        self.setWindowTitle(texts['title_new'])
        self.setWindowIcon(QIcon(ICON_PATH))
        self.text_edit = QTextEdit()

        # Yazı tipi ayarları
        font = QFont("Courier New", 12)  
        self.text_edit.setFont(font)
        
        self.setCentralWidget(self.text_edit)
        
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.initial_text = self.text_edit.toPlainText()

        self.create_actions()
        self.create_menus()
        
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def on_text_changed(self):
        title = self.windowTitle()
        if self.text_edit.toPlainText() != self.initial_text:
            if not title.endswith("*"):
                self.setWindowTitle(title + "*")
        else:
            if title.endswith("*"):
                self.setWindowTitle(title[:-1])

    def create_actions(self):
        style = self.style()

        self.new_action = QAction(style.standardIcon(QStyle.SP_FileIcon), '', self)
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.triggered.connect(self.new_file)

        self.open_action = QAction(style.standardIcon(QStyle.SP_DialogOpenButton), '', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction(style.standardIcon(QStyle.SP_DialogSaveButton), '', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.save_file)

        self.save_as_action = QAction(style.standardIcon(QStyle.SP_DriveHDIcon), '', self)
        self.save_as_action.triggered.connect(self.save_as_file)

        self.exit_action = QAction(style.standardIcon(QStyle.SP_DialogCancelButton), '', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

        self.undo_action = QAction(style.standardIcon(QStyle.SP_ArrowBack), '', self)
        self.undo_action.setShortcut('Ctrl+Z')
        self.undo_action.triggered.connect(self.text_edit.undo)

        self.redo_action = QAction(style.standardIcon(QStyle.SP_ArrowForward), '', self)
        self.redo_action.setShortcut('Ctrl+Y')
        self.redo_action.triggered.connect(self.text_edit.redo)

        self.find_action = QAction(style.standardIcon(QStyle.SP_TitleBarContextHelpButton), '', self)
        self.find_action.setShortcut('Ctrl+F')
        self.find_action.triggered.connect(self.find_text_dialog)

        self.replace_action = QAction(style.standardIcon(QStyle.SP_MediaPlay), '', self)
        self.replace_action.setShortcut('Ctrl+H')
        self.replace_action.triggered.connect(self.show_find_replace_dialog)

        self.about_action = QAction(QIcon(ICON_PATH), '', self)
        self.about_action.triggered.connect(self.show_about_dialog)

        # Dil seçimi aksiyonları
        self.lang_tr_action = QAction('Türkçe', self)
        self.lang_tr_action.triggered.connect(lambda: self.update_language('tr'))

        self.lang_en_action = QAction('English', self)
        self.lang_en_action.triggered.connect(lambda: self.update_language('en'))

    def create_menus(self):
        menubar = self.menuBar()
        texts = self.get_language_texts()['menu']

        self.file_menu = menubar.addMenu(texts['file'])
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)

        self.edit_menu = menubar.addMenu(texts['edit'])
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)
        
        self.search_menu = menubar.addMenu(texts['search'])
        self.search_menu.addAction(self.find_action)
        self.search_menu.addAction(self.replace_action)

        language_menu = menubar.addMenu('Language')
        language_menu.addAction(self.lang_tr_action)
        language_menu.addAction(self.lang_en_action)

        self.help_menu = menubar.addMenu(texts['help'])
        self.help_menu.addAction(self.about_action)

        self.retranslateUi()

    # Dosya Fonksiyonları
    def new_file(self):
        if self.maybe_save():
            self.text_edit.clear()
            self.setWindowTitle(self.get_language_texts()['title_new'])
            self.current_file = None
            self.initial_text = ""

    def open_file(self):
        if self.maybe_save():
            texts = self.get_language_texts()
            filename, _ = QFileDialog.getOpenFileName(self, texts['file_dialog_title_open'], '.', texts['file_filter'])
            if filename:
                self.open_file_from_command_line(filename)

    # Yeni eklenen metot
    def open_file_from_command_line(self, filename):
        texts = self.get_language_texts()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.text_edit.setText(f.read())
            self.setWindowTitle(f'Lintextor - {filename}')
            self.current_file = filename
            # Burası önemli: Dosya açıldığında başlangıç metnini güncelle
            self.initial_text = self.text_edit.toPlainText()
        except Exception as e:
            QMessageBox.warning(self, texts['file_error_title'], texts['file_error_text'].format(e))
    
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8', newline='\r\n') as f:
                    f.write(self.text_edit.toPlainText())
                # Yıldızı kaldırmak için başlangıç metnini güncelle
                self.initial_text = self.text_edit.toPlainText()
                self.on_text_changed()  # Yıldızın anında gitmesi için tetikle
                return True
            except Exception as e:
                texts = self.get_language_texts()
                QMessageBox.warning(self, texts['file_error_title'], texts['save_error_text'].format(e))
                return False
        else:
            return self.save_as_file()

    def save_as_file(self):
        texts = self.get_language_texts()
        filename, _ = QFileDialog.getSaveFileName(self, texts['file_dialog_title_save'], '.', texts['file_filter'])
        if filename:
            if not filename.endswith('.txt'):
                filename += '.txt'
            try:
                with open(filename, 'w', encoding='utf-8', newline='\r\n') as f:
                    f.write(self.text_edit.toPlainText())
                self.setWindowTitle(f'Lintextor - {filename}')
                self.current_file = filename
                # Yıldızı kaldırmak için başlangıç metnini güncelle
                self.initial_text = self.text_edit.toPlainText()
                self.on_text_changed()  # Yıldızın anında gitmesi için tetikle
                return True
            except Exception as e:
                QMessageBox.warning(self, texts['file_error_title'], texts['save_error_text'].format(e))
                return False
        return False
    
    def maybe_save(self):
        if self.text_edit.toPlainText() == self.initial_text:
            return True
        
        texts = self.get_language_texts()
        reply = QMessageBox.warning(self, texts['save_prompt_title'],
                                    texts['save_prompt_text'],
                                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        if reply == QMessageBox.Save:
            return self.save_file()
        elif reply == QMessageBox.Cancel:
            return False
        return True

    def closeEvent(self, event):
        if self.maybe_save():
            event.accept()
        else:
            event.ignore()

    # Bul Fonksiyonları
    def find_text_dialog(self):
        texts = self.get_language_texts()
        text, ok = QInputDialog.getText(self, texts['find_input_title'], texts['find_input_label'], text=self.last_find_text)
        if ok and text:
            self.last_find_text = text
            self.find_next_or_first(text)
        else:
            self.clear_highlights()
    
    # Yeni ve daha işlevsel bulma metodu
    def find_next_or_first(self, text, start_from_current=False):
        texts = self.get_language_texts()
        
        cursor = self.text_edit.textCursor()
        
        # Eğer start_from_current=True ise, şu anki imleçten itibaren ara.
        if start_from_current:
            cursor = self.text_edit.document().find(text, cursor)
        else:
            # Aksi halde, belgenin başından itibaren ara.
            cursor = self.text_edit.document().find(text)

        if not cursor.isNull():
            self.text_edit.setTextCursor(cursor)
            format = QTextCharFormat()
            format.setBackground(QColor("yellow"))
            
            selection = QTextEdit.ExtraSelection()
            selection.format = format
            selection.cursor = cursor
            self.text_edit.setExtraSelections([selection])
            return True
        else:
            # Başka bir eşleşme bulunamazsa bu mesajı göster
            QMessageBox.information(self, texts['find_not_found_title'], texts['replace_no_more_text'])
            self.clear_highlights()
            return False
    
    def clear_highlights(self):
        self.text_edit.setExtraSelections([])
            
    # Bul ve Değiştir Fonksiyonları
    def show_find_replace_dialog(self):
        if not self.find_dialog:
            self.find_dialog = FindReplaceDialog(self)
        
        self.find_dialog.find_input.setText(self.last_find_text)
        self.find_dialog.update_texts()

        result = self.find_dialog.exec_()

        if result == QDialog.Accepted:
            find_text = self.find_dialog.find_input.text()
            replace_text = self.find_dialog.replace_input.text()
            self.last_find_text = find_text

            if not find_text:
                return

            action = self.find_dialog.button_action
            if action == 'find':
                self.find_next_or_first(find_text)
            elif action == 'replace':
                self.replace_once(find_text, replace_text)
            elif action == 'replace_all':
                self.replace_all(find_text, replace_text)

    def replace_once(self, find_text, replace_text):
        if not find_text:
            return
        
        texts = self.get_language_texts()
        
        cursor = self.text_edit.textCursor()
        
        # Seçili metin varsa ve aranacak metinle eşleşiyorsa, sadece bu seçimi değiştir.
        if cursor.hasSelection() and cursor.selectedText() == find_text:
            cursor.insertText(replace_text)
            self.text_edit.setTextCursor(cursor)
            self.clear_highlights()
            # Değiştirme işleminden sonra bir sonraki eşleşmeyi bul ve vurgula.
            self.find_next_or_first(find_text, start_from_current=True)
            return

        # Eğer seçili metin yoksa, ilk eşleşmeyi bul ve değiştir.
        cursor = self.text_edit.document().find(find_text)

        if not cursor.isNull():
            # Metni bulduktan sonra değiştir.
            cursor.insertText(replace_text)
            # Değiştirme işleminden sonra imleci değiştirilen metnin sonuna taşı.
            new_cursor = self.text_edit.textCursor()
            new_cursor.setPosition(cursor.selectionEnd())
            self.text_edit.setTextCursor(new_cursor)

            # Bir sonraki eşleşmeyi bul ve vurgula.
            self.find_next_or_first(find_text, start_from_current=True)
        else:
            QMessageBox.information(self, texts['replace_title'], texts['replace_no_more_text'])
            self.clear_highlights()

    def replace_all(self, find_text, replace_text):
        if find_text:
            texts = self.get_language_texts()
            content = self.text_edit.toPlainText()
            new_content = content.replace(find_text, replace_text)
            self.text_edit.setText(new_content)
            self.clear_highlights()
            QMessageBox.information(self, texts['replace_title'], texts['replace_all_text'])

    def show_about_dialog(self):
        texts = self.get_language_texts()
        QMessageBox.about(self, texts['about_title'], texts['about_text'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lintextor()

    # Eğer komut satırı argümanı olarak bir dosya yolu varsa, o dosyayı aç.
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        ex.open_file_from_command_line(file_path)

    sys.exit(app.exec_())
