def lock_and_key (key_cuts, lock_pinning,minimum):
     
     isCheck = ((6-minimum) <= (key_cuts +  lock_pinning) <= (6+ minimum)) or ((key_cuts + lock_pinning -6) < minimum ) 

