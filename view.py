# view - The file where we put all the print and user realted information

def getuser_state():
	state = input("Enter name of your State : ")
	return state

def showuser_data(data,dates):
	print("Total Number of Lok Sabha Seats in your State is : ",data[1])
	print("Total Number of Phase-1 Seats : ",data[2],"and it is on ",dates[0])
	print("Total Number of Phase-2 Seats : ",data[3],"and it is on ",dates[1])
	print("Total Number of Phase-3 Seats : ",data[4],"and it is on ",dates[2])
	print("Total Number of Phase-4 Seats : ",data[5],"and it is on ",dates[3])
	print("Total Number of Phase-5 Seats : ",data[6],"and it is on ",dates[4])
	print("Total Number of Phase-6 Seats : ",data[7],"and it is on ",dates[5])
	print("Total Number of Phase-7 Seats : ",data[8],"and it is on ",dates[6])
	return