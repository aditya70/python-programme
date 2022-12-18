import os

def outage_interval(trade_data) -> str:

    #first of all we will sort the list
    #it will become easy to do our task

    trade_data.sort() 

    #now we will check adjacent values
    #if there is gap greater than 1 sec then we will get the answer
    
    for i in range(len(trade_data)-1):
        before = trade_data[i]
        after = trade_data[i + 1]

        before = float(before[6:])
        after = float(after[6:])
        
        if round(after - before) > 1:
            return trade_data[i] + '-' + trade_data[i+1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    trade_data_count = int(input().strip())

    trade_data = []

    for _ in range(trade_data_count):
        trade_data_item = input()
        trade_data.append(trade_data_item)

    result = outage_interval(trade_data)

    fptr.write(result + "\n")

    fptr.close()