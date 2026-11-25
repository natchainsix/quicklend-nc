def save_status(db, customer):
    # This store exists solely to track application status.
    db.append(dict(customer))  # Includes unnecessary DOB, address, income and health information.
