from database.db_operations import save_client, print_all_clients
from workflows.study_flow import study_workflow
from workflows.travel_flow import travel_workflow
from workflows.work_visa_flow import work_visa_workflow
from workflows.pr_flow import pr_workflow
from workflows.consultation_flow import consultation_workflow

print('=== WELCOME TO GLOBALPATH AGENCY ===')

while True:
    service = input('''
Choose Service:
1. Study Abroad
2. Travel / Tourism
3. Work Visa
4. PR / Relocation
5. Consultation
6. Exit System

Enter option : ''')

    if service == '1':
        client = study_workflow()
        client_id = save_client(client)
        print('Intake complete. ID:', client_id)
    elif service == '2':
        client = travel_workflow()
        client_id = save_client(client)
        print('Intake complete. ID:', client_id)
    elif service == '3':
        client = work_visa_workflow()
        client_id = save_client(client)
        print('Intake complete. ID:', client_id)
    elif service == '4':
        client = pr_workflow()
        client_id = save_client(client)
        print('Intake complete. ID:', client_id)
    elif service == '5':
        client = consultation_workflow()
        client_id = save_client(client)
        print('Intake complete. ID:', client_id)
    elif service == '6':
        print_all_clients()
        print('Closing GlobalPath System....')
        break
    else:
        print('Invalid option. Try again.')
