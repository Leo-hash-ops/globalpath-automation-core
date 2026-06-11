from datetime import datetime
import sqlite3
from automation.follow_up_rules import get_follow_up_hours
from database.db_operations import update_client_status

def check_follow_ups():
    print('\n=== GLOBALPATH AUTO WORKER — FOLLOW-UP CHECK ===')
    print(f'Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('-' * 50)

    conn = sqlite3.connect('globalpath.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM clients')
        clients = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f'[!] Database query failed: {e}')
        conn.close()
        return
    finally:
        conn.close()

    if not clients:
        print('No clients in database.')
        return

    now = datetime.now()
    flagged = 0
    skipped = 0

    for client in clients:
        try:
            client_id  = client['id']
            name       = client['name']
            phone      = client['phone']
            service    = client['service']
            status     = client['status']
            created_at = client['created_at']
        except IndexError:
            print('[!] Table columns mismatch. Run db_setup.py.')
            return

        if status != 'new':
            skipped += 1
            continue

        if not created_at:
            skipped += 1
            continue

        try:
            saved_time = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        except Exception:
            print(f'[!] Could not parse timestamp for client {client_id}. Skipping.')
            continue

        hours_passed   = (now - saved_time).total_seconds() / 3600
        required_hours = get_follow_up_hours(service)

        if hours_passed >= required_hours:
            print(f'[FOLLOW-UP NEEDED]')
            print(f'  Name    : {name}')
            print(f'  Phone   : {phone}')
            print(f'  Service : {service}')
            if service == 'Study Abroad' and client['level']:
                print(f'  Details : {client["level"]} | Budget: {client["budget"]}')
            elif service == 'Work Visa' and client['profession']:
                print(f'  Details : {client["profession"]} | Exp: {client["experience"]}')
            elif service == 'Travel/Tourism' and client['purpose']:
                print(f'  Details : {client["purpose"]} | To: {client["destination"]}')
            print()
            update_client_status(client_id, 'flagged')
            flagged += 1

    print('-' * 50)
    print(f'Checked : {len(clients)} client(s)')
    print(f'Skipped : {skipped} already handled')
    print(f'Flagged : {flagged} need follow-up')
    print('=' * 50)
