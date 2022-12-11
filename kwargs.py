def argumen(**kwargs):
    for x in kwargs:
        if "start" in x:
            print("ada")
        # print(x)

    # for k, v in kwargs.items():
    #     print(k, v)

argumen(start=1, max=99)
