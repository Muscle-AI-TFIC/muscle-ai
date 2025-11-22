def update_waiting_list_status(results: list, supabase):
    if not results:
        print("No users to update in waiting_list.")
        return

    user_ids = [r["user_id"] for r in results]

    print(f"Updating waiting_list for {len(user_ids)} users...")

    try:
        supabase.table("waiting_list").update({"waiting": False}).in_("user_id", user_ids).execute()

        print("waiting_list successfully updated.")
    except Exception as e:
        print(f"Error updating waiting_list: {e}")
