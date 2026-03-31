def process_refunds(refund_queue):
    print(f"Processing {len(refund_queue)} refunds.")
    
    # BUG: Assumes the queue is never empty. Will crash if refund_queue is []
    next_refund = refund_queue[0] 
    
    print(f"Processing refund for: {next_refund}")
    return True

if __name__ == "__main__":
    empty_daily_queue = []
    process_refunds(empty_daily_queue)