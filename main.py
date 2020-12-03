import smtplib, ssl, random

# creating members list
member_list = [(x[0], x[1]) for x in [l.split(",") for l in open("members.csv", "r").read().splitlines()]]
target_list = list(member_list)

random.shuffle(member_list)
random.shuffle(target_list)


message_raw = open("message.txt", "r").read()

# email and password are hardcoded, feel free to use this address
santa_email = "el.secret.santa101@gmail.com"
pwd = "GcM2p58ee3VscQ"


port = 465  # For SSL
# create a secure SSL context
context = ssl.create_default_context()

def msg_put_values(receiver_name, target_name) :
    msg = "From: Santa\nSubject: Secret Santa 2020\n" +  message_raw
    msg = msg.replace("[RECEIVER]", receiver_name)
    msg = msg.replace("[TARGET]", target_name)
    return msg


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server :
    server.login(santa_email, pwd)
    i = 0
    total_len = len(target_list)
    print("BEGIN")
    for (member_name, member_email) in member_list :
        random_index = random.randrange(len(target_list))
        (target_name, target_email) = target_list[random_index]
        while target_name == member_name and target_email == member_email :
            random_index = random.randrange(len(target_list))
            (target_name, target_email) = target_list[random_index]
        target_list.pop(random_index)
        message = msg_put_values(member_name, target_name)
        server.sendmail(santa_email, member_email, message.encode("utf8"))
        i += 1
        print(" - sent", i, "/", total_len)

print("DONE")