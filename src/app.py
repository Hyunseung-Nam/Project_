# app.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow      # Qt Designer에서 생성된 파일
from naver_news_api import search_news

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 검색 버튼 시그널 연결
        self.btn_search.clicked.connect(self.on_search)

        self.setWindowTitle("네이버 뉴스 검색기") # 창 제목 설정

    def on_search(self):
        # 사용자 입력 읽어오기
        query     = self.edit_query.text().strip()
        display     = self.spin_display.value()
        sort     = "sim" if self.combo_sort.currentText() == "정확도순" else "date"
        
        if not query:
            QMessageBox.warning(self, "알림", "검색어를 입력하세요.")
            return

        try:
            fname = search_news(query, display, sort)
        except Exception as e:
            QMessageBox.critical(self, "오류", str(e))
            return

        # 성공 메시지
        msg = (
            f"결과가 `{fname}` 파일로 저장되었습니다."
        )
        QMessageBox.information(self, "검색 완료", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())