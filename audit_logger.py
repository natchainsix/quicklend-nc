def audit(log, customer, event):
    log.append({"event": event, "customer": dict(customer)})
