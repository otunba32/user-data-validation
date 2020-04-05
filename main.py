from uuid import uuid1
from models.user import User


if __name__ == '__main__':
    # list to store all users
    users = []
    # generate a unique user ID
    user_id = str(uuid1())
    # input first name
    first_name = input('Enter first name: ')
    # input last name
    last_name = input('Enter last name: ')
    # input email address
    email = input('Enter email: ')

    # create the user object
    user = User(user_id, first_name, last_name, email)

    # display the suggested password
    print('Suggested password: {}' . format(user.password))

    # ask user if the password is OK
    user_choice = input("Are you okay with the suggested password (Yes or No): ")

    # if user does not enter yes, then ask for new password
    if user_choice.lower() != 'yes':

        # collect preferred password
        preferred_password = input("Kindly type in your preferred password: ")

        # while the preferred password does not meet the requirements, ask the user to enter another
        while len(preferred_password) < 7:
            # show notice about password length
            print("\nPassword should be greater than or equal to 7 in length.\n")
            # request for preferred password again
            preferred_password = input("Kindly type a password greater than or equal to 7 character: ")

        # at this point password is fine, so assign password to user
        user.password = preferred_password

    print("Thank you for signing up")

    # add the user to the list of users
    users.append(user)

    # print every user in the list
    for user in users:
        print(user)
