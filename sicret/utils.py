import random


def random_name(suffix=False):
    adjectives = [
        "Cybernetic",
        "Digital",
        "Quantum",
        "Virtual",
        "Encrypted",
        "Holographic",
        "Parallel",
        "Algorithmic",
        "Synthetic",
        "Futuristic",
        "Cryptographic",
        "Neural",
        "Binary",
        "Phantom",
        "Invisible",
        "Shadow",
        "Stealth",
        "Transcendent",
        "Hyper",
        "Mega",
        "Nano",
        "Pseudo",
        "Recursive",
        "Silicon",
        "Simulated",
        "Spectral",
        "Subnet",
        "Super",
        "Techno",
        "Turbo",
        "Ultra",
        "Virtual",
        "Wired",
        "Zenith",
    ]

    nouns = [
        "Matrix",
        "Grid",
        "Code",
        "System",
        "Network",
        "Firewall",
        "Datastream",
        "Cryptogram",
        "Cyberspace",
        "Mainframe",
        "Algorithm",
        "Protocol",
        "Bandwidth",
        "Binary",
        "Byte",
        "Cache",
        "Circuit",
        "Compiler",
        "Cypher",
        "Database",
        "Framework",
        "Gateway",
        "Hyperlink",
        "Interface",
        "Kernel",
        "Node",
        "Pixel",
        "Quantum",
        "Router",
        "Server",
        "Torrent",
        "Vector",
        "Vertex",
        "Widget",
        "Zenith",
        "Zettabyte",
    ]

    adjective = random.choice(adjectives).lower()
    noun = random.choice(nouns).lower()

    if suffix:
        number = random.randint(0, 999)
        return f"{adjective}-{noun}-{number}"

    return f"{adjective}-{noun}"
