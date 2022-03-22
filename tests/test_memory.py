from RWMem import RWmem

rwm = RWmem("explorer")

print(
f"""
{rwm.process_name}
{rwm.process_id}
{rwm.process_handle}
{rwm.base_address}
"""
)