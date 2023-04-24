import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

  
server.login('yashhts123@gmail.com', "zzqigyvxtvgvxnei")

subject = "CHALLENGES COMPLETED"
body = " NAME: Naina Garg \n Email: naina.2125it1204@kiet.edu \n Ph.No:8384885359 \nB.Tech IT \n 2nd year \n2200290139007 \n Photo: https://drive.google.com/file/d/18t2bEa5voxk-vDP94uCYiZwHypd94qeS/view?usp=sharing \n Git repo:https://github.com/NainaGarg-2004/CABIN4J "
msg = f"subject: {subject} \n\n\n {body}"

server.sendmail(
        'yashhts123@gmail.com',
        'sales@cabin4j.com',
    msg
    )
print('Message is sent succesfully!')

