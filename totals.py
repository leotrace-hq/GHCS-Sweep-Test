from invoices import invoices_for


def total_due(db_path, customer):
    return sum(amount for _, amount in invoices_for(db_path, customer))
