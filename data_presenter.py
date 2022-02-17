open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

total_choc = 0
total_straw = 0
total_van = 0

# for row in open_file:
#     item = row.rstrip('\n').split(',')
#     for value in item:
#         if item[2].startswith('C'):
#             total_choc += 1
#         elif item[2].startswith('S'):
#             total_straw += 1
#         elif item[2].startswith('V'):
#             total_van += 1

# print("Chocolate: ", total_choc)
# print("Strawberry: ", total_straw)
# print("Vanilla ", total_van)

total = 0

for row in open_file:
    item = row.rstrip('\n').split(',')
    # print(float(item[3]) * float(item[4]))
    total += float(item[3]) * float(item[4])

print(total)  



open_file.close()