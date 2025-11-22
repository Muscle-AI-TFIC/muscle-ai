def get_waiting_list(supabase):
    response = (supabase.table("waiting_list").select("user_id").eq("waiting", True).execute())

    data = response.data if hasattr(response, "data") else response

    return [entry["user_id"] for entry in data]
