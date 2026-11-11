def movie_ticket_price(num_children, num_adults, num_seniors, show_time):
    # per adult: £15
    # per senior: £12
    # per child: £5
    cost = 0

    firstTwoChildrenFree = False # do a x = max(x - 2, 0)
    oneChildFree = False # just x = x- 1
    seniorHalfPrice = False # x * 0.5
    showBefore3 = False # total = total * 0.95

    # if num_seniors >=1: # if at least 1 senior, remove a child ticket price if exists
    #     num_children = max(num_children - 1, 0)

    # if num_adults >=2: # 2 adults or more, first 2 children attend for free
    #     if num_children >=2:
    #         num_children = max(num_children - 2, 0) # take away 2 but the most it will go down to is 0?

    # if (num_adults >=2) and (num_seniors == 1):
    #     num_seniors = num_seniors * 0.5

    if (num_children <0) or (num_adults <0) or (num_seniors <0) or (show_time <0):
        return None # If any input is negative, return None

    if show_time <15:
        showBefore3 = True

    if (num_adults >=2) and (num_seniors == 1):
        seniorHalfPrice = True
        firstTwoChildrenFree = True

    if (num_seniors >=1):
        oneChildFree = True

    if num_adults >=2:
        firstTwoChildrenFree = True

    ## calculate actual ticket price

    if (oneChildFree == True) and (firstTwoChildrenFree == False):
        num_children = max(num_children - 1, 0)

    if (firstTwoChildrenFree == True):
        num_children = max(num_children - 2, 0)

    if seniorHalfPrice == True:
        num_seniors = num_seniors * 0.50

    cost += num_children * 5
    cost += num_seniors * 12
    cost += num_adults * 15

    if showBefore3 == True:
        cost = cost * 0.95
        return cost
    elif showBefore3 == False:
        return cost