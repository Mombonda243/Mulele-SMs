from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField 
from kivymd.uix.textfield import MDTextField 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.metrics import dp
from kivy.uix.button import Button
import json
import datetime
import calendar
from kivy.uix.scrollview import ScrollView
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDIconButton
from kivy.core.window import Window
import http.client
import urllib.parse
from kivymd.uix.snackbar import MDSnackbar
from kivy.uix.popup import Popup
import json
from kivymd.uix.card import MDCard
from kivy.network.urlrequest import UrlRequest


Window.size=(360, 640)
class MyFondColor(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint=(1, 0.1)
        self.pos_hint={"top": 1}
        self.current_server = "Server 1"  # Server 1 actif par défaut

          # first color      
        self.color1=MDFloatLayout(
            size_hint=(1, 0.05), 
            pos_hint={"top": 0.6})
        self.add_widget (self.color1)
         
        # second color
        self.color2=MDFloatLayout (
            size_hint=(1, 0.5), pos_hint={
            "centre_x" : 0.5, "top" : 0.7})
            
        self.add_widget (self.color2)  
        
 
       
        with self.color1.canvas.before:
            Color(0.20, 0, 0.50, 1)
            self.rec=Rectangle(pos=self.pos, 
                size=self.size)
            self.bind(pos=self.update,
                 size=self.update)
                 
                     
                    
           #       
    def update(self,instance, *args):
         self.rec.pos=self.pos
         self.rec.size=self.size
         
         
         
     
     
class EnvoieSmS(MDScreen):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SMS_HISTORY_FILE = "sms_history.json"  # Fichier pour stocker l'historique des SMS
        self.sms_status_file = "blabla.json"
        
        self.sms_data1 = {}  # Initialisation vide
        self.sms_data = {}  # Initialisation vide
        self.countsms = 0
        self.countnotice = 0
        
        self.load_sms_status()  # Charge les données depuis le fichier JSON
        
        # Vérification et initialisation si nécessaire
        if not self.sms_data:
            self.sms_data = {
                "sms_count": 100,
                "expiration_date": self.get_expiration_date(),
                "payment_code": str(self.calculate_payment_code(100)),
                "sms_status": "active"
            }
            self.save_sms_status()
        
        # Background Color 
        self.MyColor=MyFondColor()
        self.add_widget (self.MyColor)
      
        #Le Champ de text et btn valide
        self.user = MDFloatLayout(
                    pos_hint={"top": 1.3})  
        self.add_widget(self.user)
        
        # Le nom du server 
        self.servair=MDFloatLayout(
            pos_hint={})
        self.add_widget(self.servair)
        
        self.titre01=MDFloatLayout()
        self.add_widget(self.titre01)
        
        
        self.num = MDTextField(
            hint_text="Nom d'expéditeur ou Chiffre",
            size_hint=(0.9, 0.5), 
            pos_hint={"center_x": 0.5, "top": 0.6}
        )

        self.exp = MDTextField(
            hint_text="Numéro du destinateur",
            size_hint=(0.9, 0.5), 
            pos_hint={"center_x": 0.5, "top": 0.5}
        )

        self.mess = MDTextField(
            hint_text="écrire votre message...",
            size_hint=(0.9, None),
            height=200,
            multiline=True,
            mode='fill',
            pos_hint={"center_x": 0.5, "top": 0.4}
        )
        
        self.btn = MDRaisedButton(
            text="Envoyez",size_hint=(0.4, 0.07), 
                pos_hint={
                    "x": 0.52, "top": 0.07},
            on_release=self.send_message)
                    
        self.correct = MDRaisedButton(
            text="Correction",
            size_hint=(0.4, 0.07), 
                pos_hint={
                    "x": 0.08, "top": 0.37},
                on_release=self.correct_text  # Lien avec la fonction
)
      

        self.btn1 = MDRaisedButton(
                text=" Server 1",
                    size_hint=(0.1, 0.07),  
                    pos_hint={"center_x":0.2,
                         "top": 0.25},
                on_release=lambda x: self.set_server("Server 1")
            )
               
                    
        self.btn2 = MDRaisedButton(
                text=" Server 2",
                    size_hint=(0.1, 0.07),  
                    pos_hint={"center_x":0.5,
                         "top": 0.25},
                    md_bg_color=(1, 0, 0, 1),
                on_release=lambda x: self.set_server("Server 2")
)  
                         
        self.btn3 = MDRaisedButton(
                text=" Server 3",
                    size_hint=(0.1, 0.07),  
                    pos_hint={"center_x": 0.8,
                        "top": 0.25},
                    md_bg_color =(1, 0, 0, 1),
                on_release=lambda x: self.set_server("Server 3")
)     
   
        titre02=MDLabel (text=" Mulele Sender",
            font_style="H5", halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1,0.80),
            pos_hint={"top":1.45})   
            
          # Menu  
        self.menu=MDFloatLayout ()
        self.add_widget(self.menu)   
        
        btn5=Button(background_normal=
          "Asset/menu.png",size_hint=
              (None, None) , size=(60, 60),
                pos_hint={
                " centre_x":1.5, "top" : 1},)
            
                
        image= FitImage(
            source="Asset/IMG.jpg" ,
            size_hint_y=(0.17),
              pos_hint={"top":0.17})                                     
        self.child =MDFloatLayout()
        
        self.countsms=0
        self.countnotice=0
            
        self.sms_data = self.sms_data if hasattr(self, 'sms_data') else {"sms_count": 100}

        self.sms = MDLabel(
            text=str(self.sms_data.get('sms_count')),
            font_style="H6",
            theme_text_color="Custom",
            text_color=(1,1,1,1),
            pos_hint={"top": 1.42, "x": 0.79}
        )

            
        self.sm1s=MDLabel(text="0",
            font_style="H6",
            theme_text_color="Custom",
            text_color=(0,0,0.90,1),
            pos_hint={"top": 1.42,"x" : 0.89})            
           
                
                        
        self.trans = MDIconButton(
                icon="comment",  
                halign="right",
                theme_text_color="Custom",
                text_color=(0,0,0,1),
                pos_hint={ "top" : 0.99, "x" : 0.75},
                on_release=self.open_recharge_popup  # Lier l'action à l'ouverture du popup
            )
                
                    
        notif= MDIconButton(
        
            icon="bell",  
            halign="right",
            theme_text_color="Custom",
            text_color=(0,0,0,1),
            pos_hint={ "top" : 0.99, "x" : 0.85},
            on_release  = self.PopupSms)  
      
        self.update_send_button()


        self.servair.add_widget(self.btn1)
        self.add_widget(self.trans)
        self.child.add_widget (notif)
        self.add_widget (self.sms)
        self.add_widget (self.sm1s)
        self.servair.add_widget(self.btn2)               
        self.servair.add_widget(self.btn3)
        self.add_widget(self.correct)
        self.mess.bind(focus=self.on_focus)
        self.user.add_widget(self.exp)
        self.user.add_widget(self.num)
        self.user.add_widget(self.mess)
        self.user.add_widget(self.child)
        self.user.add_widget(self.btn)
        self.titre01.add_widget (titre02)
        self.menu.add_widget(btn5)
        self.add_widget(image)





    def open_recharge_popup(self, instance):
        """Ouvre un popup pour saisir le code de recharge."""
        # Créer un BoxLayout pour organiser le champ de texte et les boutons
        box = MDBoxLayout(orientation='vertical', padding=10)

        # Créer un champ de texte pour entrer le code
        self.code_input = MDTextField(
            hint_text="Entrez votre code de recharge",
            multiline=False,
            size_hint_y=None,
            height=30,
            pos_hint={"center_x": 0.5}  # Centrer le champ de texte
        )
        box.add_widget(self.code_input)

        # Créer un bouton pour valider l'entrée
        validate_btn = Button(text="Valider", size_hint_y=None, height=50)
        validate_btn.bind(on_release=self.validate_recharge_code)
        box.add_widget(validate_btn)

        # Créer le Popup
        self.popup = Popup(
            title="Recharge",
            content=box,
            size_hint=(0.8, 0.4),
            auto_dismiss=True  # Le popup ne se ferme pas tout seul
        )
        self.popup.open()

    def validate_recharge_code(self, instance):
        """Valide et applique le code de recharge saisi."""
        code = self.code_input.text.strip()  # Récupère le code saisi

        if not code:
            snack = MDSnackbar()  # Créer une instance de MDSnackbar
            snack.add_widget(MDLabel(text="Veuillez entrer un code de recharge"))
            snack.open()  # Affiche le snack
            return
        
        # Appeler la méthode handle_recharge pour vérifier le code
        if self.handle_recharge(code):
            snack = MDSnackbar()  # Créer une instance de MDSnackbar
            snack.add_widget(MDLabel(text="Recharge réussie! ✅ , Redemarrez votre applcation"))
            snack.open()
            self.redema()  # Affiche le snack
          
        else:
            snack = MDSnackbar()  # Créer une instance de MDSnackbar
            snack.add_widget(MDLabel(text="Code incorrect ! ❌"))
            snack.open()  # Affiche le snack

        # Fermer le popup
        self.popup.dismiss()
   

    def redema(self, instance):
            ref = MDSnackbar()
            ref.add_widget(MDLabel(text="Redemarrez votre application"))
            ref.open()
    
    def get_expiration_date(self):
        """Retourne la date d'expiration du mois en cours (dernier jour du mois)."""
        today = datetime.date.today()
        last_day = calendar.monthrange(today.year, today.month)[1]  # Dernier jour du mois
        expiration_date = datetime.date(today.year, today.month, last_day)
        return expiration_date.strftime("%Y-%m-%d")  # Format YYYY-MM-DD


    def load_sms_status(self):
        """Charge l'état du compteur de SMS et la date d'expiration depuis le fichier local."""
        try:
            with open(self.sms_status_file, "r", encoding="utf-8") as file:
                self.sms_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ Fichier SMS non trouvé ou invalide, création d'un nouveau fichier.")
            self.sms_data = {}
            self.save_sms_status()

        print(f"🔍 SMS Data chargé : {self.sms_data}")
        self.check_sms_status()
    # decrement_sms_count
    def calculate_payment_code(self, sms_count):
        """Calcule le code de paiement basé sur le nombre de SMS."""
        return (sms_count * 15) // 100

    def check_sms_status(self):
        """Vérifie si l'état des SMS est toujours actif et si la date d'expiration est dépassée."""
        today = datetime.date.today()
        expiration_date = datetime.datetime.strptime(self.sms_data.get('expiration_date', self.get_expiration_date()), "%Y-%m-%d").date()

        if today >= expiration_date:
            # SMS expirés → désactiver et réinitialiser
            self.sms_data['sms_count'] = 0
            self.sms_data['sms_status'] = "inactive"
            self.sms_data['expiration_date'] = self.get_expiration_date()
            self.sms_data['payment_code'] = str(self.calculate_payment_code(100))
            self.save_sms_status()
            return False  # SMS inactifs après expiration
        return True  # SMS actifs




    def validate_code_length(self, code):
        """Vérifie la longueur et le format du code."""
        if len(code) != 10 or not code.isdigit():
            return False
        return True

    def validate_code_content(self, code):
        """Vérifie la présence de '15' et si le dernier chiffre est 0 ou 9."""
        if "15" not in code:
            return False

        # Vérifie si le dernier caractère est 0 ou 9
        if not (code[-1] == '0' or code[-1] == '9'):
            return False

        return True

    def handle_recharge(self, code):
        """Vérifie le code de recharge et applique la recharge si les conditions sont remplies."""
        if code in self.sms_data.get("used_codes", []):
            self.show_snackbar("Code déjà utilisé ❌", success=False)
            return False

        if not self.validate_code_length(code):
            self.show_snackbar("Code invalide (doit contenir 10 chiffres) ❌", success=False)
            return False

        if not self.validate_code_content(code):
            self.show_snackbar("Code invalide (doit contenir '15' et finir par 0 ou 9) ❌", success=False)
            return False

        # Code valide, recharge les SMS
        self.sms_data["sms_count"] = 100
        self.sms_data["sms_status"] = "active"
        self.sms_data["expiration_date"] = self.get_expiration_date()
        self.sms_data["payment_code"] = str(self.calculate_payment_code(100))  # Calcul du code de paiement
        self.sms_data.setdefault("used_codes", []).append(code)
        self.save_sms_status()

        self.update_send_button()
        self.show_snackbar("Recharge réussie ! ✅", success=True)

        return True


    def set_server(self, server_name):
        self.current_server = server_name
            # Afficher l'alerte du serveur sélectionné avant l'envoi
        self.alert(self.current_server)

        # Réinitialiser la couleur de tous les boutons
        print(f"{server_name} sélectionné !")
        
        # Afficher un Snackbar si Server 1 est sélectionné
        if server_name == "Server 1":
            self.alert(f"{server_name} sélectionné avec succès !")

    def alert(self, server_name):
        """Affiche un Snackbar indiquant quel serveur est sélectionné."""
        
        if self.current_server == "Server 1":
            self.btn1.md_bg_color = (0.2, 0.2, 0.4, 1)  # Gris foncé
            self.btn2.md_bg_color = (0.2, 0.2, 0.2, 1)
            self.btn3.md_bg_color = (0.2, 0.2, 0.2, 1)

        elif self.current_server == "Server 2":
            self.btn1.md_bg_color = (0.2, 0.2, 0.2, 1)  # Gris foncé
            self.btn2.md_bg_color = (0.2, 0.2, 0.4, 1)
            self.btn3.md_bg_color = (0.2, 0.2, 0.2, 1)

        elif self.current_server == "Server 3":
            self.btn1.md_bg_color = (0.2, 0.2, 0.2, 1)  # Gris foncé
            self.btn2.md_bg_color = (0.2, 0.2, 0.2, 1)
            self.btn3.md_bg_color = (0.2, 0.2, 0.4, 1)

        snackbar = MDSnackbar(
            MDLabel(
                text=f"Serveur actif : {server_name}",
                theme_text_color="Custom",
                text_color=(0.2, 0.4, 0.2, 1),
            )
        )
        snackbar.open()

    def send_message(self, instance):
            """Envoie un message si les SMS sont actifs."""
            if hasattr(self, "_sending") and self._sending:
                return  # Empêche un double envoi
            self._sending = True  # Active le verrou

            try:
                if not self.exp.text or not self.num.text or not self.mess.text:
                    self.show_snackbar("Erreur: Remplissez tous les champs avant d'envoyer le message.", success=False)
                    return

                if not self.check_sms_status():
                    self.show_snackbar("Les SMS sont inactifs. Veuillez recharger vos crédits.", success=False)
                    return  

                # Appeler la méthode d'envoi de SMS après vérification
                if self.current_server == "Server 1":
                    self.send_via_server1()
                elif self.current_server == "Server 2":
                    print("Envoi via Server 2 (API non définie)")
                elif self.current_server == "Server 3":
                    print("Envoi via Server 3 (API non définie)")
                else:
                    self.show_snackbar("Aucun serveur sélectionné", success=False)
                    print("Aucun serveur sélectionné")
                    
            except Exception as e:
                self.show_snackbar(f"Erreur lors de l'envoi du message : {str(e)}", success=False)
            finally:
                self._sending = False  # Réinitialise le verrou



    def send_via_server1(self):
        """Envoie un message via Server 1 et met à jour le compteur de SMS."""
        conn = http.client.HTTPSConnection("api.easysendsms.app")
        payload = urllib.parse.urlencode({
            'username': 'djddhdkdjnhdhddh',
            'password': 'RTYUIOIUYGJK',
            'to': self.exp.text,
            'from': self.num.text,
            'text': self.mess.text,
            'type': '0'
        })
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        try:
            conn.request("POST", "/bulksms", payload, headers)
            res = conn.getresponse()
            data = res.read().decode("utf-8")

            if "success" in data.lower():
                if self.sms_data['sms_count'] > 0:
                    self.sms_data['sms_count'] -= 1
                    print(f"📉 SMS décrémenté : {self.sms_data['sms_count']}")  # Vérification
                    self.decrement_sms_count()
                    self.save_sms(self.exp.text, self.num.text, self.mess.text, "success")
                    self.show_snackbar("Message envoyé avec succès ! ✅", success=True)

            else:
                # ❌ Échec de l'envoi → ne pas décrémenter le compteur
                self.save_sms(self.exp.text, self.num.text, self.mess.text, "Echec")
                self.decrement_sms_count()
                self.show_snackbar("Échec de l'envoi du message ❌", success=False)

        except Exception as e:
            print(f"Erreur: {e}")
            self.show_snackbar("Erreur lors de l'envoi du SMS ❌", success=False)


    def show_snackbar(self, messages, success=True):
        """Affiche un Snackbar avec un message clair selon l'état de l'envoi."""
        sms=int(self.sm1s.text)
        self.mont=(sms +  1)

        color = (0.2, 0.8, 0.2, 1) if success else (0.8, 0.2, 0.2, 1)
        
        snackbar = MDSnackbar(
            MDLabel(
                text=messages,
                theme_text_color="Custom",
                text_color=color
            )
        )
        snackbar.open()
        



    def save_sms(self, to, sender, message, status):
        """Enregistre les SMS envoyés ou échoués dans un fichier JSON et met à jour les compteurs."""

        sms_data1=  {
            "to": to,
            "from": sender,
            "message": message,
            "status": status
        }

        try:
            # Charger l'historique existant
            with open(self.SMS_HISTORY_FILE, "r", encoding="utf-8") as file:
                sms_history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            sms_history = []

        # Ajouter le nouveau SMS
        sms_history.append(sms_data1)

        # Sauvegarder dans le fichier
        with open(self.SMS_HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(sms_history, file, indent=4, ensure_ascii=False)

        # Vérifier si self.sm1s est bien un MDLabel (évite l'erreur)
        if not isinstance(self.sm1s, MDLabel):
            print(f"⚠️ Erreur: self.sm1s a été modifié ({type(self.sm1s)}) ! Réinitialisation...")
            import traceback
            traceback.print_stack()  # Affiche où l'erreur s'est produite
            self.sm1s = MDLabel(text="0")  # Réinitialisation pour éviter l'erreur

        # 🔢 Mettre à jour le compteur des SMS envoyés
        sms_count1 = len(sms_history)
        self.sm1s.text = str(sms_count1)# 

        # 🔻 Mettre à jour le compteur des SMS restants
        try:
            current_count = int(self.sms.text)
            self.sms.text = str(current_count - 1) if current_count > 0 else "0"  # Empêcher un compteur négatif
        except ValueError:
            print("⚠️ Erreur : self.sms.text n'est pas un nombre valide ! Réinitialisation à 0.")
            self.sms.text = "0"

        print(f"SMS sauvegardé : {sms_data1}")
        # print(f"Nombre total de SMS envoyés : {sms_count1}")

    def update_send_button(self):
        """Met à jour l'état du bouton d'envoi selon l'état des SMS et la date d'expiration."""
        print(f"🔘 Mise à jour du bouton : {self.sms_data['sms_status']}")  # Log pour débogage
        today = datetime.date.today()
        expiration_date = datetime.datetime.strptime(self.sms_data.get('expiration_date', self.get_expiration_date()), "%Y-%m-%d").date()

        # Si les SMS sont inactifs ou si le mois est expiré, désactiver le bouton
        if self.sms_data['sms_status'] == "inactive" or today >= expiration_date or self.sms_data['sms_count'] <= 0:
            self.btn.disabled = True
            print("🔘 Le mois est expiré ou SMS inactifs : bouton désactivé.")
        else:
            self.btn.disabled = False
            print("🔘 Les SMS sont actifs : bouton activé.")




    
    def PopupSms(self, instance):
        """Affiche un popup contenant tous les messages du fichier sms_history.json avec MDCard."""
        try:
            # Charger les SMS enregistrés
            with open(self.SMS_HISTORY_FILE, "r", encoding="utf-8") as file:
                sms_history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            sms_history = []

        # Conteneur principal vertical
        sms_content = MDBoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        sms_content.bind(minimum_height=sms_content.setter('height'))

        if not sms_history:
            sms_content.add_widget(MDLabel(text="Aucun message enregistré.", size_hint_y=None, height=40))
        else:
            for sms in sms_history:
                text = f"[b]To:[/b] {sms['to']}\n[b]From:[/b] {sms['from']}\n[b]Message:[/b]\n{sms['message']}\n\n[b]Statut:[/b] {sms['status']}"

                # MDCard pour styliser chaque message
                message_card = MDCard(
                    size_hint=(1, None),
                    height=max(120, len(sms['message'].split("\n")) * 20),
                    padding=10,
                    elevation=4,  # Ombre pour un meilleur rendu
                    radius=[10, 10, 10, 10],  # Coins arrondis
                    md_bg_color=(0.95, 0.95, 0.95, 1)  # Couleur de fond douce
                )

                # Label pour afficher le texte du SMS
                message_label = MDLabel(
                    text=text,
                    markup=True,
                    size_hint_y=None,
                    height=max(90, len(sms['message'].split("\n")) * 20),
                    text_size=(400, None),
                    halign="left",
                    valign="top",
                    color=(0, 0, 0, 1)
                )

                message_card.add_widget(message_label)

                # Ajouter un espace entre les cartes
                separator = Widget(size_hint_y=None, height=10)

                sms_content.add_widget(message_card)
                sms_content.add_widget(separator)

        # Ajouter les messages dans un ScrollView
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(sms_content)

        # Créer et ouvrir le Popup
        popup = Popup(
            title="📩 Historique des SMS",
            content=scroll_view,
            size_hint=(0.9, 0.7),
            auto_dismiss=True
        )
        popup.open()


    def decrement_sms_count(self):
        sms_status_file = "blabla.json"

        # Charger les données existantes du fichier JSON
        try:
            with open(sms_status_file, "r", encoding="utf-8") as file:
                sms_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Erreur : Impossible de lire le fichier JSON.")
            return

        # Vérifier si "sms_count" est bien présent
        if "sms_count" in sms_data and isinstance(sms_data["sms_count"], int):
            sms_data["sms_count"] -= 1  # Décrémenter le nombre de SMS

            # Sauvegarder les nouvelles valeurs
            with open(sms_status_file, "w", encoding="utf-8") as file:
                json.dump(sms_data, file, indent=4, ensure_ascii=False)

            print(f"✅ SMS mis à jour avec succès ! Nouveau sms_count : {sms_data['sms_count']}")
        else:
            print("⚠️ Erreur : Clé 'sms_count' absente ou invalide dans le fichier JSON.")

    def save_sms_status(self):
        """Sauvegarde l'état du compteur et de la date d'expiration dans le fichier JSON."""
        try:
            print(f"💾 Sauvegarde des données : {self.sms_data}")  # Vérification avant écriture
            with open(self.sms_status_file, "w", encoding="utf-8") as file:
                json.dump(self.sms_data, file, indent=4, ensure_ascii=False)

                file.flush()  # ⚠️ Force l'écriturez
            print("✅ Fichier JSON mis à jour avec succès !")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde JSON : {e}")


    # si on touche le champ de texte
    def on_focus(self, instance, value):
           
           if value == True:
               instance.height=200
           else :
               instance.height=200
    
               print(" correct")
    
    
 

    def correct_text(self, instance):
        """Envoie le texte à l'API pour correction et met à jour le champ de texte."""
        url = "http://127.0.0.1:8000/correct"
        text_to_correct = self.mess.text  # Récupère le texte actuel

        if not text_to_correct.strip():
            return  # Ne fait rien si le champ est vide

        headers = {"Content-Type": "application/json"}
        data = json.dumps({"text": text_to_correct})

        def on_success(req, result):
            corrected_text = result.get("corrected", text_to_correct)
            self.mess.text = corrected_text  # Met à jour le champ avec le texte corrigé

        def on_error(req, error):
            print("Erreur de correction :", error)

        def on_failure(req, result):
            print("Échec de la requête :", result)

        UrlRequest(
            url, 
            on_success=on_success, 
            on_error=on_error, 
            on_failure=on_failure, 
            req_body=data, 
            req_headers=headers, 
            method="POST"
        )

    
# Screen Manager
class sms(MDScreenManager):
    def __init__(self, **kwargs):
        super ().__init__(**kwargs)
        self.add_widget(EnvoieSmS(
        name=" EnvoieSmS"))
        
        
# Run Application 
class SmsMul(MDApp):
    def build(self):
        return sms()
if __name__=="__main__":
    SmsMul().run()