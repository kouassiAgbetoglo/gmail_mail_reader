from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QHeaderView, QWidget
from PyQt5.uic import loadUi
import sys
import myWidgets
from google_gmail import Mymail

class MainUI(QMainWindow):
    
    is_read_mail_tab = False 
    is_send_mail_tab = False
    
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("mail_gui.ui", self)        
        self.setFixedSize(535, 380)
        # binding action to menu action to create read and send mail tab
        self.Messagerie.triggered.connect(self.read_mail_pressed)
        #self.actionSend_mail.triggered.connect(self.send_mail_pressed)
        
        self.myMail = Mymail()
        self.myMail.auth_google()
        
        
        

    # create tab window
    
    def read_mail_pressed(self):
        if not self.is_read_mail_tab: # check if the tab is created 
            
            
            """
            self.myMail.get_message_service() 
            self.myMail.get_message_id()
            self.myMail.get_message_payload()
            self.messages = self.myMail.get_message()"""
            
            self.is_read_mail_tab = True  # Update the flag to indicate the tab is created
            # if not create the table and disable the tab creation
            """self.read_mail_tab = myWidgets.Ui_Form()
            self.read_mail_tab.setupUi(self, "Read mail.")"""
            
            self.read_mail_tab = myWidgets.Ui_mail_reader_form()
            self.read_mail_tab.setupUi(self)
            
            #self.read_mail_tab.closeUI(self.close_read_mail_tab)
            #self.gridLayout.addWidget(self.read_mail_tab.tabWidget, 0,0)
            self.gridLayout.addWidget(self.read_mail_tab.main_tab_widget, 0,0)

            
            """self.get_messages_items()
            self.read_mail_tab.add_mail_list()
            self.read_mail_tab.list_event()"""
            
            """self.read_mail_tab.print_list_items()
            print("Fonction used.")
            """
            #self.read_mail_tab.refreshUI(self.refresh_mail)
    
    def close_read_mail_tab(self):
        self.gridLayout.removeWidget(self.read_mail_tab.tabWidget) # remove the widget from the main window
        self.read_mail_tab.tabWidget.deleteLater() # delete it 
        
        self.is_read_mail_tab = False
        
    def get_messages_items(self):
        mail_origin = []
        mail_content = []
        mail_subject = []
        
        for x in self.messages:
            mail_origin.append(x["From"])
            mail_content.append(str(x["Content"]))
            mail_subject.append(x["Subject"])
        
        self.read_mail_tab.clear_all()
        
         
        self.read_mail_tab.content = mail_content  
        self.read_mail_tab.mail_subject = mail_subject  
        self.read_mail_tab.mail_list = mail_origin


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())