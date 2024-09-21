try: 
    with open("//Users//jomollijoy//Desktop//Python//FileHandling//A.txt") as f2:
        with open("//Users//jomollijoy//Desktop//Python//FileHandling//B.txt", "w") as f3:
            for i in f2:
                f3.write(i)
except:
    print("File Not Available. Please Create File Before Reading.")

else: 
    f2.close()
    print("File Closed!")
