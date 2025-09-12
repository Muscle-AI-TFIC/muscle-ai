import firebase_admin
from firebase_admin import credentials, auth
import json

def get_user_firebase():

    if not firebase_admin._apps:
        cred_path = "C:/Users/murad/OneDrive/Documentos/muscle-ai/src/muscle_ai/key.json"
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
 
    user_data= []

    for user in auth.list_users().iterate_all():
        user_data.append({
            'id': user.uid,
            'email': user.email,
            "name": user.display_name,
            "active": user.disabled,
        })
    return user_data

def save_user_json(user_data, filepath):

    with open(filepath, "w", encoding="utf-8") as file:

        json.dump(user_data, file, indent=2, ensure_ascii=False)
    print(f"As informações foram salvas com sucesso em {filepath}")

def main():
    
    cred_path = "C:/Users/murad/OneDrive/Documentos/muscle-ai/src/muscle_ai/key.json"
    output_file = "user.json"

    try:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("Verificando conexao")

        users = get_user_firebase()
        save_user_json(users, output_file)

    except FileNotFoundError:
        print(f"Erro: o arquivo com as credenciais {cred_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()