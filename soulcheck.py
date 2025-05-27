import hashlib

soul_file = "soulroot/guardian_core.yaml"
hash_file = "soulroot/.soulroot.hash"

def read_soulroot(path):
    with open(path, "rb") as f:
        return f.read()

def generate_hash(content):
    return hashlib.sha256(content).hexdigest()

def verify_soulroot():
    try:
        current = generate_hash(read_soulroot(soul_file))
        with open(hash_file, "r") as f:
            stored = f.read().strip()
        if current == stored:
            print("✅ Soulroot integrity verified.")
        else:
            print("🚨 WARNING: Soulroot file has been modified!")
    except FileNotFoundError:
        print("⚠️  No hash found. Creating new soulroot hash now...")
        with open(hash_file, "w") as f:
            f.write(generate_hash(read_soulroot(soul_file)))
        print("✅ New soulroot hash created.")

if __name__ == "__main__":
    verify_soulroot()
