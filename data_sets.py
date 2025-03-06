import sqlite3

activities = [
        {
            "id": "230,BSYP-502,1,2025,VÅR,1,2-2",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-502",
            "emne_versjon": "1",
            "semester_ar": 2025,
            "semester_termin": "VÅR",
            "termin_nummer": 1,
            "aktivitet": "2-2",
            "disiplin": "PRAKSIS",
            "navn": "VÅR BSYP-502 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        },
        {
            "id": "230,BSYP-502,1,2025,VÅR,1,2-3",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-502",
            "emne_versjon": "1",
            "semester_ar": 2025,
            "semester_termin": "VÅR",
            "termin_nummer": 1,
            "aktivitet": "2-3",
            "disiplin": "PRAKSIS",
            "navn": "VÅR BSYP-502 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        },
        {
            "id": "230,BSYP-200,1,2025,HØST,1,2-4",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-200",
            "emne_versjon": "1",
            "semester_ar": 2025,
            "semester_termin": "HØST",
            "termin_nummer": 1,
            "aktivitet": "2-4",
            "disiplin": "PRAKSIS",
            "navn": "HØST BSYP-200 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        },
        {
            "id": "230,BSYP-200,1,2025,HØST,1,2-5",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-200",
            "emne_versjon": "1",
            "semester_ar": 2025,
            "semester_termin": "HØST",
            "termin_nummer": 1,
            "aktivitet": "2-5",
            "disiplin": "PRAKSIS",
            "navn": "HØST BSYP-200 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        },
        {
            "id": "230,BSYP-400,1,2026,VÅR,1,2-6",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-502",
            "emne_versjon": "1",
            "semester_ar": 2026,
            "semester_termin": "VÅR",
            "termin_nummer": 1,
            "aktivitet": "2-4",
            "disiplin": "PRAKSIS",
            "navn": "VÅR BSYP-400 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        },
        {
            "id": "230,BSYP-400,1,2026,VÅR,1,2-7",
            "emne_institusjon": 230,
            "emne_kode": "BSYP-502",
            "emne_versjon": "1",
            "semester_ar": 2026,
            "semester_termin": "VÅR",
            "termin_nummer": 1,
            "aktivitet": "2-5",
            "disiplin": "PRAKSIS",
            "navn": "VÅR BSYP-400 Praksisgruppe",
            "praksis_days": 32,
            "perioder_fraDato": None,
            "perioder_tilDato": None,
            "period": None
        }
    ]

members = [
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-2",
        "role": "teacher",
        "plnr": 49791,
        "user_name": "user123",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "49791@grr.la"
    },
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-2",
        "role": "student",
        "plnr": 587074,
        "user_name": "user456",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994941,
        "epost": "587074@grr.la"
    },
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-2",
        "role": "student",
        "plnr": 670165,
        "user_name": "user789",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994753,
        "epost": "670165@grr.la"
    },
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-3",
        "role": "teacher",
        "plnr": 38288,
        "user_name": "user101",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "38288@grr.la"
    },
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-3",
        "role": "student",
        "plnr": 720359,
        "user_name": "user202",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994756,
        "epost": "720359@grr.la"
    },
    {
        "id": "230,BSYP-502,1,2025,VÅR,1,2-3",
        "role": "student",
        "plnr": 802299,
        "user_name": "user303",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994814,
        "epost": "802299@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-4",
        "role": "teacher",
        "plnr": 857145,
        "user_name": "user404",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "857145@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-4",
        "role": "student",
        "plnr": 653667,
        "user_name": "user505",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994839,
        "epost": "653667@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-4",
        "role": "student",
        "plnr": 670301,
        "user_name": "user606",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994964,
        "epost": "670301@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-5",
        "role": "teacher",
        "plnr": 60792,
        "user_name": "user707",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "60792@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-5",
        "role": "student",
        "plnr": 207613,
        "user_name": "user808",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 992307,
        "epost": "207613@grr.la"
    },
    {
        "id": "230,BSYP-200,1,2025,HØST,1,2-5",
        "role": "student",
        "plnr": 719826,
        "user_name": "user909",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994737,
        "epost": "719826@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-6",
        "role": "teacher",
        "plnr": 48599,
        "user_name": "user1010",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "48599@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-6",
        "role": "student",
        "plnr": 727364,
        "user_name": "user1111",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 995460,
        "epost": "727364@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-6",
        "role": "student",
        "plnr": 804182,
        "user_name": "user1212",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 994665,
        "epost": "804182@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-",
        "role": "teacher",
        "plnr": 99886677,
        "user_name": "user1313",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": None,
        "epost": "99886677@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-",
        "role": "student",
        "plnr": 814626,
        "user_name": "user1414",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 995298,
        "epost": "814626@grr.la"
    },
    {
        "id": "230,BSYP-400,1,2026,VÅR,1,2-",
        "role": "student",
        "plnr": 863401,
        "user_name": "user1515",
        "first_name": "First Name",
        "last_name": "Last Name",
        "student_nummer": 995413,
        "epost": "863401@grr.la"
    }
]





