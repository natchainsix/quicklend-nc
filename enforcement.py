def enforcement_step(notice_validated, service_verified, legal_period_elapsed, breach_remedied):
    return ["TERMINATE", "DEMAND_FULL_BALANCE", "SEND_DEFAULT_NOTICE"]
