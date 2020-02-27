import json

mode = 'start'

if mode == "start":
    # message = f"Welcome to CHARISMATIC EVANGELISTIC MINISTRY"
    message = f"Welcome to CHARISMATIC EVANGELISTIC MINISTRY Payment Service:"

    response = {"services": [{"id": 1, "name": "First Fruit"},
                             {"id": 2, "name": "Tithe"},
                             {"id": 3, "name": "Pledge"},
                             {"id": 4, "name": "Welfare"},
                             {"id": 5, "name": "Christ To The Rural World"},
                             {"id": 6, "name": "Day of Help"},
                             {"id": 7, "name": "General Offering"}
                             ]}


    # message = ""
    count = 0

    for n in response['services']:
        acct_id = n['id']
        source_account = n['name']
        count += 1
        message += str(count) + '. ' + str(source_account) + '^'

    store_array = response['services']
    print(store_array)
    str_conv = json.dumps(store_array)
    print(str_conv)
    stored_data = f"{str_conv}"
    print(stored_data)
    # message = f"Please select a payment Type from options:^{message}"
    print(message)
    menu_response = int(input())
    print(menu_response)


    if menu_response:
        sel0 = menu_response
        sel0 = int(sel0)
        sel = sel0 - 1
        print(f"sel = {sel}")

        # extract_reply = extract.split('?')
        # rest = extract_reply[0]
        # payment_list = extract_reply[1]
        #
        trnx_type_list = json.loads(stored_data)
        trnx_id = trnx_type_list[sel]['id']
        trnx_name = trnx_type_list[sel]['name']
        print(trnx_name)
        #
        stored_data = f"{trnx_id}|{trnx_name}"
        print(stored_data)
        message = f"Enter membership number or enter 0 to skip"
        print(message)
        menu_response = int(input())
        # print(menu_response)
        if menu_response == 0:
            print("Go ahead and make payment")
            message = f"Enter amount you to pay:"
            print(message)
            amount_response = int(input())

            if amount_response:
                message = f"The amount entered is GHS {amount_response}"
                print(message)
                message = f"Choose payment network/platform:"
                print(message)
                response = {"payment": [{"id": 1, "name": "MTN Mobile Money"},
                                         {"id": 2, "name": "Vodafone Cash"},
                                         {"id": 3, "name": "AirtelTigo Cash"}
                                         ]}

                message = ""
                count = 0

                for n in response['payment']:
                    acct_id = n['id']
                    source_account = n['name']
                    count += 1
                    message += str(count) + '. ' + str(source_account) + '^'

                store_array = response['payment']
                str_conv = json.dumps(store_array)
                stored_data = f"{str_conv}"
                print(stored_data)
                # message = f"Please select a payment Type from options:^{message}"
                # print(message)
                menu_response = int(input())
                print(menu_response)

                if menu_response:
                    sel0 = menu_response
                    sel0 = int(sel0)
                    sel = sel0 - 1
                    print(f"sel = {sel}")

                    # extract_reply = extract.split('?')
                    # rest = extract_reply[0]
                    # payment_list = extract_reply[1]
                    #
                    payment_list = json.loads(stored_data)
                    payment_id = payment_list[sel]['id']
                    payment_name = payment_list[sel]['name']
                    print(payment_name)
                    #
                    stored_data = f"{payment_id}|{payment_name}"
                    print(stored_data)
                    message = f"Enter membership phone number"
                    print(message)
                    menu_response = int(input())
                    print(menu_response)
        else:
            message = f"Your membership number is {menu_response}"
            print(message)
            message = f"Enter amount you to pay:"
            print(message)
            amount_response = int(input())

            if amount_response:
                message = f"The amount entered is GHS {amount_response}"
                print(message)
                message = f"Choose payment network/platform:"
                print(message)
                response = {"payment": [{"id": 1, "name": "MTN Mobile Money"},
                                        {"id": 2, "name": "Vodafone Cash"},
                                        {"id": 3, "name": "AirtelTigo Cash"}
                                        ]}

                message = ""
                count = 0

                for n in response['payment']:
                    acct_id = n['id']
                    source_account = n['name']
                    count += 1
                    message += str(count) + '. ' + str(source_account) + '^'

                store_array = response['payment']
                str_conv = json.dumps(store_array)
                stored_data = f"{str_conv}"
                print(stored_data)
                # message = f"Please select a payment Type from options:^{message}"
                # print(message)
                menu_response = int(input())
                print(menu_response)

                if menu_response:
                    sel0 = menu_response
                    sel0 = int(sel0)
                    sel = sel0 - 1
                    print(f"sel = {sel}")

                    # extract_reply = extract.split('?')
                    # rest = extract_reply[0]
                    # payment_list = extract_reply[1]
                    #
                    payment_list = json.loads(stored_data)
                    payment_id = payment_list[sel]['id']
                    payment_name = payment_list[sel]['name']
                    print(payment_name)
                    #
                    stored_data = f"{payment_id}|{payment_name}"
                    print(stored_data)
                    message = f"Enter membership phone number"
                    print(message)
                    menu_response = int(input())
                    print(menu_response)


    # session_processor.store_menupoint.store_menupoint(request, "CROPAY", stored_data)