def add_members():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS members;''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
    id VARCHAR NOT NULL,
    role VARCHAR NOT NULL,
    plnr INTEGER NOT NULL,
    user_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    student_nummer VARCHAR,
    epost VARCHAR NOT NULL,
    PRIMARY KEY (id, epost)
    )
    ''')

    for member in members:
        cursor.execute('''
        INSERT INTO members (id, role, plnr, user_name, first_name, last_name, student_nummer, epost)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            member['id'], 
            member['role'], 
            member['plnr'], 
            member['user_name'], 
            member['first_name'], 
            member['last_name'], 
            None if member['student_nummer'] is None else member['student_nummer'],  # Ensure NULL for None values
            member['epost']
        ))

    conn.commit()
    conn.close()


def add_activities():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    # Drop the existing table if it exists and create the new table
    cursor.execute('''DROP TABLE IF EXISTS activities;''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activities (
        id VARCHAR NOT NULL, 
        emne_institusjon INTEGER NOT NULL, 
        emne_kode VARCHAR NOT NULL, 
        emne_versjon VARCHAR NOT NULL, 
        semester_ar INTEGER NOT NULL, 
        semester_termin VARCHAR NOT NULL, 
        termin_nummer INTEGER NOT NULL, 
        aktivitet VARCHAR NOT NULL, 
        disiplin VARCHAR NOT NULL, 
        navn VARCHAR NOT NULL, 
        praksis_days INTEGER, 
        perioder_fraDato VARCHAR, 
        perioder_tilDato VARCHAR, 
        period VARCHAR, 
        PRIMARY KEY (id)
    )
    ''')

    # Insert the activities data
    for activity in activities:
        cursor.execute('''
        INSERT INTO activities (
            id, 
            emne_institusjon, 
            emne_kode, 
            emne_versjon, 
            semester_ar, 
            semester_termin, 
            termin_nummer, 
            aktivitet, 
            disiplin, 
            navn, 
            praksis_days, 
            perioder_fraDato, 
            perioder_tilDato, 
            period
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            activity['id'],
            activity['emne_institusjon'],
            activity['emne_kode'],
            activity['emne_versjon'],
            activity['semester_ar'],
            activity['semester_termin'],
            activity['termin_nummer'],
            activity['aktivitet'],
            activity['disiplin'],
            activity['navn'],
            activity['praksis_days'] if activity['praksis_days'] is not None else None,  # Handle None for praksis_days
            activity['perioder_fraDato'] if activity['perioder_fraDato'] is not None else None,
            activity['perioder_tilDato'] if activity['perioder_tilDato'] is not None else None,
            activity['period'] if activity['period'] is not None else None
        ))

    conn.commit()
    conn.close()

 

def add_termin():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    # Drop the existing table if it exists
    cursor.execute('DROP TABLE IF EXISTS termin;')

    # Create the "termin" table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS termin (
        year VARCHAR NOT NULL,
        termin VARCHAR NOT NULL,
        PRIMARY KEY (year, termin)
    )
    ''')

    # Insert the termin data
    cursor.execute('''
        INSERT INTO termin (year, termin) 
        VALUES (?, ?)
    ''', ('2025', 'VÅR'))

    conn.commit()
    conn.close()








