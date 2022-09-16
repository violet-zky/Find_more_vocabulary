import accurate
import csv
if __name__ == '__main__':
    filename = r'.\picture\2.jpg'
    words = accurate.getwords(filename)
    print(words)
    text = []
    with open('./wd_database/example.csv', encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            # if(row[0]==words[0]):
            text.append(row)
    file = open("./text/context.csv", "w", encoding='UTF-8')
    writer = csv.writer(file)
    # print(text)
    # print(text[1][0]==words[1])
    # print(words[1])
    for i in range(len(text)-1):
        # print(text[i])
        if(text[i][0] == words[i]):
            writer.writerow(text[i])
    file.close()
    # print(text)
    # with open("./context.csv", "w", encoding='UTF-8') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for row in text:
    #         print(row)
    #         writer.writerow(row)
