    #ID & Name : 20CE013 Mayank Chovatiya
    #Aim       : Mr. Anant is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
    #            One fine day, a finite number of tourists come to stay at the hotel.
    #            The tourists consist of:
    #            → A Captain.
    #            → An unknown group of families consisting K of  members per group where  K ≠ 1.
    #            The Captain was given a separate room, and the rest were given one room per group. 
    #            Mr. Anant has an unordered list of randomly arranged room entries. The list consists 
    #            of the room numbers for all of the tourists. The room numbers will appear K times per 
    #            group except for the Captain's room. Mr. Anant needs you to help him find the Captain's 
    #            room number. The total number of tourists or the total number of groups of families is not 
    #            known to you. You only know the value of K and the room number list.

    K = int(input())

    room_list = map(int, input().split())
    room_list = sorted(room_list)

    #In example  K is 5, there must be 6 groups and 31 elementss.also, all numbers repeat 5(k) except room number 8.
    #Means, 8 = Captain's room number.
    for i in range(len(room_list)):
        if(i != len(room_list)-1):
            if(room_list[i]!=room_list[i-1] and room_list[i]!=room_list[i+1]):
                print(room_list[i])
                break;
        else:
            print(room_list[i])
            