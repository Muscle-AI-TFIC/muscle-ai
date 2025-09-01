import firebase_admin
from firebase_admin import credentials, auth
import json

cread_path = "C:/Users/murad/OneDrive/Documentos/muscle-ai/src/muscle_ai/key.json"
output_file = "user.json"

try:
    cred = credentials.Certificate(cread_path)
    firebase_admin.initialize_app(cred)

    print("Verificando conexao")

    users = auth.list_users()

    #print("\n Lista dos usuarios cadastrados:") // mexer para que ele mostre os dados para comparacao do json

    user_data = []

    for user in users.users:
            user_data = {
                'id': user.uid,
                'email' : user.email, 
                "name" : user.display_name,  
                "active": user.disabled 
            }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent= 4)

        

    # Esta mensagem deve ser impressa SOMENTE depois que o loop terminar.
    print(f"As informacoes foram salvas com sucesso em {output_file}")


except FileNotFoundError:
    print(f"Erro: o arquivo com as credenciais {cread_path} nao foi achado")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")