def argumen(*argv):
    i = 0
    for arg in argv:
        i += 1
        print(f"[{i}] {arg}")

argumen("tes", "dua", "tiga")
