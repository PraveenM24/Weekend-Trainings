for _ in range(int(input())):
    length=int(input())
    encode=str(input())
    alpha={'0000':'a',
    '0001':'b',
    '0010':'c',
    '0011':'d',
    '0100':'e',
    '0101':'f',
    '0110':'g',
    '0111':'h',
    '1000':'i',
    '1001':'j',
    '1010':'k',
    '1011':'l',
    '1100':'m',
    '1101':'n',
    '1110':'o',
    '1111':'p'
    }
    decode=''
    for a in range(length//4):
        sep=encode[4*a:(4*a)+4]
        decode+=alpha[sep]
    print(decode)