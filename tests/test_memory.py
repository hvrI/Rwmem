import logging
import rwmem

logging.getLogger('pymem').setLevel(logging.WARNING)

rwm = rwmem.Rwmem("explorer")

print(
f"""
{rwm.process_name}
{rwm.process_id}
{rwm.process_handle}
{rwm.base_address}
"""
)