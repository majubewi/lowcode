import csv
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTPRecipientsRefused

def sendmail(mailmessage,toaddrs):
    try:
        print("Sending mail to: " + toaddrs)
        #From and To
        fromaddr = 'svpoltringen@tueit.de'  
        toaddrs  = toaddrs

        #Constructing the MIME Mail Message
        msg = MIMEMultipart('alternative')
        msg.set_charset('utf8')
        msg["FROM"] = fromaddr
        msg["To"] = toaddrs
        #msg["Cc"] = "sv.poltringen@arcor.de"
        msg['Subject'] = Header(
            "SV Poltringen Feldsponsor".encode('utf-8'),
            'UTF-8'
        ).encode()

        #Mailcontent
        _attach = MIMEText(mailmessage.encode('utf-8'), 'html', 'UTF-8')        
        msg.attach(_attach)

        # The actual mail send  
        password = ''
        server = smtplib.SMTP('smtp.tueit.de:587')  
        server.starttls()  
        server.login(fromaddr,password)
        server.send_message(msg)
        server.quit()
    except SMTPRecipientsRefused as e:
        print("Error sending to Addr: " + toaddrs + " " +  str(e))


if __name__ == "__main__":

    with open('generate_email_from_csv/mailmessage.html') as mailfile:
        messagetemplate = mailfile.read()

    with open('generate_email_from_csv/unpaied_reservations.csv') as csvfile:
        
        #Alternative 1: Manually go through csv-rows
        reader = dict_reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            #First Row => Column Names
            if line_count == 0:
                column_names = row
                print(row)
                line_count += 1
            #Content
            else:
                feld = row["id"]
                price = row["price"]
                email = row["email"]
                mailmessage = messagetemplate.format(feld=feld,price=price)
                print(mailmessage)

                sendmail(mailmessage,email)
                line_count +=1
                break #For testing purposes, remove for production

        #Alternative 2: To json
        data = {}
        for row in dict_reader:
            id = row['id'] #Column Name of id
            data[id] = row
        #print(json.dumps(data, indent=4, sort_keys=True))

        
            