import time

# ---------------------------------------------------------
# 1. The "Slow" Database
# ---------------------------------------------------------
# Imagine this is fetching from AWS Redshift or a complex SQL query
def get_user_from_db(user_id):
    print(f"  [Database] Searching for user {user_id} (Slow)...")
    time.sleep(2)  # Simulate a 2-second delay
    return {"id": user_id, "name": "Michael Machado", "role": "Senior Engineer"}

# ---------------------------------------------------------
# 2. The "Fast" Cache
# ---------------------------------------------------------
# In production, this would be a Redis instance.
# Here, we use a global dictionary to simulate it.
CACHE = {}
CACHE_EXPIRY = {}  # To track when data gets "stale"

def get_user_profile(user_id):
    print(f"\n--- Requesting Profile for User {user_id} ---")

    # STEP 1: Check the Cache first
    if user_id in CACHE:
        print("  [Cache] HIT! Returning instant data.")
        return CACHE[user_id]

    # STEP 2: If not in Cache, ask the Database
    print("  [Cache] MISS. Asking Database...")
    user_data = get_user_from_db(user_id)

    # STEP 3: Save to Cache for next time
    CACHE[user_id] = user_data
    print("  [Cache] Data stored for next time.")
    return user_data

# ---------------------------------------------------------
# 3. The Simulation
# ---------------------------------------------------------
if __name__ == "__main__":
    # First Request: The user logs in (Cold Start)
    # This will be slow (2 seconds)
    start = time.time()
    user = get_user_profile(101)
    print(f"Time taken: {time.time() - start:.2f} seconds")

    # Second Request: The user refreshes the page
    # This should be INSTANT (0 seconds)
    start = time.time()
    user = get_user_profile(101)
    print(f"Time taken: {time.time() - start:.2f} seconds")

    # Third Request: Another user (Different ID)
    # This will be slow again
    start = time.time()
    user = get_user_profile(102)
    print(f"Time taken: {time.time() - start:.2f} seconds")
