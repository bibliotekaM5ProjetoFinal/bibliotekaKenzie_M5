from users.models import User
from loans.models import Loan
from datetime import datetime, timedelta

def schedule_user_loans():
    users = User.objects.all()
    # print("======== USER ========")
    for user in users:
        # print(f"==== user: '{user.username}' loans ====")
        loans = Loan.objects.filter(user=user)
        for loan in loans:
            # print(f" --- {loan}")
            check_user_loans(loan, user)
    # print("======== ---- ========")
    
def check_user_loans(loan: Loan, user: User):
    today_date = datetime.now().date()
    expiration_date = loan.loan_date + timedelta(days=7)
    while expiration_date.weekday() >= 5:
            expiration_date += timedelta(days=1)
    
    # print(f"Loan Date:          {loan.loan_date}")
    # print(f"Expiration Date:    {expiration_date}")
    # if loan.devolution_date and loan.devolution_date > expiration_date:
    #     print(f"Block Date:         {loan.devolution_date + timedelta(days=2)}")
    # print(f"Devolution Date:    {loan.devolution_date}")

    # Bloquear usuário - se o usuário ainda não entregou uma cópia pendente.
    if loan.devolution_date is None and today_date > expiration_date and user.can_loan == True:
        user.can_loan = False
        user.save()
        # print(f"O usuário {user.username} não entregou uma cópia do livro {loan.book_copy}")

    # Desbloquear usuário - se o usuário não possui mais cópias pendentes e está além da taxa de bloqueio (2 dias após a devolução).
    if loan.devolution_date and today_date >= loan.devolution_date + timedelta(days=2) and user.can_loan == False:
        user.can_loan = True
        user.save()
        # print(f"O usuário {user.username} realizou a entrega da cópia e está perdoado")