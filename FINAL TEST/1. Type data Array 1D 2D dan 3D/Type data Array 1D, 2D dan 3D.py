#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

# ARRAY 1 DIMENSI
array_1d = [6, 12, 18, 24, 30]
print("Array 1 Dimensi:")
print(array_1d)
print("-------------------------")

# ARRAY 2 DIMENSI
# (Array dalam array)
array_2d = [
    [3, 6, 9],
    [12, 15, 18],
    [21, 24, 27]
]
print("Array 2 Dimensi:")
for baris in array_2d:
    print(baris)
print("-------------------------")

# ARRAY 3 DIMENSI
# (Array 2D di dalam array)
array_3d = [
    [   # layer 1
        [11, 33],
        [66, 99]
    ],
    [   # layer 2
        [22, 44],
        [77, 88]
    ]
]

print("Array 3 Dimensi:")
for layer in array_3d:
    for baris in layer:
        print(baris)
    print("layer selesai")
