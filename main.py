import csv
import os

_FILENAME = 'history.csv'

def makeCapitalizedName(list):
    capitalized_namelist = []
    for name in list:
        capitalized_namelist.append(name.capitalize())
    return ' '.join(capitalized_namelist)

def SortedDictByValue(dict):
    sorted_dict = {}
    return sorted(dict.items(), key=lambda x: -x[1])



if __name__ == "__main__":

    print('こんにちは！私はRobokoです。あなたの名前は何ですか？')
    name = input()
    print(f'{name}さん。どこのレストランが好きですか？')
    restaurant_names = input().split(' ')
    restaurant_name = makeCapitalizedName(restaurant_names)

    #
    if(os.path.exists(_FILENAME)):
        with open(_FILENAME, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            csvdic = {}
            for row in reader:
                csvdic.update({row['Name'] : int(row['Count'])})
            sorteddic = SortedDictByValue(csvdic)

        with open(_FILENAME, 'w') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            isNotExist = True
            for item in sorteddic:
                if(restaurant_name == item[0]):
                    isNotExist = False
                    writer.writerow({'Name' : item[0] , 'Count' : item[1]+1})
                else:
                    writer.writerow({'Name' : item[0] , 'Count' : item[1]})
            if(isNotExist):
                writer.writerow({'Name' : restaurant_name , 'Count' : 1})
            
    else:
        #output restaurant_name to csv file
        with open(_FILENAME, 'w') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Name' : restaurant_name , 'Count' : 1})




    print(f'{name}さん。ありがとうございました。')
    print('良い一日を！さようなら。')
