import json
import sys


def main():
    try:
        data = {}
        def getUserInfo(firstname = sys.argv[1], lastname = sys.argv[2], age = sys.argv[3], city = sys.argv[4]):
            data.update({"firstname" : firstname})
            data.update({"lastname" : lastname})
            data.update({"age" : age})
            data.update({"city" : city})

        def parseToJson(dataToParse):
            getUserInfo()
            with open('data.txt', 'a') as dataFile:
                json.dump(dataToParse, dataFile)
                dataFile.write("\n")
                

        parseToJson(data)
    except IndexError:
        print("Please enter 'name', 'surname', 'age' and 'city' respectively.")


main()
