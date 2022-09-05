import difflib

def retrieve_placeholder(msg, list, placeholder_key):
    appended_stock = ""
    final_key = ""
    break_statement = False
    for price_request_text in list:
        print('{} => {}'.format(price_request_text, msg))
        generated_initial_key = False
        initial_key = 0
        for i, s in enumerate(difflib.ndiff(price_request_text, msg)):
            if s[0] == ' ':
                continue
            elif s[0] == '-':
                print(u'Delete "{}" from position {}'.format(s[-1], i))
            elif s[0] == '+':
                print(u'Add "{}" to position {}'.format(s[-1], i))
                appended_stock = appended_stock + s[-1]
                #print(appended_stock)
            try:
                res = ""
                if not generated_initial_key:
                    generated_initial_key = True
                    initial_key = i
                    res = msg[i:].split()[0]
                    if msg[i - 1] != " ":
                        print("11: " + msg[i - 1])
                        res = msg[i - 1:].split()[0]
                    elif msg[i - 2] != " ":
                        print("22: " + msg[i - 2])
                        res = msg[i - 2:].split()[0]
                    price_request_text2 = price_request_text.replace("{" + placeholder_key + "}", str(res)).lower()
                    msg = msg.lower()
                    print("res: " + str(res) + " (" + str(i) + ")")
                    print("req2: '" + price_request_text2 + "'")
                    print("original: '" + msg + "'")
                    print("NEW NEW NEW 1: " + price_request_text.replace("{" + placeholder_key + "}", res).lower())
                    print("NEW NEW NEW 2: " + msg.lower())

                    if price_request_text2 == msg:
                        final_key = str(res)
                        print("Final Key Found! Key: " + final_key)
                        break_statement = True
                        break
                    if price_request_text.replace("{" + placeholder_key + "}", res).lower() == msg.lower():
                        final_key = str(res)
                        print("Final Key Found! Key: " + final_key)
                        break_statement = True
                        break
                elif generated_initial_key:
                    res = msg[initial_key:].split()[0]
                    if msg[initial_key - 1] != " ":
                        print("11: " + msg[initial_key - 1])
                        res = msg[initial_key - 1:].split()[0]
                    # elif msg[initial_key-2] != " ":
                    #    print("22: " + msg[initial_key-2])
                    #    res = msg[initial_key-2:].split()[0]
                    price_request_text2 = price_request_text.replace("{" + placeholder_key + "}", str(res)).lower()
                    msg = msg.lower()
                    print("res: " + str(res) + " (" + str(initial_key) + ")")
                    print("req2: '" + price_request_text2 + "'")
                    print("original: '" + msg + "'")
                    print("NEW NEW NEW 1: " + price_request_text.replace("{" + placeholder_key + "}", res).lower())
                    print("NEW NEW NEW 2: " + msg.lower())

                    if price_request_text2 == msg:
                        final_key = str(res)
                        print("Final Key Found! Key: " + final_key)
                        break
                    if price_request_text.replace("{" + placeholder_key + "}", res).lower() == msg.lower():
                        final_key = str(res)
                        print("Final Key Found! Key: " + final_key)
                        break_statement = True
                        break
            finally:
                if break_statement:
                    break
                else:
                    continue
        if break_statement:
            break
    print("final key 2: " + final_key)
    return final_key


lis = ["Hello there, {name} how are you doing today?"]

text_todo = "Hello there, Mustafa how are you doing today?"
strd = retrieve_placeholder(text_todo, lis, "name")
print("Input: " + text_todo)
print("key: " + strd)