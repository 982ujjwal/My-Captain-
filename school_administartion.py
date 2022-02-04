#project 1:Basic school administrator Program]
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a' ,newline='' ) as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email id"])
        writer.writerow(info_list)


if __name__ =='__main__':
    Condition=True
    student_num=1
    while(Condition):
        student_info=input("Enter Some  Student Information For Student #{} in the following format (Name Age Contact_Number Email_id) : ".format(student_num))

        print("Entered Information : "+student_info)
        #split
        
        student_info_list=student_info.split(' ')
        print("Entered Split up information is "+str(student_info_list)) 
        
        print("Enterd Information is- \nName: {} \nAge: {} \ncontact_Number: {} \nEmai_id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check=input("Is The Entered Information Correct?(yes/no): ")
        
        if choice_check=="yes":
             write_into_csv(student_info_list)
             condition_check=input("Enter (yes/no)If you want enter information for another student: ")
             if condition_check=="yes":
                Condition=True
                student_num=student_num+1
             elif condition_check=="no":
                Condition=False 
        elif choice_check=='no':
            print("\n Please re-eneter the value! ")        
            
            
       
        
           