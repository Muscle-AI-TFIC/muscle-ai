import firebase_admin
from firebase_admin import credentials, auth, firestore
import json
import os

def initialize_firebase():
    if not firebase_admin._apps:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        cred_path = os.path.join(project_root, "key.json")
        
        if not os.path.exists(cred_path):
            raise FileNotFoundError(f"key.json not found at {cred_path}")
        
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully.")


def get_user_firebase():

    initialize_firebase()
 
    user_data = []

    for user in auth.list_users().iterate_all():
        user_data.append({
            'id': user.uid,
            'email': user.email,
            "name": user.display_name,
            "active": user.disabled,
        })
    return user_data

def get_traning_firebase():

    initialize_firebase()

    db = firestore.client()
    docs = db.collection("trainings").stream()
 
    traning_data = []

    for doc in docs:
        data = doc.to_dict()
        traning_data.append({
            'id': doc.id,
            'Age': data.get('idade'),
            'Goal': data.get('objetivo'),
            'Weight': data.get('peso'),
        })
    return traning_data

def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f"json file saved on {filepath}")
