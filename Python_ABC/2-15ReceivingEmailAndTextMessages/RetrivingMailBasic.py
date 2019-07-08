import imapclient

imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
imapObj.login('pythonabc@qq.com', 'xuapwdrgxocnddec')

# imapObj.select_folder('INBOX', readonly=True)
# UIDs = imapObj.search('SINCE 05-Dec-2017')
# print(UIDs)

