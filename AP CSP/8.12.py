x = input("Enter a genome string: ")
st = 0
end = 0
c = 1
for i in x[2::1]:
    c += 1
    fi = x[c - 2]
    se = x[c - 1]
    if fi + se + i == "ATG":
        st = c + 1
    if fi + se + i == "TAG" or fi + se + i == "TAA" or fi + se + i == "TGA":
        end = c - 2
    if st != 0 and end != 0 and st != -1 and end != -1:
        print(x[st:end])
        st = -1
        end = -1
if st == 0 or end ==0:
    print("no gene is found")