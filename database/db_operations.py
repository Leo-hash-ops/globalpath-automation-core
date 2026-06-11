import sqlite3
from datetime import datetime

def save_client(client):
    conn = sqlite3.connect('globalpath.db')
    cursor = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO clients (
            name, phone, email, nationality, service,
            country, level, passport, budget,
            destination, purpose, travel_date, custom_purpose,
            profession, experience,
            pathway, funds,
            consult_service, consultation_type, preferred_date,
            status, created_at
        ) VALUES (
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?,
            ?, ?,
            ?, ?, ?,
            ?, ?
        )
    ''', (
        client.get('name'), client.get('phone'),
        client.get('email'), client.get('nationality'),
        client.get('service'),
        client.get('country'), client.get('level'),
        client.get('passport'), client.get('budget'),
        client.get('destination'), client.get('purpose'),
        client.get('travel_date'), client.get('custom_purpose'),
        client.get('profession'), client.get('experience'),
        client.get('pathway'), client.get('funds'),
        client.get('consult_service'),
        client.get('consultation_type'),
        client.get('preferred_date'),
        'new', current_time
    ))
    client_id = cursor.lastrowid
    conn.commit()
    conn.close()
    print(f'=== CLIENT SAVED === ID: {client_id}')
    return client_id

def get_all_clients():
    conn = sqlite3.connect('globalpath.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients ORDER BY created_at DESC')
    clients = cursor.fetchall()
    conn.close()
    return clients

def get_client_by_id(client_id):
    conn = sqlite3.connect('globalpath.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (client_id,))
    client = cursor.fetchone()
    conn.close()
    return client

def get_clients_by_status(status):
    conn = sqlite3.connect('globalpath.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM clients WHERE status = ? ORDER BY created_at DESC',
        (status,))
    clients = cursor.fetchall()
    conn.close()
    return clients

def print_all_clients():
    conn = sqlite3.connect('globalpath.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients ORDER BY created_at DESC')
    clients = cursor.fetchall()
    conn.close()
    if not clients:
        print('No clients in database yet.')
        return
    print('=== ALL GLOBALPATH CLIENTS ===')
    print(f'Total: {len(clients)} client(s)')
    print('-' * 60)
    for c in clients:
        print(f"ID:{c['id']:>3} | {c['name']:<20} | {c['service']:<18} | {c['status']}")
    print('-' * 60)

def update_client_status(client_id, new_status):
    conn = sqlite3.connect('globalpath.db')
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE clients SET status = ? WHERE id = ?',
        (new_status, client_id))
    conn.commit()
    conn.close()
    print(f'Client {client_id} updated to: {new_status}')
