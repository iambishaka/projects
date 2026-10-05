# 'w' = opens file in write mode, creates file if not exist
# file = open("applications.txt", "w")

# write the data with write method
# file.write("Hello Mama!")

# Always close or data may corrupt
# file.close()

# with open("application_1.txt", "w") as file:
#     file.write("Hellloooo there!")

# with open("barunrocks.txt", "r") as file:
#     for line in file:
#         print(line, end="")
#         print("----")
    # content = file.read()
    # print(content)
    # print("======================")
    # data = file.readlines()
    # for i in data:
        # print(i)

with open("applications.txt", "a") as file:
    file.write("Name : Bishaka\n")
