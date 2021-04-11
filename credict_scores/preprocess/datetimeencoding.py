from datetime import datetime


def start_stop_proces(start_list,stop_list, is_hour = True):
    days_list = []
    num_of_list = len(start_list)
    for idx in range(num_of_list):

        if str(start_list[idx]) == "NaT" and str(stop_list[idx]) == "NaT":
            days_list.append(-999)
            continue

        if str(start_list[idx]) == "NaT":
            delta = (-stop_list[idx])
        elif  str(stop_list[idx]) == "NaT":
            delta = (start_list[idx])
        else:
            delta = (stop_list[idx]-start_list[idx])

        # print(int(delta.days))
        days_list.append(int(delta.days))



    return days_list


# if __name__ == "__main__":
