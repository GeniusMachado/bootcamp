import hashlib

# ---------------------------------------------------------
# The "Cluster" of Database Nodes
# ---------------------------------------------------------
# Imagine these are 3 separate servers holding parts of the data
SHARDS = {
    0: [],  # Server A
    1: [],  # Server B
    2: []   # Server C
}

def get_shard_id(key):
    """
    Determines which Shard a specific piece of data belongs to.
    We use a HASH function to distribute it evenly.
    """
    # 1. Turn the key (e.g., "User123") into a number
    hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)

    # 2. Modulo by number of shards (3) to find the bucket (0, 1, or 2)
    shard_id = hash_value % 3
    return shard_id

def insert_data(user_id, data):
    # Step 1: Figure out WHERE this data lives
    target_shard = get_shard_id(user_id)

    # Step 2: Save it there
    SHARDS[target_shard].append((user_id, data))
    print(f"Saving User '{user_id}' -> Shard {target_shard}")

# ---------------------------------------------------------
# The Simulation
# ---------------------------------------------------------
if __name__ == "__main__":
    users = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank"]

    print("--- INSERTING DATA ---")
    for user in users:
        insert_data(user, f"Profile Data for {user}")

    print("\n--- SHARD DISTRIBUTION ---")
    print(f"Shard 0 has {len(SHARDS[0])} users: {[u[0] for u in SHARDS[0]]}")
    print(f"Shard 1 has {len(SHARDS[1])} users: {[u[0] for u in SHARDS[1]]}")
    print(f"Shard 2 has {len(SHARDS[2])} users: {[u[0] for u in SHARDS[2]]}")
