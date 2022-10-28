roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
decimal = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]

def replace_roman(char) :
    for y in range(len(roman)) :
        if char == roman[y] :
            dec_num = decimal[y]
    return dec_num

def convRomanToDecimal(userstr) :
    res = 0
    i = 0
    while(i < len(userstr)) :
        s1 = replace_roman(userstr[i])
        
        if(i+1 <  len(userstr)) :
            s2 = replace_roman(userstr[i+1])

            if (s1 >= s2) :
                res = res + s1 
                i = i + 1

            else :
                res = res + (s2 - s1)
                i = i + 2

        else :
            res = res + s1 
            i = i + 1

    return res

def convDecimalToRoman(num) :
	roman_num = ''
	i = 0

	while num > 0 :
		for _ in range(num // decimal[i]) :
			roman_num += roman[i]
			num -= decimal[i]
		i += 1
	return roman_num

while True :
	print("--------------------MENU CARD-----------------------")
	print("\nTHIS IS YOUR PROGRAM TO CONVERT ROMAN AND DECIMAL NUMERALS")
	print("\n SELECT THE DESIRED OPTIONS FROM BELOW : ")
	print("\n 1] ENTER 1 TO CONVERT YOUR ROMAN NUMERAL TO DECIMAL NUMERAL \n 2] ENTER 2 TO CONVERT YOUR DECIMAL NUMERAL TO ROMAN NUMERAL")
	int_input = int(input("\n ENTER YOUR CHOICE : "))
	if int_input == 1 :
		userstr = input("Enter your Roman Numeral : ")
		print("Your Decimal Numeral is :", convRomanToDecimal(userstr.upper()))
	elif int_input == 2 :
		usernum = int(input("Enter your Decimal Numeral : "))
		print("Your Roman Numeral is :", convDecimalToRoman(usernum))



