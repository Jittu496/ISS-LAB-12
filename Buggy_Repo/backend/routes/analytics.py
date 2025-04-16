from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

# FIXED: Added prefix to router for proper API organization
router = APIRouter(prefix="/analytics")

async def get_items_collection():
    from db import init_db
    return init_db()["items_collection"]

async def get_users_collection():
    from db import init_db
    return init_db()["users_collection"]

@router.get("/")
async def get_analytics():
    items_collection = await get_items_collection()
    users_collection = await get_users_collection()
    
    items = []
    async for item in items_collection.find():
        items.append(item)
    
    # FIXED: Removed hardcoded users list and initialized empty array
    users = []
    async for user in users_collection.find():
        users.append(user)
    
    item_count = len(items)
    user_count = len(users)
    
    # FIXED: Changed field names from "names" to "name" and "usernames" to "username"
    # to match the correct database schema
    item_name_lengths = np.array([len(item["name"]) for item in items]) if items else np.array([])
    user_username_lengths = np.array([len(user["username"]) for user in users]) if users else np.array([])
    
    stats = {
        "item_count": item_count,
        "user_count": user_count,
        "avg_item_name_length": float(item_name_lengths.mean()) if item_name_lengths.size > 0 else 0.0,
        "avg_user_username_length": float(user_username_lengths.mean()) if user_username_lengths.size > 0 else 0.0,
        "max_item_name_length": int(item_name_lengths.max()) if item_name_lengths.size > 0 else 0,
        "max_user_username_length": int(user_username_lengths.max()) if user_username_lengths.size > 0 else 0,
    }
    
    plt.figure(figsize=(8, 6))
    
    if item_name_lengths.size > 0:
        plt.hist(item_name_lengths, bins=10, alpha=0.5, label="Item Names", color="blue")
    if user_username_lengths.size > 0:
        plt.hist(user_username_lengths, bins=10, alpha=0.5, label="Usernames", color="green")
    
    plt.title("Distribution of Name Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.legend()
    
    # FIXED: Removed inappropriate comment
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close()
    
    # FIXED: Added chart data to response which was missing
    return JSONResponse({
        "stats": stats,
        "chart": f"data:image/png;base64,{image_base64}"
    })
