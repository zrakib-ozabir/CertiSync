import cv2 
list_names = ["Jimin","Varsha Chhabria","Dilip Chhabria","Shahrukh Khan","Abdullah Rahman"];

for index, name in enumerate(list_names):
    template= cv2.imread('certificate_template.jpg')
    cv2.putText(template,name,(454,882),cv2.FONT_HERSHEY_COMPLEX,4,(40,103,160),3,cv2.LINE_AA)
    cv2.imwrite(f'C:/Users/User/Downloads/certificate/certis_generated/{name}.jpg',template)
    print('Processing Certificate {}/{}'.format(index+1,len(list_names)))